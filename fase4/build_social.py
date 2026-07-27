# -*- coding: utf-8 -*-
"""Fase 4A — Pack de social do ONE by GrowUp.
Gera social.html com todas as peças (posts e slides de carrossel) em <div class="art">
identificadas por id; um script de screenshot exporta cada uma em PNG nos formatos.

Sistema visual (item 4.1): fundo #101014, wash radial na cor do módulo, tile+ícone,
nome Poppins, "One" na cor, descritor Manrope, selo/assinatura ONE by GrowUp no rodapé.
"""
import base64

KIT = '/home/user/Growup_sis/fase1/kit'
F = 'node_modules/@fontsource'

def b64(p):
    return base64.b64encode(open(p, 'rb').read()).decode()

def load(f):
    return open(f'{KIT}/{f}').read()

fontcss = ''
for fam, w, f in [('Poppins','600','poppins/files/poppins-latin-600-normal.woff2'),
                  ('Poppins','700','poppins/files/poppins-latin-700-normal.woff2'),
                  ('Manrope','400','manrope/files/manrope-latin-400-normal.woff2'),
                  ('Manrope','500','manrope/files/manrope-latin-500-normal.woff2'),
                  ('Manrope','700','manrope/files/manrope-latin-700-normal.woff2')]:
    fontcss += f'@font-face{{font-family:"{fam}";font-weight:{w};src:url(data:font/woff2;base64,{b64(F+"/"+f)}) format("woff2")}}\n'

logo_off = load('one-by-growup_principal_offwhite.svg')
appicon = load('one_appicon.svg')

MODS = [
    ('nexa',   'Nexa',   '#DE571B', 'atrai',      'Sua operação de marketing completa — sem agência.',
     'Campanhas, auditorias, landing pages e automação — o marketing inteiro rodando dentro do seu sistema.'),
    ('sales',  'Sales',  '#4767FA', 'converte',   'Do lead ao fechamento, um funil que vende.',
     'Pipeline visual, leads do Meta Ads caindo direto no funil e réguas de follow-up automáticas.'),
    ('profit', 'Profit', '#5E8C54', 'lucra',      'Vendas, receitas e despesas sob controle — lucro à vista.',
     'Financeiro sem planilha: vendas, despesas, metas e o mapa do seu faturamento por estado.'),
    ('flow',   'Flow',   '#3A50D2', 'executa',    'Projetos, tarefas e processos rodando no ritmo certo.',
     'Kanban, Gantt e processos mapeados — sua operação inteira visível e no prazo.'),
    ('north',  'North',  '#2E8FA3', 'dá o norte', 'Os números que dão o norte das suas decisões.',
     'Conversão, receita e funil em dashboards que respondem antes de você perguntar.'),
    ('growth', 'Growth', '#7B4FE0', 'acelera',    'Inteligência e agentes de IA trabalhando pelo seu crescimento.',
     'Agentes de IA, diagnósticos e planejamento estratégico — o cérebro do ecossistema.'),
]
ICONS = {
 'nexa':   '<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5v3l3 .6L19 19V5L7 9.9l-3 .6z"/><path d="M8.5 15l1 4"/></g>',
 'sales':  '<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16l-6 7v5.5L10 15v-3L4 5z"/></g>',
 'profit': '<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 17l5-5 4 3 7-7"/><path d="M15 8h5v5"/></g>',
 'flow':   '<g fill="#fff"><rect x="3.5" y="5" width="12" height="3.2" rx="1.6"/><rect x="8.5" y="10.4" width="12" height="3.2" rx="1.6"/><rect x="3.5" y="15.8" width="8" height="3.2" rx="1.6"/></g>',
 'north':  '<g fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="8.6"/><path fill="#fff" stroke="none" d="M15.6 8.4l-2.4 4.8-4.8 2.4 2.4-4.8 4.8-2.4z"/></g>',
 'growth': '<g fill="#fff"><path d="M12 2.6l2.1 6 6 2.1-6 2.1-2.1 6-2.1-6-6-2.1 6-2.1 2.1-6z"/></g>',
}

def footer(dark=True):
    return '<div class="foot"><div class="fl">' + logo_off + '</div><span>O método GrowUp em forma de plataforma.</span></div>'

def icon(slug, size=64):
    return f'<svg viewBox="0 0 24 24" style="width:{size}px;height:{size}px">{ICONS[slug]}</svg>'

arts = []

# ---------- POST DE LANÇAMENTO ----------
launch = f'''
  <div class="hero-chips">
    <span style="--r:-4deg">CRM</span><span style="--r:3deg">planilhas</span><span style="--r:-2deg">agência</span>
    <span style="--r:4deg">tarefas</span><span style="--r:-3deg">financeiro</span><span style="--r:2deg">relatórios</span>
  </div>
  <div class="hero-app">{appicon}</div>
  <h1 class="hero-t">Todo o seu negócio<br>em <em>um</em>.</h1>
  <p class="hero-s">CRM · Financeiro · Operação · Relatórios · Marketing · IA</p>
  {footer()}'''
arts.append(('post_lancamento', launch, 'launch'))

