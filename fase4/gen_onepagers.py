# -*- coding: utf-8 -*-
"""One-pagers dos 6 módulos do ONE by GrowUp (A4, PDF) — Fase 4B item 4.6."""
import os
from fontTools.ttLib import TTFont as FT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

OUT = '/home/user/Growup_sis/fase4/onepagers'
os.makedirs(OUT, exist_ok=True)
FDIR = 'fonts_ttf'
os.makedirs(FDIR, exist_ok=True)

# converte woff2 -> ttf
F = 'node_modules/@fontsource'
for fam, w, src in [('Poppins','600','poppins/files/poppins-latin-600-normal.woff2'),
                    ('Poppins','700','poppins/files/poppins-latin-700-normal.woff2'),
                    ('Manrope','400','manrope/files/manrope-latin-400-normal.woff2'),
                    ('Manrope','700','manrope/files/manrope-latin-700-normal.woff2')]:
    dst = f'{FDIR}/{fam}-{w}.ttf'
    if not os.path.exists(dst):
        f = FT(f'{F}/{src}')
        f.flavor = None
        f.save(dst)
pdfmetrics.registerFont(TTFont('Poppins-SB', f'{FDIR}/Poppins-600.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-B', f'{FDIR}/Poppins-700.ttf'))
pdfmetrics.registerFont(TTFont('Manrope', f'{FDIR}/Manrope-400.ttf'))
pdfmetrics.registerFont(TTFont('Manrope-B', f'{FDIR}/Manrope-700.ttf'))

INK = HexColor('#141414'); MUTED = HexColor('#6C6C70'); PAPER = HexColor('#F8F8FA')
BLUE = HexColor('#4767FA'); DARKBG = HexColor('#101014')
LOGO_OFF = ImageReader('/home/user/Growup_sis/fase1/kit/one-by-growup_principal_offwhite@2000.png')
LOGO_AZ = ImageReader('/home/user/Growup_sis/fase1/kit/one-by-growup_principal_azul@2000.png')

MODS = [
 ('nexa','Nexa','#DE571B','ATRAI','Sua operação de marketing completa — sem agência.',
  ['Campanhas e auditorias de marketing com relatórios gerados por IA',
   'Landing pages e páginas de captura integradas direto ao funil',
   'Diagnóstico de marketing público que gera leads sozinho',
   'Planejamento de conteúdo e mídia paga dentro do sistema',
   'Automação de disparos e réguas de relacionamento'],
  'Para quem paga agência e não vê resultado — ou faz tudo na mão.'),
 ('sales','Sales','#4767FA','CONVERTE','Do lead ao fechamento, um funil que vende.',
  ['Pipeline Kanban visual com estágios configuráveis',
   'Leads do Meta Ads caindo automaticamente no funil',
   'Réguas de follow-up automáticas por WhatsApp',
   'Checklist, documentos e scripts por lead',
   'Análise do funil por IA apontando onde vaza dinheiro'],
  'Para quem perde negócio por falta de follow-up e visibilidade.'),
 ('profit','Profit','#5E8C54','LUCRA','Vendas, receitas e despesas sob controle — lucro à vista.',
  ['Vendas, receitas, despesas e metas sem planilha',
   'Importação de despesas por PDF com leitura por IA',
   'Mapa do Brasil com faturamento por estado',
   'Relatórios por cliente e por fornecedor',
   'Comparativos anuais de receita e despesa'],
  'Para quem só descobre o lucro (ou o prejuízo) no fim do mês.'),
 ('flow','Flow','#3A50D2','EXECUTA','Projetos, tarefas e processos rodando no ritmo certo.',
  ['Projetos e tarefas em Kanban, Gantt e timeline',
   'Editor de mapas de processos (BPMN, SWOT, organogramas)',
   'Avaliação de desempenho da equipe integrada',
   'Compartilhamento de projetos com o cliente final',
   'Gestão de custo por hora de cada membro'],
  'Para quem tem a operação no WhatsApp e os processos na cabeça.'),
 ('north','North','#2E8FA3','DÁ O NORTE','Os números que dão o norte das suas decisões.',
  ['Conversão, receita e funil em dashboards vivos',
   'Visão consolidada de todos os módulos do ONE',
   'Relatórios prontos para reunião de diretoria',
   'Histórico e tendências sem montar planilha',
   'Exportação para apresentações e PDFs'],
  'Para quem decide no feeling porque os números nunca estão prontos.'),
 ('growth','Growth','#7B4FE0','ACELERA','Inteligência e agentes de IA trabalhando pelo seu crescimento.',
  ['Agentes de IA comercial, de marketing e de processos',
   'Diagnósticos de maturidade com recomendações práticas',
   'Planejamento estratégico: SWOT, GPD, canvas e personas',
   'Base de prospecção com listas e exportação',
   'Questionários de cliente com link público'],
  'Para quem quer um time de inteligência sem contratar um time.'),
]

