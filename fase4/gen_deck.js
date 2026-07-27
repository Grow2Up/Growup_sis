// Deck comercial ONE by GrowUp — pptxgenjs
const pptxgen = require('pptxgenjs');
const sharp = require('sharp');
const fs = require('fs');

const KIT = '/home/user/Growup_sis/fase1/kit';
const INK = '141414', PAPER = 'FFFFFF', DARK = '101014', MUTED = '6C6C70';
const BLUE = '4767FA', DEEP = '3A50D2';

const MODS = [
  { key:'nexa',  nome:'Nexa One',  cor:'DE571B', verbo:'ATRAI',      desc:'Sua operação de marketing completa — sem agência.',
    feats:['Campanhas e auditorias de marketing com relatórios gerados por IA','Landing pages e captura de leads integradas ao funil','Diagnóstico de marketing público que gera leads sozinho','Automação de conteúdo e mídia paga planejadas no sistema'],
    stat:['— 1', 'agência para pagar todo mês'] },
  { key:'sales', nome:'Sales One', cor:'4767FA', verbo:'CONVERTE',   desc:'Do lead ao fechamento, um funil que vende.',
    feats:['Pipeline Kanban visual com estágios do seu jeito','Leads do Meta Ads caindo direto no funil','Réguas de follow-up automáticas por WhatsApp','Análise do funil por IA apontando onde vaza dinheiro'],
    stat:['100%','dos leads em um só lugar'] },
  { key:'profit', nome:'Profit One', cor:'5E8C54', verbo:'LUCRA',    desc:'Vendas, receitas e despesas sob controle — lucro à vista.',
    feats:['Vendas, receitas, despesas e metas sem planilha','Importação de despesas por PDF com leitura por IA','Mapa do Brasil com faturamento por estado','Comparativos anuais e relatórios por cliente e fornecedor'],
    stat:['R$', 'cada real com origem e destino'] },
  { key:'flow',  nome:'Flow One',  cor:'3A50D2', verbo:'EXECUTA',    desc:'Projetos, tarefas e processos rodando no ritmo certo.',
    feats:['Projetos e tarefas em Kanban, Gantt e timeline','Editor de mapas de processos (BPMN, SWOT, organogramas)','Avaliação de desempenho da equipe integrada','Compartilhamento de projetos com o cliente final'],
    stat:['0','tarefas perdidas no WhatsApp'] },
  { key:'north', nome:'North One', cor:'2E8FA3', verbo:'DÁ O NORTE', desc:'Os números que dão o norte das suas decisões.',
    feats:['Conversão, receita e funil em dashboards vivos','Visão consolidada de todos os módulos','Relatórios prontos para reunião de diretoria','Histórico e tendências sem montar planilha'],
    stat:['1','tela para decidir com segurança'] },
  { key:'growth', nome:'Growth One', cor:'7B4FE0', verbo:'ACELERA',  desc:'Inteligência e agentes de IA trabalhando pelo seu crescimento.',
    feats:['Agentes de IA comercial, de marketing e de processos','Diagnósticos de maturidade com recomendações','Planejamento estratégico: SWOT, GPD, canvas e personas','Base de prospecção com listas e exportação'],
    stat:['24/7','IA trabalhando pelo negócio'] },
];

const ICONS = {
  nexa:  '<path d="M4 10.5v3l3 .6L19 19V5L7 9.9l-3 .6z" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M8.5 15l1 4" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
  sales: '<path d="M4 5h16l-6 7v5.5L10 15v-3L4 5z" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
  profit:'<path d="M4 17l5-5 4 3 7-7" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 8h5v5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
  flow:  '<g fill="#fff"><rect x="3.5" y="5" width="12" height="3.2" rx="1.6"/><rect x="8.5" y="10.4" width="12" height="3.2" rx="1.6"/><rect x="3.5" y="15.8" width="8" height="3.2" rx="1.6"/></g>',
  north: '<circle cx="12" cy="12" r="8.6" fill="none" stroke="#fff" stroke-width="2"/><path d="M15.6 8.4l-2.4 4.8-4.8 2.4 2.4-4.8 4.8-2.4z" fill="#fff"/>',
  growth:'<path d="M12 2.6l2.1 6 6 2.1-6 2.1-2.1 6-2.1-6-6-2.1 6-2.1 2.1-6z" fill="#fff"/>',
};