# ---------- POSTS POR MÓDULO ----------
for slug, nome, cor, verbo, desc, longdesc in MODS:
    art = f'''
  <div class="wash" style="background:radial-gradient(circle at 50% 30%, {cor}2e 0%, transparent 62%)"></div>
  <div class="mod-tile" style="background:{cor}">{icon(slug)}</div>
  <h1 class="mod-t">{nome} <em style="color:{cor}">One</em></h1>
  <div class="mod-v" style="color:{cor}">{verbo}</div>
  <p class="mod-d">{desc}</p>
  <div class="mod-strip"><i style="background:{cor}"></i><i style="background:{cor};opacity:.55"></i><i style="background:{cor};opacity:.25"></i></div>
  {footer()}'''
    arts.append((f'post_{slug}-one', art, 'mod'))

# ---------- CARROSSEL DE LANÇAMENTO (8 slides 4:5) ----------
# capa
arts.append(('carrossel_01_capa', f'''
  <div class="hero-app sm">{appicon}</div>
  <h1 class="hero-t">Quantas ferramentas<br>você paga para<br>gerir seu negócio?</h1>
  <p class="hero-s2">Arrasta que a gente resolve. →</p>
  {footer()}''', 'launch'))
# slides módulos
for i, (slug, nome, cor, verbo, desc, longdesc) in enumerate(MODS):
    arts.append((f'carrossel_{i+2:02d}_{slug}', f'''
  <div class="wash" style="background:radial-gradient(circle at 50% 26%, {cor}30 0%, transparent 60%)"></div>
  <div class="sl-top"><span class="sl-n" style="color:{cor}">{i+1}/6</span></div>
  <div class="mod-tile" style="background:{cor}">{icon(slug)}</div>
  <h1 class="mod-t">{nome} <em style="color:{cor}">One</em></h1>
  <div class="mod-v" style="color:{cor}">{verbo}</div>
  <p class="mod-d2">{longdesc}</p>
  {footer()}''', 'mod'))
# fechamento (sem CTA — assinatura da marca)
arts.append(('carrossel_08_fechamento', f'''
  <div class="hero-logo">{logo_off}</div>
  <h1 class="hero-t sm2">Um sistema.<br>Seis módulos.<br>Todo o seu crescimento.</h1>
  <p class="hero-s2">O método GrowUp em forma de plataforma.</p>''', 'launch'))

arts_html = ''
for name, inner, kind in arts:
    arts_html += f'<div class="art" id="{name}" data-kind="{kind}"><div class="inner">{inner}</div></div>\n'

html = '''<!doctype html><html><head><meta charset="utf-8"><style>
''' + fontcss + '''
*{box-sizing:border-box;margin:0}
body{background:#333;font-family:"Manrope",sans-serif;display:flex;flex-direction:column;gap:40px;padding:40px}
.art{width:1080px;height:1350px;background:#101014;position:relative;overflow:hidden;flex:none}
.art .inner{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:90px 80px}
.wash{position:absolute;inset:0}
.art.sq{height:1080px}
/* 9:16 — zona segura do Meta (stories/reels): ~250px topo, ~340px base, UI lateral */
.art.story{height:1920px}
.art.story .inner{padding:280px 110px 380px}
.art.story .foot{bottom:340px}
.art.story .sl-top{top:290px;right:110px}

.hero-chips{display:flex;flex-wrap:wrap;gap:16px;justify-content:center;max-width:70%;margin-bottom:60px}
.hero-chips span{background:#1E1F2A;border:2px solid #343544;color:#B9BAC6;font-size:27px;padding:14px 30px;border-radius:99px;transform:rotate(var(--r))}
.hero-app{width:200px;margin-bottom:60px}
.hero-app.sm{width:150px;margin-bottom:70px}
.hero-logo{width:600px;margin-bottom:80px}
.hero-t{font-family:"Poppins";font-weight:700;font-size:92px;line-height:1.1;color:#F1F1F2}
.hero-t em{font-style:normal;color:#4767FA}
.hero-t.sm2{font-size:76px}
.hero-s{color:#9C9CA6;font-size:30px;margin-top:44px;letter-spacing:.02em}
.hero-s2{color:#9C9CA6;font-size:32px;margin-top:50px}

.mod-tile{width:170px;height:170px;border-radius:42px;display:flex;align-items:center;justify-content:center;margin-bottom:56px}
.mod-tile svg{width:92px;height:92px}
.mod-t{font-family:"Poppins";font-weight:700;font-size:110px;line-height:1;color:#F1F1F2}
.mod-t em{font-style:normal}
.mod-v{font-family:"Poppins";font-weight:600;font-size:34px;letter-spacing:.34em;text-transform:uppercase;margin-top:26px}
.mod-d{color:#C9CAD4;font-size:40px;line-height:1.4;max-width:82%;margin-top:48px}
.mod-d2{color:#C9CAD4;font-size:38px;line-height:1.45;max-width:86%;margin-top:46px}
.mod-strip{display:flex;gap:14px;margin-top:66px}
.mod-strip i{width:74px;height:14px;border-radius:8px}
.sl-top{position:absolute;top:70px;right:80px}
.sl-n{font-family:"Poppins";font-weight:700;font-size:34px}

.foot{position:absolute;bottom:64px;left:0;right:0;display:flex;flex-direction:column;align-items:center;gap:16px}
.foot .fl{width:230px}
.foot span{color:#5d5e6c;font-size:22px}
</style></head><body>
''' + arts_html + '''
</body></html>'''
open('social.html', 'w').write(html)

names = [n for n, _, _ in arts]
open('social_names.txt', 'w').write(chr(10).join(names))
print('social.html com', len(arts), 'peças')
