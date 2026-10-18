# RimWorld MCP Helper Functions
# Provides natural language interface to the RimWorld MCP server

$script:McpUrl = "http://localhost:8787/"
$script:IdCounter = 1

function Send-McpRequest {
    param([string]$Method, [hashtable]$Params)
    
    $script:IdCounter++
    $body = @{
        jsonrpc = "2.0"
        id = $script:IdCounter
        method = $Method
        params = $Params
    } | ConvertTo-Json -Depth 10
    
    $headers = @{ "Content-Type" = "application/json" }
    $result = Invoke-WebRequest -Uri $script:McpUrl -Method POST -Body $body -Headers $headers -UseBasicParsing
    $response = $result.Content | ConvertFrom-Json
    
    if ($response.result.content) {
        $text = $response.result.content[0].text
        try {
            return ($text | ConvertFrom-Json)
        } catch {
            return $text
        }
    }
    return $response.result
}

# === GAME STATE ===

function Get-GameStatus {
    $status = Send-McpRequest "tools/call" @{ name = "get_status"; arguments = @{} }
    if (-not $status -or -not ($status -is [pscustomobject])) {
        return $status
    }
    Write-Host "=== $($status.colonyName) ==="
    Write-Host "Day: $($status.daysPassed) | Storyteller: $($status.storyteller) | Difficulty: $($status.difficulty)"
    Write-Host "Colonists: $($status.colonistCount) | Wealth: $($status.wealthTotal)"
    Write-Host ""
    $colonists = $status.bundled.list_colonists.colonists
    foreach ($pawn in $colonists) {
        $mental = if ($pawn.mentalState) { " [MENTAL: $($pawn.mentalState)]" } else { "" }
        Write-Host "  $($pawn.name): HP $($pawn.health)% | Mood $($pawn.mood)% | $($pawn.job)$mental"
    }
    if ($status.bundled.get_alerts.activeAlerts.Count -gt 0) {
        Write-Host ""
        Write-Host "Alerts:"
        foreach ($alert in $status.bundled.get_alerts.activeAlerts) {
            Write-Host "  ! $($alert.label)"
        }
    }
    return $status
}

function Get-Colonists {
    $result = Send-McpRequest "tools/call" @{ name = "list_colonists"; arguments = @{} }
    foreach ($pawn in $result.colonists) {
        $mental = if ($pawn.mentalState) { " [MENTAL: $($pawn.mentalState)]" } else { "" }
        Write-Host "$($pawn.name) ($($pawn.id)): HP $($pawn.health)% | Mood $($pawn.mood)% | $($pawn.job)$mental"
    }
}

function Get-ColonistNeeds {
    param([string]$Name)
    $result = Send-McpRequest "tools/call" @{ name = "get_pawn"; arguments = @{ name = $Name; tab = "needs" } }
    Write-Host "=== $($result.name) Needs ==="
    foreach ($need in $result.needs) {
        $bar = "[" + ("|" * [math]::Floor($need.percent / 10)) + (" " * (10 - [math]::Floor($need.percent / 10))) + "]"
        Write-Host "  $($need.label): $bar $($need.percent)%"
    }
    if ($result.thoughts.Count -gt 0) {
        Write-Host ""
        Write-Host "Thoughts:"
        foreach ($thought in $result.thoughts) {
            $sign = if ($thought.moodOffset -ge 0) { "+" } else { "" }
            Write-Host "  $($thought.label): $sign$($thought.moodOffset)"
        }
    }
}

function Get-Map {
    $result = Send-McpRequest "tools/call" @{ name = "get_map"; arguments = @{} }
    Write-Host "Map: $($result.sizeX)x$($result.sizeZ) | Biome: $($result.biome)"
    Write-Host ""
    Write-Host "Legend: #=wall %=rock +=door *=tree ~=water .=ground V=geyser ?=fogged"
    Write-Host ""
    foreach ($row in $result.terrainOverview.grid) {
        Write-Host $row
    }
}

function Get-Conditions {
    $result = Send-McpRequest "tools/call" @{ name = "get_conditions"; arguments = @{} }
    Write-Host "Date: $($result.date) | Hour: $($result.hour)"
    Write-Host "Season: $($result.season) | Weather: $($result.weather.current)"
    Write-Host "Temperature: $($result.temperature.outdoorC)°C"
}

