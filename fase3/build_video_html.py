# -*- coding: utf-8 -*-
"""Gera video.html — animação do vídeo ONE by GrowUp (72s) com seek(t) determinístico."""
import base64, re, random

KIT = '/home/user/Growup_sis/fase1/kit'
F = 'node_modules/@fontsource'

def b64(p):
    return base64.b64encode(open(p, 'rb').read()).decode()

fontcss = ''
for fam, w, f in [('Poppins','600','poppins/files/poppins-latin-600-normal.woff2'),
                  ('Poppins','700','poppins/files/poppins-latin-700-normal.woff2'),
                  ('Manrope','400','manrope/files/manrope-latin-400-normal.woff2'),
                  ('Manrope','500','manrope/files/manrope-latin-500-normal.woff2'),
                  ('Manrope','700','manrope/files/manrope-latin-700-normal.woff2')]:
    fontcss += f'@font-face{{font-family:"{fam}";font-weight:{w};src:url(data:font/woff2;base64,{b64(F+"/"+f)}) format("woff2")}}\n'

# ---- logo offwhite com classes por parte (letras / monograma / assinatura) ----
logo = open(f'{KIT}/one-by-growup_principal_offwhite.svg').read()
m = re.match(r'(<svg[^>]*>)(.*)</svg>', logo, re.S)
svg_open, body = m.group(1), m.group(2)
gpos = body.index('<g ')
gend = body.index('</g>') + 4
letters = body[:gpos]
mono = body[gpos:gend]
sig = body[gend:]
lp = re.findall(r'<path\b[^>]*/>', letters)
letters_tagged = ''.join(f'<g class="wl{i}">{p}</g>' for i, p in enumerate(lp))
logo_anim = (svg_open.replace('<svg', '<svg id="logoAnim"', 1)
             + letters_tagged
             + f'<g class="wmono">{mono}</g>'
             + f'<g class="wsig">{sig}</g></svg>')
logo_plain = logo
appicon = open(f'{KIT}/one_appicon.svg').read()

# ---- chips da dor (posições pré-computadas, determinísticas) ----
chip_specs = [
    ('CRM', 16, 38, -5), ('planilhas', 62, 34, 4), ('agência de marketing', 33, 46, -3),
    ('gestor de tarefas', 66, 52, 6), ('financeiro', 14, 60, 3), ('relatórios', 44, 64, -6),
    ('disparos WhatsApp', 60, 72, 2), ('BI', 36, 76, -4), ('e-mail mkt', 22, 50, 5),
    ('landing pages', 48, 40, -2),
]
chips = [(lb, x, y, r) for lb, x, y, r in chip_specs]
chips_html = ''.join(
    f'<div class="chip" id="chip{i}" style="left:{x}%;top:{y}%;--rot:{r}deg">{lb}</div>'
    for i, (lb, x, y, r) in enumerate(chips))
chips_js = '[' + ','.join(f'{{x:{x},y:{y},r:{r}}}' for _, x, y, r in chips) + ']'

# ---- módulos do tour ----
MODS_PY = [
    ('nexa',   'Nexa',   '#DE571B', 'ATRAI',      'Sua operação de marketing completa — sem agência.', 'meg'),
    ('sales',  'Sales',  '#4767FA', 'CONVERTE',   'Do lead ao fechamento, um funil que vende.', 'fun'),
    ('profit', 'Profit', '#5E8C54', 'LUCRA',      'Vendas, receitas e despesas sob controle — lucro à vista.', 'chart'),
    ('flow',   'Flow',   '#3A50D2', 'EXECUTA',    'Projetos, tarefas e processos rodando no ritmo certo.', 'gantt'),
    ('north',  'North',  '#2E8FA3', 'DÁ O NORTE', 'Os números que dão o norte das suas decisões.', 'stats'),
    ('growth', 'Growth', '#7B4FE0', 'ACELERA',    'Inteligência e agentes de IA trabalhando pelo seu crescimento.', 'chat'),
]
ICONS = {
 'meg':   '<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5v3l3 .6L19 19V5L7 9.9l-3 .6z"/><path d="M8.5 15l1 4"/></g>',
 'fun':   '<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16l-6 7v5.5L10 15v-3L4 5z"/></g>',
 'chart': '<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 17l5-5 4 3 7-7"/><path d="M15 8h5v5"/></g>',
 'gantt': '<g fill="#fff"><rect x="3.5" y="5" width="12" height="3.2" rx="1.6"/><rect x="8.5" y="10.4" width="12" height="3.2" rx="1.6"/><rect x="3.5" y="15.8" width="8" height="3.2" rx="1.6"/></g>',
 'stats': '<g fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="8.6"/><path fill="#fff" stroke="none" d="M15.6 8.4l-2.4 4.8-4.8 2.4 2.4-4.8 4.8-2.4z"/></g>',
 'chat':  '<g fill="#fff"><path d="M12 2.6l2.1 6 6 2.1-6 2.1-2.1 6-2.1-6-6-2.1 6-2.1 2.1-6z"/></g>',
}

