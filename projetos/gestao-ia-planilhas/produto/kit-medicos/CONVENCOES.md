# Convenções do Kit de Gestão para Médicos (obrigatórias para todo build_*.py)

Leia também `../revisao-interna-2.md` (Relatório A: os defeitos que os revisores pegaram no Kit Advogados) e `../../02-oferta/medicos.md`.

1. **Helpers**: `from ssg import *` (cores, F, fill, hdr, inp, calc, kpi, lista, widths, como_usar, proteger, salvar) e
   `import dados`. `dados.py` é a FONTE ÚNICA do exemplo: clínica (PESSOAS, TURNOS, SALAS, FERIADOS), custos fixos, convênios
   (prazo e glosa histórica), procedimentos (duração, material, retorno) e TABELA de preços por pagador, ~156 pacientes
   (PACIENTES), agenda gerada turno a turno (AGENDA_TODA de 05/01 a hoje + 21 dias; AGENDA = o que aparece na 01, desde 01/07),
   parcelas a prazo (PARCELAS), guias e lotes de convênio (GUIAS, LOTES), orçamentos (ORCAMENTOS), lançamentos do caixa
   (LANCAMENTOS, gerados dos fechamentos do dia, parcelas pagas, lotes pagos e saídas), totais mensais (TOTAIS), estado em
   qualquer data (estado), histórico da 17 (HISTORICO), agenda por mês (resumo_agenda, faltas, lista_retorno), DRE (dre),
   provisão (provisao_10) e metas (metas_19). Nunca invente outra clínica, outros nomes ou outros números: tudo vem de
   `dados.py` para as 20 planilhas baterem entre si. Os números "de verdade" do exemplo estão em `NUMEROS.md`.
2. **Arquivo standalone**: sem links entre arquivos. Se precisar de dado de outra planilha, tenha uma aba de entrada
   amarela com exemplo preenchido a partir de `dados.py` (02 e 16 copiam a Agenda da 01; 14 copia Pacientes da 01; 13 · Guias
   vem dos atendimentos de convênio da 01; 09/10/11/12/18 copiam totais do Painel da 09; 17 copia os painéis de 01, 02, 09, 13,
   14 e 15; 20 copia o Histórico da 17 e a 18).
3. **Abas**: "Como usar" (primeira, via `como_usar`), depois Painel/aba principal, depois Config e as abas de dados
   (20: Como usar, Painel, Resumo, Config, Indicadores). Nomes amigáveis, sem abreviação. Painel congelado (freeze_panes) em
   tabelas longas.
4. **Células**: amarelas (`inp`) só onde o cliente digita; tudo o mais `calc` e protegido (`proteger(wb)`, sem senha).
   Nunca pinte de amarelo célula bloqueada. Listas suspensas (`lista`) em todo campo de escolha, apontando para
   intervalos SEM células vazias no meio: use `=OFFSET(Config!$B$5,0,0,MAX(1,COUNTA(Config!$B$5:$B$30)),1)` e
   a nota "preencha de cima para baixo, sem pular linha". Colunas auxiliares (chaves de ranking, concatenação) sempre ocultas.
