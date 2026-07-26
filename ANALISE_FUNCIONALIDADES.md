# Análise de Funcionalidades — Growup SIS (sistema.grow2up.com.br)

> Análise gerada a partir do código-fonte do projeto **growup-sis** hospedado no Lovable
> (publicado em `growup-sis.lovable.app` / `sistema.grow2up.com.br`).
> Observação: este repositório GitHub (`Grow2Up/Growup_sis`) estava vazio no momento da análise —
> o código-fonte vive no Lovable e não está sincronizado com o GitHub.

## Visão geral

O **Growup — Sistema de Gestão Empresarial** é uma plataforma SaaS **multi-tenant** de gestão
de negócios ("Business Suite"), com módulos habilitáveis por cliente/tenant e forte uso de IA
(chatbots e agentes especializados por área).

## Stack técnica

| Camada | Tecnologia |
|---|---|
| Frontend | React 18 + Vite + TypeScript, shadcn/ui, Tailwind CSS, TanStack Query, React Router (SPA com lazy loading) |
| Backend | Supabase (projeto `hhnbbpjsmvwedyvbtsuf`): Auth, PostgreSQL com RLS/migrations, ~26 Edge Functions (Deno) |
| IA | Edge functions de chat/análise (CRM, diagnóstico, planejamento estratégico, GPD, gestor de projetos, relatórios de auditoria), chat em tempo real com áudio (`RealtimeAudio`) |
| Integrações | Meta (Facebook) Lead Ads via webhook, WhatsApp (notificações e campanhas), extração de despesas de PDF |
| Hospedagem | Lovable (build/publicação) com domínio próprio |

## Controle de acesso

- **Login por e-mail/senha** (Supabase Auth); sem auto-cadastro — contas criadas pelo administrador.
- **3 níveis de papel**: usuário comum, **Admin** (`/admin`) e **Master Admin** (`/master-admin`).
- **Multi-tenant**: cada tenant tem módulos habilitados/bloqueados (`useTenantModules`,
  `TenantModulesManager`); cards do dashboard aparecem "locked" quando o módulo não está contratado.
- Rotas protegidas via `ProtectedRoute` (com variantes `adminOnly` e `masterOnly`).

## Módulos principais (hub `/dashboard`)

### 1. CRM (`/crm`)
- Pipeline visual **Kanban** com estágios configuráveis (gerenciador de estágios do funil).
- Gestão de leads: criação, detalhe, **mesclagem de duplicados**, checklist, documentos anexos,
  scripts de abordagem, agendamento de contatos e dashboard de agendamentos.
- Visualizações: Kanban, lista, gráfico de funil, dashboard por canal de origem.
- **Integração Meta Lead Ads** (webhook `meta-leads-webhook`) para captura automática de leads.
- Automação por mudança de estágio (`process-lead-stage-change`) e notificações por
  e-mail/WhatsApp (`send-lead-notification`, `send-whatsapp-notification`).
- **Análise de CRM com IA** (`crm-analysis`) + chatbot flutuante do CRM.

### 2. Relatórios (`/reports`)
- Estatísticas consolidadas de conversão, leads e receita (`ReportsStats`).

### 3. Marketing (`/marketing`)
- **Auditoria de Marketing** (`/marketing-audit`): projetos por cliente, auditorias por tipo,
  dashboards por tipo de auditoria e **relatórios gerados por IA**
  (`generate-audit-report`, `generate-type-dashboard-analysis`).
- **Auditoria de Vendas** (`/sales-audit`) com projetos próprios.
- **Landing Page Builder** (`/landing-page`) + template de geração de leads.
- **Diagnóstico de Marketing público** (`/diagnostico_marketing`): questionário de captura de
  leads sem login (`public-lead-capture`), com chatbot de diagnóstico por IA (`diagnostic-chat`).

### 4. Growth Intelligence (`/growth-intelligence`)
- **Agentes de IA** especializados (`/ai-agents`): Agente Comercial, Agente de Marketing e
  Agente de Processos.
- **Base de dados** (`/growth-intelligence/database`): listas de prospecção, perfis
  (inclui perfis LinkedIn), assistente de criação de listas e exportação (inclusive formato Meta).