def mock_ui(kind, cor):
    if kind == 'fun':  # kanban
        cols = ''
        names = ['Lead', 'Atendimento', 'Proposta', 'Fechamento']
        ccols = ['#E0B429', '#4767FA', '#7B4FE0', '#5E8C54']
        for c in range(4):
            cards = ''.join(f'<div class="kcard" data-col="{c}" data-i="{k}"></div>' for k in range(3 - (c % 2)))
            cols += f'<div class="kcol"><div class="kdot" style="background:{ccols[c]}"></div><div class="klab">{names[c]}</div>{cards}</div>'
        return f'<div class="kanban">{cols}<div class="kmove" id="kmove"></div></div>'
    if kind == 'chart':
        return ('<div class="chartwrap"><div class="bignum" id="bignum">R$ 0</div>'
                '<svg viewBox="0 0 400 150" class="linechart"><path id="lc" d="M10,130 C60,120 90,95 140,90 C200,84 220,60 280,48 C330,38 360,26 392,18" '
                f'fill="none" stroke="{cor}" stroke-width="5" stroke-linecap="round"/></svg>'
                '<div class="chbars">' + ''.join(f'<i style="--h:{h}%;background:{cor}" class="chb" data-i="{i}"></i>' for i, h in enumerate([34,52,44,66,58,80,92])) + '</div></div>')
    if kind == 'gantt':
        rows = ''
        for i, (w, off) in enumerate([(62, 4), (44, 18), (70, 10), (38, 34), (54, 22)]):
            rows += f'<div class="grow"><i class="gbar" data-i="{i}" style="--w:{w}%;--off:{off}%;background:{cor}"></i><span class="gchk" data-i="{i}">✓</span></div>'
        return f'<div class="gantt">{rows}</div>'
    if kind == 'stats':
        tiles = ''
        for i, (lab, val) in enumerate([('Conversão', '37%'), ('Receita', 'R$ 148k'), ('Leads', '312'), ('NPS', '86')]):
            tiles += f'<div class="stile" data-i="{i}"><b>{val}</b><span>{lab}</span></div>'
        return (f'<div class="stats">{tiles}<div class="sbars">'
                + ''.join(f'<i class="sb" data-i="{i}" style="--h:{h}%;background:{cor}"></i>' for i, h in enumerate([40,65,50,78,60,88]))
                + '</div></div>')
    if kind == 'chat':
        return ('<div class="chat">'
                '<div class="bub user" data-i="0">Como acelero minhas vendas este mês?</div>'
                f'<div class="bub bot" data-i="1" style="border-color:{cor}"><b style="color:{cor}">Growth One</b><br>Analisei seu funil: 23 propostas paradas há 7+ dias. Disparei a régua de follow-up e agendei 9 contatos.</div>'
                '<div class="bub user" data-i="2">Perfeito. E o marketing?</div>'
                f'<div class="bub bot" data-i="3" style="border-color:{cor}"><b style="color:{cor}">Growth One</b><br>O Nexa One está com CTR 2,4% — criei 3 variações de criativo para teste.</div>'
                '</div>')
    if kind == 'meg':
        cards = ''
        for i, lab in enumerate(['Campanha · Leads Q3', 'Auditoria de Marketing', 'Landing · Diagnóstico']):
            cards += (f'<div class="mcard" data-i="{i}"><i style="background:{cor}"></i><div><b>{lab}</b>'
                      '<div class="mbar"><span class="mfill" data-i="%d" style="background:%s"></span></div></div></div>' % (i, cor))
        return f'<div class="mcards">{cards}</div>'
    return ''

