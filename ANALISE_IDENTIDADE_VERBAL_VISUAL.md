# Análise da Identidade Verbal e Visual — GrowUp

> Baseada no código-fonte do sistema (design tokens, logo, metadados e textos de interface)
> do projeto **growup-sis** (sistema.grow2up.com.br).

---

## 1. Identidade Verbal

### 1.1 Nomenclatura e assinaturas

A marca aparece com **grafias e nomes inconsistentes** ao longo do produto:

| Onde | Como aparece |
|---|---|
| Título da aba / SEO (`index.html`) | **GrowUp 360** |
| Tela de login | **Growup** — "Sistema de Gestão Empresarial" |
| Dashboard | **Business Suite** — "Acelere seu crescimento" |
| Rodapé do dashboard | "Powered by **GrowUp** • Sua plataforma completa de crescimento" |
| PDF do diagnóstico | "**GrowUp** - Sistema de Gestão Empresarial" |
| Twitter/X (meta tag) | @growup360 |
| Domínio | grow2up.com.br |

Há pelo menos **4 variações** convivendo: *Growup*, *GrowUp*, *GrowUp 360* e *Grow2Up* (domínio e nome do arquivo do logo), além de dois descritores concorrentes ("Sistema de Gestão Empresarial" × "Sua plataforma completa de crescimento" × "Business Suite / Hub de Negócios").

### 1.2 Taglines e propostas de valor

- **"Sua plataforma completa de crescimento"** (assinatura principal, usada em SEO e rodapé)
- **"Acelere seu crescimento"** (subtítulo do header)
- **"Escolha o módulo e acelere os resultados do seu negócio"**
- O conceito-âncora é claramente **crescimento/aceleração** — coerente com o nome GrowUp e com o símbolo de seta ascendente.

### 1.3 Tom de voz

- **Direto e orientado a resultado.** Os CTAs dos módulos não descrevem a função, vendem o benefício: **"Vender Mais"** (CRM), **"Ver Insights"** (Relatórios), **"Criar Campanha"** (Marketing), **"Ativar IA"** (Growth), **"Ver Finanças"** (ERP), **"Gerenciar"** (Operacional).
- **Benefício antes da funcionalidade** nas descrições: "Transforme leads em vendas…", "Insights que impulsionam resultados…", "Marketing que converte…", "IA trabalhando pelo seu crescimento, 24 horas por dia", "Suas finanças sob controle total", "Processos organizados, resultados previsíveis e equipe alinhada".
- **Informal-profissional, com tratamento por "você"** e proximidade: "Como devemos te chamar?", "Qual o nome da sua empresa?", "Bem-vindo ao seu Hub de Negócios".
- **Gatilhos de conversão** nas páginas públicas: "100% Gratuito", "Resultado Imediato", "Iniciar Diagnóstico Gratuito", "Falar com um especialista", com reforço de segurança ("Seus dados estão seguros e não serão compartilhados").
- Idioma: **português brasileiro**, mas com **anglicismos estruturais** (Business Suite, Growth Intelligence, Hub, leads, insights) — posicionamento de "consultoria moderna de growth". Nota: o HTML declara `lang="en"` apesar do conteúdo em pt-BR.

### 1.4 Vocabulário de domínio

O funil usa termos próprios e consistentes: **Lead → Atendimento → Proposta → Fechamento** — cada um com cor própria no design system, o que integra a linguagem verbal à visual.

---

## 2. Identidade Visual

### 2.1 Logo e símbolo

- **Símbolo**: seta ascendente/diagonal (↗) estilizada dentro de um contorno — remete a crescimento; funciona como favicon e ícone de app.
- **Versão selo circular** (tela de login): wordmark "GROWUP" repetido em círculo ao redor do símbolo, em azul — uso de assinatura tipo "badge".
- Aplicações: header do sistema (fundo claro em card com borda suave), PDF de relatórios (versão própria `growup-logo-pdf.png`), materiais públicos.

### 2.2 Paleta cromática

**Cor primária** — azul vivo, "Professional blue":
- Sistema: `hsl(214 88% 52%)` ≈ **#1A76F0**
- Nos PDFs a marca usa **#4052F6** (azul-índigo) — *duas versões de azul primário convivem*.

**Cores modulares** (cada módulo do produto tem cor própria — "color coding" funcional):

