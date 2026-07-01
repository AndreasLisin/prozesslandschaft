# -*- coding: utf-8 -*-
"""
Generator fuer die EINHAUS Prozesslandschaft (zentrales Hauptboard).

- Erzeugt das gemeinsame Design (assets/style.css, assets/hub.js), den Hub (index.html),
  je Prozess ein Unter-Dashboard, die Kopiervorlage und die README.
- Regel zum Schutz von Kollegen-Inhalten:
    * Prozess MIT kuratierten Kacheln (tiles = Liste)  -> wird IMMER neu erzeugt (gehoert uns).
    * Prozess OHNE Kacheln (tiles = None)              -> Geruest nur anlegen, wenn noch nicht vorhanden.
  Ein Kollege bearbeitet also gefahrlos "seinen" Prozess-Ordner; ein erneuter Lauf ueberschreibt ihn nicht.

Neuen Prozess ergaenzen: in STRUCTURE eintragen und dieses Skript erneut ausfuehren.
"""

import os
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))
LACK = "https://andreaslisin.github.io/lackierung-dashboard/"


def url(path):
    return LACK + quote(path, safe="/")


# ---------------------------------------------------------------------------
# SVG-Icons (feather-Stil, Innen-Pfade)
# ---------------------------------------------------------------------------
ICONS = {
    "doc":       '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>',
    "wrench":    '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "check":     '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
    "pencil":    '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>',
    "grid":      '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    "activity":  '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    "bars":      '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><path d="M3 20h18"/>',
    "droplet":   '<path d="M12 2a10 10 0 1 0 0 20c1.1 0 2-.9 2-2 0-.5-.2-1-.5-1.3-.3-.4-.5-.8-.5-1.2 0-.8.7-1.5 1.5-1.5H17a5 5 0 0 0 5-5c0-4.4-4.5-8-10-8z"/><circle cx="7.5" cy="11.5" r="1.2"/><circle cx="12" cy="7.5" r="1.2"/><circle cx="16.5" cy="11.5" r="1.2"/>',
    "layers":    '<rect x="2" y="3" width="20" height="5" rx="1"/><rect x="2" y="10" width="20" height="5" rx="1"/><rect x="2" y="17" width="20" height="5" rx="1"/>',
    "plus":      '<line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>',
}


def T(name, slug, tiles=None):
    return {"name": name, "slug": slug, "tiles": tiles}


# ---------------------------------------------------------------------------
# Paint-Shop-Unterboard: die bestehenden Lackierung-Tools (Live-URLs)
# ---------------------------------------------------------------------------
PAINT_SHOP_TILES = [
    {"name": "Wartungsübersicht",             "icon": "wrench",   "url": url("01_Wartungsübersicht/Wartung_Anlagen.html"),
     "desc": "Wartungstermine aller Anlagen mit E-Mail-Erinnerung."},
    {"name": "Rüstfreigabe Roboter",          "icon": "check",    "url": url("03_Rüstfreigabe_Lackierroboter/Ruestfreigabe_Checkliste.html"),
     "desc": "Pre-Release-Checkliste Lackier- & Beflammroboter (FB-96/FB-95)."},
    {"name": "Eingabe Rüstfreigabe Kabinen",  "icon": "pencil",   "url": url("04_Rüstfreigabe_Lackierkabinen/Ruestfreigabe_Mobil.html"),
     "desc": "Checkliste Lackierkabinen ausfüllen (FB-64)."},
    {"name": "Rüstfreigabe Kabinen",          "icon": "grid",     "url": url("04_Rüstfreigabe_Lackierkabinen/Ruestfreigabe_Dashboard.html"),
     "desc": "Echtzeit-Übersicht der Rüstfreigaben Lackierkabinen."},
    {"name": "OEE Auswertung Lackierroboter", "icon": "activity", "url": url("06_OEE_Kabine1/OEE_Auswertung.html"),
     "desc": "OEE-Kennzahlen, Trend & Störungspareto Kabine 1."},
    {"name": "OEE Eingabe Lackierroboter",    "icon": "bars",     "url": url("06_OEE_Kabine1/OEE_Kabine1_Tablet.html"),
     "desc": "Schichterfassung für den Lackierroboter."},
    {"name": "OEE Auswertung Beflammroboter", "icon": "activity", "url": url("07_OEE_Beflammroboter/OEE_Auswertung.html"),
     "desc": "OEE-Kennzahlen, Trend & Störungspareto Beflammroboter."},
    {"name": "OEE Eingabe Beflammroboter",    "icon": "bars",     "url": url("07_OEE_Beflammroboter/OEE_Beflammroboter_Tablet.html"),
     "desc": "Schichterfassung für den Beflammroboter."},
    {"name": "Schulungsnachweis Q-Zirkel",    "icon": "doc",      "url": url("09_Schulungsnachweis/Schulungsnachweis_Ausschuss.html"),
     "desc": "Nachweis der morgendlichen Unterweisung (n.i.O.-Teile)."},
    {"name": "Spies Hecker Lackformeln",      "icon": "droplet",  "url": url("08_Lackformeln/Lackformeln_Dashboard.html"),
     "desc": "Mischformeln durchsuchen, Mengenrechner & Neuanlage."},
    {"name": "Lackaufbauten",                 "icon": "layers",   "url": url("10_Lackaufbauten/index.html"),
     "desc": "Materialblöcke & kompletter Aufbau je Farbton."},
]


