/* Seu Sócio Gestor — consentimento (ANPD), Pixel condicionado, preferências */
(function () {
  var KEY = 'ssg_consent_v1';
  var DEFAULT = { necessario: true, medicao: false, publicidade: false, ts: 0 };

  function ler() {
    try { var v = JSON.parse(localStorage.getItem(KEY)); if (v && v.ts) return v; } catch (e) {}
    return null;
  }
  function gravar(c) {
    c.ts = Date.now();
    try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {}
    window.ssgConsent = c;
    document.dispatchEvent(new CustomEvent('ssg:consent', { detail: c }));
    aplicar(c);
  }
  function aplicar(c) {
    if (c.publicidade && window.SSG && window.SSG.pixelId && !window.__ssgPixel) {
      window.__ssgPixel = true;
      /* Meta Pixel só carrega com consentimento de publicidade. */
      !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
      window.fbq('init', window.SSG.pixelId);
      window.fbq('track', 'PageView', {}, { eventID: window.SSG.pageViewId || undefined });
    }
  }

  var atual = ler();
  window.ssgConsent = atual || DEFAULT;
  if (atual) aplicar(atual);

  var banner = document.getElementById('consent');
  if (banner && !atual && !/\/cookies\//.test(location.pathname)) {
    banner.hidden = false;
    banner.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-consent]');
      if (!b) return;
      var tudo = b.getAttribute('data-consent') === 'all';
      gravar({ necessario: true, medicao: tudo, publicidade: tudo });
      banner.hidden = true;
    });
  }

  /* Página de preferências */
  var form = document.getElementById('pref-form');
  if (form) {
    var med = form.querySelector('[name=medicao]');
    var pub = form.querySelector('[name=publicidade]');
    var estado = document.getElementById('pref-estado');
    function render() {
      var c = ler();
      med.checked = !!(c && c.medicao);
      pub.checked = !!(c && c.publicidade);
      estado.textContent = c ? ('Escolha registrada em ' + new Date(c.ts).toLocaleString('pt-BR')) : 'Você ainda não registrou uma escolha.';
    }
    render();
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      gravar({ necessario: true, medicao: med.checked, publicidade: pub.checked });
      render();
    });
    form.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-consent]');
      if (!b) return;
      var tudo = b.getAttribute('data-consent') === 'all';
      gravar({ necessario: true, medicao: tudo, publicidade: tudo });
      render();
    });
  }

  /* Preserva UTM e fbclid nos links de checkout (quando existirem) */
  try {
    var q = location.search;
    if (q && q.length > 1) {
      document.querySelectorAll('a[data-checkout]').forEach(function (a) {
        var sep = a.href.indexOf('?') > -1 ? '&' : '?';
        a.href = a.href + sep + q.slice(1);
      });
    }
  } catch (e) {}
})();
