#!/usr/bin/env python3
"""
SolarPunk Autonomous Agent
Main control interface for your system
"""

import os
import sys
import subprocess
from datetime import datetime

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the agent header"""
    clear_screen()
    print("\n" + "="*60)
    print("          SOLARPUNK AUTONOMOUS AGENT v2.0")
    print("="*60)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"User: MeekoThaRaccoon")
    print(f"Cloudflare: https://solarpunkagent.pages.dev")
    print("="*60)

def run_diagnostics():
    """Run system diagnostics"""
    print("\n[RUNNING DIAGNOSTICS]")
    print("-"*40)
    
    # Check Git status
    print("Checking Git repositories...")
    try:
        result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
        if 'MeekoThaRaccoon' in result.stdout:
            print("✓ Connected to GitHub")
        else:
            print("✗ GitHub connection issue")
    except:
        print("✗ Git not available")
    
    # Check Cloudflare
    print("\nChecking Cloudflare...")
    try:
        import requests
        response = requests.get('https://solarpunkagent.pages.dev', timeout=5)
        print(f"✓ Website online (HTTP {response.status_code})")
    except:
        print("✗ Website check failed")
    
    # Check Python
    print(f"\nPython: {sys.version}")
    
    input("\nPress Enter to continue...")

def deploy_website():
    """Deploy website to Cloudflare"""
    print("\n[DEPLOYING WEBSITE]")
    print("-"*40)
    
    # Get current directory
    current_dir = os.getcwd()
    
    # Check if dist folder exists
    dist_path = os.path.join(current_dir, 'dist')
    if os.path.exists(dist_path):
        print("✓ Found dist folder")
        
        # List files in dist
        files = os.listdir(dist_path)
        print(f"  Files: {len(files)}")
        for file in files[:5]:  # Show first 5 files
            print(f"  - {file}")
        if len(files) > 5:
            print(f"  ... and {len(files)-5} more")
    else:
        print("✗ No dist folder found")
        print("  Create one with: mkdir dist")
    
    # Ask to deploy
    print("\nDeploy to GitHub? (y/n): ", end='')
    choice = input().strip().lower()
    
    if choice == 'y':
        print("\nDeploying...")
        try:
            # Add all files
            subprocess.run(['git', 'add', '.'], check=True)
            
            # Commit
            subprocess.run(['git', 'commit', '-m', f'Deploy: {datetime.now()}'], 
                          check=True, capture_output=True)
            
            # Push
            result = subprocess.run(['git', 'push', 'origin', 'master'], 
                                   capture_output=True, text=True)
            if result.returncode == 0:
                print("✓ Successfully deployed!")
                print("  Cloudflare will auto-deploy in 1-2 minutes")
                print("  Check: https://solarpunkagent.pages.dev")
            else:
                print("✗ Push failed")
                print(f"  Error: {result.stderr[:100]}")
        except Exception as e:
            print(f"✗ Deployment error: {e}")
    
    input("\nPress Enter to continue...")

def fix_repositories():
    """Fix all repository connections"""
    print("\n[FIXING REPOSITORIES]")
    print("-"*40)
    
    print("This will fix all Git remotes to use MeekoThaRaccoon")
    print("\nRepositories to fix:")
    print("1. SolarPunk-Autonomous (this one)")
    print("2. SolarPunk-Nexus (web_dashboard)")
    print("3. SolarPunk-Memvid (memvid_repo)")
    print("4. Others as needed")
    
    print("\nRun fix? (y/n): ", end='')
    choice = input().strip().lower()
    
    if choice == 'y':
        print("\nFixing...")
        
        # This is where you'd run your quick_fix.py
        try:
            import quick_fix
            quick_fix.fix_git_remotes()
            print("✓ Repositories fixed!")
        except:
            print("✗ Could not run fix script")
            print("  Run: python quick_fix.py manually")
    
    input("\nPress Enter to continue...")

def check_cloudflare():
    """Check Cloudflare status"""
    print("\n[CLOUDFLARE STATUS]")
    print("-"*40)
    
    print("Live URLs:")
    print("  • https://solarpunkagent.pages.dev")
    print("  • https://0499a26f.solarpunkagent.pages.dev")
    
    print("\nDashboard:")
    print("  • https://dash.cloudflare.com")
    
    print("\nGitHub App:")
    print("  • https://github.com/apps/cloudflare-pages")
    
    print("\nAuto-deploy is ENABLED")
    print("Any push to SolarPunk-Autonomous will auto-deploy")
    
    input("\nPress Enter to continue...")

def main_menu():
    """Main agent menu"""
    while True:
        print_header()
        
        print("\nMAIN MENU:")
        print("1. Run Diagnostics")
        print("2. Deploy Website")
        print("3. Fix Repositories")
        print("4. Check Cloudflare")
        print("5. Open SolarPunk Folder")
        print("6. Exit Agent")
        
        print("\n" + "-"*30)
        choice = input("Select option (1-6): ").strip()
        
        if choice == '1':
            run_diagnostics()
        elif choice == '2':
            deploy_website()
        elif choice == '3':
            fix_repositories()
        elif choice == '4':
            check_cloudflare()
        elif choice == '5':
            print("\nOpening SolarPunk folder...")
            os.startfile("C:\\Users\\carol\\SolarPunk")
        elif choice == '6':
            print("\nAgent shutting down. Goodbye!")
            break
        else:
            print("\nInvalid choice. Press Enter to try again.")
            input()

if __name__ == "__main__":
    print("Agent starting...")
    main_menu()