# ---------------------------------------------------------------------------
# Prozesslandschaft (bestaetigt aus den beiden Screenshots)
# ---------------------------------------------------------------------------
STRUCTURE = [
    ("Unternehmensleitung", [
        T("Risikomanagement", "risikomanagement"),
        T("Unternehmenspolitik und Strategie", "unternehmenspolitik-und-strategie"),
        T("Nachhaltigkeit", "nachhaltigkeit"),
    ]),
    ("Managementsysteme", [
        T("Arbeits- und Gesundheitsmanagement", "arbeits-und-gesundheitsmanagement"),
        T("Qualitätsmanagement IATF 16949", "qualitaetsmanagement-iatf-16949"),
    ]),
    ("KVP", [
        T("KVP", "kvp"),
    ]),
    ("Vertrieb", [
        T("Vertrieb", "vertrieb"),
    ]),
    ("Supply Chain Management SCM", [
        T("Logistik", "logistik"),
        T("Produktionsplanung", "produktionsplanung"),
        T("Beschaffung Anlagen Werkzeuge", "beschaffung-anlagen-werkzeuge"),
        T("Beschaffung Setzteile", "beschaffung-setzteile"),
        T("Beschaffung Hilfs- u. Betriebsstoffe", "beschaffung-hilfs-u-betriebsstoffe"),
        T("Beschaffung Produktionsmaterial", "beschaffung-produktionsmaterial"),
    ]),
    ("Produktion", [
        T("Paint Shop", "paint-shop", PAINT_SHOP_TILES),
        T("EOL", "eol"),
    ]),
    ("Ressourcen", [
        T("Werk, Anlagen und Einrichtungen", "werk-anlagen-und-einrichtungen"),
        T("Personelle Ressourcen", "personelle-ressourcen"),
    ]),
    ("Wartung - und Instandhaltungsmanagement", [
        T("Instandhaltung", "instandhaltung"),
    ]),
    ("IT", [
        T("IT", "it"),
    ]),
    ("Projektmanagement", [
        T("Projektmanagement", "projektmanagement"),
    ]),
    ("Qualitätssicherung", [
        T("Prüfprozesse", "pruefprozesse"),
    ]),
]


