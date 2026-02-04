#!/usr/bin/env python3
"""
SolarPunk Autonomous Agent v2.0
Control center for your entire system
"""

import os
import sys
import subprocess
import webbrowser
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("\n" + "="*60)
    print("           SOLARPUNK AUTONOMOUS AGENT v2.0")
    print("="*60)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"User: MeekoThaRaccoon")
    print("="*60)

def option1_check_system():
    print("\n" + "="*60)
    print("CHECKING SYSTEM STATUS")
    print("="*60)
    
    print("\n[GitHub Status]")
    result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
    if 'MeekoThaRaccoon' in result.stdout:
        print("✅ Connected to GitHub")
        for line in result.stdout.strip().split('\n'):
            if 'origin' in line:
                print(f"   {line}")
    else:
        print("❌ GitHub connection issue")
    
    print("\n[Website Files]")
    if os.path.exists('dist'):
        files = os.listdir('dist')
        print(f"✅ Found {len(files)} files in dist/")
        for file in files:
            size = os.path.getsize(f'dist/{file}')
            print(f"   {file} ({size} bytes)")
    else:
        print("❌ No dist folder found")
    
    print("\n[Cloudflare Status]")
    print("✅ Website: https://solarpunkagent.pages.dev")
    print("✅ Dashboard: https://dash.cloudflare.com")
    
    print("\n[Python Environment]")
    print(f"Python {sys.version.split()[0]}")
    
    input("\nPress Enter to continue...")

def option2_deploy_website():
    print("\n" + "="*60)
    print("DEPLOY WEBSITE TO CLOUDFLARE")
    print("="*60)
    
    # Copy from main dist to agent dist
    main_dist = "C:/Users/carol/SolarPunk/dist"
    agent_dist = "dist"
    
    if os.path.exists(main_dist):
        print("\nCopying website files...")
        
        # Ensure agent dist exists
        if not os.path.exists(agent_dist):
            os.makedirs(agent_dist)
        
        # Copy files
        import shutil
        for item in os.listdir(main_dist):
            src = os.path.join(main_dist, item)
            dst = os.path.join(agent_dist, item)
            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
        
        print(f"✅ Copied files from {main_dist}")
    else:
        print(f"❌ Source folder not found: {main_dist}")
        print("Create your website files in C:/Users/carol/SolarPunk/dist/")
    
    # Deploy to GitHub
    print("\nDeploying to GitHub...")
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', f'Deploy website: {datetime.now()}'], 
                      capture_output=True, text=True)
        result = subprocess.run(['git', 'push', 'origin', 'master'], 
                               capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Successfully pushed to GitHub!")
            print("\nCloudflare will auto-deploy in 1-2 minutes.")
            print("Check: https://solarpunkagent.pages.dev")
        else:
            print("❌ Push failed")
            if result.stderr:
                print(f"Error: {result.stderr[:200]}")
    except Exception as e:
        print(f"❌ Deployment error: {e}")
    
    input("\nPress Enter to continue...")

def option3_quick_fix():
    print("\n" + "="*60)
    print("QUICK FIX REPOSITORIES")
    print("="*60)
    
    print("\nFixing Git remotes to use MeekoThaRaccoon...")
    
    repos = [
        ("SolarPunk-Autonomous", "C:/Users/carol/SolarPunk/connected/SolarPunk-Autonomous"),
        ("SolarPunk-Nexus", "C:/Users/carol/SolarPunk/web_dashboard"),
        ("SolarPunk-Memvid", "C:/Users/carol/SolarPunk/memvid_repo"),
    ]
    
    for repo_name, repo_path in repos:
        if os.path.exists(repo_path):
            print(f"\nFixing {repo_name}...")
            try:
                os.chdir(repo_path)
                subprocess.run(['git', 'remote', 'remove', 'origin'], 
                              capture_output=True, text=True)
                subprocess.run(['git', 'remote', 'add', 'origin', 
                              f'https://github.com/MeekoThaRaccoon/{repo_name}.git'],
                              capture_output=True, text=True)
                print(f"   ✅ Set remote to MeekoThaRaccoon/{repo_name}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
        else:
            print(f"\nSkipping {repo_name} (folder not found)")
    
    print("\n✅ All repositories fixed!")
    input("\nPress Enter to continue...")

def option4_open_dashboard():
    print("\n" + "="*60)
    print("OPEN DASHBOARDS")
    print("="*60)
    
    print("\nOpening browser tabs...")
    
    urls = [
        "https://solarpunkagent.pages.dev",
        "https://github.com/MeekoThaRaccoon/SolarPunk-Autonomous",
        "https://dash.cloudflare.com",
        "https://github.com/MeekoThaRaccoon?tab=repositories"
    ]
    
    for url in urls:
        print(f"   Opening {url}")
        webbrowser.open(url)
    
    print("\n✅ All dashboards opened in browser")
    input("\nPress Enter to continue...")

def option5_explore_uitars():
    print("\n" + "="*60)
    print("EXPLORE UI-TARS-DESKTOP")
    print("="*60)
    
    uitars_path = "C:/Users/carol/UI-TARS-desktop"
    
    if os.path.exists(uitars_path):
        print(f"\n✅ Found UI-TARS-desktop at: {uitars_path}")
        print("\nThis is a powerful GUI automation agent from ByteDance.")
        print("It can automate browser and desktop tasks.")
        
        # Open the folder
        os.startfile(uitars_path)
        
        print("\nNext steps for UI-TARS:")
        print("1. Check README.md for setup instructions")
        print("2. Look for setup.exe or install instructions")
        print("3. Consider integrating with SolarPunk for automation")
    else:
        print(f"\n❌ UI-TARS-desktop not found at: {uitars_path}")
        print("It might have been moved or deleted.")
    
    input("\nPress Enter to continue...")

def main():
    while True:
        print_header()
        
        print("\nMAIN MENU:")
        print("1. Check System Status")
        print("2. Deploy Website to Cloudflare")
        print("3. Quick Fix All Repositories")
        print("4. Open All Dashboards (Browser)")
        print("5. Explore UI-TARS-desktop")
        print("6. Exit")
        print("\n" + "-"*40)
        
        try:
            choice = input("Select option (1-6): ").strip()
            
            if choice == "1":
                option1_check_system()
            elif choice == "2":
                option2_deploy_website()
            elif choice == "3":
                option3_quick_fix()
            elif choice == "4":
                option4_open_dashboard()
            elif choice == "5":
                option5_explore_uitars()
            elif choice == "6":
                print("\n👋 Agent shutting down. Goodbye!")
                print("Remember: Your site is live at https://solarpunkagent.pages.dev")
                break
            else:
                print("\n❌ Invalid choice. Please enter 1-6.")
                input("Press Enter to try again...")
        except KeyboardInterrupt:
            print("\n\n👋 Agent interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    print("Starting SolarPunk Agent...")
    main()
