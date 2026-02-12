import subprocess
import sys

def run_command(command):
    print(f"Futtatás: {command}")
    try:
        subprocess.check_call([sys.executable, "-m"] + command.split())
    except subprocess.CalledProcessError as e:
        print(f"Hiba történt: {e}")
        sys.exit(1)

def main():
    print("--- Automation Test Telepítő ---")
    
    run_command("pip install --upgrade pip")
    
    run_command("pip install -r requirements.txt")
    
    run_command("playwright install chromium")
    
    print("\n✅ Telepítés sikeres! Most már futtathatod a tesztet a 'pytest' paranccsal.")

if __name__ == "__main__":
    main()