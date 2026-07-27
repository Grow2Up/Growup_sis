# -*- coding: utf-8 -*-
"""Constrói o kit vetorial ONE by GrowUp a partir das letras oficiais do wordmark growup.

Letras oficiais: g r o w u p + monograma (LOGO HORIZONTAL/SVG/04.svg)
Derivadas na mesma anatomia: n (u espelhado), b (p rotacionado 180°),
y (u + descendente), e (construída com as métricas do o).
"""
import numpy as np
from svgpathtools import svg2paths2, Path, parse_path
from shapely.geometry import Polygon, MultiPolygon, box
from shapely.ops import unary_union
import shapely.affinity as aff

SRC = '/home/user/Growup_sis/brand/PACOTE DA MARCA/LOGO HORIZONTAL/SVG/04.svg'
OUT = '/home/user/Growup_sis/fase1/kit'
import os
os.makedirs(OUT, exist_ok=True)

paths, attrs, svg_att = svg2paths2(SRC)
L = {'g': paths[5], 'r': paths[0], 'o': paths[1], 'w': paths[2],
     'u': paths[3], 'p': paths[4], 'mono': paths[6]}

BASELINE = 149.9   # baseline comum (o=149.7, r=150, u=148.8)
XH_TOP = 62.0      # topo da altura-x

# ---------- helpers ----------

def path_to_polys(p, n=140):
    """Amostra um Path (com subpaths) para polígonos shapely (even-odd)."""
    subs = p.continuous_subpaths()
    rings = []
    for s in subs:
        pts = [s.point(t) for t in np.linspace(0, 1, n)]
        rings.append(Polygon([(pt.real, pt.imag) for pt in pts]))
    # even-odd: maior = exterior, contidos = furos
    rings.sort(key=lambda r: r.area, reverse=True)
    outer = rings[0]
    holes = [r for r in rings[1:] if outer.contains(r.representative_point())]
    others = [r for r in rings[1:] if not outer.contains(r.representative_point())]
    poly = Polygon(outer.exterior.coords, [h.exterior.coords for h in holes])
    if others:
        poly = unary_union([poly] + others)
    return poly


def poly_to_d(poly, prec=1):
    """Converte shapely (Multi)Polygon em path data SVG (even-odd)."""
    if isinstance(poly, MultiPolygon):
        geoms = list(poly.geoms)
    else:
        geoms = [poly]
    parts = []
    for g in geoms:
        for ring in [g.exterior] + list(g.interiors):
            pts = list(ring.coords)
            d = 'M' + ' '.join(f'{x:.{prec}f},{y:.{prec}f}' for x, y in pts[:-1]) + 'z'
            parts.append(d)
    return ' '.join(parts)


def transform_path(p, sx=1, sy=1, rot=None, dx=0, dy=0, about=None):
    """Aplica escala/rotação/translação a um Path svgpathtools."""
    q = p
    if about is None:
        xmin, xmax, ymin, ymax = p.bbox()
        about = complex((xmin+xmax)/2, (ymin+ymax)/2)
    if sx != 1 or sy != 1:
        q = q.scaled(sx, sy, origin=about)
    if rot:
        q = q.rotated(rot, origin=about)
    if dx or dy:
        q = q.translated(complex(dx, dy))
    return q


def path_d(p, prec=2):
    return p.d()

# ---------- letras derivadas ----------
# n = u espelhado verticalmente (mesma caixa)
n_path = transform_path(L['u'], rot=180)

# b = p rotacionado 180°, elevado para a baseline
b_path = transform_path(L['p'], sy=-1)
bxmin, bxmax, bymin, bymax = b_path.bbox()
b_path = b_path.translated(complex(0, BASELINE - bymax))

# y = u + descendente no stem direito (profundidade do p)
u_poly = path_to_polys(L['u'])
uxmin, uxmax, uymin, uymax = L['u'].bbox()
P_DESC = 193.4  # profundidade do descendente do p
stem_w = 34.0
tail = box(uxmax - stem_w, BASELINE - 10, uxmax, P_DESC)
y_poly = unary_union([u_poly, tail])

# e = construída com métricas do o
oxmin, oxmax, oymin, oymax = L['o'].bbox()
ow, oh = oxmax - oxmin, oymax - oymin          # 99.2 x 86.9
cx, cy = ow/2, oh/2
outer = aff.scale(Polygon([(np.cos(t), np.sin(t)) for t in np.linspace(0, 2*np.pi, 200)]),
                  ow/2, oh/2, origin=(0, 0))
outer = aff.translate(outer, cx, cy)
# contra-forma superior (eco do miolo do o: 29.8 x 33.7 -> metade superior)
up_counter = aff.scale(Polygon([(np.cos(t), np.sin(t)) for t in np.linspace(0, 2*np.pi, 120)]),
                       15.0, 9.0, origin=(0, 0))
up_counter = aff.translate(up_counter, cx, cy - 11.5)
# abertura inferior-direita (fenda diagonal, eco do corte do o oficial)
slot = Polygon([(cx - 8.0, cy + 3.5), (ow + 2, cy + 3.5), (ow + 2, cy + 21.5), (cx - 8.0, cy + 21.5)])
slot = aff.rotate(slot, -12, origin=(cx, cy))
e_poly = outer.difference(up_counter).difference(slot)
# posiciona a e na baseline
e_poly = aff.translate(e_poly, 0, BASELINE - oh)  # topo = BASELINE-oh => bottom=BASELINE

# ---------- normalização: cada glifo com d + bbox ----------
class G:
    def __init__(self, d, bbox):
        self.d = d; self.xmin, self.xmax, self.ymin, self.ymax = bbox
    @property
    def w(self): return self.xmax - self.xmin

