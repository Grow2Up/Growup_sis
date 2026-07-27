# Status do projeto — retomada rápida

> Nota de handoff para a próxima sessão de trabalho.
> Última atualização: 26/07/2026.

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

**Próximo passo**: item 1.4 — tipografia institucional (validar Poppins) +
paleta expandida/tokens (dataviz, estados, funil, light/dark); depois 1.1
(identidade verbal) e 1.5 (brandbook).

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