function Get-Alerts {
    $result = Send-McpRequest "tools/call" @{ name = "get_alerts"; arguments = @{} }
    if ($result.activeAlerts.Count -gt 0) {
        Write-Host "=== ALERTS ==="
        foreach ($alert in $result.activeAlerts) {
            Write-Host "  ! $($alert.label): $($alert.explanation)"
        }
    }
    if ($result.activeLetters.Count -gt 0) {
        Write-Host ""
        Write-Host "=== LETTERS ==="
        foreach ($letter in $result.activeLetters) {
            Write-Host "  * $($letter.label)"
        }
    }
    if ($result.activeAlerts.Count -eq 0 -and $result.activeLetters.Count -eq 0) {
        Write-Host "No alerts or letters."
    }
}

# === GAME CONTROL ===

function Pause-Game {
    Send-McpRequest "tools/call" @{ name = "set_speed"; arguments = @{ action = "pause" } }
    Write-Host "Game paused."
}

function Resume-Game {
    Send-McpRequest "tools/call" @{ name = "set_speed"; arguments = @{ action = "unpause" } }
    Write-Host "Game resumed."
}

function Wait-Days {
    param([int]$Days = 1)
    # Never bare-unpause: advance via wait_for_event (server caps at 1 game-hour during crises).
    $status = Get-GameStatus
    $targetDay = $status.daysPassed + $Days
    $iterations = 0
    $maxIterations = [math]::Max(1, $Days * 24 + 10)
    while ($iterations -lt $maxIterations) {
        $cur = (Send-McpRequest "tools/call" @{ name = "get_status"; arguments = @{} }).daysPassed
        if ($cur -ge $targetDay) { break }
        Send-McpRequest "tools/call" @{ name = "wait_for_event"; arguments = @{ maxGameHours = 24; pause = "always" } } | Out-Null
        $iterations++
    }
    Pause-Game
    $final = (Send-McpRequest "tools/call" @{ name = "get_status"; arguments = @{} }).daysPassed
    Write-Host "Waited $Days day(s). Now Day $final."
    return $final
}

# === BUILDING ===

function Build-Thing {
    param(
        [string]$Thing,
        [int]$X,
        [int]$Z,
        [string]$Material = $null
    )
    $buildArgs = @{ def = $Thing; x = $X; z = $Z }
    if ($Material) { $buildArgs.stuff = $Material }
    $result = Send-McpRequest "tools/call" @{ name = "build"; arguments = $buildArgs }
    if ($result.placed) {
        Write-Host "Built $Thing at ($X,$Z)"
    } else {
        Write-Host "Failed: $($result.error)$($result.reason)"
    }
    return $result
}

function Build-Room {
    param([int]$X1, [int]$Z1, [int]$X2, [int]$Z2, [string]$Material = "WoodLog")
    # Walls only; place a door separately with Build-Thing.
    return (Build-Wall -X1 $X1 -Z1 $Z1 -X2 $X2 -Z2 $Z2 -Material $Material)
}

function Build-Wall {
    param([int]$X1, [int]$Z1, [int]$X2, [int]$Z2, [string]$Material = "WoodLog")
    $result = Send-McpRequest "tools/call" @{ name = "build"; arguments = @{
        def = "Wall"; minX = $X1; minZ = $Z1; maxX = $X2; maxZ = $Z2; fill = "outline"; stuff = $Material
    }}
    Write-Host "Built $($result.cells) wall cells"
    return $result
}

function Build-Room {
    param([int]$X1, [int]$Z1, [int]$X2, [int]$Z2, [string]$Material = "WoodLog")
    $result = Send-McpRequest "tools/call" @{ name = "build"; arguments = @{
        def = "Wall"; minX = $X1; minZ = $Z1; maxX = $X2; maxZ = $Z2; fill = "outline"; stuff = $Material
    }}
    Write-Host "Built $($result.cells) wall cells for room"
    return $result
}

# === ZONES ===

function New-StockpileZone {
    param([int]$X1, [int]$Z1, [int]$X2, [int]$Z2)
    $result = Send-McpRequest "tools/call" @{ name = "designate"; arguments = @{
        designator = "Designator_ZoneAddStockpile_Resources"; minX = $X1; minZ = $Z1; maxX = $X2; maxZ = $Z2
    }}
    Write-Host "Stockpile zone created: $($result.cells) cells"
    return $result
}

