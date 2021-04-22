# Schiffeversenken
## Voraussetzungen
Installiere benötigte Libarys via pipenv (Recomendet):
```bash
pipenv install
```
via pip und requirements.txt
```bash
pip install -r requirements.txt
```
- Python-Version: 3.9+
- Keyboard-Version: 0.13.5
- Sudo Rechte unter Linux (da /dev/keyboard abgehört wird)

## Spielen
Es gelten die allgemeinen Regeln für Schiffeversenken [[Wiki](https://de.wikipedia.org/wiki/Schiffe_versenken)]
### Spiel starten
Windows:
```bash
python.exe .\starter.py
```
Linux:
```bash
sudo python ./starter.py
```
### Spielstand speichern
Zu einem beliebigen Zeitpunkt die Tastenkombination `strg + s` drücken<br>
Am ende vom Zug wird der Speicherpfad abgefragt (Optional) - Default ist das aktuelle Datum als Name
### Spielstand Laden
Das Spiel normal starten und die Option 2 im Menü auswählen. Anschließend den Pfad zum gespeicherten Spielstand eingeben
