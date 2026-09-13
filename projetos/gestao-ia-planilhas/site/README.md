# Site do Seu Sócio Gestor

Site estático, sem framework. Uma marca, um domínio (`seusociogestor.com.br`), uma página por
produto. Base construída em 2026-09-13 a partir de `01-pesquisa/resumo-rodada-4.md`.

## Estrutura

```
site/
  config.json        dados da empresa, e-mails, domínio, ID do Pixel (vazio até existir)
  build.py           monta public/ a partir de src/ (python3, sem dependências)
  src/layout.html    cabeçalho, rodapé legal e banner de cookies, comuns a todas as páginas
  src/pages/*.html   conteúdo de cada página (primeiras linhas: title, description)
  public/            saída pronta para publicar (é o que vai para a hospedagem)
    assets/css/site.css   estilo (tokens da marca em 03-marca/tokens.css)
    assets/js/site.js     consentimento (ANPD), Pixel condicionado, preferências, UTM
    assets/img/           logos SVG, ícone, imagem de compartilhamento
    _headers              cabeçalhos de segurança e cache (Cloudflare Pages)
    sitemap.xml, robots.txt, 404.html
  screenshots/       prints mobile e desktop gerados com Chromium
```

Páginas: `/` (home institucional e catálogo), `/sobre/`, `/suporte/`, `/termos/`,
`/privacidade/`, `/cookies/` (preferências funcionais), `/reembolso/`, `404`.
Páginas de produto (`/kit/`, `/ia/`, `/advogados/`, `/medicos/`, `/dentistas/`,
`/entregadores/`) e de obrigado entram uma a uma, na ordem do README do projeto.

## Como editar e publicar

1. Edite `config.json` (CNPJ, razão social, endereço, e-mails) ou os arquivos em `src/`.
2. Rode `python3 build.py`. Nunca edite `public/*.html` à mão: o build sobrescreve.
3. Faça commit de `src/`, `config.json` e `public/`.
4. Hospedagem recomendada: **Cloudflare Pages**, projeto ligado a este repositório, diretório de
   saída `projetos/gestao-ia-planilhas/site/public`, sem comando de build (a pasta já vem pronta).
   Domínio: apontar `seusociogestor.com.br` e `www` para o Pages nas DNS da GoDaddy (ou
   transferir a zona para a Cloudflare, mais simples). O `.com` redireciona para o `.com.br`.

## Regras que o código já cumpre

- Banner de cookies com "Aceitar todos", "Rejeitar não necessários" e "Configurar" com o mesmo
  destaque; nada ligado por padrão além do necessário; escolha registrada em `localStorage`
  (`ssg_consent_v1`) e alterável em `/cookies/`.
- Pixel da Meta só carrega se `config.json` tiver `meta_pixel_id` e o visitante tiver aceitado
  publicidade. Sem consentimento, nada é enviado, nem pelo navegador nem pelo servidor.
- Links com `data-checkout` recebem os parâmetros UTM e `fbclid` da URL atual.
- Rodapé com razão social, CNPJ, endereço, e-mail e prazo de resposta em todas as páginas
  (Decreto 7.962/2013); aviso de não afiliação à Meta; direito de arrependimento citado.
- Fontes do Google com `display=swap`; imagens SVG; sem bibliotecas externas.

## Pendências

- Preencher `config.json` com CNPJ, razão social completa e endereço (hoje marcados "a preencher").
- Criar as caixas `suporte@` e `privacidade@` no domínio (GoDaddy ou Cloudflare Email Routing).
- Auto-hospedar as fontes (WOFF2) antes do tráfego pago, para reduzir o LCP.
- Adicionar medição (opcional) sob a categoria "medição" do consentimento.
