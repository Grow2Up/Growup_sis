# -*- coding: utf-8 -*-
"""Fase 3 · item 3.1 — Roteiro + Storyboard do vídeo ONE by GrowUp (para aprovação)."""
import base64

KIT = '/home/user/Growup_sis/fase1/kit'
F = 'node_modules/@fontsource'

def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

def load(f):
    return open(f'{KIT}/{f}').read()

fontcss = ''
for fam, w, f in [('Poppins','600','poppins/files/poppins-latin-600-normal.woff2'),
                  ('Poppins','700','poppins/files/poppins-latin-700-normal.woff2'),
                  ('Manrope','400','manrope/files/manrope-latin-400-normal.woff2'),
                  ('Manrope','500','manrope/files/manrope-latin-500-normal.woff2'),
                  ('Manrope','700','manrope/files/manrope-latin-700-normal.woff2')]:
    fontcss += f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:normal;font-display:swap;src:url(data:font/woff2;base64,{b64(F+"/"+f)}) format("woff2")}}\n'

logo_off = load('one-by-growup_principal_offwhite.svg')
appicon = load('one_appicon.svg')

MODS = [
    ('Nexa One',   '#DE571B', 'atrai',        'Sua operação de marketing completa — sem agência.',
     'megafone', '<path d="M4 10.5v3l3 .6L19 19V5L7 9.9l-3 .6z"/><path d="M8.5 15l1 4"/>', 'stroke',
     'Campanhas, auditorias e landing pages na tela'),
    ('Sales One',  '#4767FA', 'converte',     'Do lead ao fechamento, um funil que vende.',
     'funil', '<path d="M4 5h16l-6 7v5.5L10 15v-3L4 5z"/>', 'stroke',
     'Kanban do funil com cards andando de coluna'),
    ('Profit One', '#5E8C54', 'lucra',        'Vendas, receitas e despesas sob controle — lucro à vista.',
     'gráfico', '<path d="M4 17l5-5 4 3 7-7"/><path d="M15 8h5v5"/>', 'stroke',
     'Gráfico de receita subindo + mapa do Brasil'),
    ('Flow One',   '#3A50D2', 'executa',      'Projetos, tarefas e processos rodando no ritmo certo.',
     'fluxo', '<rect x="3.5" y="5" width="12" height="3.2" rx="1.6"/><rect x="8.5" y="10.4" width="12" height="3.2" rx="1.6"/><rect x="3.5" y="15.8" width="8" height="3.2" rx="1.6"/>', 'fill',
     'Gantt/kanban de tarefas completando'),
    ('North One',  '#2E8FA3', 'dá o norte',   'Os números que dão o norte das suas decisões.',
     'bússola', '<circle cx="12" cy="12" r="8.6" fill="none"/><path d="M15.6 8.4l-2.4 4.8-4.8 2.4 2.4-4.8 4.8-2.4z" class="f"/>', 'mixed',
     'Dashboard de métricas ganhando vida'),
    ('Growth One', '#7B4FE0', 'acelera',      'Inteligência e agentes de IA trabalhando pelo seu crescimento.',
     'faísca', '<path d="M12 2.6l2.1 6 6 2.1-6 2.1-2.1 6-2.1-6-6-2.1 6-2.1 2.1-6z"/>', 'fill',
     'Chat do agente de IA respondendo + insights'),
]

def icon_svg(icon, mode, color='#fff', size=44):
    if mode == 'stroke':
        inner = f'<g fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon}</g>'
    elif mode == 'fill':
        inner = f'<g fill="{color}" stroke="none">{icon}</g>'
    else:
        fixed = icon.replace('class="f"', f'fill="{color}" stroke="none"')
        inner = f'<g fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{fixed}</g>'
    return f'<svg viewBox="0 0 24 24" style="width:{size}px;height:{size}px">{inner}</svg>'

# cenas do tour (uma por módulo)
tour_scenes = ''
t0 = 22
for i, (nome, cor, verbo, desc, icname, icon, mode, visual) in enumerate(MODS):
    t1, t2 = t0 + i*6, t0 + (i+1)*6
    tour_scenes += f'''
    <div class="scene">
      <div class="frame" style="background:linear-gradient(135deg, {cor}18, #101014 60%), #101014">
        <div class="fr-mod">
          <div class="fr-tile" style="background:{cor}">{icon_svg(icon, mode)}</div>
          <div class="fr-modname">{nome.split(' ')[0]} <em style="color:{cor}">One</em></div>
          <div class="fr-verb" style="color:{cor}">{verbo}</div>
          <div class="fr-desc">{desc}</div>
          <div class="fr-ui" style="border-color:{cor}55">
            <div class="fr-ui-bar" style="background:{cor}"></div>
            <div class="fr-ui-note">{visual}</div>
          </div>
        </div>
      </div>
      <div class="meta">
        <span class="time">{t1:02d}–{t2:02d}s</span>
        <b>Cena {4+i} — {nome}</b>
        <p><b>Animação:</b> a cor do módulo invade a tela; tile+ícone entram com bounce sutil; "{verbo}" pulsa; a tela do sistema desliza por trás mostrando {visual.lower()}.</p>
        <p class="txt">Texto on-screen: <i>"{nome} {verbo}."</i> + descritor</p>
      </div>
    </div>'''

