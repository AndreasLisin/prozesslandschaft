/* Theme-Umschalter (bleibt ueber Seiten erhalten) + Datum im Kopf */
(function(){
  var KEY='pl-theme';
  function label(t){return t==='dark' ? '<span class="icon">\u2600\ufe0f</span> Hell' : '<span class="icon">\ud83c\udf19</span> Dunkel';}
  function apply(t){document.documentElement.setAttribute('data-theme',t);
    var b=document.getElementById('themeBtn'); if(b) b.innerHTML=label(t);}
  window.toggleTheme=function(){
    var cur=document.documentElement.getAttribute('data-theme')==='dark'?'dark':'light';
    var next=cur==='dark'?'light':'dark';
    try{localStorage.setItem(KEY,next);}catch(e){}
    apply(next);
  };
  var saved='dark'; try{saved=localStorage.getItem(KEY)||'dark';}catch(e){}
  apply(saved);
  document.addEventListener('DOMContentLoaded',function(){
    var s='dark'; try{s=localStorage.getItem(KEY)||'dark';}catch(e){}
    apply(s);
    var d=document.getElementById('headerDatum');
    if(d){d.textContent=new Date().toLocaleDateString('de-DE',{weekday:'short',day:'2-digit',month:'2-digit',year:'numeric'});}
  });
})();