# ---------------------------------------------------------------------------
# Design (gemeinsames Stylesheet + JS)
# ---------------------------------------------------------------------------
STYLE_CSS = """/* EINHAUS Prozesslandschaft - gemeinsames Design (aus dem Lackier-Dashboard abgeleitet) */
@import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&display=swap');

:root{
  --primary:#1a3a5c; --primary-light:#2558a0; --border:#c0ccd8; --bg:#f4f6f9;
  --card:#ffffff; --header:#ffffff; --footer:#ffffff; --text:#1a2535; --text-muted:#5a6a7a;
  --icon-bg:#e8eef7; --logo-text:#111; --logo-tagline:#444; --divider:#c0ccd8;
}
[data-theme="dark"]{
  --primary:#4a8fd4; --primary-light:#6aaee8; --border:#2e3c4e; --bg:#0f1923;
  --card:#1a2635; --header:#111e2d; --footer:#111e2d; --text:#e0eaf4; --text-muted:#7a9ab8;
  --icon-bg:#1e3048; --logo-text:#ffffff; --logo-tagline:#aaaaaa; --divider:#2e3c4e;
}

*{box-sizing:border-box;margin:0;padding:0}
html,body{min-height:100%;font-family:Arial,Helvetica,sans-serif;background:var(--bg);color:var(--text);
  display:flex;flex-direction:column;transition:background .25s,color .25s}

header{background:var(--header);padding:18px 32px;box-shadow:0 2px 8px rgba(0,0,0,.15);
  display:flex;align-items:center;gap:24px;flex-shrink:0;z-index:10;transition:background .25s}
.logo-wrap{display:flex;flex-direction:column;gap:6px}
.logo-text{font-size:38px;font-weight:900;letter-spacing:4px;color:var(--logo-text);line-height:1;
  font-family:'Comfortaa','Arial Black',Arial,sans-serif;transition:color .25s}
.logo-sub-row{display:flex;align-items:center;gap:10px}
.logo-stripes{display:flex;gap:3px;height:12px}
.logo-stripes span{display:block;width:16px;height:12px;transform:skewX(-18deg)}
.s1{background:#c0c0c0}.s2{background:#ffd400}.s3{background:#44bef0}.s4{background:#3aaa35}
.s5{background:#e8007d}.s6{background:#e83010}.s7{background:#1155bb}
.logo-tagline{font-size:10px;font-weight:bold;letter-spacing:1.5px;color:var(--logo-tagline);text-transform:uppercase}
.header-divider{width:1px;height:52px;background:var(--divider);margin:0 8px;flex-shrink:0}
.header-info{display:flex;flex-direction:column}
.header-title{font-size:20px;font-weight:bold;color:var(--primary);letter-spacing:.5px}
.header-subtitle{font-size:12px;color:var(--text-muted);margin-top:3px}

.header-right{margin-left:auto;display:flex;align-items:center;gap:12px}
.btn-back{display:inline-flex;align-items:center;gap:8px;background:var(--icon-bg);
  border:1px solid var(--border);border-radius:20px;padding:7px 16px;cursor:pointer;font-size:14px;
  font-weight:bold;color:var(--primary);text-decoration:none;white-space:nowrap;transition:all .2s}
.btn-back:hover{border-color:var(--primary-light);background:var(--card)}
.btn-back svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}
.theme-toggle{background:var(--icon-bg);border:1px solid var(--border);border-radius:20px;padding:6px 14px;
  cursor:pointer;font-size:13px;color:var(--text-muted);display:flex;align-items:center;gap:6px;
  white-space:nowrap;flex-shrink:0;transition:all .2s}
.theme-toggle:hover{border-color:var(--primary-light);color:var(--text)}
.theme-toggle .icon{font-size:15px}

main{flex:1;max-width:980px;margin:0 auto;width:100%;padding:40px 24px}
.section-title{font-size:13px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:var(--text-muted);
  margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid var(--border);transition:color .25s,border-color .25s}
.section-title:not(:first-of-type){margin-top:34px}

.tool-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}
.tool-card{background:var(--card);border:2px solid var(--border);border-radius:10px;padding:14px;cursor:pointer;
  text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:6px;box-shadow:0 2px 6px rgba(0,0,0,.05);
  transition:all .15s}
.tool-card:hover{border-color:var(--primary-light);box-shadow:0 6px 20px rgba(37,88,160,.2);transform:translateY(-3px)}
.tool-icon{width:32px;height:32px;background:var(--icon-bg);border-radius:8px;display:flex;align-items:center;justify-content:center}
.tool-icon svg{width:16px;height:16px;stroke:var(--primary-light);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.tool-name{font-size:14px;font-weight:bold;color:var(--primary)}
.tool-desc{font-size:11px;color:var(--text-muted);line-height:1.5}
.tool-arrow{margin-top:auto;font-size:13px;color:var(--primary-light);align-self:flex-end}

.empty-state{background:var(--card);border:2px dashed var(--border);border-radius:12px;padding:28px;text-align:center;
  margin-bottom:18px;color:var(--text-muted)}
.empty-icon{font-size:34px;margin-bottom:8px}
.empty-title{font-size:16px;font-weight:bold;color:var(--text);margin-bottom:6px}
.empty-state p{font-size:13px;line-height:1.6;max-width:640px;margin:0 auto}
.empty-state code{background:var(--icon-bg);padding:1px 6px;border-radius:4px;font-size:12px}
.add-card{border-style:dashed}

footer{text-align:center;padding:16px;font-size:11px;color:var(--text-muted);border-top:1px solid var(--border);
  background:var(--footer);flex-shrink:0;transition:background .25s,border-color .25s}

@media (max-width:640px){
  header{flex-wrap:wrap;gap:12px;padding:14px 16px}
  .logo-text{font-size:28px}
  .header-divider{display:none}
  .header-right{width:100%;margin-left:0;justify-content:flex-start}
  main{padding:24px 14px}
}
"""