def from_path(p):
    return G(p.d(), p.bbox())

def from_poly(poly):
    xmin, ymin, xmax, ymax = poly.bounds
    return G(poly_to_d(poly), (xmin, xmax, ymin, ymax))

GL = {k: from_path(v) for k, v in L.items()}
GL['n'] = from_path(n_path)
GL['b'] = from_path(b_path)
GL['y'] = from_poly(y_poly)
GL['e'] = from_poly(e_poly)

# ---------- composição ----------

def place(g, x):
    """Retorna (d transformado via translate, próximo x). Alinha xmin em x."""
    dx = x - g.xmin
    return (g.d, dx, x + g.w)

def compose(seq, gap=6.5, scale=1.0, x0=0.0):
    """seq: lista de nomes de glifo ou ('gap', v). Retorna lista (d, dx, dy=0) e largura."""
    items = []
    x = x0
    for it in seq:
        if isinstance(it, tuple):
            x += it[1]; continue
        g = GL[it]
        d, dx, x2 = place(g, x)
        items.append((d, dx))
        x = x2 + gap
    return items, x - gap

def group_svg(items, fill, extra_transform=''):
    inner = '\n'.join(f'  <path transform="translate({dx:.2f},0) {extra_transform}" fill="{fill}" fill-rule="evenodd" d="{d}"/>' for d, dx in items)
    return inner

# “one” + monograma
one_items, one_w = compose(['o', 'n', 'e'], gap=7)
mono_g = GL['mono']
MONO_GAP = 17
mono_dx = one_w + MONO_GAP - mono_g.xmin
total_main_w = one_w + MONO_GAP + mono_g.w

# assinatura "by growup" (escala 0.30) — b y + g r o w u p oficiais
SIG_SCALE = 0.30
# growup nas posições originais (preserva kerning oficial; g começa em 15.1)
G_X0 = GL['g'].xmin
grow_items = [(GL[k].d, -G_X0) for k in ['g','r','o','w','u','p']]
grow_w = GL['p'].xmax - G_X0
# b e y compostos antes, com espaço de palavra
by_items, by_w = compose(['b', 'y'], gap=7)
WORD_GAP = 26
sig_items = by_items + [(d, dx + by_w + WORD_GAP) for d, dx in grow_items]
sig_w = by_w + WORD_GAP + grow_w

# ---------- geração dos SVGs ----------
COLOR = {
    'azul':      {'letters': '#3A50D2', 'mono': '#4767FA'},
    'offwhite':  {'letters': '#F1F1F1', 'mono': '#4767FA'},
    'preto':     {'letters': '#141414', 'mono': '#141414'},
    'branco-total': {'letters': '#F1F1F1', 'mono': '#F1F1F1'},
}

# geometria vertical: wordmark ocupa y 16..193 (asc b/w até 16; desc até 193)
# assinatura abaixo: baseline principal 149.9; assinatura topo em 149.9+34
SIG_Y = BASELINE + 36            # deslocamento vertical da assinatura
VIEW_H = 260

for name, c in COLOR.items():
    parts = []
    parts.append(group_svg(one_items, c['letters']))
    parts.append(f'  <path transform="translate({mono_dx:.2f},0)" fill="{c["mono"]}" fill-rule="evenodd" d="{mono_g.d}"/>')
    # assinatura em grupo escalado
    sig_inner = group_svg(sig_items, c['letters'])
    parts.append(f'  <g transform="translate(0,{SIG_Y:.1f}) scale({SIG_SCALE})">\n{sig_inner}\n  </g>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-8 8 {total_main_w+16:.0f} {VIEW_H}">\n'
           + '\n'.join(parts) + '\n</svg>')
    open(f'{OUT}/one-by-growup_principal_{name}.svg', 'w').write(svg)

# app icon: monograma branco em quadrado azul arredondado
mono_d = mono_g.d
mw, mh = mono_g.w, mono_g.ymax - mono_g.ymin
S = 1024
scale_i = S * 0.56 / mw
tx = (S - mw * scale_i) / 2 - mono_g.xmin * scale_i
ty = (S - mh * scale_i) / 2 - mono_g.ymin * scale_i
appicon = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}">\n'
           f'  <rect width="{S}" height="{S}" rx="{S*0.235:.0f}" fill="#4767FA"/>\n'
           f'  <path transform="translate({tx:.1f},{ty:.1f}) scale({scale_i:.4f})" fill="#FFFFFF" fill-rule="evenodd" d="{mono_d}"/>\n'
           f'</svg>')
open(f'{OUT}/one_appicon.svg', 'w').write(appicon)

# versão vertical: "one"+mono em cima, assinatura centralizada embaixo
for name, c in [('azul', COLOR['azul']), ('offwhite', COLOR['offwhite'])]:
    parts = []
    parts.append(group_svg(one_items, c['letters']))
    parts.append(f'  <path transform="translate({mono_dx:.2f},0)" fill="{c["mono"]}" fill-rule="evenodd" d="{mono_g.d}"/>')
    sig_scaled_w = sig_w * SIG_SCALE
    sig_x = (total_main_w - sig_scaled_w) / 2
    sig_inner = group_svg(sig_items, c['letters'])
    parts.append(f'  <g transform="translate({sig_x:.1f},{SIG_Y:.1f}) scale({SIG_SCALE})">\n{sig_inner}\n  </g>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-8 8 {total_main_w+16:.0f} {VIEW_H}">\n'
           + '\n'.join(parts) + '\n</svg>')
    open(f'{OUT}/one-by-growup_vertical_{name}.svg', 'w').write(svg)

print('kit principal gerado em', OUT)
print('largura one+mono: %.1f  assinatura: %.1f' % (total_main_w, sig_w * SIG_SCALE))

