# EINHAUS Prozesslandschaft

Zentrales Hauptboard der EINHAUS Oberfl&auml;chenveredelung GmbH. Oben stehen die Prozesse
(gruppiert nach Bereichen); hinter jedem Prozess werden die Dashboards **direkt hier** aufgebaut.

Live: siehe GitHub-Pages-URL des Repos (`https://<konto>.github.io/prozesslandschaft/`).

## Aufbau

```
index.html            Prozesslandschaft (Ebene 1) - wird vom Generator erzeugt
assets/style.css      gemeinsames Design (nur hier aendern -> wirkt ueberall)
assets/hub.js         Theme-Umschalter + Datum
assets/_TEMPLATE_prozess.html   Kopiervorlage fuer ein neues Prozess-Dashboard
<prozess>/index.html  Unter-Dashboard des Prozesses (Ebene 2)
build_prozesslandschaft.py      Generator
```

## Ein Dashboard hinter einem Prozess aufbauen

1. Ordner des Prozesses oeffnen (z. B. `eol/`).
2. `assets/_TEMPLATE_prozess.html` als Startpunkt kopieren **oder** die vorhandene `index.html`
   des Prozesses bearbeiten.
3. Titel anpassen und je Tool eine Kachel eintragen (Block `<a class="tool-card"> ... </a>`).
   Eigene Tools als eigene `.html`-Datei im selben Prozess-Ordner ablegen und im `href` verlinken.
4. Speichern und committen (bzw. ueber GitHub hochladen).

> Design nie pro Seite kopieren - immer `assets/style.css` verwenden, damit alles einheitlich bleibt.

## Neuen Prozess ergaenzen

In `build_prozesslandschaft.py` die Liste `STRUCTURE` erweitern und das Skript erneut ausfuehren:

```
python build_prozesslandschaft.py
```

Der Generator erzeugt `index.html` neu und legt fehlende Prozess-Gerueste an.
**Bereits vorhandene Prozess-Seiten werden nicht ueberschrieben** (Kollegen-Inhalte bleiben erhalten).

## Zugriff

Mitarbeit ueber GitHub (als Collaborator mit Schreibrecht). Zugaenge bitte selbst anlegen /
den Repo-Owner um Einladung bitten - keine Passwoerter im Chat teilen.
