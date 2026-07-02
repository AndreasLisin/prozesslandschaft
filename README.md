# EINHAUS Prozesslandschaft

Zentrales Hauptboard der EINHAUS Oberflächenveredelung GmbH. Oben stehen die Prozesse
(gruppiert nach Bereichen); hinter jedem Prozess werden die Dashboards **direkt hier** aufgebaut.

**Live:** https://andreaslisin.github.io/prozesslandschaft/

## So funktioniert es

Die komplette Prozesslandschaft wird aus **einer einzigen Datei** aufgebaut: **`struktur.js`**.
Dort stehen alle Gruppen, Prozesse und die Dashboards je Prozess. Zum Ändern braucht man **kein
Python und keinen Build** – einfach `struktur.js` bearbeiten, speichern, fertig.

```
index.html      Prozesslandschaft (wird aus struktur.js aufgebaut)
prozess.html    Prozess-Unterseite (wird aus struktur.js aufgebaut)
struktur.js     >>> HIER wird alles gepflegt <<<  (Gruppen, Prozesse, Dashboards)
assets/style.css   gemeinsames Design (nur hier ändern -> wirkt überall)
assets/render.js   Aufbaulogik (normalerweise nicht anfassen)
assets/hub.js      Hell/Dunkel-Umschalter + Datum
assets/_TEMPLATE_dashboard.html   Starter-Vorlage für ein eigenes Tool
```

## Prozesslandschaft anpassen (Gruppe/Prozess ändern, hinzufügen, umbenennen)

1. Auf GitHub die Datei **`struktur.js`** öffnen → Bleistift-Symbol (Bearbeiten).
2. Ändern:
   - **Prozess umbenennen:** `name` anpassen.
   - **Neuen Prozess anlegen:** in der passenden Gruppe ergänzen:
     `{ name: "Mein Prozess", slug: "mein-prozess" }`
     (slug = kleingeschrieben, keine Umlaute/Leerzeichen → Bindestriche).
   - **Neue Gruppe anlegen:** einen weiteren `{ titel: "…", prozesse: [ … ] }`-Block ergänzen.
   - **Reihenfolge:** entspricht der Reihenfolge in der Liste.
3. Unten **„Commit changes"** klicken. Nach ~1 Minute ist die Änderung live.

> Auf Kommas und Klammern achten. Im Zweifel eine bestehende Zeile kopieren und anpassen.

## Dashboard hinter einem Prozess ergänzen

1. Eigene HTML-Seite bauen (Starter: `assets/_TEMPLATE_dashboard.html` kopieren) und in den
   Ordner des Prozesses legen, z. B. `eol/mein_dashboard.html`.
   (Auf GitHub: „Add file → Upload files" bzw. „Create new file" mit Pfad `eol/mein_dashboard.html`.)
2. In `struktur.js` beim passenden Prozess einen `tiles`-Eintrag ergänzen:
   ```js
   { name: "Paint Shop", slug: "paint-shop", tiles: [
       { name: "Mein Dashboard", url: "eol/mein_dashboard.html", beschreibung: "Kurze Erklärung." }
   ]}
   ```
3. Commit → nach ~1 Minute live. Externe Links (mit `https://…`) öffnen in einem neuen Tab.

## Zugriff

Mitarbeit über GitHub als **Collaborator** – damit hat man **volles Schreibrecht auf alle Dateien**
(Prozesslandschaft, Dashboards, Design). Konto anlegen auf https://github.com/signup, den
**Benutzernamen** dem Repo-Owner nennen → Einladung annehmen. Keine Passwörter teilen.
