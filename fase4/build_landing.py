# -*- coding: utf-8 -*-
"""Página 'Conheça o ONE' (item 4.7) — HTML autocontido para o site da GrowUp."""
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
    fontcss += f'@font-face{{font-family:"{fam}";font-weight:{w};font-display:swap;src:url(data:font/woff2;base64,{b64(F+"/"+f)}) format("woff2")}}\n'

logo_off = load('one-by-growup_principal_offwhite.svg')
appicon = load('one_appicon.svg')

MODS = [
    ('nexa','Nexa','#DE571B','atrai','Sua operação de marketing completa — sem agência.',
     '<path d="M4 10.5v3l3 .6L19 19V5L7 9.9l-3 .6z"/><path d="M8.5 15l1 4"/>','stroke'),
    ('sales','Sales','#4767FA','converte','Do lead ao fechamento, um funil que vende.',
     '<path d="M4 5h16l-6 7v5.5L10 15v-3L4 5z"/>','stroke'),
    ('profit','Profit','#5E8C54','lucra','Vendas, receitas e despesas sob controle — lucro à vista.',
     '<path d="M4 17l5-5 4 3 7-7"/><path d="M15 8h5v5"/>','stroke'),
    ('flow','Flow','#3A50D2','executa','Projetos, tarefas e processos rodando no ritmo certo.',
     '<rect x="3.5" y="5" width="12" height="3.2" rx="1.6"/><rect x="8.5" y="10.4" width="12" height="3.2" rx="1.6"/><rect x="3.5" y="15.8" width="8" height="3.2" rx="1.6"/>','fill'),
    ('north','North','#2E8FA3','dá o norte','Os números que dão o norte das suas decisões.',
     '<circle cx="12" cy="12" r="8.6" fill="none"/><path d="M15.6 8.4l-2.4 4.8-4.8 2.4 2.4-4.8 4.8-2.4z" class="f"/>','mixed'),
    ('growth','Growth','#7B4FE0','acelera','Inteligência e agentes de IA trabalhando pelo seu crescimento.',
     '<path d="M12 2.6l2.1 6 6 2.1-6 2.1-2.1 6-2.1-6-6-2.1 6-2.1 2.1-6z"/>','fill'),
]

def icon(ic, mode, cor):
    if mode == 'stroke':
        inner = f'<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ic}</g>'
    elif mode == 'fill':
        inner = f'<g fill="#fff">{ic}</g>'
    else:
        fixed = ic.replace('class="f"', 'fill="#fff" stroke="none"')
        inner = f'<g fill="none" stroke="#fff" stroke-width="2">{fixed}</g>'
    return f'<svg viewBox="0 0 24 24">{inner}</svg>'

cards = '\n'.join(f'''
      <div class="mcard" style="--mc:{cor}">
        <div class="mtile" style="background:{cor}">{icon(ic, mode, cor)}</div>
        <h3>{nome} <em style="color:{cor}">One</em></h3>
        <span class="verb" style="color:{cor}">{verbo}</span>
        <p>{desc}</p>
      </div>''' for slug, nome, cor, verbo, desc, ic, mode in MODS)

