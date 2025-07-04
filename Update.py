#!/usr/bin/env python3
# update.py - Auto updater for kali tool
# @ CREATE BY YATHARTH

import os
import shutil

def banner():
    print("\033[1;92m")
    print("  ██████╗ ██╗   ██╗████████╗██╗  ██╗ █████╗  ██████╗ ████████╗██╗  ██╗ ")
    print("  ██╔══██╗██║   ██║╚══██╔══╝██║  ██║██╔══██╗██╔═══██╗╚══██╔══╝██║  ██║ ")
    print("  ██████╔╝██║   ██║   ██║   ███████║███████║██║   ██║   ██║   ███████║ ")
    print("  ██╔═══╝ ██║   ██║   ██║   ██╔══██║██╔══██║██║   ██║   ██║   ██╔══██║ ")
    print("  ██║     ╚██████╔╝   ██║   ██║  ██║██║  ██║╚██████╔╝   ██║   ██║  ██║ ")
    print("  ╚═╝      ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ")
    print("\033[1;93m")
    print("                @ CREATE BY YATHARTH - Auto Updater")
    print("\033[0m")

def remove_old_tool():
    if os.path.exists("kali"):
        print("\033[1;91m[*] Removing old 'kali' directory...\033[0m")
        shutil.rmtree("kali")
        print("\033[1;92m[+] Removed successfully.\033[0m")
    else:
        print("\033[1;93m[*] 'kali' directory not found, skipping removal.\033[0m")

def clone_new_tool():
    print("\033[1;94m[*] Cloning new tool from GitHub...\033[0m")
    os.system("git clone https://github.com/riti-web/YT.git")
    print("\033[1;92m[+] Cloned successfully.\033[0m")

if __name__ == "__main__":
    banner()
    remove_old_tool()
    clone_new_tool()
