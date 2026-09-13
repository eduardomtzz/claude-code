// helpers comuns dos modelos de apresentação do Kit Completo
const pptxgen = require('pptxgenjs');
const C={UVA:'3B1F5E', SOL:'FFC83D', LILAS:'7A5AA8', LILC:'B89BE0', LAV:'F3EEFB', TINTA:'1F1235', BR:'FFFFFF', CINZA:'5A4A78', VERDE:'DDF3E7', VERDE_T:'155E3C', VERM:'FBE4E4', VERM_T:'7A1F1F'};
const H='Arial';
function novo(titulo){ const p=new pptxgen(); p.layout='LAYOUT_16x9'; p.author='Seu Sócio Gestor'; p.title=titulo; return p; }
function simbolo(p,s,x,y,k,dark){ const c1=dark?C.LILC:C.LILAS, c2=dark?C.BR:C.UVA;
  s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x,y:y+0.40*k,w:0.42*k,h:0.14*k,fill:{color:c1},rectRadius:0.06*k,line:{color:c1}});
  s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x+0.10*k,y:y+0.22*k,w:0.42*k,h:0.14*k,fill:{color:c2},rectRadius:0.06*k,line:{color:c2}});
  s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x+0.20*k,y:y+0.04*k,w:0.42*k,h:0.14*k,fill:{color:c2},rectRadius:0.06*k,line:{color:c2}});
  s.addShape(p.shapes.OVAL,{x:x+0.62*k,y:y+0.44*k,w:0.13*k,h:0.13*k,fill:{color:C.SOL},line:{color:C.SOL}}); }
function rodape(p,s,dark,txt){ s.addText(txt,{x:0.5,y:5.22,w:7.5,h:0.25,fontFace:H,fontSize:8,color:dark?C.LILC:C.LILAS,isTextBox:true,margin:0}); simbolo(p,s,9.0,5.05,0.55,dark); }
function titulo(s,txt,sub){ s.addText(txt,{x:0.5,y:0.35,w:9,h:0.8,fontFace:H,fontSize:24,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'top',fit:'shrink'});
  if(sub) s.addText(sub,{x:0.5,y:1.12,w:9,h:0.35,fontFace:H,fontSize:12,color:C.CINZA,isTextBox:true,margin:0}); }
function cards(p,s,itens,y,h,destaque){ itens.forEach((k,i)=>{const x=0.5+i*(9/itens.length); const w=9/itens.length-0.2; const d=(i===destaque);
  s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x,y:y,w:w,h:h,fill:{color:d?C.SOL:C.LAV},line:{color:d?C.SOL:C.LAV},rectRadius:0.12});
  s.addText(k[0],{x:x+0.2,y:y+0.15,w:w-0.4,h:0.8,fontFace:H,fontSize:26,bold:true,color:C.UVA,isTextBox:true,margin:0,fit:'shrink'});
  s.addText(k[1],{x:x+0.2,y:y+0.95,w:w-0.4,h:0.35,fontFace:H,fontSize:13,bold:true,color:C.UVA,isTextBox:true,margin:0});
  if(k[2]) s.addText(k[2],{x:x+0.2,y:y+1.3,w:w-0.4,h:h-1.4,fontFace:H,fontSize:10.5,color:C.CINZA,isTextBox:true,margin:0,valign:'top'}); }); }
function lista(s,itens,x,y,w,h,fs){ const arr=[]; itens.forEach((t,i)=>{ if(t.startsWith('#')) arr.push({text:t.slice(1),options:{bold:true,color:C.UVA,breakLine:i<itens.length-1}}); else arr.push({text:t,options:{bullet:true,breakLine:i<itens.length-1}}); });
  s.addText(arr,{x:x,y:y,w:w,h:h,fontFace:H,fontSize:fs||12,color:C.TINTA,isTextBox:true,margin:0,valign:'top',paraSpaceAfter:6}); }
function capa(p,titulo_,sub,frase,rod){ const s=p.addSlide(); s.background={color:C.UVA}; simbolo(p,s,0.5,0.5,1.0,true);
  s.addText(titulo_,{x:0.5,y:1.9,w:9,h:0.9,fontFace:H,fontSize:36,bold:true,color:C.BR,isTextBox:true,margin:0,fit:'shrink'});
  s.addText(sub,{x:0.5,y:2.85,w:9,h:0.4,fontFace:H,fontSize:16,color:C.LILC,isTextBox:true,margin:0});
  if(frase) s.addText(frase,{x:0.5,y:3.6,w:8.5,h:0.7,fontFace:H,fontSize:14,color:C.BR,italic:true,isTextBox:true,margin:0});
  rodape(p,s,true,rod); return s; }
function fecho(p,titulo_,itens,rod){ const s=p.addSlide(); s.background={color:C.UVA};
  s.addText(titulo_,{x:0.5,y:0.6,w:9,h:0.9,fontFace:H,fontSize:30,bold:true,color:C.BR,isTextBox:true,margin:0,fit:'shrink'});
  const arr=itens.map((t,i)=>({text:t,options:{bullet:true,breakLine:i<itens.length-1}}));
  s.addText(arr,{x:0.5,y:1.7,w:9,h:3,fontFace:H,fontSize:16,color:C.BR,isTextBox:true,margin:0,valign:'top',paraSpaceAfter:10});
  rodape(p,s,true,rod); return s; }
module.exports={pptxgen,C,H,novo,simbolo,rodape,titulo,cards,lista,capa,fecho};
