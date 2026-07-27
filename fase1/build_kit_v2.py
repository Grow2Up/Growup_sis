# -*- coding: utf-8 -*-
"""Kit v2 — wordmark fiel à Proposta A aprovada no Painel 1:
"one" minúsculo em desenho geométrico arredondado limpo (Poppins Bold em outlines)
+ monograma oficial + assinatura "BY GROWUP" em caps espaçadas.
"""
import os, re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from svgpathtools import svg2paths2

OUT = '/home/user/Growup_sis/fase1/kit'
os.makedirs(OUT, exist_ok=True)

# ---------- fontes ----------
F = 'node_modules/@fontsource'
f700 = TTFont(f'{F}/poppins/files/poppins-latin-700-normal.woff2')
f600 = TTFont(f'{F}/poppins/files/poppins-latin-600-normal.woff2')

def make_text(font, text, size, tracking=0.0):
    """Retorna [(d, dx, scale)], largura total. tracking em unidades de size."""
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); upm = font['head'].unitsPerEm
    s = size / upm
    x = 0.0; items = []
    for ch in text:
        if ch == ' ':
            x += 0.32 * size + tracking * size
            continue
        gname = cmap[ord(ch)]
        pen = SVGPathPen(gs); gs[gname].draw(pen)
        items.append((pen.getCommands(), x, s))
        x += gs[gname].width * s + tracking * size
    return items, x - (tracking * size if text else 0)

def group(items, fill, dx0=0, dy0=0):
    return '\n'.join(
        f'  <path transform="translate({dx0+dx:.2f},{dy0:.2f}) scale({s:.5f},-{s:.5f})" fill="{fill}" d="{d}"/>'
        for d, dx, s in items)

# ---------- monograma oficial ----------
paths, attrs, svg_att = svg2paths2('/home/user/Growup_sis/brand/PACOTE DA MARCA/LOGO HORIZONTAL/SVG/04.svg')
mono = paths[6]
mono_d = mono.d()
mxmin, mxmax, mymin, mymax = mono.bbox()
MW, MH = mxmax - mxmin, mymax - mymin  # 112.5 x 86.3

# ---------- métricas do wordmark ----------
SIZE = 130                      # tamanho do "one" (cap/x geral)
one_items, one_w = make_text(f700, 'one', SIZE, tracking=-0.012)
# altura-x do Poppins ~0.528*upm; queremos monograma alinhado à altura da caixa "one"
# baseline em y=0 (glifos desenham para cima com scale(-y))
X_HEIGHT = 0.528 * SIZE         # ~68.6
ASC = 0.75 * SIZE               # altura do 'e'/'o' arredondado ~ x-height; 'one' não tem ascendentes
# monograma escalado para bater com a altura-x (como no logo growup, mono ocupa a altura-x)
msc = X_HEIGHT / MH * 1.28      # levemente maior que a x-height (como no painel aprovado)
mono_h = MH * msc
MONO_GAP = 0.16 * SIZE

# assinatura BY GROWUP caps espaçadas (como aprovado)
SIG_SIZE = 0.175 * SIZE
sig_items, sig_w = make_text(f600, 'BY GROWUP', SIG_SIZE, tracking=0.24)
SIG_DY = 0.30 * SIZE            # distância abaixo da baseline

total_w = one_w + MONO_GAP + MW * msc
view_pad = 10
VB_X = -view_pad
VB_Y = -(X_HEIGHT * 1.32 + view_pad)          # topo
VB_W = total_w + 2 * view_pad
VB_H = X_HEIGHT * 1.32 + SIG_DY + SIG_SIZE * 1.1 + 2 * view_pad

COLOR = {
    'azul':         {'letters': '#3A50D2', 'mono': '#4767FA', 'sig': '#3A50D2'},
    'offwhite':     {'letters': '#F1F1F1', 'mono': '#4767FA', 'sig': '#F1F1F1'},
    'preto':        {'letters': '#141414', 'mono': '#141414', 'sig': '#141414'},
    'branco-total': {'letters': '#F1F1F1', 'mono': '#F1F1F1', 'sig': '#F1F1F1'},
}

def wordmark_svg(c, center_sig=False):
    parts = []
    parts.append(group(one_items, c['letters']))
    # monograma: base alinhada à baseline, sobe além da x-height
    mty = -(mono_h) ; mtx = one_w + MONO_GAP
    parts.append(f'  <g transform="translate({mtx:.2f},{mty:.2f}) scale({msc:.5f}) translate({-mxmin:.2f},{-mymin:.2f})"><path fill="{c["mono"]}" fill-rule="evenodd" d="{mono_d}"/></g>')
    sig_x = (total_w - sig_w) / 2 if center_sig else 2.0
    parts.append(group(sig_items, c['sig'], dx0=sig_x, dy0=SIG_DY + SIG_SIZE))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB_X:.1f} {VB_Y:.1f} {VB_W:.1f} {VB_H:.1f}">\n'
            + '\n'.join(parts) + '\n</svg>')

for name, c in COLOR.items():
    open(f'{OUT}/one-by-growup_principal_{name}.svg', 'w').write(wordmark_svg(c))
open(f'{OUT}/one-by-growup_vertical_azul.svg', 'w').write(wordmark_svg(COLOR['azul'], center_sig=True))
open(f'{OUT}/one-by-growup_vertical_offwhite.svg', 'w').write(wordmark_svg(COLOR['offwhite'], center_sig=True))

print('kit v2 gerado — largura total: %.1f, viewbox %.0fx%.0f' % (total_w, VB_W, VB_H))