async function iconPng(key){
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="256" height="256">${ICONS[key]}</svg>`;
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return 'image/png;base64,' + buf.toString('base64');
}

(async () => {
  const icons = {};
  for (const m of MODS) icons[m.key] = await iconPng(m.key);

  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE'; // 13.33 x 7.5
  const W = 13.33, H = 7.5;
  const T = 'Poppins', B = 'Calibri';

  // ---------- 1. CAPA ----------
  let s = pres.addSlide();
  s.background = { color: DARK };
  s.addImage({ path: `${KIT}/one-by-growup_principal_offwhite@2000.png`, x: W/2-2.6, y: 1.7, w: 5.2, h: 5.2*175/403 });
  s.addText('Todo o seu negócio em um.', { x: 0, y: 4.5, w: W, h: 0.7, align: 'center', fontFace: T, fontSize: 28, bold: true, color: 'F1F1F2' });
  s.addText('Apresentação comercial · GrowUp', { x: 0, y: 5.35, w: W, h: 0.4, align: 'center', fontFace: B, fontSize: 14, color: '9C9CA6' });
  // faixa dos módulos na base
  const cores = MODS.map(m => m.cor);
  cores.forEach((c, i) => s.addShape('rect', { x: i*(W/6), y: H-0.12, w: W/6, h: 0.12, fill: { color: c } }));
  s.addNotes('Abertura: o ONE é a plataforma da GrowUp. Uma frase: todo o negócio em um só sistema.');

  // ---------- 2. A DOR ----------
  s = pres.addSlide();
  s.background = { color: PAPER };
  s.addText('Quantas ferramentas\nvocê paga para\ngerir seu negócio?', { x: 0.6, y: 0.55, w: 6.6, h: 2.3, fontFace: T, fontSize: 34, bold: true, color: INK, lineSpacing: 40 });
  const dores = [
    'CRM em uma ferramenta, financeiro em planilha',
    'Agência de marketing cara e fora do seu controle',
    'Tarefas no WhatsApp, processos na cabeça',
    'Relatórios montados à mão toda sexta-feira',
    'Nenhuma ferramenta conversa com a outra',
  ];
  s.addText(dores.map((d, i) => ({ text: d, options: { bullet: { code: '2022', indent: 14 }, breakLine: i < dores.length-1, paraSpaceAfter: 12 } })),
    { x: 0.65, y: 2.9, w: 6.2, h: 3.6, fontFace: B, fontSize: 16, color: '3a3a40' });
  // chips visuais à direita
  const chipData = [['CRM','7.9','1.2'],['planilhas','10.6','1.0'],['agência de mkt','8.6','2.2'],['gestor de tarefas','10.9','2.6'],['disparos WhatsApp','8.2','3.4'],['BI / relatórios','10.7','4.1'],['e-mail mkt','8.7','4.7'],['landing pages','10.3','5.5']];
  chipData.forEach(([lb, x, y], i) => {
    s.addShape('roundRect', { x: +x, y: +y, w: 2.0, h: 0.55, rectRadius: 0.27, fill: { color: 'F1F1F3' }, line: { color: 'D8D8DE', width: 1 }, rotate: (i%2? 4 : -4) });
    s.addText(lb, { x: +x, y: +y, w: 2.0, h: 0.55, align: 'center', fontFace: B, fontSize: 12, color: MUTED, rotate: (i%2? 4 : -4), margin: 0 });
  });
  s.addText('+ mensalidades somadas, dados espalhados, ninguém enxergando o todo.', { x: 7.9, y: 6.3, w: 4.9, h: 0.7, fontFace: B, italic: true, fontSize: 13, color: MUTED });

  // ---------- 3. A VIRADA ----------
  s = pres.addSlide();
  s.background = { color: DARK };
  s.addImage({ path: `${KIT}/one_appicon@512.png`, x: W/2-0.75, y: 1.15, w: 1.5, h: 1.5 });
  s.addText([
    { text: 'Todo o seu negócio em ', options: { color: 'F1F1F2' } },
    { text: 'um', options: { color: BLUE } },
    { text: '.', options: { color: 'F1F1F2' } },
  ], { x: 0, y: 3.0, w: W, h: 0.9, align: 'center', fontFace: T, fontSize: 40, bold: true });
  s.addText('ONE by GrowUp — o método GrowUp em forma de plataforma.', { x: 0, y: 4.05, w: W, h: 0.5, align: 'center', fontFace: B, fontSize: 17, color: '9C9CA6' });
  s.addText('CRM  ·  Financeiro  ·  Operação  ·  Relatórios  ·  Marketing  ·  IA', { x: 0, y: 5.15, w: W, h: 0.5, align: 'center', fontFace: T, fontSize: 15, bold: true, color: '6C6C78' });
  s.addNotes('A virada: em vez de N ferramentas, uma plataforma com o método da GrowUp embutido.');

  // ---------- 4. ECOSSISTEMA ----------
  s = pres.addSlide();
  s.background = { color: PAPER };
  s.addText('Não é um software. É um ecossistema.', { x: 0.6, y: 0.55, w: 12, h: 0.8, fontFace: T, fontSize: 32, bold: true, color: INK });
  // 3 níveis
  const lv = [
    ['growup', 'A consultoria: método, auditorias e gente que já acelerou dezenas de negócios', 'EDEDEF', INK],
    ['one', 'A plataforma: o método vira rotina diária dentro do seu sistema', 'E7EBFE', DEEP],
    ['6 módulos', 'Onde acontece: vendas, lucro, execução, norte, marketing e IA', 'F6F6F8', INK],
  ];
  lv.forEach(([t, d, bg, tc], i) => {
    const y = 1.75 + i*1.35;
    s.addShape('roundRect', { x: 0.8, y, w: 3.3, h: 1.0, rectRadius: 0.14, fill: { color: bg } });
    s.addText(t, { x: 0.8, y: y, w: 3.3, h: 1.0, align: 'center', fontFace: T, fontSize: 22, bold: true, color: tc, margin: 0 });
    s.addText(d, { x: 4.5, y: y+0.08, w: 5.6, h: 0.9, fontFace: B, fontSize: 14, color: '3a3a40', valign: 'middle' });
    if (i < 2) s.addText('↓', { x: 2.25, y: y+0.95, w: 0.4, h: 0.42, fontFace: B, fontSize: 20, color: 'B0B0B8', align: 'center', margin: 0 });
  });
  // grid de módulos à direita
  MODS.forEach((m, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 10.35 + col*1.42, y = 1.9 + row*1.42;
    s.addShape('roundRect', { x, y, w: 1.2, h: 1.2, rectRadius: 0.2, fill: { color: m.cor } });
    s.addImage({ data: icons[m.key], x: x+0.3, y: y+0.3, w: 0.6, h: 0.6 });
  });
  s.addText('Nexa · Sales · Profit · Flow · North · Growth', { x: 9.9, y: 6.35, w: 3.3, h: 0.6, align: 'center', fontFace: B, fontSize: 11, color: MUTED });

  // ---------- 5-10. MÓDULOS ----------
  for (const m of MODS) {
    s = pres.addSlide();
    s.background = { color: PAPER };
    s.addShape('roundRect', { x: 0.7, y: 0.7, w: 1.15, h: 1.15, rectRadius: 0.2, fill: { color: m.cor } });
    s.addImage({ data: icons[m.key], x: 0.985, y: 0.985, w: 0.58, h: 0.58 });
    s.addText([
      { text: m.nome.split(' ')[0] + ' ', options: { color: INK } },
      { text: 'One', options: { color: m.cor } },
    ], { x: 2.1, y: 0.68, w: 7.5, h: 0.85, fontFace: T, fontSize: 40, bold: true, margin: 0 });
    s.addText(m.verbo, { x: 2.13, y: 1.5, w: 7.5, h: 0.4, fontFace: T, fontSize: 14, bold: true, color: m.cor, charSpacing: 6, margin: 0 });
    s.addText(m.desc, { x: 0.72, y: 2.35, w: 7.3, h: 0.8, fontFace: B, fontSize: 19, italic: true, color: '3a3a40' });
    s.addText(m.feats.map((f, i) => ({ text: f, options: { bullet: { code: '2022', indent: 14 }, breakLine: i < m.feats.length-1, paraSpaceAfter: 14 } })),
      { x: 0.78, y: 3.35, w: 7.2, h: 3.3, fontFace: B, fontSize: 15.5, color: '3a3a40' });
    // stat callout
    s.addShape('roundRect', { x: 8.7, y: 2.35, w: 3.9, h: 3.4, rectRadius: 0.18, fill: { color: 'F6F6F8' } });
    s.addText(m.stat[0], { x: 8.7, y: 2.9, w: 3.9, h: 1.4, align: 'center', fontFace: T, fontSize: 60, bold: true, color: m.cor, margin: 0 });
    s.addText(m.stat[1], { x: 8.95, y: 4.4, w: 3.4, h: 0.9, align: 'center', fontFace: B, fontSize: 14, color: MUTED, margin: 0 });
    s.addText('ONE by GrowUp', { x: 0.72, y: 6.95, w: 4, h: 0.35, fontFace: T, fontSize: 10, bold: true, color: 'B0B0B8' });
  }

  // ---------- 11. NARRATIVA ----------
  s = pres.addSlide();
  s.background = { color: PAPER };
  s.addText('Seis módulos, um ciclo de crescimento', { x: 0.6, y: 0.6, w: 12, h: 0.8, fontFace: T, fontSize: 32, bold: true, color: INK });
  const ciclo = [['Nexa','atrai'],['Sales','converte'],['Profit','lucra'],['Flow','executa'],['North','dá o norte'],['Growth','acelera']];
  ciclo.forEach(([n, v], i) => {
    const m = MODS.find(x => x.nome.startsWith(n));
    const x = 0.62 + i*2.12, y = 3.0;
    s.addShape('roundRect', { x, y, w: 1.86, h: 1.75, rectRadius: 0.14, fill: { color: 'F6F6F8' } });
    s.addShape('roundRect', { x: x+0.6, y: y+0.22, w: 0.66, h: 0.66, rectRadius: 0.12, fill: { color: m.cor } });
    s.addImage({ data: icons[m.key], x: x+0.765, y: y+0.385, w: 0.33, h: 0.33 });
    s.addText(n, { x, y: y+0.92, w: 1.86, h: 0.4, align: 'center', fontFace: T, fontSize: 15, bold: true, color: INK, margin: 0 });
    s.addText(v, { x, y: y+1.28, w: 1.86, h: 0.35, align: 'center', fontFace: B, fontSize: 12, color: m.cor, margin: 0 });
    if (i < 5) s.addText('→', { x: x+1.8, y: y+0.62, w: 0.4, h: 0.5, fontFace: B, fontSize: 18, color: 'B0B0B8', align: 'center', margin: 0 });
  });
  s.addText('Cada módulo alimenta o próximo — e o Growth One, com IA, acelera o ciclo inteiro.', { x: 0.6, y: 5.5, w: 12, h: 0.5, fontFace: B, fontSize: 15, italic: true, color: MUTED, align: 'center' });

  // ---------- 12. POR QUE O ONE ----------
  s = pres.addSlide();
  s.background = { color: PAPER };
  s.addText('Por que o ONE — e não mais uma ferramenta', { x: 0.6, y: 0.6, w: 12.1, h: 0.8, fontFace: T, fontSize: 32, bold: true, color: INK });
  const cols = [
    ['Substitui a colcha de retalhos', 'CRM, financeiro, operação, relatórios e marketing em uma assinatura — menos custo, zero integração para manter.'],
    ['O método GrowUp embutido', 'Não é software vazio: funis, réguas, diagnósticos e planejamento chegam prontos, do jeito que a consultoria aplica.'],
    ['IA em todos os módulos', 'Agentes que analisam funil, geram relatórios, leem despesas em PDF e trabalham 24/7 pelo seu crescimento.'],
  ];
  cols.forEach(([t, d], i) => {
    const x = 0.7 + i*4.2;
    s.addShape('roundRect', { x, y: 1.9, w: 3.85, h: 3.9, rectRadius: 0.16, fill: { color: 'F6F6F8' } });
    s.addText(String(i+1), { x: x+0.35, y: 2.25, w: 0.8, h: 0.8, fontFace: T, fontSize: 34, bold: true, color: BLUE, margin: 0 });
    s.addText(t, { x: x+0.35, y: 3.05, w: 3.2, h: 0.95, fontFace: T, fontSize: 17, bold: true, color: INK, margin: 0 });
    s.addText(d, { x: x+0.35, y: 4.05, w: 3.2, h: 1.6, fontFace: B, fontSize: 13.5, color: '3a3a40', margin: 0 });
  });

  // ---------- 13. CTA ----------
  s = pres.addSlide();
  s.background = { color: DARK };
  s.addImage({ path: `${KIT}/one-by-growup_principal_offwhite@2000.png`, x: W/2-2.1, y: 1.5, w: 4.2, h: 4.2*175/403 });
  s.addText('Vamos colocar o seu negócio em um?', { x: 0, y: 3.9, w: W, h: 0.7, align: 'center', fontFace: T, fontSize: 26, bold: true, color: 'F1F1F2' });
  s.addShape('roundRect', { x: W/2-1.55, y: 4.9, w: 3.1, h: 0.72, rectRadius: 0.14, fill: { color: BLUE } });
  s.addText('Fale com a GrowUp', { x: W/2-1.55, y: 4.9, w: 3.1, h: 0.72, align: 'center', fontFace: T, fontSize: 16, bold: true, color: 'FFFFFF', margin: 0 });
  s.addText('sistema.grow2up.com.br', { x: 0, y: 5.9, w: W, h: 0.4, align: 'center', fontFace: B, fontSize: 13, color: '6C6C78' });
  cores.forEach((c, i) => s.addShape('rect', { x: i*(W/6), y: H-0.12, w: W/6, h: 0.12, fill: { color: c } }));

  await pres.writeFile({ fileName: 'deck-one-by-growup.pptx' });
  console.log('DECK OK');
})();
