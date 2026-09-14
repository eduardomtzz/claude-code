# Oferta: Kit de Gestão para Médicos

Produto 4 da escada (aprovada em 2026-09-13). Página `/medicos`. Preço único: **R$ 697**.
Rascunho de 2026-09-14 a partir de `01-pesquisa/resumo-rodada-3.md` (censo: clínica/consultório é a maior vertical,
~10 mil anúncios ativos), `censo-verticais.md`, `saas-precos.md`, da oferta dos Dentistas (`dentistas.md`, que
compartilha o núcleo de clínica) e dos aprendizados dos kits 1 a 3 (`produto/revisao-interna-1.md` e `-2.md`).
Este kit **cria o núcleo de clínica** que os produtos 5 (Dentistas) e 7 (Estética) vão clonar.

## Promessa

De "atendo o dia inteiro e não sei se a clínica dá lucro" para: agenda com ocupação e faltas medidas, preço de
consulta e procedimento calculado pela hora de atendimento, convênio com glosa e prazo sob controle, caixa com
provisão de impostos e repasse aos colegas separado, e o painel da clínica em uma tela. Rotina de 30 minutos por
semana. Sem mensalidade, sem sistema, sem contratar ninguém.

Linha obrigatória no topo da página: "Kit de planilhas prontas + manual + aulas curtas + prompts de IA.
Você baixa, preenche e usa. Não é software médico, não é prontuário, não tem mensalidade."

**Nunca:** promessa de resultado financeiro, de "lotar a agenda", de captar pacientes; nada clínico (diagnóstico,
conduta, prontuário, receituário); nenhum dado de paciente além de nome fictício, contato, valor e data; nenhuma
peça de publicidade médica pronta (a Resolução CFM 2.336/2023 regula o que o médico pode divulgar; o kit avisa
quando um texto precisa dessa revisão).

## Mecanismo: cinco núcleos, um fechamento por semana

1. **Agenda que se mede.** Horas disponíveis × atendidas por profissional e sala, faltas e remarcações, lista de
   retorno. A rotina de segunda confere a semana; a de sexta fecha o caixa.
2. **Preço pela hora, não pela tabela do vizinho.** Custo da hora de atendimento (fixo + equipe + pró-labore ÷
   horas atendidas) + material + margem = preço de consulta e procedimento. Simulador convênio × particular com
   prazo de recebimento e glosa esperada.
3. **Caixa com provisão e repasse.** Entradas por paciente, convênio e categoria; saídas; provisão de impostos, 13º e
   férias; repasse aos médicos parceiros e pró-labore separados; reserva de três meses de custo fixo.
4. **Recebíveis sem surpresa.** Guias enviadas × pagas × glosadas por convênio; parcelas particulares com régua
   de cobrança educada; orçamentos apresentados × aprovados; conciliação de cartão e taxas.
5. **Painel de sexta.** Uma tela: ocupação, faltas, caixa do mês, convênio a receber e glosas, orçamentos abertos.
   O prompt "Explicar o mês" transforma em texto para o sócio ou o contador.

Por que funciona: software de clínica (Clínica Experts a partir de R$ 62/mês; 4Medic, OnDoctor, HiDoctor, Kure com
planos maiores) cobra todo mês e vive de agenda e prontuário; a parte do dinheiro fica com o contador, que só vê
o mês passado. Planilha avulsa não tem método nem rotina. O kit entrega custo-hora, provisão e uma rotina curta.

## Avatar

Médico ou médica dono(a) de consultório ou clínica pequena (1 a 3 médicos, 1 recepcionista, 1 a 2 colegas por
repasse), 5 a 20 anos de formado, atende particular e 2 a 4 convênios, PJ médica no Simples ou lucro presumido.
Nunca teve aula de gestão. Não sabe o custo da própria hora; aceita tabela de convênio sem calcular; descobre a
glosa quando o extrato chega; mistura conta pessoal e da clínica; a recepção não mede falta nem conversão de
orçamento. Já viu software de clínica e paga sem usar a parte financeira, ou desistiu. Compra pelo celular, à noite.

