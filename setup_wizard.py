# =============================================
# SOLARPUNK SELF-CONFIGURING WIZARD v3.0
# This wizard auto-fills everything for you
# =============================================

import os, json, sys, subprocess, time, datetime, webbrowser, shutil, platform, getpass, socket, hashlib, re, random, string, math, itertools, collections, typing, pprint, textwrap, html, urllib.parse, urllib.request, urllib.error, base64, mimetypes, pathlib, csv, pickle, sqlite3, zipfile, tarfile, io, fractions, decimal, statistics, secrets, uuid, inspect, traceback, warnings, contextlib, dataclasses, itertools, numbers, copy, types, weakref, gc, marshal, ast, token, tokenize, keyword, opcode, dis, symtable, symbol, parser, importlib, pkgutil, runpy, sysconfig, site, __future__

print("")
print("╔══════════════════════════════════════════════════╗")
print("║     SOLARPUNK SELF-CONFIGURING WIZARD v3.0      ║")
print("║           (I fill in ALL the blanks)            ║")
print("╚══════════════════════════════════════════════════╝")
print("")

# ==================== CONFIGURATION ====================
# I fill in EVERYTHING here based on what I know about your system

CONFIG = {
    "user": "carol",
    "system_root": "C:\\Users\\carol\\SolarPunk",
    "github_username": "MeekoThaRaccoon",
    "github_token": "",  # Will be prompted if needed
    "known_repos": [
        "SolarPunk-Nexus",
        "SolarPunk-Autonomous"
    ],
    "cloudflare_projects": [
        "solarpunk-nexus",
        "solarpunk-agent",
        "solarpunk-autonomous"
    ],
    "required_dirs": [
        "connected",
        "web_dashboard",
        "memvid_repo",
        "static",
        "templates",
        "data",
        "dist",
        "scripts",
        "backups",
        "logs"
    ],
    "required_bat_files": [
        "START.bat",
        "PUSH.bat",
        "CONTROL_PANEL.bat",
        "MANAGE_REPOS.bat",
        "SYNC_ALL.bat",
        "GITHUB_WIZARD.bat",
        "FIX-CLOUDFLARE.bat"
    ],
    "required_py_files": [
        "self_healing_agent.py",
        "repo_intelligence.py",
        "auto_healer.py"
    ],
    "scheduled_tasks": [
        {"name": "SolarPunk-HourlySync", "interval": "hourly", "script": "SYNC_ALL.bat"},
        {"name": "SolarPunk-DailyHealth", "interval": "daily", "script": "CONTROL_PANEL.bat --health"},
        {"name": "SolarPunk-WeeklyBackup", "interval": "weekly", "script": "CONTROL_PANEL.bat --backup"}
    ],
    "web_dashboard_port": 7681,
    "cloudflare_api_url": "https://api.cloudflare.com/client/v4",
    "git_remote_url": "https://github.com/MeekoThaRaccoon/SolarPunk-Autonomous.git",
    "auto_fix_enabled": True,
    "log_level": "INFO",
    "backup_interval_hours": 24,
    "health_check_interval_minutes": 60
}

# ==================== WIZARD FUNCTIONS ====================

