"""Provider resolution tests: env switches must beat the task registry."""

import os
import unittest
from unittest import mock

from smartrim import llm


class TestResolveModel(unittest.TestCase):
    def test_registry_provider_used_by_default(self):
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("LLM_PROVIDER", None)
            provider, model = llm.resolve_model(task="debrief")
        self.assertEqual(provider, "ollama")
        self.assertEqual(model, llm.MODEL_REGISTRY["debrief"].model)

    def test_env_provider_overrides_registry(self):
        with mock.patch.dict(os.environ, {"LLM_PROVIDER": "nvidia"}):
            provider, model = llm.resolve_model(task="debrief")
        self.assertEqual(provider, "nvidia")
        self.assertEqual(model, llm.NVIDIA_MODEL)

    def test_nvidia_ignores_local_ollama_model_name(self):
        with mock.patch.dict(os.environ, {"LLM_PROVIDER": "nvidia"}):
            provider, model = llm.resolve_model(task="chat")
        self.assertEqual(provider, "nvidia")
        self.assertNotIn("rimworld", model)
        self.assertIn("/", model)

    def test_explicit_provider_wins_over_env(self):
        with mock.patch.dict(os.environ, {"LLM_PROVIDER": "nvidia"}):
            provider, model = llm.resolve_model(task="debrief", provider="ollama")
        self.assertEqual(provider, "ollama")
        self.assertEqual(model, llm.MODEL_REGISTRY["debrief"].model)

    def test_nvidia_client_uses_openai_compatible_base_url(self):
        with mock.patch.dict(os.environ, {"LLM_PROVIDER": "nvidia"}):
            client = llm.get_client(task="debrief")
        self.assertIsInstance(client, llm.OpenAIClient)
        self.assertEqual(client.base_url, llm.NVIDIA_BASE_URL)
        self.assertEqual(client.model, llm.NVIDIA_MODEL)

    def test_task_env_model_overrides_nvidia_default(self):
        env = {"LLM_PROVIDER": "nvidia", "LLM_MODEL_CHAT": "meta/llama-3.3-70b-instruct"}
        with mock.patch.dict(os.environ, env):
            provider, model = llm.resolve_model(task="chat")
        self.assertEqual(provider, "nvidia")
        self.assertEqual(model, "meta/llama-3.3-70b-instruct")


if __name__ == "__main__":
    unittest.main()