Dores em ordem (censo e anúncios ativos): "trabalho muito e não vejo o dinheiro" (caixa e pró-labore), convênio
que paga em 60 a 90 dias e glosa, preço de consulta e procedimento no chute, faltas e agenda com buracos,
imposto e contador, repasse mal calculado ao colega.

## Produto: 20 planilhas em 5 núcleos

Formato: Excel 2016+/Microsoft 365 e Google Sheets, só funções 2007+, fórmulas protegidas sem senha, clínica fictícia
preenchida ("Clínica Vida Plena", 2 sócios: Dra. Carolina Mendes, clínica médica, e Dr. Paulo Andrade, cardiologia;
1 médica parceira por repasse, Dra. Renata Sousa, endocrinologia, 2 turnos por semana; 1 recepcionista, Bruna
Carvalho; 3 convênios fictícios: Saúde Total, MediPlan, Vida Care; 156 pacientes fictícios), dados de setembro de
2026 com agosto fechado, datas relativas a hoje onde houver agenda, aba "Como usar" em cada arquivo, formato
brasileiro, valores em cache. Só dados administrativos fictícios. **Nada clínico. O kit não é prontuário.**

| Núcleo | # | Planilha | Resolve |
|---|---|---|---|
| 1. Agenda | 1 | Agenda e ocupação por profissional e sala (horas disponíveis × atendidas) | "quantas horas vazias?" |
| | 2 | Faltas, remarcações e lista de retorno (taxa de falta por dia e convênio) | "por que a agenda esvazia?" |
| | 3 | Rotina da semana da clínica (segunda e sexta) | "por onde começo?" |
| | 4 | Checklist de abertura e fechamento do dia (agenda confirmada, caixa fechado, guias separadas) | dia sem fechamento |
| 2. Preço | 5 | Custo da hora de atendimento (fixo + equipe + pró-labore ÷ horas de atendimento) | "quanto custa a minha hora?" |
| | 6 | Precificação de consulta e procedimento (hora + material + margem) | preço certo |
| | 7 | Simulador convênio × particular (tabela, prazo, glosa esperada, custo do dinheiro) | "vale a pena este convênio?" |
| | 8 | Tabela de preços e referência por procedimento | preço coerente |
| 3. Caixa | 9 | Caixa da clínica (entradas por paciente, convênio e categoria; saídas) | "cadê o dinheiro" |
| | 10 | Provisão de impostos, 13º e férias | susto no fim do ano |
| | 11 | Repasse aos médicos parceiros e pró-labore dos sócios (PF × clínica) | "pago 50 % e sobra nada" |
| | 12 | Reserva de três meses e metas de caixa | vulnerabilidade |
| 4. Recebíveis | 13 | Convênios a receber (guias enviadas, pagas, glosadas, recurso de glosa) | "quanto o convênio deve?" |
| | 14 | Parcelas particulares e inadimplência com régua de cobrança | quem atrasou, quando cobrar |
| | 15 | Orçamentos apresentados × aprovados (funil da recepção) | "quanto vou fechar?" |
| | 16 | Conciliação de cartão e taxas (crédito, débito, Pix, antecipação) | taxa comendo margem |
| 5. Painel | 17 | Painel da clínica (ocupação, faltas, caixa, convênio a receber, glosas, orçamentos) | uma tela |
| | 18 | Resultado mensal simplificado (DRE da clínica) | lucro de verdade |
| | 19 | Metas do trimestre da clínica | ritmo da meta |
| | 20 | Resumo do mês para a IA e para o contador | fechamento em texto |

Reaproveitamento honesto: 3, 9, 10, 11, 12, 14, 15, 17, 18, 19 e 20 derivam das planilhas do Kit Advogados
(mesma arquitetura, vocabulário da clínica, regras próprias: convênio, glosa, repasse). 1, 2, 4, 5, 6, 7, 8, 13 e
16 são novas. Este é o núcleo de clínica: Dentistas troca convênio por laboratório de prótese e cadeira; Estética
troca por pacote de sessões e insumos.

Acompanha:
- **Manual de implantação** (PDF, cerca de 20 páginas): quatro semanas, as 20 planilhas distribuídas, rotina de
  segunda (agenda) e de sexta (caixa e painel).
