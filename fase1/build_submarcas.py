# -*- coding: utf-8 -*-
"""Gera as sub-marcas dos 6 Ones (lockup: tile+ícone+nome) e o Selo ONE.
Texto vetorizado em Poppins (OFL) via fonttools — sem dependência de fonte no arquivo final.
"""
import math, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

FONT = 'node_modules/@fontsource/poppins/files/poppins-latin-600-normal.woff2'
OUT = '/home/user/Growup_sis/fase1/kit'
os.makedirs(OUT, exist_ok=True)

font = TTFont(FONT)
glyphset = font.getGlyphSet()
cmap = font.getBestCmap()
UPM = font['head'].unitsPerEm  # 1000 típico

def glyph_path(ch):
    gname = cmap[ord(ch)]
    pen = SVGPathPen(glyphset)
    glyphset[gname].draw(pen)
    return pen.getCommands(), glyphset[gname].width

def text_paths(text, size):
    """Retorna [(d, dx)] e largura total; coordenadas y invertidas p/ SVG."""
    s = size / UPM
    x = 0.0
    items = []
    for ch in text:
        if ch == ' ':
            x += 0.30 * size
            continue
        d, adv = glyph_path(ch)
        items.append((d, x, s))
        x += adv * s
    return items, x

def text_svg_group(text, size, fill, x0=0, y0=0):
    items, w = text_paths(text, size)
    g = []
    for d, dx, s in items:
        g.append(f'<path transform="translate({x0+dx:.1f},{y0:.1f}) scale({s:.5f},-{s:.5f})" fill="{fill}" d="{d}"/>')
    return '\n'.join(g), w

MODULES = [
    ('nexa',   'Nexa',   '#DE571B', '<path d="M4 10.5v3l3 .6L19 19V5L7 9.9l-3 .6z"/><path d="M8.5 15l1 4"/>', 'stroke'),
    ('sales',  'Sales',  '#4767FA', '<path d="M4 5h16l-6 7v5.5L10 15v-3L4 5z"/>', 'stroke'),
    ('growth', 'Growth', '#7B4FE0', '<path d="M12 2.6l2.1 6 6 2.1-6 2.1-2.1 6-2.1-6-6-2.1 6-2.1 2.1-6z"/>', 'fill'),
    ('profit', 'Profit', '#5E8C54', '<path d="M4 17l5-5 4 3 7-7"/><path d="M15 8h5v5"/>', 'stroke'),
    ('flow',   'Flow',   '#3A50D2', '<rect x="3.5" y="5" width="12" height="3.2" rx="1.6"/><rect x="8.5" y="10.4" width="12" height="3.2" rx="1.6"/><rect x="3.5" y="15.8" width="8" height="3.2" rx="1.6"/>', 'fill'),
    ('north',  'North',  '#2E8FA3', '<circle cx="12" cy="12" r="8.6" fill="none"/><path d="M15.6 8.4l-2.4 4.8-4.8 2.4 2.4-4.8 4.8-2.4z" class="f"/>', 'mixed'),
]

