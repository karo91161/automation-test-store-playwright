# Automation Test Store - E2E Purchase

Ez a projekt egy End-to-End (E2E) automatizált tesztet valósít meg az Automation Test Store weboldalon. Teszt menete:

- Regisztráció: Új fiókot hoz létre egyedi, időbélyeggel ellátott adatokkal.
- Termékválasztás: Megkeresi a pólókat, majd ár szerint csökkenő sorrendbe rendezi őket.
- Kosárba tétel: Kiválasztja és kosárba teszi a két legdrágább elérhető pólót.
- Rendelés: Végigviszi a checkout folyamatot és megerősíti a vásárlást.
- Ellenőrzés: Validálja a sikeres rendelésről szóló visszaigazolást.

## 🛠️ Telepítés és futtatás

A projekt tartalmaz egy automatizált telepítő szkriptet, amely gondoskodik a Python függőségekről és a szükséges böngészőmotorról.

1. Klónozd a repository-t:
   `git clone https://github.com/karo91161/automation-test-store-playwright.git .`
2. Nyiss egy terminált a projekt gyökérmappájában. _Megjegyzés: Javasolt virtuális környezet (venv) használata, de anélkül is működik._
3. Futtasd a telepítő szkriptet:
   ```bash
   python setup_project.py
   ```
4. Teszt futtatása: `python -m pytest` parancs segítségével.

## 🆘 Manuális telepítés (ha a szkript nem futna)

Ha a setup_project.py hibaüzenetet dobna vagy elakadna, kövesd az alábbi lépéseket a környezet kézi beállításához:

Függőségek telepítése:

```bash
pip install -r requirements.txt
playwright install chromium
```
