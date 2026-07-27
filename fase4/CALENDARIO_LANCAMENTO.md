# Calendário de lançamento — ONE by GrowUp (item 4.8)

> Sequência sugerida de 4 semanas usando os materiais prontos do repositório.
> Todas as publicações nos canais da GrowUp (princípio do ecossistema).
> Datas são relativas ao "Dia D" = dia da publicação do sistema em produção.

## Pré-lançamento (semana -1)

| Dia | Ação | Material |
|---|---|---|
| D-5 | Publicar o sistema no Lovable (produção vira ONE) e validar | Fase 2 concluída |
| D-3 | Teaser nos stories: app icon + "vem aí" (recorte do vídeo, cena 1) | `fase3/one-by-growup_video_9x16.mp4` (0–6s) |
| D-2 | Aquecer a base por WhatsApp/e-mail: "segunda-feira seu sistema muda" | pitch 10s do `fase1/GUIA_VERBAL.md` |
| D-1 | Stories com a pergunta da dor (enquete: "quantas ferramentas você paga?") | `post_lancamento_9x16.png` |

## Semana 1 — o lançamento

| Dia | Ação | Material |
|---|---|---|
| D | **Vídeo de lançamento no feed** (16:9 ou 4:5) + post fixado | `fase3/one-by-growup_video_1080p.mp4` |
| D | Mesmo vídeo em reels/stories | `fase3/one-by-growup_video_9x16.mp4` |
| D+1 | **Carrossel "conheça o ONE"** (8 slides) | `fase4/social/carrossel_01..08_*_4x5.png` |
| D+2 | Post de lançamento estático (reforço p/ quem não viu) | `post_lancamento_4x5.png` |
| D+4 | Atualizar página "Conheça o ONE" no site + bio dos perfis | `fase4/landing-conheca-o-one.html` |

## Semanas 2–3 — um módulo por vez (na ordem da narrativa)

| Dia | Post | Material |
|---|---|---|
| D+7 | **Nexa One** (atrai) — provocação: "demita a agência" | `post_nexa-one_*` + one-pager no comercial |
| D+9 | **Sales One** (converte) | `post_sales-one_*` |
| D+11 | **Profit One** (lucra) | `post_profit-one_*` |
| D+14 | **Flow One** (executa) | `post_flow-one_*` |
| D+16 | **North One** (dá o norte) | `post_north-one_*` |
| D+18 | **Growth One** (acelera) — fecho com IA, o diferencial | `post_growth-one_*` |

Cada post de módulo: versão 4:5 no feed + 9:16 nos stories no mesmo dia.
Legenda: dor → benefício → "parte do ONE by GrowUp" → CTA "link na bio".

## Semana 4 — conversão

| Dia | Ação | Material |
|---|---|---|
| D+21 | Reels: cortes do tour dos módulos (6–10s cada, 1 por dia útil) | recortes do `video_9x16` (cenas 4–9) |
| D+23 | Prova social: print de tela real + resultado de cliente | capturas do sistema publicado |
| D+25 | Carrossel educativo: "o método GrowUp em 6 passos" (usar narrativa) | derivar do gerador `build_social.py` |
| D+28 | Oferta/CTA: "diagnóstico gratuito" → funil do Nexa One | `/diagnostico_marketing` do sistema |

## Comercial (paralelo, a partir do Dia D)

- **Deck** (`fase4/deck-one-by-growup.pptx`) nas reuniões de venda
- **One-pagers** (`fase4/onepagers/*.pdf`) como material de follow-up por módulo
- Assinatura de e-mail da equipe com o logo novo + tagline

## Regras rápidas

1. Toda peça assina GrowUp; primeira menção "ONE by GrowUp", depois "o ONE"
2. Um módulo por post — nunca misturar cores de módulos numa mesma peça
3. Sempre par feed + stories no mesmo dia
4. Novas peças: gerar via `fase4/build_social.py` para manter a família