W, H = A4  # 595 x 842

for slug, nome, cor, verbo, desc, feats, quem in MODS:
    C = HexColor(cor)
    c = canvas.Canvas(f'{OUT}/onepager_{slug}-one.pdf', pagesize=A4)
    # fundo
    c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)
    # header dark
    c.setFillColor(DARKBG); c.rect(0, H-150, W, 150, fill=1, stroke=0)
    c.setFillColor(C); c.rect(0, H-150, W, 4, fill=1, stroke=0)
    c.drawImage(LOGO_OFF, 40, H-100, width=120, height=120*175/403, mask='auto')
    c.setFont('Manrope', 9); c.setFillColor(HexColor('#9C9CA6'))
    c.drawRightString(W-40, H-60, 'O método GrowUp em forma de plataforma.')
    # tile do módulo
    c.setFillColor(C)
    c.roundRect(40, H-260, 64, 64, 14, fill=1, stroke=0)
    # nome
    c.setFillColor(INK); c.setFont('Poppins-B', 40)
    nome_w = c.stringWidth(nome + ' ', 'Poppins-B', 40)
    c.drawString(120, H-238, nome)
    c.setFillColor(C); c.drawString(120 + nome_w, H-238, 'One')
    c.setFont('Poppins-SB', 12); c.setFillColor(C)
    c.drawString(122, H-258, ' '.join(verbo))
    # descritor
    c.setFillColor(INK); c.setFont('Manrope-B', 14)
    c.drawString(40, H-300, desc)
    # features
    y = H - 345
    c.setFont('Manrope', 11.5)
    for f in feats:
        c.setFillColor(C); c.circle(48, y+4, 2.6, fill=1, stroke=0)
        c.setFillColor(HexColor('#3a3a40'))
        c.drawString(60, y, f)
        y -= 26
    # bloco "para quem"
    c.setFillColor(white); c.roundRect(40, y-74, W-80, 62, 10, fill=1, stroke=0)
    c.setFillColor(C); c.setFont('Poppins-SB', 10)
    c.drawString(56, y-36, 'PARA QUEM É')
    c.setFillColor(HexColor('#3a3a40')); c.setFont('Manrope', 11.5)
    c.drawString(56, y-56, quem)
    # ecossistema
    ys = y - 120
    c.setFillColor(MUTED); c.setFont('Manrope', 10)
    c.drawString(40, ys, 'Parte do ONE by GrowUp — junto com:')
    outros = [m for m in MODS if m[0] != slug]
    x = 40; ys2 = ys - 26
    for oslug, onome, ocor, *_ in outros:
        oc = HexColor(ocor)
        c.setFillColor(oc); c.roundRect(x, ys2-4, 10, 10, 3, fill=1, stroke=0)
        c.setFillColor(HexColor('#3a3a40')); c.setFont('Manrope-B', 9.5)
        label = onome + ' One'
        c.drawString(x+15, ys2-2, label)
        x += 20 + c.stringWidth(label, 'Manrope-B', 9.5) + 18
    # rodapé CTA
    c.setFillColor(DARKBG); c.rect(0, 0, W, 84, fill=1, stroke=0)
    c.setFillColor(BLUE); c.roundRect(40, 22, 150, 38, 9, fill=1, stroke=0)
    c.setFillColor(white); c.setFont('Poppins-SB', 12)
    c.drawCentredString(115, 35, 'Fale com a GrowUp')
    c.setFillColor(HexColor('#9C9CA6')); c.setFont('Manrope', 10)
    c.drawRightString(W-40, 36, 'sistema.grow2up.com.br')
    c.save()
    print('ok', slug)

print('one-pagers gerados em', OUT)
