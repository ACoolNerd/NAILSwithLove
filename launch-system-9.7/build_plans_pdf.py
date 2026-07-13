from pathlib import Path
import re
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

ROOT=Path(__file__).parent
C={"burg":colors.HexColor('#7A2036'),"blush":colors.HexColor('#FBEEE6'),"gold":colors.HexColor('#C9A227'),"cream":colors.HexColor('#FFF9F5'),"plum":colors.HexColor('#3A1420')}
ss=getSampleStyleSheet()
ss.add(ParagraphStyle(name='T',parent=ss['Title'],fontName='Times-Bold',fontSize=25,leading=29,textColor=C['burg'],spaceAfter=8))
ss.add(ParagraphStyle(name='S',parent=ss['Normal'],fontSize=11,leading=15,textColor=C['plum'],spaceAfter=16))
ss.add(ParagraphStyle(name='H1x',parent=ss['Heading1'],fontName='Times-Bold',fontSize=17,leading=21,textColor=C['burg'],spaceBefore=10,spaceAfter=6))
ss.add(ParagraphStyle(name='H2x',parent=ss['Heading2'],fontName='Times-Bold',fontSize=13,leading=16,textColor=C['burg'],spaceBefore=8,spaceAfter=4))
ss.add(ParagraphStyle(name='B',parent=ss['BodyText'],fontSize=9.2,leading=13,textColor=C['plum'],spaceAfter=5))
ss.add(ParagraphStyle(name='L',parent=ss['BodyText'],fontSize=9.1,leading=12.5,leftIndent=12,firstLineIndent=-7,textColor=C['plum'],spaceAfter=3))
ss.add(ParagraphStyle(name='Sm',parent=ss['BodyText'],fontSize=7.4,leading=9.6,textColor=colors.HexColor('#665A60')))

def inline(s):
 s=s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'(?<!\*)\*(.+?)\*(?!\*)',r'<i>\1</i>',s)
 s=re.sub(r'`(.+?)`',r'<font name="Courier">\1</font>',s)
 return s

def footer(canvas,doc,label):
 canvas.saveState();canvas.setStrokeColor(C['blush']);canvas.line(18*mm,15*mm,192*mm,15*mm)
 canvas.setFillColor(colors.HexColor('#6B6064'));canvas.setFont('Helvetica',7.5)
 canvas.drawString(18*mm,10*mm,label);canvas.drawRightString(192*mm,10*mm,f'Page {doc.page}')
 canvas.restoreState()

def build(src,out,label):
 lines=src.read_text(encoding='utf-8').splitlines();story=[];i=0
 while i<len(lines):
  line=lines[i].rstrip()
  if not line:i+=1;continue
  if line.startswith('# '): story+=[Spacer(1,12*mm),Paragraph(inline(line[2:]),ss['T'])];i+=1;continue
  if line.startswith('## '): story.append(Paragraph(inline(line[3:]),ss['H1x']));i+=1;continue
  if line.startswith('### '): story.append(Paragraph(inline(line[4:]),ss['H2x']));i+=1;continue
  if line.startswith('|'):
   raw=[]
   while i<len(lines) and lines[i].startswith('|'):raw.append(lines[i]);i+=1
   rows=[]
   for k,r in enumerate(raw):
    cells=[x.strip() for x in r.strip('|').split('|')]
    if k==1 and all(set(x)<=set(':-') for x in cells):continue
    rows.append([Paragraph(inline(x),ss['Sm']) for x in cells])
   widths=None
   if len(rows[0])==2:widths=[112*mm,55*mm]
   elif len(rows[0])==4:widths=[48*mm,39*mm,39*mm,41*mm]
   t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),C['burg']),('TEXTCOLOR',(0,0),(-1,0),colors.white),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#D8C8CD')),('ROWBACKGROUNDS',(0,1),(-1,-1),[C['cream'],colors.white]),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
   story += [t,Spacer(1,4*mm)];continue
  if re.match(r'^\d+\. ',line): story.append(Paragraph(line.split('.',1)[0]+'. '+inline(line.split('.',1)[1].strip()),ss['L']));i+=1;continue
  if line.startswith('- '): story.append(Paragraph('• '+inline(line[2:]),ss['L']));i+=1;continue
  para=[line];i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||- |\d+\. )',lines[i]):para.append(lines[i].rstrip());i+=1
  story.append(Paragraph('<br/>'.join(inline(x) for x in para),ss['B']))
 doc=SimpleDocTemplate(str(out),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=17*mm,bottomMargin=20*mm,title=label,author='Nails with Love by Yesenia')
 doc.build(story,onFirstPage=lambda c,d:footer(c,d,label),onLaterPages=lambda c,d:footer(c,d,label))

build(ROOT/'startup-plan-en.md',ROOT/'Nails-with-Love-Startup-Plan-English.pdf','Nails with Love — English Startup Plan')
build(ROOT/'plan-de-inicio-es.md',ROOT/'Nails-with-Love-Plan-de-Inicio-Espanol.pdf','Nails with Love — Plan de Inicio Español')
print('PDF plans created')
