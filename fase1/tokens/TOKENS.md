# ONE by GrowUp — Tokens de design (item 1.4)

> Especificação da tipografia institucional e da paleta funcional.
> Arquivo aplicável: `tokens.css` (mesma pasta). Painel de aprovação:
> https://claude.ai/code/artifact/510ddca9-d099-4150-b888-87988a34cc51

## Tipografia

| Papel | Fonte / peso | Uso |
|---|---|---|
| Display | **Poppins 700** | Títulos de página, números-herói, capas |
| Marca / módulos | **Poppins 600** | Nomes dos Ones, headers de card, botões-destaque |
| Interface | **Manrope 500/700** | Menus, botões, labels, tabelas (números tabulares) |
| Texto | **Manrope 400** | Parágrafos, descrições, relatórios |
| Técnico | ui-monospace | Códigos, IDs, valores hex |

Ambas open-source (SIL OFL) — disponíveis via Google Fonts / @fontsource.
Fallback `system-ui`. PDFs gerados passam de Arial para Poppins/Manrope.

## Paleta

**Marca (oficial)**: #4767FA (principal), #3A50D2, #DE571B, #5E8C54, #F1F1F1, #6C6C70, #141414

**Módulos (aprovado Painel 1)**: Nexa #DE571B · Sales #4767FA · Growth #7B4FE0 (ext.) · Profit #5E8C54 · Flow #3A50D2 · North #2E8FA3 (ext.)

**Estados**: sucesso #5E8C54 · alerta #DB9A1F · erro #D64545 · info #4767FA

**Funil (recalibrado)**: Lead #E0B429 · Atendimento #4767FA · Proposta #7B4FE0 · Fechamento #5E8C54

**Neutros (escala fria, hue 240)**: #F8F8FA → #F1F1F1* → #E3E3E8 → #C9C9D1 → #A0A0AA → #6C6C70* → #45454C → #24242A → #15151A → #141414* (* = oficiais)

**Dataviz**: categórico = 6 cores dos módulos (chart-1…6); sequencial = rampa do azul (#EDF0FE → #1D2A70)

## Temas

- **Claro**: background #F8F8FA, card #FFF, foreground #141414
- **Escuro**: background #101014, card #191922, foreground #F1F1F1
- `--primary` em ambos: **#4767FA** (corrige o #1A76F0 atual, fora da marca)

## Migração (Fase 2) — principais trocas no sistema

| Token atual | Atual | Novo |
|---|---|---|
| --primary | 214 88% 52% | **229 95% 63%** |
| --crm | 220 91% 48% | 229 95% 63% |
| --growth | 280 87% 55% | 258 70% 59% |
| --erp | 160 84% 39% | 109 25% 44% |
| --operational | 25 95% 53% | 231 63% 53% |
| --reports | 0 84% 60% | 190 56% 41% |
| funil (lead…fechamento) | Tailwind | ver acima |
| font-family | system-ui | Poppins + Manrope |
| PDFs | #4052F6 / Arial | #4767FA / Poppins |
