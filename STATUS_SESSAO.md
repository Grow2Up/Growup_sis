# Status do projeto — retomada rápida

> Nota de handoff para a próxima sessão de trabalho.
> Última atualização: 27/07/2026.

## Onde paramos

**Fase 0 (naming e arquitetura) CONCLUÍDA e aprovada.** O planejamento mestre
está em `PLANEJAMENTO_ONE_BY_GROWUP.md` (fonte editável) e
`PLANEJAMENTO_ONE_BY_GROWUP.pdf` (versão apresentável).

**Fase 1 em andamento — itens 1.2 + 1.3 CONCLUÍDOS e aprovados** (27/07/2026):
- Wordmark: Proposta A aprovada ("one" minúsculo herdeiro do growup)
- Mapa de cores dos 6 módulos aprovado: Nexa #DE571B, Sales #4767FA,
  Growth #7B4FE0 (ext.), Profit #5E8C54, Flow #3A50D2, North #2E8FA3 (ext.)
- Ícones aprovados (traço geométrico)
- Kit vetorial v2 em `fase1/kit/` (SVG+PNG): assinatura principal em 4
  colorways, vertical, app icon, selo e 6 sub-marcas (+variantes dark).
  IMPORTANTE: o wordmark aprovado é o da Proposta A do Painel 1 — "one"
  geométrico arredondado LIMPO (Poppins Bold em outlines) + monograma
  oficial + "BY GROWUP" caps espaçadas. A v1 (letras do logo growup com
  corte no "o") foi REJEITADA pelo usuário. Gerador: fase1/build_kit_v2.py.
- Painel (artefato): https://claude.ai/code/artifact/c83772d2-b423-4169-9c0c-58131c4cae0c
- Scripts geradores: `fase1/build_kit.py` e `fase1/build_submarcas.py`

**Item 1.4 APROVADO** (Poppins + Manrope e paleta funcional completa):
- Proposta: Poppins (display/marca) + Manrope (UI/texto)
- Paleta funcional: estados, funil recalibrado, neutros frios, dataviz
- Arquivos: `fase1/tokens/tokens.css` + `fase1/tokens/TOKENS.md`
- Painel 2: https://claude.ai/code/artifact/510ddca9-d099-4150-b888-87988a34cc51

**Item 1.1 APROVADO** (Painel 3):
- Tagline recomendada: "Todo o seu negócio em um." + descritor
  "O método GrowUp em forma de plataforma."
- 6 descritores de módulo, tom de voz (4 princípios), regras de grafia,
  regras do ecossistema e pitches (10s/30s)
- Guia: `fase1/GUIA_VERBAL.md` · Painel 3:
  https://claude.ai/code/artifact/4f618c76-c0c3-4c04-b72b-d513f02fd08e
- Aprovado: tagline "Todo o seu negócio em um." + descritor + descritores
  de módulo + tom de voz + regras

**Item 1.5 CONCLUÍDO — FASE 1 ENCERRADA** (27/07/2026):
- Brandbook v1: `fase1/brandbook-one-by-growup.html` (navegável) +
  `fase1/BRANDBOOK_ONE_BY_GROWUP.pdf`
- Artefato: https://claude.ai/code/artifact/8951a458-25e2-431d-b583-f2398c14aed0

**FASE 2 EM EXECUÇÃO via agente do Lovable** (27/07/2026) — etapas aplicadas
no PREVIEW (produção intocada; publicar é decisão do usuário no Lovable):
- Etapa 1 (4,3 cr, commit 2aa3e40): fontes Poppins/Manrope, todos os tokens
  light/dark (azul #4767FA, módulos, funil, dataviz), logos em public/brand/
  (login/header/favicon), meta tags/lang pt-BR. Knowledge do projeto Lovable
  gravado com as regras da marca.
- Etapa 2 (3,4 cr, commit 7292170): 6 cards e páginas renomeados para os
  Ones com descritores oficiais; "Business Suite"/"Hub de Negócios" removidos;
  login com tagline; rodapé institucional.
- Etapa 3a (2,8 cr, commit 12a9e74): PDFs (logo/azul/fontes/rodapés),
  chatbots renomeados, páginas públicas atualizadas.
- Etapa 3b (3,2 cr, commit f232a12): navegação — Planejamento Estratégico
  sob Growth One, Avaliação sob Flow One, Mensagens camada neutra; rotas
  antigas preservadas.
- QA final (4,5 cr, commit b97fc38): strings residuais corrigidas, cores
  cruas → tokens, og/twitter image antigos removidos, dark mode com
  --operacional/--erp clareados p/ contraste, font-display nos títulos
  restantes, typecheck limpo, assets /brand/* 200 OK.

**FASE 2 CONCLUÍDA NO PREVIEW** (total ~18,2 créditos Lovable).
**Pendente do usuário**: validar o preview e PUBLICAR no Lovable (produção
sistema.grow2up.com.br segue com a marca antiga até publicar).
**Próximo**: Fase 3 (roteiro do vídeo) e Fase 4A (posts/carrosséis).

## Decisões-chave (não rediscutir)

- Sistema: **ONE by GrowUp** (substituiu "Family One", "GrowUp 360", "Business Suite")
- Módulos: **Nexa One** (Marketing), **Sales One** (CRM), **Growth One**
  (Growth Intelligence), **Profit One** (ERP), **Flow One** (Operacional),
  **North One** (Relatórios)
- Encaixes: Planejamento Estratégico → Growth One; Avaliação de Desempenho →
  Flow One; Mensagens → camada transversal
- Princípio do ecossistema: o ONE nunca se comunica sozinho — sempre
  atrelado à GrowUp (hierarquia GrowUp → ONE → módulos)
- Paleta oficial GrowUp: #4767FA (azul principal), #3A50D2, #DE571B, #5E8C54,
  #F1F1F1, #6C6C70, #141414

## Arquivos no repositório

| Arquivo | Conteúdo |
|---|---|
| `ANALISE_FUNCIONALIDADES.md` | Mapeamento completo dos módulos e funcionalidades do sistema |
| `ANALISE_IDENTIDADE_VERBAL_VISUAL.md` | Análise da identidade atual + comparativo com a marca oficial |
| `PLANEJAMENTO_ONE_BY_GROWUP.md` / `.pdf` | Planejamento mestre (fases 1–4) |
| `brand/PACOTE DA MARCA/` | Pacote oficial da marca GrowUp (logos horizontal/vertical + 19 selos, em AI/PDF/PNG/SVG) — preservado do upload do usuário |

## Contexto técnico

- O código do sistema **não está neste repositório** (repo estava vazio) — vive
  no projeto Lovable **growup-sis** (id `a03c663b-0797-45a0-b41b-08431434017d`,
  workspace `6lYCRubYYj5L6UTW1Cnl`), acessível via MCP Lovable.
  Publicado em growup-sis.lovable.app / sistema.grow2up.com.br.
- Backend: Supabase externo (projeto `hhnbbpjsmvwedyvbtsuf`).
- A rede do ambiente bloqueia sistema.grow2up.com.br — usar o MCP do Lovable
  para ler código/telas.
- Pendência externa (item 2.1): conectar Lovable ↔ GitHub no painel do Lovable
  para popular este repo com o código e habilitar capturas reais para o vídeo.
- Branch de trabalho: `claude/sistema-grow2up-analysis-btb1wa`.