html = '''<title>ONE by GrowUp — Fase 3 · Roteiro & Storyboard do vídeo</title>
<style>
''' + fontcss + '''
:root{--ground:#F2F2F0;--surface:#FFF;--surface-2:#F7F7FB;--ink:#141414;--muted:#6C6C70;--line:#E2E2E6;--accent:#4767FA}
@media (prefers-color-scheme: dark){:root{--ground:#0E0F15;--surface:#16171F;--surface-2:#1C1D27;--ink:#F1F1F2;--muted:#9C9CA6;--line:#2A2B36}}
:root[data-theme="dark"]{--ground:#0E0F15;--surface:#16171F;--surface-2:#1C1D27;--ink:#F1F1F2;--muted:#9C9CA6;--line:#2A2B36}
:root[data-theme="light"]{--ground:#F2F2F0;--surface:#FFF;--surface-2:#F7F7FB;--ink:#141414;--muted:#6C6C70;--line:#E2E2E6}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:"Manrope",system-ui,sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1000px;margin:0 auto;padding:48px 24px 80px}
.eyebrow{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:0 0 10px}
h1{font-family:"Poppins";font-weight:700;font-size:clamp(26px,4.2vw,38px);line-height:1.14;margin:0 0 10px;letter-spacing:-.01em}
h2{font-family:"Poppins";font-weight:600;font-size:19px;margin:0 0 4px}
.lead{color:var(--muted);max-width:64ch;font-size:15.5px;margin:0 0 6px}
section{margin-top:50px}
.note{font-size:13px;color:var(--muted)}
.specs{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.specs span{font-size:12.5px;font-weight:700;border:1px solid var(--line);background:var(--surface);border-radius:99px;padding:5px 13px}

/* timeline */
.tl{display:flex;height:34px;border-radius:9px;overflow:hidden;border:1px solid var(--line);margin:16px 0 4px;font-size:10.5px;font-weight:700;color:#fff;text-align:center}
.tl div{display:flex;align-items:center;justify-content:center;overflow:hidden;white-space:nowrap}
.tl-cap{display:flex;justify-content:space-between;font-size:11px;color:var(--muted)}

/* scenes */
.scene{display:grid;grid-template-columns:minmax(280px,420px) 1fr;gap:20px;margin-top:22px;align-items:start}
.frame{aspect-ratio:16/9;border-radius:12px;overflow:hidden;position:relative;border:1px solid #23232e;display:flex;align-items:center;justify-content:center;padding:20px}
.meta{font-size:13.5px}
.meta b{font-family:"Poppins";font-size:15px;display:block;margin:2px 0 6px}
.meta p{margin:0 0 6px;color:var(--muted)}
.meta .txt{color:var(--ink)}
.time{font-family:ui-monospace,Menlo,monospace;font-size:11.5px;color:var(--accent);font-weight:700}

/* frame contents */
.fr-logo{width:62%}
.fr-tag{color:#F1F1F2;font-family:"Poppins";font-weight:700;font-size:clamp(15px,2.6vw,24px);text-align:center}
.fr-tag em{font-style:normal;color:#4767FA}
.fr-sub{color:#9C9CA6;font-size:11px;text-align:center;margin-top:6px}
.chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;max-width:85%}
.chips span{background:#1E1F2A;border:1px solid #343544;color:#B9BAC6;font-size:10.5px;padding:5px 10px;border-radius:99px;transform:rotate(var(--r,0deg))}
.fr-mod{display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center;width:100%}
.fr-tile{width:52px;height:52px;border-radius:13px;display:flex;align-items:center;justify-content:center}
.fr-modname{font-family:"Poppins";font-weight:700;font-size:21px;color:#F1F1F2}
.fr-modname em{font-style:normal}
.fr-verb{font-family:"Poppins";font-weight:600;font-size:12px;letter-spacing:.18em;text-transform:uppercase}
.fr-desc{color:#B9BAC6;font-size:11px;max-width:78%}
.fr-ui{margin-top:6px;width:70%;border:1px solid;border-radius:8px;background:#15161e;padding:6px 8px;display:flex;gap:7px;align-items:center}
.fr-ui-bar{width:34px;height:5px;border-radius:3px}
.fr-ui-note{font-size:9.5px;color:#7d7e8c;text-align:left}
.hier-fr{display:flex;align-items:center;gap:12px;color:#F1F1F2;font-family:"Poppins";font-weight:600;font-size:15px}
.hier-fr .arr{color:#5b5c6b}
.dots6{display:flex;gap:5px}
.dots6 i{width:11px;height:11px;border-radius:4px}
.cta-btn{background:#4767FA;color:#fff;font-family:"Poppins";font-weight:600;font-size:12px;border-radius:9px;padding:8px 18px;margin-top:10px}

/* audio + approval */
.opts{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.opt{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px;font-size:13px}
.opt b{font-family:"Poppins";font-size:13.5px;display:block;margin-bottom:4px}
.opt.rec{border-color:var(--accent)}
.badge{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;padding:2px 8px;border-radius:99px;background:var(--accent);color:#fff;margin-left:6px}
.approve{background:var(--surface-2);border:1px dashed var(--line);border-radius:14px;padding:22px 24px;margin-top:50px}
.approve ol{margin:10px 0 0;padding-left:20px}
.approve li{margin-bottom:8px;font-size:14.5px}
.approve li b{color:var(--accent)}
footer{margin-top:56px;font-size:12.5px;color:var(--muted);border-top:1px solid var(--line);padding-top:18px}
@media (max-width:720px){.scene{grid-template-columns:1fr}}
</style>

<div class="wrap">
  <header>
    <p class="eyebrow">Fase 3 · Entrega 3.1 · Para aprovação</p>
    <h1>Vídeo de lançamento — roteiro &amp; storyboard</h1>
    <p class="lead">Cada quadro abaixo é o keyframe real da animação final (mesma identidade, mesmos assets). Aprovando o storyboard, a produção anima exatamente o que você vê aqui.</p>
    <div class="specs"><span>≈ 72 segundos</span><span>1080p · 16:9</span><span>Motion graphics</span><span>11 cenas</span><span>pt-BR</span></div>
  </header>

  <section>
    <h2>Linha do tempo</h2>
    <div class="tl">
      <div style="flex:6;background:#141414">Abertura</div>
      <div style="flex:8;background:#3c3d49">A dor</div>
      <div style="flex:8;background:#4767FA">A virada</div>
      <div style="flex:6;background:#DE571B">Nexa</div>
      <div style="flex:6;background:#4767FA">Sales</div>
      <div style="flex:6;background:#5E8C54">Profit</div>
      <div style="flex:6;background:#3A50D2">Flow</div>
      <div style="flex:6;background:#2E8FA3">North</div>
      <div style="flex:6;background:#7B4FE0">Growth</div>
      <div style="flex:8;background:#141414">Ecossistema</div>
      <div style="flex:6;background:#4767FA">CTA</div>
    </div>
    <div class="tl-cap"><span>0s</span><span>~36s</span><span>72s</span></div>
  </section>

  <section>
    <h2>Cenas</h2>

    <div class="scene">
      <div class="frame" style="background:#101014">
        <div style="text-align:center;width:100%"><div class="fr-logo" style="margin:0 auto">''' + logo_off + '''</div></div>
      </div>
      <div class="meta">
        <span class="time">00–06s</span>
        <b>Cena 1 — Abertura</b>
        <p><b>Animação:</b> fundo preto; o monograma desenha-se (a seta "rompe" o contêiner U para fora, eco do conceito da marca); o wordmark "one" desliza da esquerda; "BY GROWUP" surge por fade.</p>
        <p class="txt">Sem texto além do logo. Som: whoosh + acorde de assinatura (se houver trilha).</p>
      </div>
    </div>

    <div class="scene">
      <div class="frame" style="background:#101014">
        <div style="text-align:center">
          <div class="fr-tag">Quantas ferramentas você paga<br>para gerir seu negócio?</div>
          <div class="chips" style="margin-top:12px">
            <span style="--r:-3deg">CRM</span><span style="--r:2deg">planilhas</span><span style="--r:-2deg">agência de marketing</span>
            <span style="--r:3deg">gestor de tarefas</span><span style="--r:-1deg">financeiro</span><span style="--r:2deg">relatórios</span>
            <span style="--r:-3deg">disparos WhatsApp</span><span style="--r:1deg">BI</span>
          </div>
        </div>
      </div>
      <div class="meta">
        <span class="time">06–14s</span>
        <b>Cena 2 — A dor</b>
        <p><b>Animação:</b> chips de ferramentas pipocam desordenadas pela tela, tortas e se acumulando — sensação de caos e custo. A pergunta digita-se no topo.</p>
        <p class="txt">Texto on-screen: "Quantas ferramentas você paga para gerir seu negócio?"</p>
      </div>
    </div>

    <div class="scene">
      <div class="frame" style="background:radial-gradient(circle at center, #1c2452 0%, #101014 70%)">
        <div style="text-align:center">
          <div style="width:74px;margin:0 auto 12px">''' + appicon + '''</div>
          <div class="fr-tag">Todo o seu negócio em <em>um</em>.</div>
        </div>
      </div>
      <div class="meta">
        <span class="time">14–22s</span>
        <b>Cena 3 — A virada</b>
        <p><b>Animação:</b> todas as chips são atraídas em espiral para o centro e são absorvidas pelo monograma (o app icon pulsa ao "engolir" cada uma). A tagline entra com o "um" em azul.</p>
        <p class="txt">Texto on-screen: tagline oficial. Este é o momento-assinatura do vídeo.</p>
      </div>
    </div>
''' + tour_scenes + '''

    <div class="scene">
      <div class="frame" style="background:#101014">
        <div style="text-align:center">
          <div class="hier-fr">growup <span class="arr">→</span> one <span class="arr">→</span> <span class="dots6"><i style="background:#DE571B"></i><i style="background:#4767FA"></i><i style="background:#5E8C54"></i><i style="background:#3A50D2"></i><i style="background:#2E8FA3"></i><i style="background:#7B4FE0"></i></span></div>
          <div class="fr-sub" style="margin-top:10px">O método GrowUp em forma de plataforma.</div>
        </div>
      </div>
      <div class="meta">
        <span class="time">58–66s</span>
        <b>Cena 10 — O ecossistema</b>
        <p><b>Animação:</b> os 6 tiles coloridos do tour recolhem-se em fila e conectam-se ao monograma; acima surge "growup" — a hierarquia da marca desenhada ao vivo.</p>
        <p class="txt">Texto on-screen: "O método GrowUp em forma de plataforma."</p>
      </div>
    </div>

    <div class="scene">
      <div class="frame" style="background:#101014">
        <div style="text-align:center;width:100%">
          <div class="fr-logo" style="margin:0 auto;width:52%">''' + logo_off + '''</div>
          <div class="cta-btn" style="display:inline-block">Fale com a GrowUp</div>
          <div class="fr-sub">sistema.grow2up.com.br</div>
        </div>
      </div>
      <div class="meta">
        <span class="time">66–72s</span>
        <b>Cena 11 — CTA</b>
        <p><b>Animação:</b> logo respira; botão de CTA entra com o shimmer da identidade; endereço em baixo. Fecho no selo ONE girando sutilmente (marca d'água).</p>
        <p class="txt">Texto on-screen: "Fale com a GrowUp" + endereço do sistema (posso trocar pelo canal que preferir: WhatsApp, site da GrowUp, etc.)</p>
      </div>
    </div>
  </section>

  <section>
    <h2>Áudio — decisão</h2>
    <div class="opts">
      <div class="opt rec"><b>A · Sem áudio embutido <span class="badge">Recomendada p/ v1</span></b>Vídeo 100% legível sem som (texto on-screen forte). Você adiciona trilha licenciada depois na edição/redes — máxima flexibilidade.</div>
      <div class="opt"><b>B · Trilha fornecida por você</b>Você me envia um MP3/WAV licenciado e eu embuto sincronizando os cortes com as batidas.</div>
      <div class="opt"><b>C · Locução TTS externa</b>Se você tiver acesso a uma ferramenta de voz (ex.: ElevenLabs), eu escrevo o script de locução e deixo o vídeo pronto para receber a voz.</div>
    </div>
  </section>

  <div class="approve">
    <h2>Para aprovar este roteiro</h2>
    <ol>
      <li><b>Estrutura:</b> as 11 cenas e a ordem do tour (narrativa da família) estão aprovadas?</li>
      <li><b>Textos on-screen:</b> ok como estão? (pergunta da dor, tagline, verbos por módulo, CTA)</li>
      <li><b>CTA final:</b> "Fale com a GrowUp" + sistema.grow2up.com.br — ou prefere WhatsApp/outro destino?</li>
      <li><b>Áudio:</b> opção A, B ou C?</li>
    </ol>
    <p class="note" style="margin-top:12px">Com as respostas, sigo para a 3.2: produção do motion graphics (1080p 16:9, MP4). As telas dos módulos entram como mockups fiéis na identidade nova; se você publicar o preview antes, posso usar capturas reais.</p>
  </div>

  <footer>ONE by GrowUp · Fase 3 — Roteiro &amp; Storyboard (item 3.1) · ~72s · Motion graphics na identidade aprovada</footer>
</div>
'''
open('storyboard-video-one.html', 'w').write(html)
print('storyboard:', len(html)//1024, 'KB')