function New-GrowingZone {
    param([int]$X1, [int]$Z1, [int]$X2, [int]$Z2, [string]$Plant = "Plant_Rice")
    $beforeZones = Send-McpRequest "tools/call" @{ name = "list_zones"; arguments = @{} }
    $beforeIds = @($beforeZones.zones | Where-Object { $_.kind -eq "growing" } | ForEach-Object { $_.id })
    $result = Send-McpRequest "tools/call" @{ name = "designate"; arguments = @{
        designator = "Designator_ZoneAdd_Growing"; minX = $X1; minZ = $Z1; maxX = $X2; maxZ = $Z2
    }}
    Write-Host "Growing zone created: $($result.cells) cells"
    $zones = Send-McpRequest "tools/call" @{ name = "list_zones"; arguments = @{} }
    $newZone = $zones.zones | Where-Object { $_.kind -eq "growing" -and ($beforeIds -notcontains $_.id) } | Select-Object -First 1
    if (-not $newZone) {
        $newZone = $zones.zones | Where-Object { $_.kind -eq "growing" } | Select-Object -Last 1
    }
    if ($newZone) {
        Send-McpRequest "tools/call" @{ name = "set_growing_zone"; arguments = @{ id = $newZone.id; plant = $Plant } } | Out-Null
        Write-Host "Plant set to $Plant"
    }
    return $result
}

function Get-Zones {
    $result = Send-McpRequest "tools/call" @{ name = "list_zones"; arguments = @{} }
    foreach ($zone in $result.zones) {
        $info = "$($zone.label) ($($zone.kind)): $($zone.cells) cells"
        if ($zone.kind -eq "growing") { $info += " | Plant: $($zone.plant)" }
        Write-Host "  $info"
    }
}

# === ORDERS ===

function Set-WorkPriority {
    param([string]$Colonist, [string]$Job, [int]$Priority)
    $result = Send-McpRequest "tools/call" @{ name = "set_work_priority"; arguments = @{
        name = $Colonist; workType = $Job; priority = $Priority
    }}
    if ($result.ok) {
        Write-Host "$Colonist -> $Job priority: $Priority"
    } else {
        Write-Host "Failed: $($result.error)"
    }
    return $result
}

function Hunt-Animal {
    param([int]$X, [int]$Z)
    $result = Send-McpRequest "tools/call" @{ name = "designate"; arguments = @{
        designator = "Designator_Hunt"; x = $X; z = $Z
    }}
    Write-Host "Animal designated for hunting at ($X,$Z)"
    return $result
}

function Chop-Trees {
    param([int]$X1, [int]$Z1, [int]$X2, [int]$Z2)
    $result = Send-McpRequest "tools/call" @{ name = "designate"; arguments = @{
        designator = "Designator_PlantsHarvestWood"; minX = $X1; minZ = $Z1; maxX = $X2; maxZ = $Z2
    }}
    Write-Host "Trees designated for chopping: $($result.applied) trees"
    return $result
}

function Mine-Rock {
    param([int]$X1, [int]$Z1, [int]$X2, [int]$Z2)
    $result = Send-McpRequest "tools/call" @{ name = "designate"; arguments = @{
        designator = "Designator_Mine"; minX = $X1; minZ = $Z1; maxX = $X2; maxZ = $Z2
    }}
    Write-Host "Rock designated for mining: $($result.applied) cells"
    return $result
}

# === COLONIST ORDERS ===

function Order-Colonist {
    param([string]$Colonist, [string]$Action, [string]$Target)
    $result = Send-McpRequest "tools/call" @{ name = "order_pawn"; arguments = @{
        id = $Colonist; command = $Action; targetId = $Target
    }}
    if ($result.ok) {
        Write-Host "$Colonist ordered to $Action $Target"
    } else {
        Write-Host "Failed: $($result.error)"
    }
    return $result
}

function Draft-Colonists {
    param([string[]]$Colonists)
    $result = Send-McpRequest "tools/call" @{ name = "draft"; arguments = @{
        action = "draft"; ids = ($Colonists -join ',')
    }}
    Write-Host "Drafted: $($Colonists -join ', ')"
    return $result
}

function Undraft-Colonists {
    param([string[]]$Colonists)
    $result = Send-McpRequest "tools/call" @{ name = "draft"; arguments = @{
        action = "undraft"; ids = ($Colonists -join ',')
    }}
    Write-Host "Undrafted: $($Colonists -join ', ')"
    return $result
}

# === RESEARCH ===

function Set-Research {
    param([string]$Project)
    $result = Send-McpRequest "tools/call" @{ name = "set_research"; arguments = @{ project = $Project } }
    if ($result.ok) {
        Write-Host "Research set to: $($result.label) (cost: $($result.cost))"
    } else {
        Write-Host "Failed: $($result.error)"
    }
    return $result
}