5. **Fórmulas**: só Excel 2007+ (SUMIFS, COUNTIFS, INDEX/MATCH, IFERROR, SUMPRODUCT), para abrir no Excel 2016 e no Google
   Sheets. Nada de MINIFS/MAXIFS/TEXTJOIN/IFS (nem com `_xlfn.`): mínimo/máximo condicional via
   `SUMPRODUCT(MIN(cond*x+(1-cond)*1E+10))` / `SUMPRODUCT(MAX(cond*x))`; concatenação condicional via coluna auxiliar oculta
   com `IF(...,item&"; ","")` e `LEFT(...,LEN-2)`. Nunca XLOOKUP/FILTER/SORT/UNIQUE. Ranking via coluna auxiliar de
   pontuação (oculta) + LARGE/MATCH/INDEX. Data vazia via `IF(x="","",x)`. Nunca `OR(x="",y+z=0)` quando y pode ser "" (dá
   #VALUE!): aninhe os IFs. Nunca IF com matriz dentro de SUMPRODUCT (não é avaliado como matriz): use coluna auxiliar.
   Número dentro de texto: `FIXED(x,casas)` (separadores seguem o idioma do Excel), nunca `ROUND(x,2)&""` nem
   `TEXT(x,"#,##0")`. Formatos: `BRL`, `BRL0`, `DATA`, `PCT` do ssg; hora como `hh:mm` (valor de tempo, não texto);
   nunca formatar taxa como soma.
6. **Datas do exemplo**: agenda futura, vencimentos em aberto e orçamentos abertos como fórmula relativa
   (`dados.prazo_formula(d)` = `=TODAY()+d`); histórico (atendimentos realizados, lotes, parcelas pagas, caixa) fixo em 2026.
   Data de referência em Config = `=TODAY()`. Horas disponíveis da agenda só contam dias já passados (até ontem).
7. **Textos**: português do Brasil, direto, sem "você" acusatório. Nada clínico (diagnóstico, conduta, prontuário, código de
   procedimento, exame): "procedimento" é só o nome administrativo do atendimento; pacientes têm nome e contato fictícios e
   nada mais. Nunca prometer "lotar a agenda", captar pacientes ou resultado financeiro: a planilha AVISA e mede; a decisão é
   da clínica. Divulgação de preços e de serviços segue as regras do CFM (o kit lembra, não redige). Cobrança de paciente
   sem exposição ou constrangimento.
8. **Exemplo coerente**: HOJE = segunda 14/09/2026 (Config = `=TODAY()`); a sexta do painel é 11/09/2026 e nenhum lançamento
   pago (caixa, parcela, lote) tem data depois dela; nada "Realizado" na agenda depois de 11/09 e nada "Agendado/Confirmado"
   antes de hoje. 17 mostra setembro em andamento (variação de agenda e caixa só quando Config diz que o mês fechou); 18 e 20
   analisam agosto (último mês fechado; 20 = agosto × julho); 16 fica em agosto; 08 usa o volume de agosto. Uma só definição
   de inadimplência (vencido ÷ (pago + vencido), só do que foi combinado a prazo); uma só glosa (glosa ÷ (pago + glosa) dos
   lotes pagos); uma só hora mínima (05: R$ 200 ÷ (1 − 0,30 − 0,11) = R$ 338,98 → R$ 340; 06/07/08 usam a mesma conta);
   custo cheio do procedimento = (minutos + 0,4 × 20 min de retorno nas consultas) ÷ 60 × custo-hora + material (06 = 07 =
   08); alíquota única de 11 % (efetiva, "combinada com o contador"); repasse 50 % da produção do mês, pago dia 10; custo do
   dinheiro 1,5 % ao mês (07). Parcela paga ⇔ entrada no caixa; lote pago ⇔ entrada no caixa (menos a glosa); recurso
   aceito ⇔ entrada "Recurso de glosa"; taxas de cartão do mês (16) ⇔ uma saída no fim do mês (09); repasse devido (11) =
   50 % da produção da parceira no Painel da 01. A 01 é a fonte da agenda e do cadastro de pacientes.
9. **Cabeçalho da aba principal**: `titulo(ws, "Clínica Vida Plena (exemplo fictício) · <nome da aba> · <mês ou data>",
   "Nada para digitar aqui..." ou a instrução certa)`. Rodapé/nota com fonte `nota()`.
10. **Verificação obrigatória** antes de entregar: copiar o .xlsx para o scratchpad e rodar
    `python3 /root/.claude/skills/synced/*/xlsx/scripts/recalc.py <copia> 300` → zero erros; ler a cópia com `data_only=True` e
    conferir 3 valores do painel contra `dados.py`. Nunca recalcular o original. Depois, com as 20 cópias recalculadas na
    mesma pasta: `python3 verifica_coerencia.py <pasta>` (0 falhas; hoje são 518 verificações) e
    `python3 cache_valores.py <pasta>` (grava só os valores calculados nos .xlsx originais, para a pré-visualização em
    celular/Drive não aparecer vazia; não use "abrir e salvar" no LibreOffice, que reescreve estilos, gráficos e colunas
    ocultas). Regerar `NUMEROS.md` com `python3 numeros.py <pasta>` (inclui a lista dos nomes de prompt citados) e as telas
    com `cd .. && python3 telas.py medicos`.
11. **Nomes de arquivo**: `NN-nome-em-minusculas-com-hifens.xlsx` exatamente como a tabela da oferta, gerados por
    `build_NN_nome.py` na pasta `kit-medicos/` (salvar em `kit-medicos/NN-....xlsx`; `entrega/` é montada depois pelo
    empacotador `../empacotar_medicos.py`).
12. **Título do documento** (`salvar(wb, arquivo, "<Nome> · Kit de Gestão para Médicos")`).
13. **Prompts citados** nos "Como usar" usam nomes provisórios no formato "Grupo NN · Título" (Agenda, Preço, Caixa,
    Recebíveis, Painel). A lista completa está no fim de `NUMEROS.md`: quem escrever a biblioteca de prompts usa exatamente
    esses nomes (ou troca aqui e regera as 20).
