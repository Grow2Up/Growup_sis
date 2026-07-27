# Guia de social — ONE by GrowUp (Fase 4A, item 4.1)

## Sistema visual das peças
- Fundo: #101014 (preto da marca com viés azul)
- Wash radial na cor do módulo (16–30% de opacidade) atrás do conteúdo
- Estrutura: tile do módulo (ícone branco) → nome em Poppins 700 com "One"
  na cor → verbo da narrativa em caps espaçadas → descritor em Manrope
- Rodapé fixo: logo ONE by GrowUp (offwhite) + "O método GrowUp em forma
  de plataforma." — toda peça assina a plataforma/ecossistema
- Formatos exportados: 4:5 (1080×1350, feed), 1:1 (1080×1080) e 9:16
  (1080×1920, stories) — dimensões oficiais do Meta
- Zona segura (9:16): conteúdo respeita ~280px no topo (nome do perfil),
  ~340px na base (caixa de resposta/UI) e 110px nas laterais — nada fica
  sobreposto pela interface de stories/reels
- Sem CTA nas peças: o convite à ação vai na legenda/caption, não na arte

## Conteúdo do pack (fase4/social/)
- `post_lancamento_*` — anúncio do ONE (chips de ferramentas + tagline)
- `post_<modulo>-one_*` — 1 post de apresentação por módulo (6)
- `carrossel_01..08_*` — carrossel de lançamento: capa (pergunta da dor),
  6 slides de módulo (numerados 1/6–6/6, descrição longa) e fechamento
  de marca (assinatura, sem CTA)
- Vídeos: `fase3/one-by-growup_video_1080p.mp4` (feed/YouTube) e
  `fase3/one-by-growup_video_9x16.mp4` (reels/stories)

## Regras de uso
- Sempre publicar nos canais da GrowUp (princípio do ecossistema)
- Legenda: primeira menção "ONE by GrowUp", depois "o ONE"
- Módulo em legenda: "Nexa One · ONE by GrowUp"
- Gerador editável: `fase4/build_social.py` (novas peças mantêm a família)
