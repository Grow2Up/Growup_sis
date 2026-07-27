# ONE by GrowUp — Planejamento Mestre de Rebranding

> Documento mestre do projeto de rebranding do sistema (antes "Growup SIS" /
> "GrowUp 360" / "Business Suite", em sistema.grow2up.com.br).
> **Fase 0 concluída e aprovada** — este documento consolida as decisões e
> detalha as fases de execução.

---

## 1. Contexto e objetivo

O sistema de gestão da GrowUp será rebatizado como **ONE by GrowUp**: uma
plataforma única composta por uma família de módulos com sufixo "One", cada um
posicionado como um sub-produto vendável. O projeto abrange naming (concluído),
identidade verbal e visual, aplicação completa no sistema e um vídeo animado de
apresentação.

O rebranding também corrige problemas identificados nas análises anteriores
(ver `ANALISE_IDENTIDADE_VERBAL_VISUAL.md`): naming fragmentado, azul primário
divergente da marca oficial e ausência de tipografia institucional.

## 2. Arquitetura da marca — APROVADA ✅

```
GrowUp (marca-mãe — pacote oficial: azul #4767FA, monograma U↗)
└── ONE by GrowUp (a plataforma)
    ├── Nexa One   → Marketing            "substitui a agência"
    ├── Sales One  → CRM / Comercial      "traz a venda"
    ├── Growth One → Growth Intelligence  "acelera com IA"
    ├── Profit One → ERP Financeiro       "garante o lucro"
    ├── Flow One   → Operacional          "faz o negócio rodar"
    └── North One  → Relatórios           "dá o norte"
```

**Narrativa da família** (base para vendas e vídeo):
*Nexa atrai → Sales converte → Profit lucra → Flow executa → North dá o norte → Growth acelera.*

**Encaixe das demais áreas do sistema** (aprovado):
| Área existente | Destino |
|---|---|
| Planejamento Estratégico (SWOT, GPD, canvas, personas) | Dentro do **Growth One** |
| Avaliação de Desempenho + taxas/hora | Dentro do **Flow One** |
| Mensagens / WhatsApp | Camada transversal da plataforma, sem sub-marca |

### Princípio de comunicação — o ecossistema GrowUp 🔑

**A plataforma nunca se comunica sozinha: ela é um meio dentro do ecossistema
GrowUp.** Isso norteia toda a identidade e todo o material:

- O ONE não é um "software à venda"; é **a plataforma que operacionaliza o
  método GrowUp** (consultoria, auditorias, agentes, crescimento).
- Toda peça de comunicação carrega o endosso da marca-mãe: assinatura
  "by GrowUp" sempre presente, identidade visual herdada (azul #4767FA,
  monograma U↗, tipografia institucional).
- Hierarquia de mensagem: **GrowUp (quem transforma) → ONE (como se
  operacionaliza) → módulos (onde acontece)**. Um post do Nexa One é, antes
  de tudo, um post da GrowUp.
- Implicação prática: não criamos perfis/canais separados para o ONE ou para
  módulos — a comunicação sai nos canais da GrowUp, com o ONE como produto
  do ecossistema.

**Memória de naming** — descartados: Family One (nome-guarda-chuva original),
Vision One (conflito: Trend Vision One/Trend Micro), Cash/Money/Fin/Balance/
Result One, Team/Ops/Task One, Radar/Pulse/Data/Insight One. Conflitos
evitados: Capital One, Bank One, Business One (SAP), Caixa One.

---

## 3. Fase 1 — Identidade verbal e visual do ONE by GrowUp

