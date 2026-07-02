/* =============================================================================
   EINHAUS Prozesslandschaft - INHALT / STRUKTUR
   =============================================================================
   Das ist die EINZIGE Datei, die man aendern muss, um die Prozesslandschaft
   anzupassen. Kein Python, kein Build - einfach hier bearbeiten, speichern,
   fertig. (Auf GitHub: Datei oeffnen -> Bleistift-Symbol -> aendern -> "Commit".)

   AUFBAU:
     gruppen = Liste von Gruppen (die grauen Ueberschriften).
     Jede Gruppe hat:  titel   und   prozesse (Liste von Kacheln).
     Jeder Prozess hat: name  (Anzeige) und  slug (Adresse, nur Kleinbuchstaben,
                        keine Umlaute/Leerzeichen -> stattdessen Bindestriche).
     Optional pro Prozess:  tiles = Liste der Dashboards/Tools, die hinter dem
                            Prozess erscheinen. Jede Kachel: name, url, (beschreibung).

   BEISPIEL neuen Prozess anlegen:
     { name: "Mein Prozess", slug: "mein-prozess" }

   BEISPIEL Dashboard hinter einem Prozess ergaenzen (in dessen "tiles"):
     { name: "Mein Dashboard", url: "eol/mein_dashboard.html",
       beschreibung: "Kurze Erklaerung." }
     -> Die eigene HTML-Datei einfach in den passenden Ordner (z.B. eol/) legen.

   Reihenfolge der Gruppen/Prozesse = Reihenfolge in dieser Liste.
   Auf korrekte Kommas und geschweifte/eckige Klammern achten.
============================================================================= */

window.PROZESSLANDSCHAFT = {
  gruppen: [

    { titel: "Unternehmensleitung", prozesse: [
      { name: "Risikomanagement", slug: "risikomanagement" },
      { name: "Unternehmenspolitik und Strategie", slug: "unternehmenspolitik-und-strategie" },
      { name: "Nachhaltigkeit", slug: "nachhaltigkeit" }
    ]},

    { titel: "Managementsysteme", prozesse: [
      { name: "Arbeits- und Gesundheitsmanagement", slug: "arbeits-und-gesundheitsmanagement" },
      { name: "Qualitätsmanagement IATF 16949", slug: "qualitaetsmanagement-iatf-16949" }
    ]},

    { titel: "KVP", prozesse: [
      { name: "KVP", slug: "kvp" }
    ]},

    { titel: "Vertrieb", prozesse: [
      { name: "Vertrieb", slug: "vertrieb" }
    ]},

    { titel: "Supply Chain Management SCM", prozesse: [
      { name: "Logistik", slug: "logistik" },
      { name: "Produktionsplanung", slug: "produktionsplanung" },
      { name: "Beschaffung Anlagen Werkzeuge", slug: "beschaffung-anlagen-werkzeuge" },
      { name: "Beschaffung Setzteile", slug: "beschaffung-setzteile" },
      { name: "Beschaffung Hilfs- u. Betriebsstoffe", slug: "beschaffung-hilfs-u-betriebsstoffe" },
      { name: "Beschaffung Produktionsmaterial", slug: "beschaffung-produktionsmaterial" }
    ]},

    { titel: "Produktion", prozesse: [
      { name: "Paint Shop", slug: "paint-shop", tiles: [
        { name: "Wartungsübersicht",             url: "https://andreaslisin.github.io/lackierung-dashboard/01_Wartungsübersicht/Wartung_Anlagen.html",
          beschreibung: "Wartungstermine aller Anlagen mit E-Mail-Erinnerung." },
        { name: "Rüstfreigabe Roboter",          url: "https://andreaslisin.github.io/lackierung-dashboard/03_Rüstfreigabe_Lackierroboter/Ruestfreigabe_Checkliste.html",
          beschreibung: "Pre-Release-Checkliste Lackier- & Beflammroboter (FB-96/FB-95)." },
        { name: "Eingabe Rüstfreigabe Kabinen",  url: "https://andreaslisin.github.io/lackierung-dashboard/04_Rüstfreigabe_Lackierkabinen/Ruestfreigabe_Mobil.html",
          beschreibung: "Checkliste Lackierkabinen ausfüllen (FB-64)." },
        { name: "Rüstfreigabe Kabinen",          url: "https://andreaslisin.github.io/lackierung-dashboard/04_Rüstfreigabe_Lackierkabinen/Ruestfreigabe_Dashboard.html",
          beschreibung: "Echtzeit-Übersicht der Rüstfreigaben Lackierkabinen." },
        { name: "OEE Auswertung Lackierroboter", url: "https://andreaslisin.github.io/lackierung-dashboard/06_OEE_Kabine1/OEE_Auswertung.html",
          beschreibung: "OEE-Kennzahlen, Trend & Störungspareto Kabine 1." },
        { name: "OEE Eingabe Lackierroboter",    url: "https://andreaslisin.github.io/lackierung-dashboard/06_OEE_Kabine1/OEE_Kabine1_Tablet.html",
          beschreibung: "Schichterfassung für den Lackierroboter." },
        { name: "OEE Auswertung Beflammroboter", url: "https://andreaslisin.github.io/lackierung-dashboard/07_OEE_Beflammroboter/OEE_Auswertung.html",
          beschreibung: "OEE-Kennzahlen, Trend & Störungspareto Beflammroboter." },
        { name: "OEE Eingabe Beflammroboter",    url: "https://andreaslisin.github.io/lackierung-dashboard/07_OEE_Beflammroboter/OEE_Beflammroboter_Tablet.html",
          beschreibung: "Schichterfassung für den Beflammroboter." },
        { name: "Schulungsnachweis Q-Zirkel",    url: "https://andreaslisin.github.io/lackierung-dashboard/09_Schulungsnachweis/Schulungsnachweis_Ausschuss.html",
          beschreibung: "Nachweis der morgendlichen Unterweisung (n.i.O.-Teile)." },
        { name: "Spies Hecker Lackformeln",      url: "https://andreaslisin.github.io/lackierung-dashboard/08_Lackformeln/Lackformeln_Dashboard.html",
          beschreibung: "Mischformeln durchsuchen, Mengenrechner & Neuanlage." },
        { name: "Lackaufbauten",                 url: "https://andreaslisin.github.io/lackierung-dashboard/10_Lackaufbauten/index.html",
          beschreibung: "Materialblöcke & kompletter Aufbau je Farbton." }
      ]},
      { name: "EOL", slug: "eol" }
    ]},

    { titel: "Ressourcen", prozesse: [
      { name: "Werk, Anlagen und Einrichtungen", slug: "werk-anlagen-und-einrichtungen" },
      { name: "Personelle Ressourcen", slug: "personelle-ressourcen" }
    ]},

    { titel: "Wartung - und Instandhaltungsmanagement", prozesse: [
      { name: "Instandhaltung", slug: "instandhaltung" }
    ]},

    { titel: "IT", prozesse: [
      { name: "IT", slug: "it" }
    ]},

    { titel: "Projektmanagement", prozesse: [
      { name: "Projektmanagement", slug: "projektmanagement" }
    ]},

    { titel: "Qualitätssicherung", prozesse: [
      { name: "Prüfprozesse", slug: "pruefprozesse" }
    ]}

  ]
};