- **Diagnóstico interno** (`/growth-intelligence/diagnostic`): wizard de diagnóstico com
  resultado, recomendações (Growup e Marketing) e chatbot.
- **Growth Audit** (`/growth-audit`).

### 5. Processos / Growth Process (`/growth-process`)
- **Editor visual de mapas de processos** (estilo BPMN): galeria de formas, edição inline,
  undo/redo, auto-save, versões, templates, alinhamento e auto-layout.
- Tipos de mapa: fluxograma, mapa mental, organograma, SWOT, sticky notes, processos de sistema.
- **Exportação PNG/PDF** e **compartilhamento público** por link (`/p/process-map/:token`).

### 6. Planejamento Estratégico (`/strategic-planning`)
- Identidade: Missão/Visão/Valores, **Matriz SWOT**, **Business Model Canvas**.
- Personas (marca e comprador), análise de concorrentes, público-alvo.
- **Plano de ação 5W2H** e **GPD** (Gerenciamento pelas Diretrizes): diretrizes, indicadores,
  desdobramento e **PDCA**, com chatbot de GPD (`gpd-chat`).
- Planejamento de conteúdo: calendário editorial, canais, tópicos, briefings, copy e métricas.
- Mídia paga: plataformas, orçamento, públicos, criativos e KPIs.
- Banco de ideias e briefing de campanha.
- **Questionários para clientes**: construtor de questionários, link público (`/q/:token`),
  lista de respostas e importação de respostas.
- Chatbot estratégico por IA (`strategic-planning-chat`).

### 7. ERP Financeiro (`/erp`)
- Abas: Visão Geral, **Vendas** (inclui venda em lote), **Receitas**, **Despesas**,
  **Fornecedores** e **Clientes**.
- **Importação de despesas de PDF com extração por IA** (`extract-pdf-expenses`) e
  categorização automática.
- Metas financeiras, filtros e relatórios (vendas por cliente, despesas por fornecedor).
- Gráficos: receita, despesas por categoria, comparativos anuais de receita/despesa.
- **Mapa do Brasil** com clientes/receita por estado e visão detalhada por estado.

### 8. Operacional (`/operational` — página inicial do sistema)
- Gestão de **projetos e tarefas**: Kanban, **Gantt**, timeline e lista; estágios configuráveis.
- Detalhe de projeto, taxas/hora por membro da equipe.
- **Compartilhamento público de projetos** (dashboard com métricas e visualização somente
  leitura de tarefas): `/shared/project/:shareToken` e `/public/project/:projectId`.
- **Análise por IA do gestor de projetos** (`project-manager-analysis`) + chatbot flutuante.

### 9. Avaliação de Desempenho (`/performance-evaluation`)
- Lista de avaliações, criação e edição de avaliações de desempenho da equipe.

### 10. Mensagens (`/mensagens`)
- Central de mensageria (WhatsApp): **templates**, envio individual e por **campanha**
  (`send-campaign-message`), **mensagens agendadas** (`process-scheduled-messages`).
- **Regras de relacionamento** (automação de mensagens disparadas por estágio do lead).
- Dashboard de métricas de mensageria, painel de testes e verificação de credenciais.

### 11. Administração (`/admin` e `/master-admin`)
- **Admin**: gestão de usuários (criar/excluir, foto/avatar, reset de credenciais e senhas),
  configurações de notificação, configuração de chatbots e do sistema.
- **Master Admin**: gestão de tenants e **habilitação de módulos por tenant**, credenciais master.

### Recursos transversais
- **Chatbot flutuante global** presente em todo o sistema (chat em tempo real, com suporte a áudio).
- Tema claro/escuro.
- Rotas públicas (sem login): diagnóstico de marketing, projetos compartilhados,
  mapas de processos e questionários de clientes.

## Resumo executivo

O sistema é uma **suíte de gestão para aceleração de negócios** — combinação de CRM + ERP
financeiro + gestão de projetos + planejamento estratégico + marketing/auditorias — diferenciada
por: (1) arquitetura multi-tenant com módulos por contrato, (2) IA embarcada em praticamente
todos os módulos (análises, relatórios e chatbots especializados), (3) automação de
relacionamento via WhatsApp/Meta Ads e (4) compartilhamento público de entregáveis
(projetos, mapas de processos, questionários e diagnósticos) para uso com clientes finais.