HUB_JS = """/* Theme-Umschalter (bleibt ueber Seiten erhalten) + Datum im Kopf */
(function(){
  var KEY='pl-theme';
  function label(t){return t==='dark' ? '<span class="icon">\\u2600\\ufe0f</span> Hell' : '<span class="icon">\\ud83c\\udf19</span> Dunkel';}
  function apply(t){document.documentElement.setAttribute('data-theme',t);
    var b=document.getElementById('themeBtn'); if(b) b.innerHTML=label(t);}
  window.toggleTheme=function(){
    var cur=document.documentElement.getAttribute('data-theme')==='dark'?'dark':'light';
    var next=cur==='dark'?'light':'dark';
    try{localStorage.setItem(KEY,next);}catch(e){}
    apply(next);
  };
  var saved='light'; try{saved=localStorage.getItem(KEY)||'light';}catch(e){}
  apply(saved);
  document.addEventListener('DOMContentLoaded',function(){
    var s='light'; try{s=localStorage.getItem(KEY)||'light';}catch(e){}
    apply(s);
    var d=document.getElementById('headerDatum');
    if(d){d.textContent=new Date().toLocaleDateString('de-DE',{weekday:'short',day:'2-digit',month:'2-digit',year:'numeric'});}
  });
})();
"""


# ---------------------------------------------------------------------------
# HTML-Bausteine
# ---------------------------------------------------------------------------
def icon_svg(name):
    return '<svg viewBox="0 0 24 24">' + ICONS.get(name, ICONS["doc"]) + '</svg>'