# ---------- lockups ----------
TILE = 64; ICON = 34; SIZE = 44; GAP = 18
for slug, name, color, icon, mode in MODULES:
    # texto: "Nexa " em ink, "One" na cor
    g1, w1 = text_svg_group(name + ' ', SIZE, '#141414')
    g2, w2 = text_svg_group('One', SIZE, color)
    text_h = SIZE
    H = TILE
    ty = H/2 + SIZE*0.36  # baseline aproximada centralizada
    tx = TILE + GAP
    total_w = tx + w1 + w2 + 6
    if mode == 'stroke':
        icon_svg = f'<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon}</g>'
    elif mode == 'fill':
        icon_svg = f'<g fill="#fff" stroke="none">{icon}</g>'
    else:
        icon_fixed = icon.replace('class="f"', 'fill="#fff" stroke="none"')
        icon_svg = f'<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon_fixed}</g>'
    isc = ICON/24
    ioff = (TILE-ICON)/2
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w:.0f} {H}">
<rect width="{TILE}" height="{TILE}" rx="16" fill="{color}"/>
<g transform="translate({ioff},{ioff}) scale({isc:.3f})">{icon_svg}</g>
<g transform="translate({tx},{ty})">
{text_svg_group(name + ' ', SIZE, '#141414', 0, 0)[0]}
{text_svg_group('One', SIZE, color, w1, 0)[0]}
</g>
</svg>'''
    open(f'{OUT}/submarca_{slug}-one.svg', 'w').write(svg)
    # variante para fundo escuro (texto off-white)
    svg_dark = svg.replace('fill="#141414"', 'fill="#F1F1F1"')
    open(f'{OUT}/submarca_{slug}-one_dark.svg', 'w').write(svg_dark)

# ---------- selo ----------
# círculo de texto "ONE BY GROWUP · " x3 + monograma central
import re
mono_d = None
src = open(f'{OUT}/one_appicon.svg').read()
ds = re.findall(r'd="([^"]+)"', src)
mono_d = max(ds, key=len)

SELO = 640
R_TEXT = 252
FSIZE = 54
phrase = 'ONE BY GROWUP · '
# largura de cada char para distribuir por arco
def char_w(ch, size):
    if ch == ' ':
        return 0.30*size
    _, adv = glyph_path(ch)
    return adv * size / UPM

text_full = phrase * 3
widths = [char_w(c, FSIZE) for c in text_full]
total_arc = sum(widths)
circ = 2*math.pi*R_TEXT
scale_fit = circ / total_arc  # ajusta tracking para fechar o círculo
widths = [w*scale_fit for w in widths]

parts = []
theta = -math.pi/2  # começa no topo
cx = cy = SELO/2
for ch, w in zip(text_full, widths):
    dtheta = w / R_TEXT
    if ch != ' ' and ch != '·':
        mid = theta + dtheta/2
        deg = math.degrees(mid) + 90
        px = cx + R_TEXT*math.cos(mid)
        py = cy + R_TEXT*math.sin(mid)
        d, adv = glyph_path(ch)
        s = FSIZE/UPM
        gw = adv*s
        parts.append(f'<g transform="translate({px:.1f},{py:.1f}) rotate({deg:.1f})"><path transform="translate({-gw/2:.1f},0) scale({s:.5f},-{s:.5f})" fill="#3A50D2" d="{d}"/></g>')
    elif ch == '·':
        mid = theta + dtheta/2
        px = cx + R_TEXT*math.cos(mid)
        py = cy + R_TEXT*math.sin(mid) - FSIZE*0.32
        parts.append(f'<circle cx="{px:.1f}" cy="{py+FSIZE*0.32:.1f}" r="5.5" fill="#4767FA"/>')
    theta += dtheta

# monograma central (bbox do monograma do logo horizontal)
MX0, MY0, MW, MH = 668.2, 62.5, 112.5, 86.3
msc = SELO*0.42/MW
mtx = (SELO - MW*msc)/2 - MX0*msc
mty = (SELO - MH*msc)/2 - MY0*msc
selo = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SELO} {SELO}">
{chr(10).join(parts)}
<path transform="translate({mtx:.1f},{mty:.1f}) scale({msc:.4f})" fill="#4767FA" fill-rule="evenodd" d="{mono_d}"/>
</svg>'''
open(f'{OUT}/one_selo.svg', 'w').write(selo)

# selo com fundo preto (offwhite/azul)
selo_dark = selo.replace('fill="#3A50D2"', 'fill="#F1F1F1"')
selo_dark = selo_dark.replace(f'viewBox="0 0 {SELO} {SELO}">',
    f'viewBox="0 0 {SELO} {SELO}"><circle cx="{SELO/2}" cy="{SELO/2}" r="{SELO/2}" fill="#141414"/>')
open(f'{OUT}/one_selo_dark.svg', 'w').write(selo_dark)

print('sub-marcas e selo gerados')