tour_html = ''
for i, (slug, nome, cor, verbo, desc, ui) in enumerate(MODS_PY):
    tour_html += f'''
  <div class="scene tour" id="tour{i}" style="--mc:{cor}">
    <div class="wash"></div>
    <div class="tour-left">
      <div class="ttile" style="background:{cor}"><svg viewBox="0 0 24 24">{ICONS[ui]}</svg></div>
      <div class="tname">{nome} <em style="color:{cor}">One</em></div>
      <div class="tverb" style="color:{cor}">{verbo}</div>
      <div class="tdesc">{desc}</div>
    </div>
    <div class="tour-right"><div class="ui-card" style="--mc:{cor}">
      <div class="ui-top"><i></i><i></i><i></i><span class="ui-url">one · {nome.lower()}</span></div>
      <div class="ui-body">{mock_ui(ui, cor)}</div>
    </div></div>
  </div>'''

html = '''<!doctype html><html><head><meta charset="utf-8"><style>
''' + fontcss + '''
*{box-sizing:border-box;margin:0}
html,body{width:1920px;height:1080px;overflow:hidden;background:#101014}
#stage{position:relative;width:1920px;height:1080px;font-family:"Manrope",sans-serif;background:#101014}
.scene{position:absolute;inset:0;opacity:0;display:flex;align-items:center;justify-content:center}

/* ---- cena 1: abertura ---- */
#s1 #logoAnim{width:900px}\n#s1 .wl0,#s1 .wl1,#s1 .wl2,#s1 .wmono,#s1 .wsig{transform-box:fill-box;transform-origin:center}
#s1 .wl0,#s1 .wl1,#s1 .wl2{opacity:0}
#s1 .wmono{opacity:0}
#s1 .wsig{opacity:0}

/* ---- cena 2: dor ---- */
#s2 .q{position:absolute;top:14%;width:100%;text-align:center;font-family:"Poppins";font-weight:700;font-size:74px;color:#F1F1F2;line-height:1.15}
.chip{position:absolute;background:#1E1F2A;border:1.5px solid #343544;color:#B9BAC6;font-size:26px;font-weight:500;padding:14px 28px;border-radius:ateur 99px;border-radius:99px;transform:rotate(var(--rot)) scale(0);white-space:nowrap}
/* ---- cena 3: virada ---- */
#s3 .appwrap{position:absolute;left:50%;top:38%;transform:translate(-50%,-50%);width:190px}
#s3 .tag{position:absolute;top:60%;width:100%;text-align:center;font-family:"Poppins";font-weight:700;font-size:86px;color:#F1F1F2}
#s3 .tag em{font-style:normal;color:#4767FA}
#s3 .bgglow{position:absolute;inset:0;background:radial-gradient(circle at 50% 40%, #1c2452 0%, #101014 60%)}

/* ---- tour ---- */
.tour .wash{position:absolute;inset:0;background:radial-gradient(circle at 24% 50%, color-mix(in srgb, var(--mc) 16%, transparent) 0%, transparent 62%)}
.tour-left{position:absolute;left:9%;top:50%;transform:translateY(-50%);width:34%;display:flex;flex-direction:column;gap:22px}
.ttile{width:120px;height:120px;border-radius:30px;display:flex;align-items:center;justify-content:center}
.ttile svg{width:64px;height:64px}
.tname{font-family:"Poppins";font-weight:700;font-size:88px;color:#F1F1F2;line-height:1}
.tname em{font-style:normal}
.tverb{font-family:"Poppins";font-weight:600;font-size:30px;letter-spacing:.3em}
.tdesc{color:#B9BAC6;font-size:30px;line-height:1.4;max-width:90%}
.tour-right{position:absolute;right:7%;top:50%;transform:translateY(-50%);width:44%}
.ui-card{background:#15161E;border:1.5px solid color-mix(in srgb, var(--mc) 40%, #23232e);border-radius:22px;overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.5)}
.ui-top{display:flex;align-items:center;gap:9px;background:#1B1C26;padding:16px 20px}
.ui-top i{width:13px;height:13px;border-radius:50%;background:#33343f}
.ui-url{margin-left:12px;color:#5d5e6c;font-size:18px}
.ui-body{padding:30px;height:430px}

/* kanban */
.kanban{display:flex;gap:18px;height:100%;position:relative}
.kcol{flex:1;background:#101018;border-radius:14px;padding:14px}
.kdot{width:12px;height:12px;border-radius:4px;margin-bottom:6px}
.klab{color:#8a8b98;font-size:16px;margin-bottom:10px}
.kcard{height:52px;border-radius:9px;background:#232433;margin-bottom:10px;transform:scale(0)}
.kmove{position:absolute;width:21%;height:52px;border-radius:9px;background:#4767FA;left:2%;top:24%;opacity:0}
/* chart */
.chartwrap{position:relative;height:100%}
.bignum{font-family:"Poppins";font-weight:700;font-size:56px;color:#F1F1F2}
.linechart{width:100%;height:190px;margin-top:8px}
#lc{stroke-dasharray:600;stroke-dashoffset:600}
.chbars{display:flex;gap:14px;align-items:flex-end;height:120px;margin-top:10px}
.chb{flex:1;border-radius:7px 7px 3px 3px;height:calc(var(--h));transform:scaleY(0);transform-origin:bottom}
/* gantt */
.gantt{display:flex;flex-direction:column;gap:26px;justify-content:center;height:100%}
.grow{position:relative;height:34px;background:#101018;border-radius:8px}
.gbar{position:absolute;left:var(--off);top:0;height:100%;width:0;border-radius:8px;display:block}
.gchk{position:absolute;right:14px;top:3px;color:#8ee08a;font-size:22px;opacity:0}
/* stats */
.stats{display:grid;grid-template-columns:1fr 1fr;gap:18px;height:100%;grid-template-rows:auto auto 1fr}
.stile{background:#101018;border-radius:14px;padding:18px 22px;transform:scale(.6);opacity:0}
.stile b{font-family:"Poppins";font-size:40px;color:#F1F1F2;display:block}
.stile span{color:#8a8b98;font-size:17px}
.sbars{grid-column:1/3;display:flex;gap:16px;align-items:flex-end;padding:6px 4px}
.sb{flex:1;border-radius:7px 7px 3px 3px;height:var(--h);transform:scaleY(0);transform-origin:bottom}
/* chat */
.chat{display:flex;flex-direction:column;gap:16px;justify-content:center;height:100%}
.bub{max-width:82%;padding:16px 20px;border-radius:16px;font-size:21px;line-height:1.35;opacity:0;transform:translateY(16px)}
.bub.user{align-self:flex-end;background:#232433;color:#d5d6e0}
.bub.bot{align-self:flex-start;background:#101018;border:1.5px solid;color:#b9bac6}
/* mkt cards */
.mcards{display:flex;flex-direction:column;gap:20px;justify-content:center;height:100%}
.mcard{display:flex;gap:16px;background:#101018;border-radius:14px;padding:18px;opacity:0;transform:translateX(40px)}
.mcard i{width:46px;height:46px;border-radius:12px;flex:none}
.mcard b{color:#d5d6e0;font-size:21px}
.mbar{margin-top:10px;height:10px;background:#232433;border-radius:6px;overflow:hidden;width:420px}
.mfill{display:block;height:100%;width:0}

/* ---- cena 10: ecossistema ---- */
#s10 .hier{display:flex;align-items:center;gap:34px;font-family:"Poppins";font-weight:700;font-size:64px;color:#F1F1F2}
#s10 .arr{color:#5b5c6b;font-weight:400}
#s10 .d6{display:flex;gap:12px}
#s10 .d6 i{width:34px;height:34px;border-radius:10px;transform:scale(0)}
#s10 .sub{position:absolute;top:63%;width:100%;text-align:center;color:#9C9CA6;font-size:34px}
/* ---- cena 11: CTA ---- */
#s11 .logo{width:760px;margin:0 auto}
#s11 .cta{display:inline-block;background:#4767FA;color:#fff;font-family:"Poppins";font-weight:600;font-size:34px;border-radius:16px;padding:22px 54px;margin-top:54px}
#s11 .url{color:#5d5e6c;font-size:26px;margin-top:26px;letter-spacing:.06em}
#s11 .inner{text-align:center}
</style></head><body>
<div id="stage">
  <div class="scene" id="s1">''' + logo_anim + '''</div>
  <div class="scene" id="s2"><div class="q" id="q2">Quantas ferramentas você paga<br>para gerir seu negócio?</div>''' + chips_html + '''</div>
  <div class="scene" id="s3"><div class="bgglow"></div><div class="appwrap" id="app3">''' + appicon + '''</div><div class="tag">Todo o seu negócio em <em>um</em>.</div></div>
''' + tour_html + '''
  <div class="scene" id="s10"><div class="hier"><span>growup</span><span class="arr">→</span><span>one</span><span class="arr">→</span><span class="d6"><i style="background:#DE571B"></i><i style="background:#4767FA"></i><i style="background:#5E8C54"></i><i style="background:#3A50D2"></i><i style="background:#2E8FA3"></i><i style="background:#7B4FE0"></i></span></div><div class="sub">O método GrowUp em forma de plataforma.</div></div>
  <div class="scene" id="s11"><div class="inner"><div class="logo">''' + logo_plain + '''</div><div class="cta">Fale com a GrowUp</div><div class="url">sistema.grow2up.com.br</div></div></div>
</div>
<script>
const CHIPS = ''' + chips_js + ''';
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const c01 = x => Math.max(0, Math.min(1, x));
const eo = t => 1 - Math.pow(1 - c01(t), 3);              // easeOutCubic
const ei = t => Math.pow(c01(t), 3);
const eio = t => { t = c01(t); return t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t+2,3)/2 };
const back = t => { t = c01(t); const c1 = 1.70158, c3 = c1 + 1; return 1 + c3*Math.pow(t-1,3) + c1*Math.pow(t-1,2) };
function vis(el, on){ el.style.opacity = on; }
function seg(t, a, b){ return c01((t - a) / (b - a)); }   // 0..1 dentro de [a,b]

const TOUR = [
  {id:'tour0', t0:22}, {id:'tour1', t0:28}, {id:'tour2', t0:34},
  {id:'tour3', t0:40}, {id:'tour4', t0:46}, {id:'tour5', t0:52},
];

window.seek = function(t){
  // esconde tudo
  $$('.scene').forEach(s => s.style.opacity = 0);

  // ---------- CENA 1 (0-6s) ----------
  if (t < 6.4){
    const s = $('#s1'); s.style.opacity = (t < 5.4) ? 1 : 1 - seg(t, 5.4, 6.0);
    const mono = $('#s1 .wmono');
    const mt = seg(t, 0.2, 1.4);
    mono.style.opacity = mt;
    mono.style.transform = `translate(${(1-back(mt))*120}px,0) scale(${0.7 + 0.3*back(mt)})`;
    mono.style.transformOrigin = '340px 60px';
    ['wl0','wl1','wl2'].forEach((c, i) => {
      const lt = seg(t, 1.2 + i*0.22, 1.9 + i*0.22);
      const el = $('#s1 .' + c);
      el.style.opacity = lt;
      el.style.transform = `translate(${(1-eo(lt))*-90}px,0)`;
    });
    const st = seg(t, 2.6, 3.4);
    const sigEl = $('#s1 .wsig');
    sigEl.style.opacity = st;
    sigEl.style.transform = `translate(0,${(1-eo(st))*24}px)`;
  }

  // ---------- CENA 2 (6-14s) ----------
  if (t >= 5.8 && t < 14.6){
    const s = $('#s2');
    s.style.opacity = seg(t, 5.9, 6.5) * (t < 13.6 ? 1 : 1 - seg(t, 13.6, 14.2));
    const q = $('#q2');
    const qt = seg(t, 6.2, 7.2);
    q.style.opacity = qt; q.style.transform = `translateY(${(1-eo(qt))*30}px)`;
    CHIPS.forEach((c, i) => {
      const ct = seg(t, 7.0 + i*0.5, 7.5 + i*0.5);
      const el = $('#chip' + i);
      el.style.transform = `rotate(${c.r}deg) scale(${back(ct)})`;
      el.style.opacity = Math.min(1, ct*2);
    });
  }

  // ---------- CENA 3 (14-22s) ----------
  if (t >= 13.8 && t < 22.6){
    const s = $('#s3');
    s.style.opacity = seg(t, 13.9, 14.5) * (t < 21.6 ? 1 : 1 - seg(t, 21.6, 22.2));
    // chips (reusa da cena 2 sobre a 3? não — some com espiral simulada no app)
    const at = seg(t, 14.2, 15.2);
    const app = $('#app3');
    const pulse = 1 + 0.06 * Math.sin(Math.PI * 6 * seg(t, 15.2, 18.2)) * (t < 18.4 ? 1 : 0);
    app.style.opacity = at;
    app.style.transform = `translate(-50%,-50%) scale(${(0.5 + 0.5*back(at)) * pulse})`;
    const tg = seg(t, 17.6, 18.8);
    const tag = $('#s3 .tag');
    tag.style.opacity = tg; tag.style.transform = `translateY(${(1-eo(tg))*40}px)`;
  }
  // chips sugadas: renderiza chips na cena 3 via cena 2 overlay
  if (t >= 13.8 && t < 17.4){
    const s2 = $('#s2');
    s2.style.opacity = Math.max(s2.style.opacity, 1 - seg(t, 16.4, 17.2));
    $('#q2').style.opacity = 1 - seg(t, 13.9, 14.6);
    CHIPS.forEach((c, i) => {
      const st = seg(t, 14.2 + i*0.18, 15.1 + i*0.18);
      const el = $('#chip' + i);
      const dx = (50 - c.x) * ei(st);
      const dy = (38 - c.y) * ei(st);
      el.style.left = (c.x + dx) + '%';
      el.style.top = (c.y + dy) + '%';
      el.style.transform = `rotate(${c.r * (1-st) + 360*ei(st)}deg) scale(${1 - ei(st)})`;
      el.style.opacity = 1 - ei(st);
    });
  } else if (t < 13.8){
    CHIPS.forEach((c, i) => { const el = $('#chip'+i); el.style.left = c.x+'%'; el.style.top = c.y+'%'; });
  }

  // ---------- TOUR (22-58s) ----------
  TOUR.forEach((cfg, mi) => {
    const lt = t - cfg.t0;              // tempo local 0..6
    if (lt < -0.4 || lt > 6.4) return;
    const s = $('#' + cfg.id);
    s.style.opacity = seg(lt, -0.2, 0.4) * (lt < 5.6 ? 1 : 1 - seg(lt, 5.6, 6.2));
    const tile = s.querySelector('.ttile');
    const tt = seg(lt, 0.1, 0.75);
    tile.style.transform = `scale(${back(tt)})`; tile.style.opacity = Math.min(1, tt*2);
    const nm = s.querySelector('.tname');
    const nt = seg(lt, 0.35, 1.0);
    nm.style.opacity = nt; nm.style.transform = `translateY(${(1-eo(nt))*30}px)`;
    const vb = s.querySelector('.tverb');
    const vt = seg(lt, 0.6, 1.2);
    vb.style.opacity = vt; vb.style.letterSpacing = (0.55 - 0.25*eo(vt)) + 'em';
    const dc = s.querySelector('.tdesc');
    const dt = seg(lt, 0.85, 1.5);
    dc.style.opacity = dt; dc.style.transform = `translateY(${(1-eo(dt))*20}px)`;
    const card = s.querySelector('.ui-card');
    const ct = seg(lt, 0.5, 1.4);
    card.style.opacity = ct;
    card.style.transform = `translateX(${(1-eo(ct))*140}px) rotate(${(1-eo(ct))*2}deg)`;

    const u = seg(lt, 1.2, 5.2);        // progresso da UI interna
    // kanban
    s.querySelectorAll('.kcard').forEach((k, i) => {
      const kt = seg(u, 0.05 + i*0.09, 0.2 + i*0.09);
      k.style.transform = `scale(${back(kt)})`;
    });
    const km = s.querySelector('.kmove');
    if (km){
      const m1 = seg(u, 0.45, 0.95);
      km.style.opacity = m1 > 0 && m1 < 1 ? 1 : (m1 >= 1 ? 1 : 0);
      km.style.left = (2 + 75.5 * eio(m1)) + '%';
      km.style.top = (24 + 10 * Math.sin(Math.PI * m1)) + '%';
    }
    // chart
    const lc = s.querySelector('#lc');
    if (lc && s.id === 'tour2'){
      lc.style.strokeDashoffset = 600 * (1 - eo(seg(u, 0.1, 0.8)));
      const bn = s.querySelector('#bignum');
      const val = Math.round(148230 * eo(seg(u, 0.15, 0.9)));
      bn.textContent = 'R$ ' + val.toLocaleString('pt-BR');
      s.querySelectorAll('.chb').forEach((b, i) => {
        b.style.transform = `scaleY(${eo(seg(u, 0.2 + i*0.08, 0.45 + i*0.08))})`;
      });
    }
    // gantt
    s.querySelectorAll('.gbar').forEach((g, i) => {
      const gt = eo(seg(u, 0.08 + i*0.12, 0.5 + i*0.12));
      g.style.width = `calc(var(--w) * ${gt})`;
    });
    s.querySelectorAll('.gchk').forEach((g, i) => {
      g.style.opacity = seg(u, 0.55 + i*0.09, 0.65 + i*0.09);
    });
    // stats
    s.querySelectorAll('.stile').forEach((el, i) => {
      const stt = seg(u, 0.05 + i*0.1, 0.3 + i*0.1);
      el.style.opacity = stt; el.style.transform = `scale(${0.6 + 0.4*back(stt)})`;
    });
    s.querySelectorAll('.sb').forEach((b, i) => {
      b.style.transform = `scaleY(${eo(seg(u, 0.4 + i*0.07, 0.65 + i*0.07))})`;
    });
    // chat
    s.querySelectorAll('.bub').forEach((b, i) => {
      const bt = seg(u, 0.08 + i*0.2, 0.28 + i*0.2);
      b.style.opacity = bt; b.style.transform = `translateY(${(1-eo(bt))*16}px)`;
    });
    // mkt
    s.querySelectorAll('.mcard').forEach((mc, i) => {
      const mt2 = seg(u, 0.06 + i*0.14, 0.3 + i*0.14);
      mc.style.opacity = mt2; mc.style.transform = `translateX(${(1-eo(mt2))*40}px)`;
    });
    s.querySelectorAll('.mfill').forEach((mf, i) => {
      mf.style.width = (eo(seg(u, 0.35 + i*0.14, 0.85 + i*0.14)) * [78, 54, 92][i]) + '%';
    });
  });

  // ---------- CENA 10 (58-66s) ----------
  if (t >= 57.6 && t < 66.6){
    const s = $('#s10');
    s.style.opacity = seg(t, 57.8, 58.5) * (t < 65.6 ? 1 : 1 - seg(t, 65.6, 66.2));
    const words = s.querySelectorAll('.hier > span');
    // growup, arr, one, arr, dots
    const seqT = [58.3, 58.9, 59.3, 59.9, 60.2];
    words.forEach((w, i) => {
      const wt = seg(t, seqT[i], seqT[i] + 0.6);
      w.style.opacity = wt;
      w.style.transform = `translateY(${(1-eo(wt))*24}px)`;
    });
    s.querySelectorAll('.d6 i').forEach((d, i) => {
      const dt2 = seg(t, 60.3 + i*0.14, 60.7 + i*0.14);
      d.style.transform = `scale(${back(dt2)})`;
      d.style.opacity = dt2 > 0 ? 1 : 0;
    });
    const sub = s.querySelector('.sub');
    const st2 = seg(t, 61.6, 62.5);
    sub.style.opacity = st2; sub.style.transform = `translateY(${(1-eo(st2))*20}px)`;
  }

  // ---------- CENA 11 (66-72s) ----------
  if (t >= 65.8){
    const s = $('#s11');
    s.style.opacity = seg(t, 66.0, 66.7);
    const lg = s.querySelector('.logo');
    const lt2 = seg(t, 66.1, 67.0);
    const breathe = 1 + 0.008 * Math.sin(2 * Math.PI * (t - 67) / 3);
    lg.style.opacity = lt2;
    lg.style.transform = `scale(${(0.92 + 0.08*eo(lt2)) * breathe})`;
    const cta = s.querySelector('.cta');
    const ct2 = seg(t, 67.0, 67.7);
    cta.style.opacity = ct2; cta.style.transform = `translateY(${(1-back(ct2))*30}px)`;
    const url = s.querySelector('.url');
    url.style.opacity = seg(t, 67.6, 68.3);
  }
};
window.seek(0);
</script>
</body></html>
'''
# corrige typo acidental
html = html.replace('border-radius:ateur 99px;', '')
open('video.html', 'w').write(html)
print('video.html:', len(html)//1024, 'KB')