def page(title_main, title_sub, body, depth=0, back_href=None):
    asset = ("../" * depth) + "assets/"
    back = ""
    if back_href:
        back = ('<a class="btn-back" href="%s">'
                '<svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg> Prozesslandschaft</a>' % back_href)
    return """<!DOCTYPE html>
<html lang="de" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s - Einhaus Prozesslandschaft</title>
<link rel="stylesheet" href="%sstyle.css">
<script src="%shub.js"></script>
</head>
<body>
<header>
  <div class="logo-wrap">
    <div class="logo-text">EINHAUS.</div>
    <div class="logo-sub-row">
      <div class="logo-stripes"><span class="s1"></span><span class="s2"></span><span class="s3"></span><span class="s4"></span><span class="s5"></span><span class="s6"></span><span class="s7"></span></div>
      <div class="logo-tagline">Oberfl&auml;chenveredelung auf h&ouml;chstem Niveau.</div>
    </div>
  </div>
  <div class="header-divider"></div>
  <div class="header-info">
    <div class="header-title">%s</div>
    <div class="header-subtitle">%s &middot; <span id="headerDatum"></span></div>
  </div>
  <div class="header-right">
    %s
    <button class="theme-toggle" id="themeBtn" onclick="toggleTheme()"><span class="icon">&#127769;</span> Dunkel</button>
  </div>
</header>
<main>
%s
</main>
<footer>EINHAUS Oberfl&auml;chenveredelung GmbH &nbsp;&middot;&nbsp; Saarlandstr. 375a, 55411 Bingen</footer>
</body>
</html>
""" % (title_main, asset, asset, title_main, title_sub, back, body)


def hub_body():
    parts = []
    for group, procs in STRUCTURE:
        cards = []
        for p in procs:
            cards.append(
                '<a class="tool-card" href="./%s/index.html">'
                '<div class="tool-icon">%s</div>'
                '<div class="tool-name">%s</div>'
                '<div class="tool-arrow">&rarr;</div></a>'
                % (p["slug"], icon_svg("doc"), p["name"])
            )
        parts.append('<div class="section-title">%s</div>\n<div class="tool-grid">\n%s\n</div>'
                     % (group, "\n".join(cards)))
    return "\n".join(parts)


def dashboard_body(tiles):
    cards = []
    for t in tiles:
        cards.append(
            '<a class="tool-card" href="%s" target="_blank" rel="noopener">'
            '<div class="tool-icon">%s</div>'
            '<div class="tool-name">%s</div>'
            '<div class="tool-desc">%s</div>'
            '<div class="tool-arrow">&#8599;</div></a>'
            % (t["url"], icon_svg(t.get("icon", "doc")), t["name"], t.get("desc", ""))
        )
    return ('<div class="section-title">Dashboards &amp; Tools</div>\n'
            '<div class="tool-grid">\n%s\n</div>' % "\n".join(cards))


def empty_body(name):
    return (
        '<div class="section-title">Dashboards &amp; Tools</div>\n'
        '<div class="empty-state">\n'
        '  <div class="empty-icon">&#128679;</div>\n'
        '  <div class="empty-title">Noch kein Dashboard hinterlegt</div>\n'
        '  <p>F&uuml;r den Prozess &bdquo;%s&ldquo; kann hier ein eigenes Dashboard aufgebaut werden. '
        'Lege deine HTML-Seite in diesem Ordner ab und trage sie unten als Kachel ein. '
        'Anleitung: siehe <code>README.md</code> und <code>assets/_TEMPLATE_prozess.html</code>.</p>\n'
        '</div>\n'
        '<div class="tool-grid">\n'
        '  <a class="tool-card add-card" href="../assets/_TEMPLATE_prozess.html" target="_blank" rel="noopener">\n'
        '    <div class="tool-icon">%s</div>\n'
        '    <div class="tool-name">Neues Dashboard aufbauen</div>\n'
        '    <div class="tool-desc">Vorlage &ouml;ffnen und als Startpunkt kopieren.</div>\n'
        '  </a>\n'
        '</div>' % (name, icon_svg("plus"))
    )


