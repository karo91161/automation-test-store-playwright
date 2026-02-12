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

    run_command("pip install pytest-html")
    
    run_command("playwright install chromium")
    
    print("\n" + "="*40)
    print("Telepítés sikeres!")
    print("Most már futtathatod a tesztet:")
    print("Sima futtatás:  pytest")
    print("HTML riporttal: pytest --html=report.html --self-contained-html")
    print("="*40)

if __name__ == "__main__":
    main()