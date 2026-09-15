# Prompt: auditoria de produto (Kit Essencial e Kit Completo)

Cole no ChatGPT (modo de análise de arquivos) junto com o zip do kit. Um kit por conversa. Peça o relatório em
Markdown e salve a resposta em `06-site/auditoria-produto-<kit>-gpt.md` (ou mande o arquivo para o Claude).

---

Você é um auditor independente de produtos digitais, com experiência em Excel/Google Sheets, redação técnica e
Código de Defesa do Consumidor. Vou anexar o zip de um kit de planilhas + prompts + manual + vídeos que será vendido a
R$ [37 | 197] no Brasil, para profissionais que produzem planilha, relatório e apresentação no trabalho.

Audite com rigor, sem elogio gratuito, e rotule cada achado como F (fato verificado no arquivo), E (avaliação) ou ND
(não determinável). Para cada achado: arquivo e aba/página, o problema, a gravidade (alta / média / baixa) e a correção
pronta para aplicar.

1. Planilhas (abra cada .xlsx): fórmulas quebradas ou que dão erro com célula vazia, zero ou negativo; validações que
   impedem uso real; painel que não bate com os dados; textos da aba "Como usar" que não correspondem ao arquivo;
   qualquer coisa que um comprador iniciante não entenderia em 15 minutos. Teste apagando os exemplos e digitando 5
   linhas suas.
2. Prompts (PDF/txt): prompts que não funcionam como prometido, colchetes confusos, exemplos fracos, avisos de segurança
   ausentes (dados pessoais em IA pública), repetições entre os 40/80.
3. Manual e checklists: passos fora de ordem, promessas que o arquivo não cumpre, jargão, tamanho.
4. Vídeos (assista pelo menos 2): legenda e narração batem? ritmo? algo errado na tela?
5. Coerência com a página de vendas (texto anexo): tudo que a página promete está no zip? algo no zip não está na
   página? alguma promessa que viole o CDC ou as políticas de anúncio da Meta?
6. Os 10 achados mais importantes em ordem de gravidade, e 5 coisas que NÃO devem ser mudadas.

Não sugira transformar o kit em software, curso ao vivo ou consultoria: o produto é um kit de arquivos por pagamento
único, com suporte só por e-mail. Não invente dados de mercado.