| Módulo | Cor | Aproximação |
|---|---|---|
| CRM | Azul profundo `hsl(220 91% 48%)` | #0B5CEA |
| Relatórios | Vermelho `hsl(0 84% 60%)` | #EF4444 |
| Marketing | (tom próprio no ModuleCard) | — |
| Growth Intelligence | Roxo `hsl(280 87% 55%)` | #AE28F0 |
| ERP Financeiro | Verde esmeralda `hsl(160 84% 39%)` | #10B77F |
| Operacional | Laranja `hsl(25 95% 53%)` | #F97316 |

**Cores de estágio do funil** (semântica de status):

| Estágio | Cor |
|---|---|
| Lead | Amarelo `hsl(45 93% 58%)` |
| Atendimento | Azul `hsl(217 91% 60%)` |
| Proposta | Roxo `hsl(271 91% 65%)` |
| Fechamento | Verde `hsl(142 71% 45%)` |

Os valores derivam da **paleta Tailwind** (blue-500, red-500, purple-500, emerald-600, orange-500…), organizados em tokens HSL com variantes `light` e `foreground`, e **tema claro e escuro completos**.

**Neutros**: fundo off-white frio `hsl(245 16% 97%)`, texto em azul-ardósia escuro `hsl(218 23% 16%)`; dark mode em azul-marinho profundo `hsl(222 47% 11%)`.

### 2.3 Tipografia

- **Nenhuma fonte proprietária configurada** — usa a pilha `font-sans` padrão do Tailwind (fontes de sistema: Inter-like/SF/Segoe). Nos PDFs, **Arial**.
- Hierarquia por peso (bold para títulos, medium para labels) e não por família; títulos com **gradiente de texto** (`bg-clip-text`) como recurso expressivo.

### 2.4 Linguagem gráfica e estilo de UI

- **Estilo geral**: SaaS moderno "clean tech" — shadcn/ui + Tailwind.
- **Cantos bem arredondados**: raio base de **12px** (`--radius: 0.75rem`), cards e pills `rounded-full` para badges.
- **Gradientes de marca**: azul→azul-claro 135° (`--gradient-primary`) em botões e títulos.
- **Profundidade suave**: sombras em 3 níveis (card, kanban, hover), sem bordas pesadas.
- **Glassmorphism** nas páginas públicas: cards translúcidos com `backdrop-blur`, orbes flutuantes desfocados nas cores da marca, padrão de grade pontilhada ao fundo.
- **Movimento como assinatura**: fade/slide de entrada escalonados (stagger), botões com **efeito shimmer**, animações float, pulse-glow e círculo de score desenhado progressivamente — transmite dinamismo/"aceleração", alinhado ao conceito verbal.
- **Iconografia**: Lucide (traço fino, consistente) — Users, Target, Brain, DollarSign, BarChart3, Settings, Shield.
- **Dataviz**: 5 cores de gráfico padronizadas (azul, amarelo, verde, roxo, vermelho) alinhadas às cores de estágio.

---

## 3. Diagnóstico de consistência

**Pontos fortes**
1. Conceito claro e coeso: crescimento/aceleração permeia nome, símbolo (seta ↗), taglines, CTAs e até as animações.
2. Design system tokenizado (HSL + variantes light/dark) — raro em produtos desse porte; facilita manutenção e consistência.
3. Color coding funcional por módulo e por estágio do funil — a cor carrega significado, não é só estética.
4. Tom de voz consistente: benefício antes da função, em todos os CTAs.

