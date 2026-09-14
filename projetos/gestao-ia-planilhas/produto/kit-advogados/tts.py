"""Narração: Google Cloud Text-to-Speech quando GOOGLE_TTS_API_KEY existir; senão, Piper (local, gratuito).
Nunca grave a chave em arquivo do repositório: ela vem da variável de ambiente."""
import os, json, base64, wave, pathlib, urllib.request
VOZ_PADRAO=os.environ.get('GOOGLE_TTS_VOICE','pt-BR-Chirp3-HD-Aoede')   # feminina; masculina: pt-BR-Chirp3-HD-Charon, pt-BR-Chirp3-HD-Fenrir
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
_piper=None
def google(texto, wav, voz=None, velocidade=1.0):
    key=os.environ['GOOGLE_TTS_API_KEY']
    body={'input':{'text':texto},'voice':{'languageCode':'pt-BR','name':voz or VOZ_PADRAO},
          'audioConfig':{'audioEncoding':'LINEAR16','sampleRateHertz':24000,'speakingRate':velocidade}}
    req=urllib.request.Request('https://texttospeech.googleapis.com/v1/text:synthesize?key='+key,data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=60) as r: audio=base64.b64decode(json.loads(r.read())['audioContent'])
    pathlib.Path(wav).write_bytes(audio)   # LINEAR16 já vem com cabeçalho WAV
def piper(texto, wav):
    global _piper
    from piper import PiperVoice
    if _piper is None: _piper=PiperVoice.load(str(S/'voz'/'pt_BR-faber-medium.onnx'))
    try:
        from piper import SynthesisConfig
        with wave.open(str(wav),'wb') as w: _piper.synthesize_wav(texto, w, syn_config=SynthesisConfig(length_scale=1.1))
    except Exception:
        with wave.open(str(wav),'wb') as w: _piper.synthesize_wav(texto, w)
def sintetiza(texto, wav, voz=None):
    """Gera o wav e devolve a duração em segundos. `voz` permite trocar a voz por cena (só no Google)."""
    if os.environ.get('GOOGLE_TTS_API_KEY'): google(texto, wav, voz)
    else: piper(texto, wav)
    with wave.open(str(wav),'rb') as w: return w.getnframes()/w.getframerate()
