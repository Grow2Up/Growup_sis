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
| 1.1 | **Identidade verbal**: tagline do ONE, descritor oficial de cada módulo (1 linha), tom de voz, regras de escrita (grafia "ONE by GrowUp", uso do "by", pt-BR) | Guia verbal (MD/PDF) | Sim |
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

## 6. Fase 4 — Materiais de lançamento *(opcional)*

- Apresentação comercial (slides) do ONE by GrowUp
- One-pager de cada módulo (PDF)
- Templates de post para redes sociais
- Página/seção "conheça o ONE" no site

## 7. Sequência e dependências

```
Fase 0 ✅ → Fase 1 (identidade) → Fase 2 (sistema) ─┐
                              └→ Fase 3 (vídeo) ────┴→ Fase 4 (materiais)
```

- Fases 2 e 3 rodam **em paralelo** após a Fase 1.
- Único insumo externo crítico: **conectar Lovable ↔ GitHub** (item 2.1, ação
  sua no painel do Lovable) — destrava trabalho direto no repositório e
  capturas de tela reais para o vídeo.

## 8. Status e próximos passos

| Fase | Status |
|---|---|
| Fase 0 — Naming e arquitetura | ✅ Concluída (ONE by GrowUp + 6 módulos + encaixes) |
| Fase 1 — Identidade | 🔜 **Próxima** — iniciar por 1.2+1.3 (logo + sub-marcas) |
| Fase 2 — Aplicação no sistema | Aguarda Fase 1 |
| Fase 3 — Vídeo | Aguarda Fase 1 |
| Fase 4 — Materiais | Opcional, ao final |

**Próxima entrega**: painel visual com proposta de logo do ONE by GrowUp e
sistema de cores/ícones dos 6 módulos, para sua reação.
