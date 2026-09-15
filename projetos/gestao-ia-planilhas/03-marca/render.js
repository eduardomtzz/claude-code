const fs=require('fs'); const launch=require('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad/pw/launch');
const svg=n=>fs.readFileSync(n+'.svg','utf8');
(async()=>{ const b=await launch(); const ctx=await b.newContext({deviceScaleFactor:2});
 const shot=async(html,w,h,file,omitBg=false)=>{ const p=await ctx.newPage(); await p.setViewportSize({width:w,height:h}); await p.setContent(`<style>html,body{margin:0;width:${w}px;height:${h}px;${omitBg?'background:transparent':''}} .c{width:${w}px;height:${h}px;display:flex;align-items:center;justify-content:center} svg{display:block}</style><div class="c">${html}</div>`); await p.waitForTimeout(300); await p.screenshot({path:file,omitBackground:omitBg,type:'png'}); await p.close(); };
 // preview board
 const board=`<div style="display:grid;gap:24px;padding:24px;background:#eee;width:1000px;box-sizing:border-box;font-family:sans-serif">
 <div style="background:#FFFAF0;padding:30px;border-radius:12px">${svg('logo-horizontal').replace('<svg','<svg style="width:700px;height:auto"')}</div>
 <div style="background:#3B1F5E;padding:30px;border-radius:12px">${svg('logo-branco').replace('<svg','<svg style="width:700px;height:auto"')}</div>
 <div style="display:flex;gap:24px;align-items:center"><div style="background:#fff;padding:20px;border-radius:12px">${svg('logo-empilhado').replace('<svg','<svg style="width:320px;height:auto"')}</div>
 ${svg('simbolo-avatar').replace('<svg','<svg style="width:160px;height:160px"')} ${svg('simbolo-fundo-sol').replace('<svg','<svg style="width:160px;height:160px"')} ${svg('logo-mono-uva').replace('<svg','<svg style="width:300px;height:auto;background:#fff"')}</div></div>`;
 await shot(board,1000,720,'preview.png');
 // deliverables
 await shot(svg('simbolo-avatar').replace('<svg','<svg style="width:540px;height:540px"').replace('rx="36"','rx="0"'),540,540,'avatar-instagram-1080.png');
 await shot(`<div style="width:820px;height:312px;background:#3B1F5E;display:flex;align-items:center;justify-content:center">${svg('logo-branco').replace('<svg','<svg style="width:560px;height:auto"')}</div>`,820,312,'capa-facebook-1640x624.png');
 await shot(svg('logo-horizontal').replace('<svg','<svg style="width:1200px;height:auto"'),1200,190,'logo-horizontal-2400.png',true);
 await shot(svg('logo-branco').replace('<svg','<svg style="width:1200px;height:auto"'),1200,190,'logo-branco-2400.png',true);
 await shot(svg('logo-empilhado').replace('<svg','<svg style="width:600px;height:auto"'),600,520,'logo-empilhado-1200.png',true);
 await shot(svg('simbolo').replace('<svg','<svg style="width:512px;height:512px"'),512,512,'simbolo-1024.png',true);
 await b.close(); console.log('rendered'); })().catch(e=>{console.error('ERR',e.message);process.exit(1)});
