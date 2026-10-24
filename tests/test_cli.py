import os
import sys
from unittest.mock import MagicMock, patch

# Ensure sidecar is on sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIDECAR_DIR = os.path.join(BASE_DIR, "sidecar")
if SIDECAR_DIR not in sys.path:
    sys.path.insert(0, SIDECAR_DIR)

import cli
import counselor
from mcp_client import McpClient


def test_mcp_client_ping_success():
    client = McpClient("http://localhost:8787/")
    with patch("requests.post") as mock_post:
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_post.return_value = mock_resp

        ok, err = client.ping(timeout=1.0)
        assert ok is True
        assert err is None
        mock_post.assert_called_once()


def test_mcp_client_ping_failure():
    client = McpClient("http://localhost:8787/")
    with patch("requests.post", side_effect=Exception("Connection refused")):
        ok, err = client.ping(timeout=1.0)
        assert ok is False
        assert "Connection refused" in err


def test_counselor_ping():
    with patch.object(counselor._client, "ping", return_value=(True, None)) as mock_ping:
        ok, err = counselor.ping()
        assert ok is True
        assert err is None
        mock_ping.assert_called_once()


def test_cli_run_ping():
    with patch.object(cli.c, "ping", return_value=(True, None)):
        res = cli.run_ping()
        assert res["status"] == "connected"
        assert res["error"] is None

    with patch.object(cli.c, "ping", return_value=(False, "timeout")):
        res = cli.run_ping()
        assert res["status"] == "offline"
        assert res["error"] == "timeout"


def test_cli_check_connection():
    with patch.object(cli.c, "ping", return_value=(True, None)):
        assert cli.check_connection() is True

    with patch.object(cli.c, "ping", return_value=(False, "Connection refused")):
        assert cli.check_connection() is False