html = '''<title>ONE by GrowUp — Todo o seu negócio em um.</title>
<style>
''' + fontcss + '''
*{box-sizing:border-box;margin:0}
:root{--ink:#141414;--muted:#6C6C70;--blue:#4767FA;--deep:#3A50D2}
body{font-family:"Manrope",system-ui,sans-serif;color:var(--ink);background:#F8F8FA;line-height:1.6}
.dark-sec{background:#101014;color:#F1F1F2}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}

/* hero */
.hero{padding:90px 0 100px;text-align:center;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;left:0;right:0;bottom:0;height:5px;background:linear-gradient(90deg,#DE571B,#4767FA,#7B4FE0,#5E8C54,#3A50D2,#2E8FA3)}
.hero .logo{width:min(400px,70vw);margin:0 auto 40px}
.hero h1{font-family:"Poppins";font-weight:700;font-size:clamp(34px,6vw,58px);line-height:1.12;letter-spacing:-.01em}
.hero h1 em{font-style:normal;color:var(--blue)}
.hero p{color:#9C9CA6;font-size:clamp(15px,2.4vw,19px);margin-top:18px;max-width:56ch;margin-left:auto;margin-right:auto}
.cta{display:inline-block;background:var(--blue);color:#fff;font-family:"Poppins";font-weight:600;font-size:17px;border-radius:13px;padding:16px 38px;margin-top:38px;text-decoration:none;transition:transform .15s,box-shadow .15s}
.cta:hover{transform:translateY(-2px);box-shadow:0 12px 30px #4767FA55}

/* dor */
.dor{padding:80px 0;text-align:center}
.dor h2{font-family:"Poppins";font-weight:700;font-size:clamp(24px,4vw,36px);max-width:22ch;margin:0 auto}
.chips{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;max-width:640px;margin:34px auto 0}
.chips span{background:#fff;border:1.5px solid #E2E2E6;color:var(--muted);font-size:14.5px;padding:9px 20px;border-radius:99px;transform:rotate(var(--r,0deg))}
.dor .resp{margin-top:36px;color:var(--muted);font-size:16px}
.dor .resp b{color:var(--ink)}

/* módulos */
.mods{padding:30px 0 90px}
.mods h2{font-family:"Poppins";font-weight:700;font-size:clamp(24px,4vw,34px);text-align:center;margin-bottom:10px}
.mods .sub{text-align:center;color:var(--muted);margin-bottom:44px}
.mgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}
.mcard{background:#fff;border:1px solid #E7E7EB;border-top:4px solid var(--mc);border-radius:16px;padding:28px;transition:transform .15s,box-shadow .15s}
.mcard:hover{transform:translateY(-4px);box-shadow:0 18px 44px rgba(20,20,20,.09)}
.mtile{width:56px;height:56px;border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:18px}
.mtile svg{width:30px;height:30px}
.mcard h3{font-family:"Poppins";font-weight:700;font-size:23px}
.mcard h3 em{font-style:normal}
.verb{font-family:"Poppins";font-weight:600;font-size:12px;letter-spacing:.22em;text-transform:uppercase;display:block;margin:4px 0 12px}
.mcard p{color:var(--muted);font-size:14.5px}

/* ecossistema */
.eco{padding:80px 0;text-align:center}
.eco .appic{width:86px;margin:0 auto 26px}
.eco h2{font-family:"Poppins";font-weight:700;font-size:clamp(24px,4vw,34px)}
.eco p{color:#9C9CA6;max-width:62ch;margin:16px auto 0;font-size:16px}
.eco .chain{margin-top:36px;font-family:"Poppins";font-weight:600;font-size:clamp(16px,3vw,22px);display:flex;gap:18px;justify-content:center;align-items:center;flex-wrap:wrap}
.eco .chain i{color:#5b5c6b;font-style:normal}

/* cta final */
.final{padding:90px 0;text-align:center}
.final .logo{width:min(340px,60vw);margin:0 auto 34px}
.final h2{font-family:"Poppins";font-weight:700;font-size:clamp(24px,4.4vw,38px)}
.final .url{color:#5d5e6c;margin-top:26px;font-size:15px}
footer{background:#0C0D11;color:#5d5e6c;text-align:center;padding:26px;font-size:13px}
</style>

<section class="dark-sec hero">
  <div class="wrap">
    <div class="logo">''' + logo_off + '''</div>
    <h1>Todo o seu negócio<br>em <em>um</em>.</h1>
    <p>CRM, financeiro, operação, relatórios, marketing e IA — a plataforma da GrowUp que substitui a sua colcha de retalhos de ferramentas.</p>
    <a class="cta" href="#contato">Fale com a GrowUp</a>
  </div>
</section>

<section class="dor">
  <div class="wrap">
    <h2>Quantas ferramentas você paga para gerir seu negócio?</h2>
    <div class="chips">
      <span style="--r:-3deg">CRM</span><span style="--r:2deg">planilhas</span><span style="--r:-2deg">agência de marketing</span>
      <span style="--r:3deg">gestor de tarefas</span><span style="--r:-1deg">financeiro</span><span style="--r:2deg">BI / relatórios</span>
      <span style="--r:-3deg">disparos WhatsApp</span><span style="--r:1deg">landing pages</span>
    </div>
    <p class="resp">Mensalidades somadas, dados espalhados, ninguém enxergando o todo.<br><b>O ONE resolve com um único sistema — e o método GrowUp embutido.</b></p>
  </div>
</section>

<section class="mods">
  <div class="wrap">
    <h2>Seis módulos, um ciclo de crescimento</h2>
    <p class="sub">Nexa atrai → Sales converte → Profit lucra → Flow executa → North dá o norte → Growth acelera.</p>
    <div class="mgrid">''' + cards + '''
    </div>
  </div>
</section>

<section class="dark-sec eco">
  <div class="wrap">
    <div class="appic">''' + appicon + '''</div>
    <h2>Não é um software. É um ecossistema.</h2>
    <p>O ONE é o método GrowUp em forma de plataforma: os funis, réguas, diagnósticos e planos que a consultoria aplica nos clientes — prontos, dentro do seu sistema, com IA trabalhando 24/7.</p>
    <div class="chain"><span>growup</span><i>→</i><span>one</span><i>→</i><span>o seu crescimento</span></div>
  </div>
</section>

<section class="final" id="contato">
  <div class="wrap">
    <div class="logo" style="filter:none">''' + load('one-by-growup_principal_azul.svg') + '''</div>
    <h2>Vamos colocar o seu negócio em um?</h2>
    <a class="cta" href="https://sistema.grow2up.com.br">Fale com a GrowUp</a>
    <p class="url">sistema.grow2up.com.br</p>
  </div>
</section>

<footer>ONE by GrowUp · O método GrowUp em forma de plataforma. © GrowUp</footer>
'''
open('landing-conheca-o-one.html', 'w').write(html)
print('landing:', len(html)//1024, 'KB')