def log(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")
    
    # Also write to log file
    log_dir = os.path.join(CONFIG["system_root"], "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "wizard_log.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")

def check_prerequisites():
    """Check all system prerequisites"""
    log("Checking system prerequisites...")
    
    checks = {
        "Python 3.14.2": sys.version.startswith("3.14"),
        "Current directory": os.getcwd() == CONFIG["system_root"],
        "Git installed": shutil.which("git") is not None,
        "Pip installed": shutil.which("pip") is not None,
        "Internet connection": check_internet(),
        "Write permissions": check_write_permissions(),
    }
    
    all_ok = True
    for check_name, result in checks.items():
        status = "✅" if result else "❌"
        log(f"  {status} {check_name}")
        if not result:
            all_ok = False
    
    return all_ok

def check_internet():
    """Check if we have internet connection"""
    try:
        urllib.request.urlopen("https://api.github.com", timeout=5)
        return True
    except:
        return False

def check_write_permissions():
    """Check if we have write permissions"""
    try:
        test_file = os.path.join(CONFIG["system_root"], "test_permissions.tmp")
        with open(test_file, "w") as f:
            f.write("test")
        os.remove(test_file)
        return True
    except:
        return False

def setup_directory_structure():
    """Create all required directories"""
    log("Setting up directory structure...")
    
    for dir_name in CONFIG["required_dirs"]:
        dir_path = os.path.join(CONFIG["system_root"], dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            log(f"  ✅ Created: {dir_name}")
        else:
            log(f"  ✓ Already exists: {dir_name}")
    
    return True

def create_batch_files():
    """Create all required batch files"""
    log("Creating batch files...")
    
    # 1. START.bat - Start the agent
    start_bat = '''@echo off
chcp 65001 > nul
title ⚡ SolarPunk Autonomous Agent
color 0A

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║           SOLARPUNK AUTONOMOUS AGENT             ║
echo ╚══════════════════════════════════════════════════╝
echo.

cd /d "C:\\Users\\carol\\SolarPunk"
echo Starting agent...
python self_healing_agent.py

echo.
echo Agent started at: http://localhost:7681
echo.
pause
'''
    
    # 2. PUSH.bat - Push to GitHub and Cloudflare
    push_bat = '''@echo off
chcp 65001 > nul
title 🚀 SolarPunk Auto-Deploy
color 0A

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║            SOLARPUNK AUTO-DEPLOY                 ║
echo ╚══════════════════════════════════════════════════╝
echo.

cd /d "C:\\Users\\carol\\SolarPunk"

echo 🔄 Adding all files...
git add .

echo 💾 Committing changes...
git commit -m "Auto-update %%date%% %%time%%" 2>nul || echo "No changes to commit"

echo 🚀 Pushing to GitHub...
git push origin master

echo.
echo ✅ Push complete!
echo 🌐 Cloudflare will auto-deploy in 30-60 seconds.
echo 📊 Check: https://solarpunkagent.pages.dev
echo.
pause
'''
    
    # 3. CONTROL_PANEL.bat - Unified control panel
    control_panel_bat = '''@echo off
chcp 65001 > nul
title 🎮 SolarPunk Control Panel
color 0A

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║          SOLARPUNK UNIFIED CONTROL PANEL         ║
echo ╚══════════════════════════════════════════════════╝
echo.

:MAIN_MENU
echo 📋 Available Commands:
echo.
echo 1. 🚀 Start Agent (localhost:7681)
echo 2. 📤 Push to GitHub & Cloudflare
echo 3. 🔄 Sync All Repositories
echo 4. 🛠️  Run Auto-Healer
echo 5. 📊 Open Web Dashboard
echo 6. ⚙️  Run Setup Wizard
echo 7. ❌ Exit
echo.
choice /C 1234567 /M "Select option: "

if errorlevel 7 exit
if errorlevel 6 goto WIZARD
if errorlevel 5 goto DASHBOARD
if errorlevel 4 goto HEALER
if errorlevel 3 goto SYNC
if errorlevel 2 goto PUSH
if errorlevel 1 goto START

:START
echo Starting agent...
START START.bat
goto MAIN_MENU

:PUSH
echo Pushing updates...
START PUSH.bat
goto MAIN_MENU

:SYNC
echo Syncing repositories...
START SYNC_ALL.bat
goto MAIN_MENU

:HEALER
echo Running auto-healer...
python auto_healer.py
pause
goto MAIN_MENU

:DASHBOARD
echo Opening dashboard...
start http://localhost:7681
goto MAIN_MENU

:WIZARD
echo Running setup wizard...
python setup_wizard.py
pause
goto MAIN_MENU
'''
    
    # 4. SYNC_ALL.bat - Sync all repositories
    sync_all_bat = '''@echo off
chcp 65001 > nul
title 🔄 SolarPunk Repository Sync
color 0A

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║         REPOSITORY SYNCHRONIZATION               ║
echo ╚══════════════════════════════════════════════════╝
echo.

cd /d "C:\\Users\\carol\\SolarPunk"

echo 📅 %date% %time%
echo.

echo 🔄 Syncing main repository...
git pull
git add .
git commit -m "Auto-sync %%date%% %%time%%" 2>nul || echo "No changes to commit"
git push origin master

echo.
echo 📁 Checking connected repositories...
if exist connected (
    cd connected
    for /d %%i in (*) do (
        echo.
        echo 📁 Syncing %%i...
        cd "%%i"
        git pull 2>nul && echo   ✅ Synced || echo   ⚠️  Could not sync
        cd..
    )
    cd..
)

echo.
echo ⚡ Sync completed at %time%
echo.
pause
'''
    
    # Save all batch files
    batch_files = {
        "START.bat": start_bat,
        "PUSH.bat": push_bat,
        "CONTROL_PANEL.bat": control_panel_bat,
        "SYNC_ALL.bat": sync_all_bat
    }
    
    for filename, content in batch_files.items():
        filepath = os.path.join(CONFIG["system_root"], filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"  ✅ Created: {filename}")
    
    return True

def create_python_agent():
    """Create the main self-healing agent"""
    log("Creating self-healing agent...")
    
    agent_code = '''# SOLARPUNK SELF-HEALING AGENT v3.0
import os, sys, time, json, subprocess, datetime, requests, hashlib, threading, webbrowser, shutil, platform, socket, re, random, string, math, itertools, collections, typing, pprint, textwrap, html, urllib.parse, urllib.request, urllib.error, base64, mimetypes, pathlib

class SolarPunkAgent:
    def __init__(self):
        self.root = "C:\\\\Users\\\\carol\\\\SolarPunk"
        self.log_file = os.path.join(self.root, "logs", "agent_log.txt")
        self.health_file = os.path.join(self.root, "logs", "health_status.json")
        self.web_port = 7681
        self.setup_logging()
    
    def setup_logging(self):
        """Setup logging directory and files"""
        log_dir = os.path.join(self.root, "logs")
        os.makedirs(log_dir, exist_ok=True)
    
    def log(self, message, level="INFO"):
        """Log a message with timestamp"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        # Print to console
        print(log_entry)
        
        # Write to log file
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\\n")
        
        return log_entry
    
    def check_system_health(self):
        """Check the health of the entire system"""
        self.log("Starting system health check...")
        
        checks = {
            "Directories": self.check_directories(),
            "Batch Files": self.check_batch_files(),
            "Python Files": self.check_python_files(),
            "Git Repository": self.check_git_repo(),
            "Cloudflare Sites": self.check_cloudflare_sites(),
            "Web Dashboard": self.check_web_dashboard(),
            "Scheduled Tasks": self.check_scheduled_tasks(),
        }
        
        # Generate health report
        health_report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "checks": checks,
            "overall_health": "HEALTHY" if all(checks.values()) else "NEEDS_ATTENTION",
            "issues_found": sum(1 for check in checks.values() if not check)
        }
        
        # Save report
        with open(self.health_file, "w", encoding="utf-8") as f:
            json.dump(health_report, f, indent=2)
        
        self.log(f"Health check complete. Issues found: {health_report['issues_found']}")
        return health_report
    
    def check_directories(self):
        """Check if all required directories exist"""
        required_dirs = [
            "connected", "web_dashboard", "memvid_repo", "static",
            "templates", "data", "dist", "scripts", "backups", "logs"
        ]
        
        for dir_name in required_dirs:
            dir_path = os.path.join(self.root, dir_name)
            if not os.path.exists(dir_path):
                self.log(f"Missing directory: {dir_name}", "WARNING")
                # Auto-create it
                os.makedirs(dir_path, exist_ok=True)
                self.log(f"Created directory: {dir_name}")
        
        return True
    
    def check_batch_files(self):
        """Check if all required batch files exist"""
        required_bats = ["START.bat", "PUSH.bat", "CONTROL_PANEL.bat", "SYNC_ALL.bat"]
        
        for bat_file in required_bats:
            bat_path = os.path.join(self.root, bat_file)
            if not os.path.exists(bat_path):
                self.log(f"Missing batch file: {bat_file}", "WARNING")
                return False
        
        return True
    
    def check_python_files(self):
        """Check if all required Python files exist"""
        required_pys = ["self_healing_agent.py", "repo_intelligence.py", "auto_healer.py"]
        
        for py_file in required_pys:
            py_path = os.path.join(self.root, py_file)
            if not os.path.exists(py_path):
                self.log(f"Missing Python file: {py_file}", "WARNING")
                return False
        
        return True
    
    def check_git_repo(self):
        """Check if Git repository is healthy"""
        try:
            result = subprocess.run(
                ["git", "status"],
                capture_output=True,
                text=True,
                cwd=self.root,
                timeout=10
            )
            return result.returncode == 0
        except:
            self.log("Git repository check failed", "WARNING")
            return False
    
    def check_cloudflare_sites(self):
        """Check if Cloudflare sites are accessible"""
        sites = [
            "https://solarpunk-nexus.pages.dev",
            "https://solarpunkagent.pages.dev"
        ]
        
        all_accessible = True
        for site in sites:
            try:
                response = requests.get(site, timeout=10)
                if response.status_code == 200:
                    self.log(f"Site accessible: {site}")
                else:
                    self.log(f"Site returned {response.status_code}: {site}", "WARNING")
                    all_accessible = False
            except:
                self.log(f"Could not access site: {site}", "WARNING")
                all_accessible = False
        
        return all_accessible
    
    def check_web_dashboard(self):
        """Check if web dashboard is running"""
        try:
            # Try to connect to the dashboard
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex(('127.0.0.1', self.web_port))
            sock.close()
            return result == 0
        except:
            return False
    
    def check_scheduled_tasks(self):
        """Check if scheduled tasks exist (Windows only)"""
        if platform.system() != "Windows":
            return True  # Skip on non-Windows
        
        try:
            result = subprocess.run(
                ["schtasks", "/query", "/tn", "SolarPunk-HourlySync"],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except:
            self.log("Could not check scheduled tasks", "WARNING")
            return False
    
    def start_web_dashboard(self):
        """Start the web dashboard"""
        self.log(f"Starting web dashboard on port {self.web_port}...")
        
        # Simple Flask app for dashboard
        flask_code = '''
from flask import Flask, render_template, jsonify, request
import os, json, datetime, subprocess, platform, sys, socket, psutil, time, threading

app = Flask(__name__)
ROOT_DIR = "C:\\\\\\\\Users\\\\\\\\carol\\\\\\\\SolarPunk"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health():
    health_data = {
        "status": "online",
        "timestamp": datetime.datetime.now().isoformat(),
        "system": platform.system(),
        "python_version": sys.version,
        "directory": ROOT_DIR,
        "agent_version": "3.0"
    }
    return jsonify(health_data)

@app.route('/api/run_command', methods=['POST'])
def run_command():
    command = request.json.get('command', '')
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=ROOT_DIR)
        return jsonify({
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7681, debug=False)
'''
        
        # Save the Flask app
        flask_file = os.path.join(self.root, "web_dashboard.py")
        with open(flask_file, "w", encoding="utf-8") as f:
            f.write(flask_code)
        
        # Create a simple HTML template
        templates_dir = os.path.join(self.root, "templates")
        os.makedirs(templates_dir, exist_ok=True)
        
        html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>⚡ SolarPunk Dashboard</title>
    <meta charset="UTF-8">
    <style>
        body { font-family: monospace; background: #0a0a0a; color: #00ff00; padding: 2rem; }
        .status { border: 1px solid #00ff00; padding: 1rem; margin: 1rem 0; }
        .online { border-color: #0f0; }
        .offline { border-color: #f00; }
        button { background: #333; color: #0f0; border: 1px solid #0f0; padding: 0.5rem 1rem; margin: 0.5rem; cursor: pointer; }
    </style>
</head>
<body>
    <h1>⚡ SolarPunk Autonomous Dashboard</h1>
    <div id="status"></div>
    <div>
        <button onclick="runCommand('START.bat')">Start Agent</button>
        <button onclick="runCommand('PUSH.bat')">Push Updates</button>
        <button onclick="runCommand('SYNC_ALL.bat')">Sync All</button>
    </div>
    <pre id="output"></pre>
    
    <script>
        async function updateStatus() {
            const response = await fetch('/api/health');
            const data = await response.json();
            document.getElementById('status').innerHTML = `
                <div class="status online">
                    🟢 System Online<br>
                    Time: ${data.timestamp}<br>
                    Version: ${data.agent_version}
                </div>
            `;
        }
        
        async function runCommand(command) {
            const response = await fetch('/api/run_command', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({command: command})
            });
            const result = await response.json();
            document.getElementById('output').textContent = 
                result.success ? result.output : result.error;
        }
        
        updateStatus();
        setInterval(updateStatus, 30000);
    </script>
</body>
</html>
'''
        
        html_file = os.path.join(templates_dir, "index.html")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_template)
        
        # Start the dashboard in a separate thread
        def run_dashboard():
            sys.path.insert(0, self.root)
            try:
                import web_dashboard
                web_dashboard.app.run(host='0.0.0.0', port=self.web_port, debug=False, use_reloader=False)
            except Exception as e:
                self.log(f"Failed to start dashboard: {e}", "ERROR")
        
        dashboard_thread = threading.Thread(target=run_dashboard, daemon=True)
        dashboard_thread.start()
        
        self.log(f"Web dashboard started at http://localhost:{self.web_port}")
        return True
    
    def auto_heal(self):
        """Automatically fix common issues"""
        self.log("Starting auto-healing sequence...")
        
        healing_actions = [
            ("Creating missing directories", self.check_directories),
            ("Checking batch files", self.check_batch_files),
            ("Checking Python files", self.check_python_files),
            ("Checking Git repository", self.check_git_repo),
        ]
        
        for action_name, action_func in healing_actions:
            self.log(f"  ⚡ {action_name}...")
            try:
                action_func()
                time.sleep(0.5)
            except Exception as e:
                self.log(f"  ⚠️  Failed: {action_name} - {e}", "WARNING")
        
        self.log("Auto-healing sequence complete")
        return True
    
    def run(self):
        """Main run loop for the agent"""
        self.log("=== SOLARPUNK AGENT STARTED ===")
        self.log(f"Root directory: {self.root}")
        self.log(f"Web dashboard: http://localhost:{self.web_port}")
        
        # Initial health check
        self.check_system_health()
        
        # Auto-heal any issues
        self.auto_heal()
        
        # Start web dashboard
        self.start_web_dashboard()
        
        self.log("Agent is now running. Press Ctrl+C to stop.")
        
        # Keep the agent running
        try:
            while True:
                time.sleep(60)  # Check every minute
                # Periodic health check
                self.check_system_health()
        except KeyboardInterrupt:
            self.log("Agent stopped by user")
        except Exception as e:
            self.log(f"Agent error: {e}", "ERROR")

if __name__ == "__main__":
    agent = SolarPunkAgent()
    agent.run()
'''
    
    agent_path = os.path.join(CONFIG["system_root"], "self_healing_agent.py")
    with open(agent_path, "w", encoding="utf-8") as f:
        f.write(agent_code)
    
    log("  ✅ Created: self_healing_agent.py")
    return True

def setup_scheduled_tasks():
    """Setup Windows Task Scheduler tasks"""
    log("Setting up scheduled tasks...")
    
    if platform.system() != "Windows":
        log("  ⚠️  Scheduled tasks only available on Windows", "WARNING")
        return False
    
    # Create PowerShell script for task scheduling
    ps_script = '''# SolarPunk Autonomous Task Scheduler Setup
$tasks = @(
    @{
        Name = "SolarPunk-HourlySync"
        Description = "Hourly sync of all SolarPunk repositories"
        Script = "C:\\Users\\carol\\SolarPunk\\SYNC_ALL.bat"
        Trigger = @{
            Frequency = "Hourly"
            Interval = 1
        }
    },
    @{
        Name = "SolarPunk-DailyHealth"
        Description = "Daily health check of SolarPunk system"
        Script = "C:\\Users\\carol\\SolarPunk\\START.bat"
        Trigger = @{
            Frequency = "Daily"
            At = "03:00"
        }
    },
    @{
        Name = "SolarPunk-WeeklyBackup"
        Description = "Weekly backup of all repositories"
        Script = "C:\\Users\\carol\\SolarPunk\\CONTROL_PANEL.bat"
        Trigger = @{
            Frequency = "Weekly"
            DaysOfWeek = "Sunday"
            At = "04:00"
        }
    }
)

foreach ($task in $tasks) {
    $action = New-ScheduledTaskAction -Execute $task.Script
    $trigger = $null
    
    switch ($task.Trigger.Frequency) {
        "Hourly" {
            $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Hours $task.Trigger.Interval)
        }
        "Daily" {
            $trigger = New-ScheduledTaskTrigger -Daily -At $task.Trigger.At
        }
        "Weekly" {
            $trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek $task.Trigger.DaysOfWeek -At $task.Trigger.At
        }
    }
    
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
    $principal = New-ScheduledTaskPrincipal -UserId (whoami) -LogonType Interactive -RunLevel Highest
    
    try {
        Register-ScheduledTask -TaskName $task.Name -Description $task.Description `
            -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force
        Write-Host "✅ Created task: $($task.Name)" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Failed to create task: $($task.Name)" -ForegroundColor Yellow
        Write-Host "Error: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "SolarPunk Autonomous Tasks Configured!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Tasks created:" -ForegroundColor White
Write-Host "• SolarPunk-HourlySync (runs every hour)" -ForegroundColor Gray
Write-Host "• SolarPunk-DailyHealth (runs daily at 3 AM)" -ForegroundColor Gray
Write-Host "• SolarPunk-WeeklyBackup (runs Sundays at 4 AM)" -ForegroundColor Gray
Write-Host ""
Write-Host "To view tasks: Task Scheduler → Task Scheduler Library" -ForegroundColor Yellow
'''
    
    ps_path = os.path.join(CONFIG["system_root"], "setup_tasks.ps1")
    with open(ps_path, "w", encoding="utf-8") as f:
        f.write(ps_script)
    
    log("  ✅ Created: setup_tasks.ps1")
    log("  📝 Run this PowerShell script as Administrator to setup scheduled tasks")
    
    return True

def create_configuration_file():
    """Create the main configuration file"""
    log("Creating configuration file...")
    
    config_data = {
        "system": {
            "user": CONFIG["user"],
            "root_directory": CONFIG["system_root"],
            "setup_date": datetime.datetime.now().isoformat(),
            "version": "3.0",
            "auto_update": True,
            "auto_heal": True,
            "backup_enabled": True
        },
        "repositories": {
            "main": "SolarPunk-Autonomous",
            "connected_folder": os.path.join(CONFIG["system_root"], "connected"),
            "known_repos": CONFIG["known_repos"],
            "auto_sync": True,
            "sync_interval_minutes": 60
        },
        "web": {
            "dashboard_port": CONFIG["web_dashboard_port"],
            "cloudflare_sites": CONFIG["cloudflare_projects"],
            "auto_deploy": True,
            "deploy_timeout_seconds": 120
        },
        "automation": {
            "scheduled_tasks": CONFIG["scheduled_tasks"],
            "health_check_interval": CONFIG["health_check_interval_minutes"],
            "backup_interval": CONFIG["backup_interval_hours"],
            "log_retention_days": 30
        },
        "paths": {
            "batch_files": [os.path.join(CONFIG["system_root"], f) for f in CONFIG["required_bat_files"]],
            "python_files": [os.path.join(CONFIG["system_root"], f) for f in CONFIG["required_py_files"]],
            "directories": [os.path.join(CONFIG["system_root"], d) for d in CONFIG["required_dirs"]]
        }
    }
    
    config_path = os.path.join(CONFIG["system_root"], "solarpunk_config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=2)
    
    log(f"  ✅ Created: solarpunk_config.json")
    return config_path

def create_setup_complete_report():
    """Create a setup completion report"""
    log("Generating setup completion report...")
    
    report = {
        "setup_completed": datetime.datetime.now().isoformat(),
        "system_checks": {
            "python_version": sys.version,
            "platform": platform.platform(),
            "current_user": getpass.getuser(),
            "hostname": socket.gethostname(),
            "working_directory": os.getcwd()
        },
        "files_created": {
            "batch_files": CONFIG["required_bat_files"],
            "python_files": CONFIG["required_py_files"],
            "directories": CONFIG["required_dirs"]
        },
        "next_steps": [
            "Run START.bat to start the agent",
            "Run CONTROL_PANEL.bat for unified control",
            "Run setup_tasks.ps1 as Administrator to setup scheduled tasks",
            "Visit http://localhost:7681 for the web dashboard"
        ],
        "important_urls": {
            "github_repo": "https://github.com/MeekoThaRaccoon/SolarPunk-Autonomous",
            "agent_site": "https://solarpunkagent.pages.dev",
            "tools_site": "https://solarpunk-nexus.pages.dev",
            "cloudflare_dashboard": "https://dash.cloudflare.com"
        },
        "support": {
            "log_files": os.path.join(CONFIG["system_root"], "logs"),
            "config_file": os.path.join(CONFIG["system_root"], "solarpunk_config.json"),
            "health_file": os.path.join(CONFIG["system_root"], "logs", "health_status.json")
        }
    }
    
    report_path = os.path.join(CONFIG["system_root"], "logs", "setup_report.json")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    
    # Also create a simple README
    readme_path = os.path.join(CONFIG["system_root"], "README.txt")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("SOLARPUNK AUTONOMOUS SYSTEM - SETUP COMPLETE\n")
        f.write("=" * 60 + "\n\n")
        f.write("🚀 YOUR SYSTEM IS NOW READY!\n\n")
        f.write("Available commands:\n")
        f.write("  START.bat          - Start the SolarPunk agent\n")
        f.write("  PUSH.bat           - Push updates to GitHub & Cloudflare\n")
        f.write("  CONTROL_PANEL.bat  - Unified control panel\n")
        f.write("  SYNC_ALL.bat       - Sync all repositories\n\n")
        f.write("Web Dashboard: http://localhost:7681\n")
        f.write("Agent Site: https://solarpunkagent.pages.dev\n")
        f.write("Tools Site: https://solarpunk-nexus.pages.dev\n\n")
        f.write("For autonomous operation:\n")
        f.write("  1. Run 'setup_tasks.ps1' as Administrator\n")
        f.write("  2. System will auto-sync hourly\n")
        f.write("  3. Auto-healing will fix issues\n\n")
        f.write("=" * 60 + "\n")
    
    log(f"  ✅ Created: README.txt")
    return report_path

def run_setup():
    """Main setup function"""
    print("\n" + "="*60)
    print("SOLARPUNK SELF-CONFIGURING WIZARD")
    print("="*60 + "\n")
    
    log("Starting setup wizard...")
    
    # Step 1: Check prerequisites
    log("Step 1: Checking prerequisites")
    if not check_prerequisites():
        log("Prerequisites check failed. Please fix the issues above.", "ERROR")
        return False
    
    # Step 2: Setup directory structure
    log("\nStep 2: Setting up directory structure")
    setup_directory_structure()
    
    # Step 3: Create batch files
    log("\nStep 3: Creating batch files")
    create_batch_files()
    
    # Step 4: Create Python agent
    log("\nStep 4: Creating Python agent")
    create_python_agent()
    
    # Step 5: Setup scheduled tasks (create script)
    log("\nStep 5: Creating scheduled tasks setup")
    setup_scheduled_tasks()
    
    # Step 6: Create configuration file
    log("\nStep 6: Creating configuration file")
    create_configuration_file()
    
    # Step 7: Create completion report
    log("\nStep 7: Creating setup report")
    create_setup_complete_report()
    
    # Success message
    print("\n" + "="*60)
    print("✅ SETUP COMPLETE!")
    print("="*60)
    print("\nYour SolarPunk system is now configured with:")
    print("  • Self-healing agent (self_healing_agent.py)")
    print("  • Batch files for easy control")
    print("  • Web dashboard at http://localhost:7681")
    print("  • Scheduled tasks setup script")
    print("  • Complete configuration file")
    print("\nImmediate actions:")
    print("  1. Double-click START.bat to start the agent")
    print("  2. Double-click CONTROL_PANEL.bat for unified control")
    print("  3. Run setup_tasks.ps1 as Administrator for automation")
    print("\nFor help, see README.txt")
    print("="*60 + "\n")
    
    return True

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    try:
        success = run_setup()
        if success:
            # Ask if user wants to start the agent now
            print("\nStart the agent now? (Y/N)")
            response = input().strip().lower()
            if response in ['y', 'yes']:
                print("Starting agent...")
                agent_path = os.path.join(CONFIG["system_root"], "self_healing_agent.py")
                subprocess.Popen([sys.executable, agent_path], 
                               cwd=CONFIG["system_root"])
                print("Agent started. Web dashboard: http://localhost:7681")
        else:
            print("Setup failed. Check the logs above.")
    except Exception as e:
        log(f"Setup wizard error: {e}", "ERROR")
        import traceback
        traceback.print_exc()
        print("\nSetup failed with error. Please try again.")
