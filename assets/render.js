/* EINHAUS Prozesslandschaft - Aufbau der Seiten aus struktur.js.
   (Diese Datei muss man normalerweise NICHT anfassen - Inhalte stehen in struktur.js.) */

(function () {
  "use strict";

  var DOC_ICON = '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>';
  var PLUS_ICON = '<line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>';

  function esc(s) {
    return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function iconSvg(inner) {
    return '<svg viewBox="0 0 24 24">' + (inner || DOC_ICON) + "</svg>";
  }
  function isAbsolute(u) { return /^https?:\/\//i.test(u || ""); }
  function href(u) { return isAbsolute(u) ? encodeURI(u) : (u || "#"); }

  function data() { return (window.PROZESSLANDSCHAFT && window.PROZESSLANDSCHAFT.gruppen) || []; }

  // Rücksprung-Ziel fuer externe Tools: wird direkt als URL-Parameter an den
  // Link angehaengt (kein localStorage/Tab-Timing noetig). Das Ziel-Tool liest
  // diesen Parameter in assets/zurueck-kontext.js und biegt seinen "Zurueck"-
  // Knopf auf DIESEN Prozess in der Prozesslandschaft um.
  function backUrlFor(slug) {
    var folder = location.pathname.substring(0, location.pathname.lastIndexOf("/") + 1);
    return location.origin + folder + "prozess.html?p=" + encodeURIComponent(slug);
  }
  function withBackParam(url, slug) {
    var sep = url.indexOf("?") > -1 ? "&" : "?";
    return url + sep + "plZurueck=" + encodeURIComponent(backUrlFor(slug));
  }

  function findProzess(slug) {
    var g = data();
    for (var i = 0; i < g.length; i++) {
      var ps = g[i].prozesse || [];
      for (var j = 0; j < ps.length; j++) {
        if (ps[j].slug === slug) return ps[j];
      }
    }
    return null;
  }

  // ---- Ebene 1: Prozesslandschaft (Hub) -----------------------------------
  window.renderHub = function () {
    var host = document.getElementById("content");
    if (!host) return;
    var g = data(), html = "";
    for (var i = 0; i < g.length; i++) {
      var cards = "";
      var ps = g[i].prozesse || [];
      for (var j = 0; j < ps.length; j++) {
        var p = ps[j];
        cards +=
          '<a class="tool-card" href="prozess.html?p=' + encodeURIComponent(p.slug) + '">' +
          '<div class="tool-icon">' + iconSvg(DOC_ICON) + "</div>" +
          '<div class="tool-name">' + esc(p.name) + "</div>" +
          '<div class="tool-arrow">&rarr;</div></a>';
      }
      html += '<div class="section-title">' + esc(g[i].titel) + "</div>\n" +
              '<div class="tool-grid">' + cards + "</div>";
    }
    host.innerHTML = html;
  };

  // ---- Ebene 2: Prozess-Unterseite ----------------------------------------
  window.renderProzess = function () {
    var host = document.getElementById("content");
    if (!host) return;
    var slug = new URLSearchParams(window.location.search).get("p") || "";
    var p = findProzess(slug);

    var titleEl = document.getElementById("procTitle");
    var titleTag = document.getElementById("procTitleTag");

    if (!p) {
      if (titleEl) titleEl.textContent = "Prozess nicht gefunden";
      host.innerHTML =
        '<div class="empty-state"><div class="empty-icon">&#10067;</div>' +
        '<div class="empty-title">Prozess nicht gefunden</div>' +
        '<p>Der Prozess &bdquo;' + esc(slug) + '&ldquo; ist in <code>struktur.js</code> nicht hinterlegt. ' +
        'Zur&uuml;ck zur <a href="index.html">Prozesslandschaft</a>.</p></div>';
      return;
    }

    if (titleEl) titleEl.textContent = p.name;
    if (titleTag) titleTag.textContent = p.name + " - Einhaus Prozesslandschaft";

    var tiles = p.tiles || [];
    if (tiles.length) {
      var cards = "";
      for (var i = 0; i < tiles.length; i++) {
        var t = tiles[i];
        var arrow = isAbsolute(t.url) ? "&#8599;" : "&rarr;";
        var target = isAbsolute(t.url) ? ' target="_blank" rel="noopener"' : "";
        var linkUrl = href(t.url);
        if (isAbsolute(t.url)) linkUrl = withBackParam(linkUrl, p.slug);
        cards +=
          '<a class="tool-card" href="' + esc(linkUrl) + '"' + target + ">" +
          '<div class="tool-icon">' + iconSvg(t.icon ? null : DOC_ICON) + "</div>" +
          '<div class="tool-name">' + esc(t.name) + "</div>" +
          (t.beschreibung ? '<div class="tool-desc">' + esc(t.beschreibung) + "</div>" : "") +
          '<div class="tool-arrow">' + arrow + "</div></a>";
      }
      host.innerHTML = '<div class="section-title">Dashboards &amp; Tools</div>' +
                       '<div class="tool-grid">' + cards + "</div>";
    } else {
      host.innerHTML =
        '<div class="section-title">Dashboards &amp; Tools</div>' +
        '<div class="empty-state"><div class="empty-icon">&#128679;</div>' +
        '<div class="empty-title">Noch kein Dashboard hinterlegt</div>' +
        '<p>F&uuml;r den Prozess &bdquo;' + esc(p.name) + '&ldquo; kann hier ein eigenes Dashboard aufgebaut werden. ' +
        'Lege deine HTML-Datei in den Ordner <code>' + esc(p.slug) + '/</code> und trage sie in ' +
        '<code>struktur.js</code> unter diesem Prozess als <code>tiles</code>-Eintrag ein. ' +
        'Anleitung: siehe <code>README.md</code>.</p></div>' +
        '<div class="tool-grid">' +
        '<a class="tool-card add-card" href="README.md" target="_blank" rel="noopener">' +
        '<div class="tool-icon">' + iconSvg(PLUS_ICON) + "</div>" +
        '<div class="tool-name">So baust du ein Dashboard auf</div>' +
        '<div class="tool-desc">Kurzanleitung in der README &ouml;ffnen.</div></a>' +
        "</div>";
    }
  };
})();
