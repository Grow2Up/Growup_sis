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
- Kit vetorial final em `fase1/kit/` (SVG+PNG): assinatura principal em 4
  colorways, vertical, app icon, selo e 6 sub-marcas (+variantes dark).
  Letras derivadas das oficiais (n=u rot180, b=p espelhado, e/y construídas);
  nomes das sub-marcas em Poppins SemiBold (proposta tipográfica p/ 1.4).
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

**Próximo passo**: Fases 2 (aplicação no sistema), 3 (vídeo) e 4A (posts/
carrosséis) podem rodar em paralelo. Fase 2 depende de decisão: aplicar via
agente do Lovable (consome créditos do workspace) ou via repo após conectar
Lovable↔GitHub (item 2.1, ação do usuário no painel do Lovable).

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
