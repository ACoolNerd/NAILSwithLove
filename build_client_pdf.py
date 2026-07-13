from pathlib import Path
import re
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Image, KeepTogether)

ROOT = Path(__file__).parent
SOURCE = ROOT / "client-growth-playbook.md"
OUTPUT = ROOT / "Columbia-Nails-Client-Growth-Playbook.pdf"
BOARD = ROOT / "concept-board-blush-boutique.png"

berry = colors.HexColor("#6E2942")
blush = colors.HexColor("#F4D6DC")
ivory = colors.HexColor("#FFF9F5")
gold = colors.HexColor("#C9A46A")
charcoal = colors.HexColor("#292326")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleBoutique", parent=styles["Title"], fontName="Times-Bold",
    fontSize=25, leading=29, textColor=berry, alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], fontSize=11, leading=15,
    textColor=charcoal, alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name="H1Boutique", parent=styles["Heading1"], fontName="Times-Bold",
    fontSize=17, leading=21, textColor=berry, spaceBefore=11, spaceAfter=7))
styles.add(ParagraphStyle(name="H2Boutique", parent=styles["Heading2"], fontName="Times-Bold",
    fontSize=13, leading=16, textColor=berry, spaceBefore=9, spaceAfter=5))
styles.add(ParagraphStyle(name="BodyBoutique", parent=styles["BodyText"], fontSize=9.3,
    leading=13.2, textColor=charcoal, spaceAfter=5))
styles.add(ParagraphStyle(name="BulletBoutique", parent=styles["BodyText"], fontSize=9.1,
    leading=12.5, leftIndent=12, firstLineIndent=-7, textColor=charcoal, spaceAfter=3))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=7.5, leading=10,
    textColor=colors.HexColor("#5E5659")))

def inline(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*(.+?)\*(?!\*)", r"<i>\1</i>", s)
    s = s.replace("  ", " ")
    return s

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(blush)
    canvas.line(18*mm, 15*mm, 192*mm, 15*mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#6B6064"))
    canvas.drawString(18*mm, 10*mm, "Boutique Nail Service — Cali | Client Growth Playbook")
    canvas.drawRightString(192*mm, 10*mm, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm,
    topMargin=18*mm, bottomMargin=20*mm, title="Boutique Nail Service — Cali",
    author="Prepared for client review")

story = [Spacer(1, 16*mm), Paragraph("Boutique Nail Service", styles["TitleBoutique"]),
    Paragraph("Cali, Colombia", styles["TitleBoutique"]),
    Paragraph("Growth, pricing, design, WhatsApp booking, and follow-up playbook", styles["Subtitle"])]
if BOARD.exists():
    img = Image(str(BOARD), width=174*mm, height=108.75*mm)
    story += [img, Spacer(1, 7*mm)]
story += [Paragraph("Prepared 13 July 2026", styles["Subtitle"]),
          Paragraph("Working draft: replace all [BRACKETED] placeholders before publishing.", styles["Small"]),
          PageBreak()]

lines = SOURCE.read_text(encoding="utf-8").splitlines()
i = 3
while i < len(lines):
    line = lines[i].rstrip()
    if not line:
        i += 1; continue
    if line.startswith("## "):
        story.append(Paragraph(inline(line[3:]), styles["H1Boutique"])); i += 1; continue
    if line.startswith("### "):
        story.append(Paragraph(inline(line[4:]), styles["H2Boutique"])); i += 1; continue
    if line.startswith("| "):
        raw=[]
        while i < len(lines) and lines[i].startswith("|"):
            raw.append(lines[i]); i += 1
        rows=[]
        for idx,r in enumerate(raw):
            cells=[c.strip() for c in r.strip("|").split("|")]
            if idx==1 and all(set(c) <= set(":-") for c in cells): continue
            rows.append([Paragraph(inline(c), styles["Small"]) for c in cells])
        widths=[34*mm, 72*mm, 25*mm, 36*mm] if len(rows[0])==4 else None
        t=Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
        t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),berry),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),("VALIGN",(0,0),(-1,-1),"TOP"),
            ("GRID",(0,0),(-1,-1),0.35,colors.HexColor("#D8C8CD")),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[ivory,colors.white]),
            ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
            ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
        story += [t, Spacer(1,5*mm)]; continue
    if line.startswith("- "):
        story.append(Paragraph("• " + inline(line[2:]), styles["BulletBoutique"])); i += 1; continue
    # collect adjacent prose lines so explicit markdown line breaks remain together
    para=[line]
    i += 1
    while i < len(lines) and lines[i].strip() and not lines[i].startswith(("## ","### ","- ","| ")):
        para.append(lines[i].rstrip()); i += 1
    text="<br/>".join(inline(x.rstrip().rstrip("  ")) for x in para)
    story.append(Paragraph(text, styles["BodyBoutique"]))

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
