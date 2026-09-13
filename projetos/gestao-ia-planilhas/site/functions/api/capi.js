/* Cloudflare Pages Function: espelho servidor dos eventos do Pixel (Meta Conversions API).
   Variáveis de ambiente no projeto do Pages: META_PIXEL_ID, META_CAPI_TOKEN, META_TEST_EVENT_CODE (só em teste).
   O navegador envia {event_name, event_id, event_time, event_source_url, custom_data, fbp, fbc}; o mesmo
   event_id vai no Pixel, e a Meta deduplica. Purchase não passa por aqui (vem da Kiwify). */
const PERMITIDOS = new Set(['PageView', 'ViewContent', 'InitiateCheckout', 'Lead']);
const CONTEUDOS = new Set(['kit-essencial', 'kit-completo']);

async function sha256(texto) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(texto.trim().toLowerCase()));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

export async function onRequestPost({ request, env }) {
  const ok = new Response(null, { status: 204 });
  if (!env.META_PIXEL_ID || !env.META_CAPI_TOKEN) return ok; // sem credenciais, não faz nada
  let b;
  try { b = await request.json(); } catch (e) { return new Response('json', { status: 400 }); }
  if (!b || !PERMITIDOS.has(b.event_name) || typeof b.event_id !== 'string' || b.event_id.length > 64) return new Response('evento', { status: 400 });

  const agora = Math.floor(Date.now() / 1000);
  const t = Number(b.event_time) || agora;
  const custom = {};
  if (b.custom_data && typeof b.custom_data === 'object') {
    const c = b.custom_data;
    if (Array.isArray(c.content_ids)) custom.content_ids = c.content_ids.filter((x) => CONTEUDOS.has(x)).slice(0, 5);
    if (typeof c.content_name === 'string') custom.content_name = c.content_name.slice(0, 120);
    if (typeof c.content_type === 'string') custom.content_type = c.content_type.slice(0, 40);
    if (Number.isFinite(Number(c.value))) custom.value = Number(c.value);
    if (c.currency === 'BRL') custom.currency = 'BRL';
  }
  const user_data = {
    client_ip_address: request.headers.get('CF-Connecting-IP') || undefined,
    client_user_agent: request.headers.get('User-Agent') || undefined,
    fbp: typeof b.fbp === 'string' && b.fbp ? b.fbp.slice(0, 80) : undefined,
    fbc: typeof b.fbc === 'string' && b.fbc ? b.fbc.slice(0, 200) : undefined,
  };
  if (typeof b.email === 'string' && b.email.includes('@')) user_data.em = [await sha256(b.email)];

  const payload = {
    data: [{
      event_name: b.event_name,
      event_time: Math.min(Math.max(t, agora - 7 * 86400), agora),
      event_id: b.event_id,
      event_source_url: typeof b.event_source_url === 'string' ? b.event_source_url.slice(0, 500) : undefined,
      action_source: 'website',
      user_data,
      custom_data: custom,
    }],
  };
  if (env.META_TEST_EVENT_CODE) payload.test_event_code = env.META_TEST_EVENT_CODE;

  try {
    await fetch(`https://graph.facebook.com/v21.0/${env.META_PIXEL_ID}/events?access_token=${encodeURIComponent(env.META_CAPI_TOKEN)}`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload),
    });
  } catch (e) { /* nunca quebra a página por causa de rastreamento */ }
  return ok;
}

export function onRequest({ request }) {
  if (request.method === 'POST') return undefined; // segue para onRequestPost
  return new Response('método', { status: 405 });
}