- **8 aulas em vídeo** (2 a 3 min, tela real, narração por IA, legenda gravada): 1 método e rotina; 2 agenda e
  faltas; 3 custo da hora; 4 preço e simulador de convênio; 5 quanto cobrar por este procedimento; 6 caixa,
  provisão e repasse; 7 convênios, parcelas e cobrança; 8 painel de sexta e fechamento.
- **Biblioteca de 41 prompts da clínica**: explicar o mês ao sócio, escrever cobrança educada, resumir os convênios,
  preparar a reunião com o contador, revisar a tabela de preços, montar a rotina da recepção, redigir recurso de
  glosa em linguagem administrativa. Todos com "quando usar", exemplo e o que conferir. Nenhum prompt produz
  conteúdo clínico nem publicidade médica.
- **3 modelos de apresentação**: resultado do mês para os sócios (8), proposta de parceria para médico que vai
  atender na clínica (10), convênios e recebíveis para o contador (8).
- **Checklists**: abertura e fechamento do dia, fechamento do mês, antes de fechar um convênio.

## Bônus (cada um mata uma objeção)

| Bônus | Objeção | Onde |
|---|---|---|
| 15 modelos de mensagem: confirmação, lembrete, falta, retorno, cobrança educada, confirmação de pagamento (e-mail e WhatsApp) | "cobrar paciente é constrangedor" | PDF + txt |
| Guia LGPD para clínica pequena (dado de saúde é sensível: o que guardar, onde, por quanto tempo; o que nunca colar em IA) | "e os dados dos pacientes?" | PDF |
| Roteiro da reunião mensal com o contador (PJ médica, Simples × presumido: o que perguntar, sem fazer contabilidade) | "não sei o que mandar para o contador" | PDF |

Sem modelo de contrato de parceria (é conteúdo jurídico) e sem peça de divulgação (publicidade médica é regulada).

## Preço e escada

- Preço único: **R$ 697** à vista ou 12× no cartão (total informado no checkout). Sem âncora riscada.
- Âncoras verdadeiras na copy: software de clínica de R$ 62 a algumas centenas por mês; uma glosa não recorrida;
  40 horas montando do zero. "Menos que um ano de um software de clínica típico, uma vez, e os arquivos ficam com você."
- Order bump no checkout: Kit IA no Trabalho · Essencial por R$ 27 para quem ainda não tem. Sem upsell no lançamento.

## Garantia

7 dias incondicional (CDC art. 49), pelo checkout ou por e-mail. "Baixou, abriu, não era o que esperava: pede o
dinheiro de volta em até 7 dias, sem explicar."

## Economia do funil

Premissas: Kiwify 8,99 % + R$ 2,49, reembolso 5 %, imposto 6 % sobre o líquido, 70 % da margem em mídia.

| Item | R$ 697 |
|---|---|
| Taxa do checkout | 65,15 |
| Líquido após reembolso e imposto | 564,20 |
| CPA máximo (100 % da margem) | R$ 564 |
| CPA alvo (70 %) | R$ 395 |
| ROAS de equilíbrio | 1,24 |
| ROAS alvo | 1,77 |
| Conversão de equilíbrio com clique a R$ 2,50 | 0,44 % |

Público na Meta: interesses em CRM (conselho), medicina, "consultório médico", cargo médico(a); Brasil; 28 a 60.
Sem categoria especial de anúncio (o produto é gestão, não saúde).

## Nome da oferta

"Kit de Gestão para Médicos" (como na home). Na copy: "o kit". Evitar "sistema", "software", "prontuário",
"médico" como adjetivo do kit. Clínica fictícia: "Clínica Vida Plena".

## Decisões para o Eduardo (registrar em DECISOES.md)

1. Preço R$ 697 confirmado, 12× no cartão, sem âncora riscada: ok?
2. Order bump com o Essencial a R$ 27: ok?
3. Clínica fictícia "Clínica Vida Plena" com as especialidades acima: ok?
4. Bônus sem modelo de contrato de parceria e sem peça de divulgação: concorda?

Enquanto não há resposta, a produção segue com essas quatro premissas.
