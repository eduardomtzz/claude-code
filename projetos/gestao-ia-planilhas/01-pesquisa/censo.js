const fs=require('fs'); const launch=require('./launch');
const TERMS=process.argv.slice(2);
const MESES={jan:1,fev:2,mar:3,abr:4,mai:5,jun:6,jul:7,ago:8,set:9,out:10,nov:11,dez:12};
function parseDate(s){ const m=s.match(/(\d{1,2}) de (\w{3})\.? de (\d{4})/); if(!m) return null; return new Date(m[3], MESES[m[2].toLowerCase()]-1, m[1]); }
const log=(...a)=>fs.appendFileSync('censo.log', new Date().toISOString().slice(11,19)+' '+a.join(' ')+'\n');
(async()=>{
 const b=await launch(); const ctx=await b.newContext({locale:'pt-BR', viewport:{width:1280,height:2400}, userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'});
 const out={};
 for (const term of TERMS){
  const p=await ctx.newPage(); p.setDefaultTimeout(60000);
  const url='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q='+encodeURIComponent(term)+'&search_type=keyword_unordered&media_type=all';
  try{
   await p.goto(url,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(7000);
   let prev=0; for (let i=0;i<12;i++){ await p.mouse.wheel(0,6000); await p.waitForTimeout(2500); const n=(await p.locator('body').innerText()).length; if(n===prev) break; prev=n; }
   const txt=(await p.locator('body').innerText()).replace(/\s+/g,' ');
   const total=(txt.match(/~?([\d.]+) resultados/)||[])[1]||'';
   const chunks=txt.split('Identificação da biblioteca:').slice(1);
   const ads=[]; const today=new Date('2026-09-12');
   for (const c of chunks){
     const id=(c.match(/^\s*(\d+)/)||[])[1]; const dateS=(c.match(/Veiculação iniciada em ([^P]+?) Plataformas/)||[])[1]||''; const d=parseDate(dateS);
     const page=(c.match(/Ver detalhes do anúncio (.+?) Patrocinado/)||[])[1]||''; const versions=/várias versões/.test(c);
     const body=(c.split('Patrocinado')[1]||'').slice(0,220).replace(/Identificação.*$/,'');
     const dom=(c.match(/\b([A-Z0-9-]+(?:\.[A-Z0-9-]+)*\.(?:COM\.BR|COM|BR|NET|ORG|IO|APP|CO|SITE|ONLINE|ME|NEGOCIO|SHOP))\b/)||[])[1]||'';
     if(id) ads.push({id,page,start:d?d.toISOString().slice(0,10):dateS,days:d?Math.round((today-d)/86400000):null,versions,dom,body});
   }
   const byPage={}; for(const a of ads){ const k=a.page||'?'; byPage[k]=byPage[k]||{page:k,ads:0,oldest:null,days:0,doms:new Set(),sample:''}; const e=byPage[k]; e.ads++; if(a.days!==null&&a.days>e.days){e.days=a.days;e.oldest=a.start;} if(a.dom)e.doms.add(a.dom); if(!e.sample)e.sample=a.body; }
   const pages=Object.values(byPage).map(e=>({...e,doms:[...e.doms].join(',')})).sort((x,y)=>y.ads-x.ads);
   out[term]={total,adsLoaded:ads.length,pages};
   log(term,'total~',total,'ads loaded',ads.length,'pages',pages.length);
  }catch(e){ log(term,'ERR',e.message.slice(0,200)); out[term]={error:e.message.slice(0,200)}; }
  await p.close();
  fs.writeFileSync('censo.json', JSON.stringify(out,null,1));
 }
 await b.close(); log('DONE');
})().catch(e=>log('FATAL',e.message));