TEMPLATE_HTML = """<!DOCTYPE html>
<!--
  KOPIERVORLAGE fuer ein Prozess-Dashboard.
  1) Diese Datei in den Ordner deines Prozesses kopieren und in  index.html  umbenennen.
  2) Unten <TITEL> und die Kacheln anpassen. Jede Kachel ist ein <a class="tool-card"> ... </a>.
  3) Eigene Tools als eigene .html-Datei im selben Ordner ablegen und als href eintragen.
  (Die Pfade ../assets/... stimmen, sobald die Datei in einem Prozess-Ordner liegt.)
-->
<html lang="de" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TITEL - Einhaus Prozesslandschaft</title>
<link rel="stylesheet" href="../assets/style.css">
<script src="../assets/hub.js"></script>
</head>
<body>
<header>
  <div class="logo-wrap">
    <div class="logo-text">EINHAUS.</div>
    <div class="logo-sub-row">
      <div class="logo-stripes"><span class="s1"></span><span class="s2"></span><span class="s3"></span><span class="s4"></span><span class="s5"></span><span class="s6"></span><span class="s7"></span></div>
      <div class="logo-tagline">Oberfl&auml;chenveredelung auf h&ouml;chstem Niveau.</div>
    </div>
  </div>
  <div class="header-divider"></div>
  <div class="header-info">
    <div class="header-title">TITEL DES PROZESSES</div>
    <div class="header-subtitle">Prozesslandschaft &middot; <span id="headerDatum"></span></div>
  </div>
  <div class="header-right">
    <a class="btn-back" href="../index.html"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg> Prozesslandschaft</a>
    <button class="theme-toggle" id="themeBtn" onclick="toggleTheme()"><span class="icon">&#127769;</span> Dunkel</button>
  </div>
</header>
<main>
  <div class="section-title">Dashboards &amp; Tools</div>
  <div class="tool-grid">

    <!-- ===== Beispiel-Kachel: kopieren und anpassen ===== -->
    <a class="tool-card" href="mein_tool.html">
      <div class="tool-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
      <div class="tool-name">Mein Dashboard</div>
      <div class="tool-desc">Kurze Beschreibung, was dieses Tool macht.</div>
      <div class="tool-arrow">&rarr;</div>
    </a>
    <!-- Neue Kachel hier einfuegen -->

  </div>
</main>
<footer>EINHAUS Oberfl&auml;chenveredelung GmbH &nbsp;&middot;&nbsp; Saarlandstr. 375a, 55411 Bingen</footer>
</body>
</html>
"""

README_MD = """# EINHAUS Prozesslandschaft

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
"""


# ---------------------------------------------------------------------------
# Schreiben
# ---------------------------------------------------------------------------
def write(path, content, overwrite=True):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True) if os.path.dirname(path) else None
    if not overwrite and os.path.exists(full):
        print("  behalten (existiert): %s" % path)
        return
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("  geschrieben: %s" % path)


def main():
    print("EINHAUS Prozesslandschaft -> %s" % ROOT)

    # Basis / Design
    write(".nojekyll", "", overwrite=True)
    write("assets/style.css", STYLE_CSS, overwrite=True)
    write("assets/hub.js", HUB_JS, overwrite=True)
    write("assets/_TEMPLATE_prozess.html", TEMPLATE_HTML, overwrite=True)
    write("README.md", README_MD, overwrite=True)

    # Ebene 1: Hub (immer neu)
    write("index.html", page("Prozesslandschaft", "EINHAUS Oberfl&auml;chenveredelung GmbH", hub_body(), depth=0), overwrite=True)

    # Ebene 2: je Prozess
    for group, procs in STRUCTURE:
        for p in procs:
            path = "%s/index.html" % p["slug"]
            if p["tiles"] is not None:
                body = dashboard_body(p["tiles"])
                html = page(p["name"], "Prozesslandschaft", body, depth=1, back_href="../index.html")
                write(path, html, overwrite=True)          # kuratiert -> immer neu
            else:
                body = empty_body(p["name"])
                html = page(p["name"], "Prozesslandschaft", body, depth=1, back_href="../index.html")
                write(path, html, overwrite=False)          # Kollegen-Geruest -> nie ueberschreiben

    print("Fertig.")


if __name__ == "__main__":
    main()
