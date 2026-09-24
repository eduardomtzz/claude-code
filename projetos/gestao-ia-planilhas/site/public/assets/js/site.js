/* Seu Sócio Gestor — consentimento (ANPD), Pixel condicionado, preferências */
(function () {
  /* Toda página abre no topo (sem restaurar rolagem), a não ser que o link aponte para uma seção (#id). */
  try {
    if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
    function topo() {
      if (location.hash && document.getElementById(location.hash.slice(1))) return;
      var html = document.documentElement, prev = html.style.scrollBehavior;
      html.style.scrollBehavior = 'auto';
      window.scrollTo(0, 0); document.body.scrollTop = 0; html.scrollTop = 0;
      html.style.scrollBehavior = prev;
    }
    topo();
    window.addEventListener('pageshow', topo);
    window.addEventListener('load', topo);
  } catch (e) {}

  /* Links para uma seção da mesma página (#id): rola até ela sem recarregar. Funciona igual no site
     publicado e em visualizadores que servem a página com outro endereço-base (prévia). "#" puro não faz nada. */
  try {
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      if (!a || a.hasAttribute('data-checkout') && a.getAttribute('href') === '#') { if (a) e.preventDefault(); return; }
      var h = a.getAttribute('href'); e.preventDefault();
      if (h.length < 2) return;
      var alvo = document.getElementById(decodeURIComponent(h.slice(1)));
      if (!alvo) return;
      alvo.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
      try { history.replaceState(null, '', h); } catch (err) {}
    });
  } catch (e) {}

  /* Índice das páginas de texto: aberto no desktop, recolhido no celular */
  try {
    var idx = document.querySelector('details.doc__indice');
    if (idx && window.matchMedia('(min-width: 900px)').matches) idx.open = true;
  } catch (e) {}

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
  /* ---- Rastreamento (Meta Pixel + Conversions API), só com consentimento de publicidade ---- */
  function uuid() {
    try { if (window.crypto && crypto.randomUUID) return crypto.randomUUID(); } catch (e) {}
    return 'e' + Date.now().toString(36) + Math.random().toString(36).slice(2, 10);
  }
  function cookie(n) { var m = document.cookie.match('(?:^|; )' + n + '=([^;]*)'); return m ? decodeURIComponent(m[1]) : ''; }
  function guardarFbc() {
    /* Meta recomenda gravar o fbclid da URL no cookie _fbc para melhorar a correspondência. */
    try {
      var m = location.search.match(/[?&]fbclid=([^&]+)/);
      if (m && !cookie('_fbc')) {
        var v = 'fb.1.' + Date.now() + '.' + decodeURIComponent(m[1]);
        document.cookie = '_fbc=' + encodeURIComponent(v) + '; max-age=' + (90 * 86400) + '; path=/; domain=' + location.hostname.replace(/^www\./, '') + '; SameSite=Lax; Secure';
      }
    } catch (e) {}
  }
  function capi(name, id, params) {
    /* Espelho do evento no servidor (Cloudflare Pages Function em /api/capi). Falha em silêncio. */
    try {
      var body = JSON.stringify({ event_name: name, event_id: id, event_time: Math.floor(Date.now() / 1000), event_source_url: location.href,
        custom_data: params || {}, fbp: cookie('_fbp'), fbc: cookie('_fbc') });
      if (navigator.sendBeacon) { navigator.sendBeacon('/api/capi', new Blob([body], { type: 'application/json' })); return; }
      fetch('/api/capi', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: body, keepalive: true }).catch(function () {});
    } catch (e) {}
  }
  function track(name, params) {
    if (!window.__ssgPixel || !window.fbq) return null;
    var id = uuid();
    window.fbq('track', name, params || {}, { eventID: id });
    if (window.SSG.capi !== false) capi(name, id, params);
    return id;
  }
  window.SSG = window.SSG || {};
  window.SSG.track = track;
  function aplicar(c) {
    if (c.publicidade && window.SSG && window.SSG.pixelId && !window.__ssgPixel) {
      window.__ssgPixel = true;
      guardarFbc();
      /* Meta Pixel só carrega com consentimento de publicidade. */
      !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
      window.fbq('init', window.SSG.pixelId);
      track('PageView');
      if (window.SSG.viewContent) track('ViewContent', window.SSG.viewContent);
      /* Purchase NÃO dispara aqui: vem do checkout (Pixel + CAPI nativos da Kiwify, no webhook de aprovação). */
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

  /* Clique no botão de compra: InitiateCheckout (só se o Pixel estiver carregado) */
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('a[data-checkout]');
    if (a) track('InitiateCheckout', window.SSG.viewContent || {});
  });

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