**Objetivo**: definir e documentar a identidade completa antes de tocar no sistema.
**Premissa**: herdar a marca-mãe GrowUp (paleta oficial #4767FA, #3A50D2,
#DE571B, #5E8C54, #F1F1F1, #6C6C70, #141414; monograma U↗; wordmark caixa-baixa).

| # | Atividade | Entrega | Aprovação sua? |
|---|---|---|---|
| 1.1 | **Identidade verbal**: tagline do ONE, descritor oficial de cada módulo (1 linha), tom de voz, regras de escrita (grafia "ONE by GrowUp", uso do "by", pt-BR) e **regras de mensagem do ecossistema** (hierarquia GrowUp → ONE → módulos; como cada peça referencia a marca-mãe) | Guia verbal (MD/PDF) | Sim |
| 1.2 | **Logo ONE by GrowUp**: wordmark + versões horizontal/vertical/selo/app icon, derivado do monograma U↗; malha de construção e área de respiro | SVG + PNG | Sim |
| 1.3 | **Sistema de sub-marcas dos 6 Ones**: lockup de nome ("Nexa One" no padrão tipográfico), ícone e cor própria de cada módulo derivada da paleta oficial | Kit SVG/PNG + tabela de cores | Sim |
| 1.4 | **Tipografia institucional** (proposta de família oficial p/ UI e materiais) + **paleta expandida** (tokens: dataviz, estados, funil, light/dark) | Especificação de tokens | Sim |
| 1.5 | **Brandbook ONE by GrowUp** consolidando 1.1–1.4 com regras de aplicação | Brandbook (HTML/PDF) | Sim (fecha a fase) |

**Método de trabalho**: cada item vai para você como painel visual (artefato)
para reação rápida; itero até aprovar. Primeira entrega: painel com propostas
de logo + cores dos módulos (1.2 + 1.3 juntos, que são o coração da identidade).

## 4. Fase 2 — Aplicação no sistema

**Objetivo**: o sistema em produção refletindo 100% a nova identidade.
**Pré-requisito**: Fase 1 aprovada. Itens 2.2–2.6 podem ser executados via
integração Lovable (ou direto no repo, após 2.1).

| # | Atividade | Entrega |
|---|---|---|
| 2.1 | **Sincronizar código Lovable ↔ GitHub** (habilita versionamento, backup e trabalho direto no repo; hoje o repo está vazio) — requer você conectar o GitHub no painel do Lovable | Repo populado |
| 2.2 | **Design tokens**: azul primário oficial (#4767FA), cores modulares recalibradas, light + dark | `index.css`/`tailwind.config` atualizados |
| 2.3 | **Renomear módulos na UI**: dashboard (cards → Nexa One, Sales One…), títulos, menus, textos, chatbots | UI rebatizada |
| 2.4 | **Reestruturar navegação** conforme arquitetura: Planejamento Estratégico sob Growth One, Avaliação sob Flow One, Mensagens como camada transversal | Navegação nova |
| 2.5 | **Identidade em todos os pontos de contato**: login, headers, favicon, OG image, meta tags/SEO ("ONE by GrowUp"), `lang="pt-BR"`, PDFs gerados (diagnóstico, relatórios), templates de e-mail/WhatsApp | Assets aplicados |
| 2.6 | **QA visual completo**: todas as telas, light/dark, páginas públicas (diagnóstico, questionários, projetos compartilhados), PDFs | Checklist aprovado |

## 5. Fase 3 — Vídeo animado de apresentação

**Objetivo**: vídeo de lançamento do ONE by GrowUp.
**Pré-requisito**: Fase 1 aprovada (identidade); telas reais dependem de 2.1
(senão, mockups fiéis em HTML).

| # | Atividade | Entrega | Aprovação sua? |
|---|---|---|---|
| 3.1 | **Roteiro + storyboard** (60–90s): abertura com logo animado → dor ("quantas ferramentas você paga hoje?") → promessa do ONE → tour pelos 6 Ones seguindo a narrativa da família → CTA | Roteiro ilustrado | Sim |
| 3.2 | **Produção motion graphics**: animação por código (render frame a frame), 1080p 16:9, MP4 | Vídeo v1 | Sim |
| 3.3 | **Rodada de ajustes** + export final; opcional versão 9:16 para redes | Vídeo final | Sim |

**Sobre áudio** (decisão sua, pode ficar para a 3.1):
- (a) vídeo com texto on-screen, sem áudio (pronto para receber trilha depois);
- (b) você fornece trilha licenciada e eu embuto;
- (c) locução via ferramenta TTS externa, se disponível.

## 6. Fase 4 — Materiais de marketing e lançamento

**Objetivo**: kit completo de comunicação do ONE nos canais da GrowUp,
seguindo o princípio do ecossistema (seção 2): toda peça assina GrowUp,
o ONE é o produto do ecossistema.
**Pré-requisito**: Fase 1 aprovada (identidade + guia verbal).

### 4A — Social media (posts e carrosséis)

| # | Atividade | Entrega |
|---|---|---|
| 4.1 | **Sistema visual para social**: grid/layout padrão das peças do ONE dentro da identidade GrowUp (composição, área do logo, uso das cores modulares, padrão de capa) — garante que qualquer peça futura "pareça família" | Guia de social + templates-base |
| 4.2 | **Posts estáticos** — versões: lançamento do ONE, 1 post de apresentação por módulo (6), posts de benefício/prova. Formatos: feed 1:1 e 4:5 + stories 9:16 | Pack de posts (PNG + fonte editável) |
| 4.3 | **Carrosséis** — versões: (a) lançamento "conheça o ONE" (capa + 6 Ones + CTA, seguindo a narrativa da família), (b) carrossel de aprofundamento por módulo (dor → solução → telas → CTA), (c) carrossel educativo/método GrowUp com o ONE como meio | Pack de carrosséis (PNG por slide + fonte editável) |
| 4.4 | **Cortes do vídeo** (da Fase 3) para social: versão 9:16 (reels/stories) e teasers curtos por módulo | Vídeos curtos |

### 4B — Comercial e institucional

| # | Atividade | Entrega |
|---|---|---|
| 4.5 | Apresentação comercial (slides) do ONE by GrowUp — estrutura ecossistema: método GrowUp → plataforma ONE → módulos | Deck |
| 4.6 | One-pager de cada módulo (PDF) com endosso GrowUp | 6 PDFs |
| 4.7 | Página/seção "conheça o ONE" no site da GrowUp | Página |
| 4.8 | Calendário de lançamento sugerido (sequência de posts/carrosséis/vídeo) | Cronograma |

## 7. Sequência e dependências

```
Fase 0 ✅ → Fase 1 (identidade) → Fase 2 (sistema) ──┐
                              ├→ Fase 3 (vídeo) ─────┼→ 4.4 (cortes) e 4.8 (calendário)
                              └→ Fase 4A/4B (mkt) ───┘
```

- Fases 2, 3 e 4A rodam **em paralelo** após a Fase 1 (posts/carrosséis só
  dependem da identidade, não do sistema pronto; apenas 4.4 depende do vídeo).
- Único insumo externo crítico: **conectar Lovable ↔ GitHub** (item 2.1, ação
  sua no painel do Lovable) — destrava trabalho direto no repositório e
  capturas de tela reais para o vídeo.

## 8. Status e próximos passos

| Fase | Status |
|---|---|
| Fase 0 — Naming e arquitetura | ✅ Concluída (ONE by GrowUp + 6 módulos + encaixes) |
| Fase 1 — Identidade | ✅ Concluída (kit de logos, tokens, guia verbal e brandbook aprovados) |
| Fase 2 — Aplicação no sistema | 🔜 Liberada |
| Fase 3 — Vídeo | 🔜 Liberada |
| Fase 4 — Marketing e lançamento | 🔜 4A liberada |

**Fase 1 concluída em 27/07/2026** — entregas: kit de logos (`fase1/kit/`),
tokens (`fase1/tokens/`), guia verbal (`fase1/GUIA_VERBAL.md`) e brandbook
(`fase1/BRANDBOOK_ONE_BY_GROWUP.pdf`).