function Get-Research {
    $result = Send-McpRequest "tools/call" @{ name = "get_research"; arguments = @{} }
    Write-Host "Completed: $($result.completedCount) | Available: $($result.availableCount) | Total: $($result.totalCount)"
    if ($result.current) {
        Write-Host "Current: $($result.current.label) ($($result.current.progressPercent)%, cost $($result.current.cost))"
    } else {
        Write-Host "No research in progress"
    }
    return $result
}

# === PRODUCTION ===

function Add-CookingBill {
    param([int]$Count = 6, [string]$StoveId)
    if (-not $StoveId) {
        $stoves = Send-McpRequest "tools/call" @{ name = "list_things"; arguments = @{ category = "building"; label = "*stove*"; limit = 5 } }
        $StoveId = ($stoves.things | Where-Object { $_.def -match "Stove" } | Select-Object -First 1).id
    }
    if (-not $StoveId) { Write-Host "No stove found. Pass -StoveId."; return }
    $result = Send-McpRequest "tools/call" @{ name = "add_bill"; arguments = @{
        id = $StoveId; recipe = "CookMealSimple"; count = $Count
    }}
    Write-Host "Added cooking bill: $Count simple meals"
    return $result
}

# === COMMUNICATION ===

function Say-Message {
    param([string]$Message)
    $result = Send-McpRequest "tools/call" @{ name = "say"; arguments = @{ text = $Message } }
    if ($result.shown) {
        Write-Host "Message displayed ($($result.chars) chars)"
    }
    return $result
}

function Read-Letter {
    param([int]$Id)
    $result = Send-McpRequest "tools/call" @{ name = "read_letter"; arguments = @{ id = $Id } }
    Write-Host "=== $($result.label) ==="
    Write-Host $result.text
    return $result
}

# === WORLD ===

function Get-World {
    $result = Send-McpRequest "tools/call" @{ name = "get_world"; arguments = @{} }
    Write-Host "=== WORLD ==="
    if ($result.factions) {
        Write-Host "Factions:"
        foreach ($faction in $result.factions) {
            Write-Host "  $($faction.name): $($faction.goodwill) goodwill"
        }
    }
    return $result
}

function Get-Wildlife {
    $result = Send-McpRequest "tools/call" @{ name = "list_wildlife"; arguments = @{} }
    Write-Host "=== WILDLIFE ==="
    foreach ($animal in $result.animals | Select-Object -First 15) {
        Write-Host "  $($animal.kind) at ($($animal.x),$($animal.z))"
    }
}

# === UTILITY ===

function Invoke-Screenshot {
    $result = Send-McpRequest "tools/call" @{ name = "screenshot"; arguments = @{} }
    if ($result.ok) {
        Write-Host "Screenshot saved to: $($result.path)"
    } else {
        Write-Host "Screenshot failed: $($result.error)"
    }
    return $result
}

function Get-Things {
    param([string]$Def, [int]$Limit = 10)
    $result = Send-McpRequest "tools/call" @{ name = "list_things"; arguments = @{ def = $Def; limit = $Limit } }
    foreach ($thing in $result.things) {
        Write-Host "  $($thing.label) ($($thing.def)) at ($($thing.x),$($thing.z))"
    }
}

# === DAILY SUMMARY ===

function New-DailySummary {
    $status = Send-McpRequest "tools/call" @{ name = "get_status"; arguments = @{} }
    $conditions = Send-McpRequest "tools/call" @{ name = "get_conditions"; arguments = @{} }
    
    Write-Host "=== DAY $($status.daysPassed) SUMMARY ==="
    Write-Host "Colony: $($status.colonyName) | Storyteller: $($status.storyteller)"
    Write-Host "Date: $($conditions.date) | Season: $($conditions.season) | Weather: $($conditions.weather.current)"
    Write-Host ""
    Write-Host "COLONISTS:"
    foreach ($pawn in $status.bundled.list_colonists.colonists) {
        $mental = if ($pawn.mentalState) { " [MENTAL: $($pawn.mentalState)]" } else { "" }
        Write-Host "  - $($pawn.name): HP $($pawn.health)% | Mood $($pawn.mood)% | $($pawn.job)$mental"
    }
    
    if ($status.bundled.get_alerts.activeAlerts.Count -gt 0) {
        Write-Host ""
        Write-Host "ALERTS:"
        foreach ($alert in $status.bundled.get_alerts.activeAlerts) {
            Write-Host "  - $($alert.label)"
        }
    }
}

# Silent load - no output
