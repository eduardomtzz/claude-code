# Convenções do Kit IA no Trabalho Completo (obrigatórias para todo build_*.py)

Dez planilhas: as 01, 02 e 03 são as mesmas do Kit Essencial (copiadas de `../kit-essencial/entrega/`
por `build_pacote.py`; as regras delas estão em `../kit-essencial/CONVENCOES.md`); as 04 a 10 são
deste kit e usam `ssg.py`. Não há `dados.py`: cada `build_*.py` traz o seu pedaço do exemplo, mas
o exemplo é um só — a agência Prisma Comunicação — e tem de fechar entre os arquivos.

Leia também `../revisao-interna-1.md`, `../auditoria/triagem-2026-09-17.md` e `../../02-oferta/kit-completo.md`.

1. **Helpers**: `from ssg import *` (cores, F, fill, borda, hdr, inp, calc, kpi, lista, nota,
   rotulo, titulo, widths, como_usar, proteger, salvar, DATA, BRL, BRL0, PCT, MESES).
   `como_usar` já acrescenta Legenda, Proteção, Requisitos, Google Sheets, Exemplos, Data de
   referência e Suporte — não repita essas linhas no `build`.
2. **Arquivo standalone**: sem link entre arquivos. Dado que vem de outra planilha entra como aba
   de entrada amarela, com o exemplo já preenchido.
3. **Abas**: "Como usar" primeira, depois o painel de leitura, depois Config, depois as abas de
   digitação. Painel com `freeze_panes` e sem linhas de grade.
4. **Células**: `inp` só onde o cliente digita; todo o resto `calc` e protegido por `proteger(wb)`,
   sem senha. Colunas auxiliares (chave de ordenação, % efetivo) ocultas e em fonte cinza.
5. **Fórmulas**: só Excel 2007+. Proibido mesmo com `_xlfn.`: MINIFS, MAXIFS, TEXTJOIN, IFS,
   SWITCH, CONCAT, XLOOKUP, FILTER, SORT, UNIQUE, SEQUENCE. Mínimo/máximo condicional via
   `SUMPRODUCT(MIN(cond*x+(1-cond)*1E+10))` / `SUMPRODUCT(MAX(cond*x))`, sempre embrulhado em
   `IF(OR(mf=0,mf>=1E+10),"",mf)` para não vazar 1E+10 nem data de 1900. Último valor de uma faixa
   via `LOOKUP(9,99E+307;faixa)`. Ranking via coluna auxiliar de pontuação oculta + LARGE/MATCH/INDEX.
6. **Listas suspensas** com `strict=True` onde digitar fora do cadastro estragaria conta: pessoa e
   projeto na 09 (sem isso o MATCH falhava, o IFERROR devolvia zero e hora trabalhada virava
   trabalho de graça, sem aviso), projeto na 04, reunião e dono na 05, categoria na 07 e na 10.
7. **Datas do exemplo**: literais, congeladas em **14/09/2026**, inclusive a data de referência em
   Config (04!B5, 05!B5, 06!B8, 08!B5), com a nota mandando trocar por `=HOJE()` ao começar a usar.
   Nunca `=TODAY()` em Config junto com datas de exemplo fixas: era o pior dos dois mundos — em
   18/09/2026 a 05 já mostrava 5 de 7 pendências atrasadas (o desenho era 3) e, em 01/10, o "Ganho
   no trimestre" da 08 iria a zero porque o trimestre virava. Única exceção: a 10 usa
   `COUNTIFS(datas;">"&TODAY())` no checklist para acusar data digitada no futuro, o que é
   verificação viva e correta (a base de exemplo termina em 13/09/2026, então fica zerada para sempre).
   A 01 do Essencial mantém prazos relativos, pelo motivo explicado nas convenções dela.
8. **Exemplo coerente entre os arquivos** (é o que `verifica_coerencia.py` cobra):
   - Os 4 projetos da 04 (Config) existem na 09 com o mesmo nome e cliente.
   - Proposta **Ganha** na 08 = projeto na 09 com o mesmo valor cobrado: Loja Verde 24.000,
     Bistrô 42 38.000, Padaria do Sol 9.500, Horizonte 16.000. Proposta enviada da Clínica
     Bem-Estar 4.500 entra na 09 com status **Proposta** e zero hora lançada.
   - Nenhuma hora na 09 antes do início do projeto na 04; projeto concluído não tem hora depois do
     prazo final. A parte da agenda que sobra vai para "Comercial e propostas".
   - Toda pendência da 05 aponta para uma reunião que existe (R-001 a R-004).
   - A última semana preenchida na aba Semanas da 06 é igual ao "Valor atual" da aba Metas; a aba
     Meses é o último valor de cada faixa (S1-4, S5-9, S10-13).
   - Toda categoria lançada na 07 (Realizado) e na 10 (Base) existe na lista de Config/Listas.
9. **Cabeçalho da aba principal**: `titulo(...)` com "Prisma Comunicação (exemplo fictício) · <aba>
   · <mês ou data>" e a instrução certa ("Nada para preencher aqui: tudo vem de ..."). Notas de
   rodapé com `nota()`.
10. **Verificação obrigatória** antes de entregar, na ordem:
    ```
    python3 build_projetos.py ... build_base.py      # todos os que mudaram
    # copiar os .xlsx para uma pasta e recalcular no LibreOffice em perfil pt-BR
    soffice --headless -env:UserInstallation=file://<perfil> --convert-to xlsx --outdir <pasta>/calc <pasta>/*.xlsx
    python3 cache_valores.py <pasta>/calc       # grava só os <v>; nunca "abrir e salvar"
    cp ../kit-essencial/0[1-3]-*.xlsx <pasta>/calc/
    python3 verifica_coerencia.py <pasta>/calc  # 0 falhas (inclui as 01-03 do Essencial)
    python3 build_pacote.py                     # monta entrega/ e o zip
    cd .. && python3 recalc_todos.py            # 0 erros de fórmula nos quatro kits
    ```
    Ao mudar a estrutura de um painel, ajuste as linhas de referência em `verifica_coerencia.py`:
    verificação apontando para a linha errada passa calada, o que é pior do que não existir. Para
    provar que ela não mente, plante um defeito numa cópia e confira que ela acusa.