**Pontos de atenção**
1. **Naming fragmentado**: Growup / GrowUp / GrowUp 360 / Grow2Up / Business Suite convivem sem hierarquia definida. Recomenda-se fixar uma grafia master (ex.: **GrowUp**) e definir o papel de "360" e "Business Suite" (produto? suíte? campanha?).
2. **Dois azuis primários** (#1A76F0 no sistema × #4052F6 nos PDFs) — unificar.
3. **Dois descritores** ("Sistema de Gestão Empresarial" × "Plataforma completa de crescimento") — o segundo é mais alinhado ao posicionamento de growth.
4. **Sem tipografia proprietária** — adotar uma família oficial (ex.: Inter ou similar) daria mais reconhecimento de marca, inclusive nos PDFs (hoje em Arial).
5. `lang="en"` no HTML para conteúdo pt-BR (detalhe técnico com impacto em SEO/acessibilidade).

---

## 4. Pacote oficial da marca × identidade implementada no sistema

> Seção adicionada após análise do **PACOTE DA MARCA** oficial (AI/PDF/PNG/SVG):
> logo horizontal (6 colorways), logo vertical (6 colorways) e 19 selos.

### 4.1 O que o pacote oficial define

**Logotipo** — wordmark "growup" em **caixa-baixa**, tipografia geométrica bold customizada
(letras vetorizadas, não é fonte de mercado), com dois recursos narrativos:
- O **"w" se transforma em linha de gráfico ascendente** (zigzag que sobe e termina em pico) —
  o crescimento está literalmente desenhado dentro do nome.
- O **"o" com corte diagonal** (vértice de balão/pin), dando personalidade às contraformas.
- Assinatura fecha com o **monograma**: contêiner em "U" de onde uma **seta ↗ explode para fora**
  — símbolo de rompimento de teto/crescimento. Existe em versão horizontal (nome + símbolo)
  e vertical (grow/up empilhados + símbolo).

**Selos (19 variações)** — badge circular com "GROWUP" repetido 4× ao redor do monograma;
versões vazadas (só a arte) e com fundo sólido (preto, azul, laranja, verde, off-white),
para redes sociais, carimbo e aplicações compactas.

**Paleta oficial** (extraída dos vetores):

| Cor | Hex | Uso no pacote |
|---|---|---|
| Azul vivo (principal) | **#4767FA** | Colorway 01 do logo vertical |
| Azul profundo | **#3A50D2** | Colorway azul do logo horizontal e selos |
| Laranja queimado | **#DE571B** | Colorway secundária |
| Verde musgo | **#5E8C54** | Colorway secundária |
| Off-white | **#F1F1F1** | Versão clara / fundos escuros |
| Cinza neutro | **#6C6C70** | Versão neutra |
| Preto | **#141414** | Versão escura / fundos de selo |

É uma paleta **sóbria e levemente terrosa** (laranja queimado + verde musgo) ancorada em
azul-índigo — bem diferente de uma paleta "tech saturada".

### 4.2 Comparativo: marca oficial × sistema

| Elemento | Pacote oficial | Sistema (implementado) | Veredito |
|---|---|---|---|
| Azul primário | #4767FA / #3A50D2 (índigo) | `hsl(214 88% 52%)` ≈ #1A76F0 (azul-céu vivo) | **Divergente** — o azul do app não é o azul da marca |
| Azul nos PDFs | — | #4052F6 | **Quase fiel** — muito próximo do #4767FA oficial; ironicamente o PDF acerta e o app erra |
| Laranja | #DE571B (queimado) | `hsl(25 95% 53%)` ≈ #F97316 (Tailwind) | Divergente (mais saturado/claro) |
| Verde | #5E8C54 (musgo) | `hsl(160 84% 39%)` ≈ #10B77F (esmeralda) | Divergente (tom frio Tailwind) |
| Roxo / vermelho / amarelo | **não existem na marca** | usados como cores de módulo e funil | Extrapolação sem respaldo no brandbook |
| Logo | wordmark caixa-baixa + monograma U↗ + selos | selo no login, monograma no favicon, wordmark no header | **Correto** — os assets certos estão em uso |
| Tipografia | wordmark custom (só logo); sem fonte de UI definida no pacote | pilha de sistema | Lacuna do pacote — falta definir fonte institucional de apoio |
| Fundo claro | #F1F1F1 | `hsl(245 16% 97%)` ≈ #F6F6F9 | Compatível |
| Preto | #141414 | foreground `hsl(218 23% 16%)` (azulado) | Compatível (leve divergência de temperatura) |

### 4.3 Conclusão revisada

1. **O maior desvio da identidade é o azul primário do sistema**: o app inteiro roda em
   #1A76F0, mas a marca é **#4767FA/#3A50D2**. Correção simples e de alto impacto — trocar
   os tokens `--primary`, `--ring` e `--gradient-primary` para o azul oficial
   (≈ `hsl(231 94% 63%)` para #4767FA).
2. As cores modulares (roxo, vermelho, amarelo, esmeralda, laranja Tailwind) são uma
   **extensão funcional legítima** (a marca não cobre dataviz/status), mas deveriam ser
   **recalibradas a partir da paleta oficial** — ex.: usar #DE571B como laranja do
   Operacional e #5E8C54 como verde de ERP/Fechamento — mantendo o índigo como eixo.
3. O pacote **não define tipografia de apoio nem tom de voz** — vale evoluí-lo para um
   brandbook com fonte institucional, regras de aplicação, área de respiro e as taglines
   oficiais (hoje o produto improvisa nesses pontos).
4. Os assets certos já estão no produto (selo, monograma, wordmark) — o problema não é
   *o que* está aplicado, e sim *a cor* em que o restante da interface foi construída.
