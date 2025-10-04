#!/usr/bin/env python3
"""
Jujutsu Kaisen: The Cursed Energy Handbook
PDF Generator (ReportLab)
This script generates a multi-page A4 PDF with a modern anime-inspired theme.
Requirements:
    pip install reportlab
Run:
    python3 jkj_handbook_generator.py
Output:
    Jujutsu_Kaisen_The_Cursed_Energy_Handbook.pdf
"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Frame, Paragraph, Table, TableStyle, Image, SimpleDocTemplate, Spacer, PageBreak, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import textwrap

# Output path
OUT_PDF = "Jujutsu_Kaisen_The_Cursed_Energy_Handbook.pdf"

# Register fonts (attempt to use common system fonts; you can replace with local fonts)
try:
    pdfmetrics.registerFont(TTFont("SourceSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("SourceSans-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("SourceSerif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
except:
    # Fallback to default fonts if system fonts not found
    pass

# Colors (obsidian background theme, spectral violet & crimson accents)
ACCENT_VIOLET = colors.HexColor("#8A2BE2")  # spectral violet
ACCENT_CRIMSON = colors.HexColor("#D7263D")  # crimson
OBSIDIAN = colors.HexColor("#0B0B0D")  # deep near-black
PAPER = colors.HexColor("#0F1113")  # slightly lighter black for content blocks
TEXT_LIGHT = colors.HexColor("#EDEDED")

PAGE_WIDTH, PAGE_HEIGHT = A4

# Helper: draw header/footer
def header_footer(canvas_obj, doc):
    canvas_obj.setFillColor(ACCENT_VIOLET)
    canvas_obj.setStrokeColor(ACCENT_VIOLET)
    canvas_obj.setLineWidth(0.8)
    # top accent line
    canvas_obj.line(20*mm, PAGE_HEIGHT - 18*mm, PAGE_WIDTH - 20*mm, PAGE_HEIGHT - 18*mm)
    # footer line
    canvas_obj.line(20*mm, 18*mm, PAGE_WIDTH - 20*mm, 18*mm)
    # page number
    canvas_obj.setFont("SourceSans", 9)
    canvas_obj.setFillColor(TEXT_LIGHT)
    page_num = canvas_obj.getPageNumber()
    canvas_obj.drawRightString(PAGE_WIDTH - 20*mm, 12*mm, f"Page {page_num}")

# Build document elements using Platypus
doc = SimpleDocTemplate(
    OUT_PDF,
    pagesize=A4,
    leftMargin=20*mm,
    rightMargin=20*mm,
    topMargin=25*mm,
    bottomMargin=25*mm,
)

# Styles
styles = {
    "h1": ParagraphStyle("h1", fontName="SourceSans-Bold", fontSize=28, leading=34, alignment=TA_CENTER, textColor=TEXT_LIGHT, spaceAfter=6),
    "h2": ParagraphStyle("h2", fontName="SourceSans-Bold", fontSize=18, leading=22, alignment=TA_LEFT, textColor=TEXT_LIGHT, spaceBefore=8),
    "normal": ParagraphStyle("normal", fontName="SourceSans", fontSize=11, leading=15, alignment=TA_LEFT, textColor=TEXT_LIGHT),
    "em": ParagraphStyle("em", fontName="SourceSans", fontSize=11, leading=15, alignment=TA_LEFT, textColor=ACCENT_VIOLET),
    "toc": ParagraphStyle("toc", fontName="SourceSans", fontSize=12, leading=16, alignment=TA_LEFT, textColor=TEXT_LIGHT),
    "cover_title": ParagraphStyle("cover_title", fontName="SourceSans-Bold", fontSize=36, leading=42, alignment=TA_CENTER, textColor=TEXT_LIGHT),
    "subtitle": ParagraphStyle("subtitle", fontName="SourceSans", fontSize=14, leading=18, alignment=TA_CENTER, textColor=ACCENT_VIOLET),
}

# Content containers
elements = []

# Cover Page
elements.append(Spacer(1, 40*mm))
title = Paragraph("Jujutsu Kaisen: <br/><b>The Cursed Energy Handbook</b>", styles["cover_title"])
elements.append(title)
elements.append(Spacer(1, 10*mm))
subtitle = Paragraph("A modern roleplaying sourcebook — A4 layout", styles["subtitle"])
elements.append(subtitle)
elements.append(Spacer(1, 8*mm))
desc = Paragraph("A homebrew Jujutsu Kaisen tabletop system. Includes archetypes, cursed energy mechanics, domains, bestiary, sample characters, and a starter module.", styles["normal"])
elements.append(Spacer(1, 12*mm))
elements.append(desc)
elements.append(Spacer(1, 20*mm))
# Stylized crest placeholder
crest_box = Table([[" "]], colWidths=[160*mm], rowHeights=[40*mm])
crest_box.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), ACCENT_VIOLET),
    ("BOX", (0,0), (-1,-1), 2, ACCENT_CRIMSON),
]))
elements.append(crest_box)
elements.append(PageBreak())

# Table of Contents (placeholder that can be updated manually)
elements.append(Paragraph("Table of Contents", styles["h1"]))
toc_text = """
1. The World of Jujutsu<br/>
2. Character Creation<br/>
3. Cursed Energy System<br/>
4. Archetypes (Classes)<br/>
&nbsp;&nbsp;4.1 Cursed Technique User<br/>
&nbsp;&nbsp;4.2 Cursed Tool Specialist<br/>
&nbsp;&nbsp;4.3 Shikigami Summoner<br/>
&nbsp;&nbsp;4.4 Reverse Curse User<br/>
&nbsp;&nbsp;4.5 Domain Specialist<br/>
&nbsp;&nbsp;4.6 Vessel / Contract User<br/>
5. Combat & Techniques<br/>
6. Bestiary<br/>
7. Game Master Tools<br/>
Appendix: Sample Characters, Starter Module, Index
"""
elements.append(Paragraph(toc_text, styles["toc"]))
elements.append(PageBreak())

# Chapter 1: The World of Jujutsu
elements.append(Paragraph("Chapter 1: The World of Jujutsu", styles["h1"]))
lore = """
Curses are born from the negative emotions of humanity. Jujutsu Sorcerers manipulate cursed energy to exorcise these manifestations...
"""
elements.append(Paragraph(lore, styles["normal"]))
elements.append(Spacer(1, 6*mm))

# Insert a two-column lore block (simulated using two tables)
col1 = Paragraph(textwrap.fill("Curses: manifestations of fear, hatred, and malice. They range from harmless apparitions to Special Grade horrors that warp reality.", 80), styles["normal"])
col2 = Paragraph(textwrap.fill("Society: Jujutsu schools like Tokyo and Kyoto teach sorcerers to control cursed energy, enforce binding vows, and police curses.", 80), styles["normal"])
table = Table([[col1, col2]], colWidths=[85*mm, 85*mm])
table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
elements.append(table)
elements.append(PageBreak())

# Chapter 2: Character Creation (sample)
elements.append(Paragraph("Chapter 2: Character Creation", styles["h1"]))
elements.append(Paragraph("Backgrounds", styles["h2"]))
bg_table_data = [
    ["Student of Jujutsu Tech", "Gain Arcana & Insight"],
    ["Cursed Tool Apprentice", "Gain Athletics & Sleight of Hand"],
    ["Exorcist's Lineage", "Gain History & Religion"],
    ["Survivor of a Curse Attack", "Gain Perception & Stealth"],
    ["Vessel / Pact-Bound", "Gain Intimidation & Deception"],
]
bg_table = Table(bg_table_data, colWidths=[60*mm, 100*mm], hAlign="LEFT")
bg_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PAPER),
    ("TEXTCOLOR", (0,0), (-1,-1), TEXT_LIGHT),
    ("GRID", (0,0), (-1,-1), 0.25, colors.gray),
    ("FONTNAME", (0,0), (-1,-1), "SourceSans"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
elements.append(bg_table)
elements.append(Spacer(1,6*mm))

# CEP Table (Cursed Energy Points)
elements.append(Paragraph("Cursed Energy Points (CEP)", styles["h2"]))
cep_text = "CEP = 10 + Level + CON modifier + WIS modifier. CEP recovers fully on a long rest, and half on a short rest. Players may convert HP to CEP at the rate 1 HP → 1 CEP."
elements.append(Paragraph(cep_text, styles["normal"]))
elements.append(PageBreak())

# Chapter 4: Archetypes - provide detailed table for one archetype plus placeholders for others
elements.append(Paragraph("Chapter 4: Archetypes (Classes)", styles["h1"]))
elements.append(Paragraph("4.1 Cursed Technique User", styles["h2"]))
ctu_desc = """
Specializes in a unique cursed technique. Choose a Signature Technique at Level 1 and evolve it as you level.
"""
elements.append(Paragraph(ctu_desc, styles["normal"]))
# Add a level feature table
ctu_table_data = [["Level", "Feature", "CEP Cost"],
                  ["1", "Signature Technique (choose one)", "Varies (3–5)"],
                  ["5", "Technique Extension", "+2 CEP"],
                  ["10", "Domain Expansion (unstable)", "10 CEP"],
                  ["15", "Domain Perfection", "n/a"],
                  ["20", "True Technique Evolution", "n/a"]]
ctu_table = Table(ctu_table_data, colWidths=[25*mm, 100*mm, 30*mm])
ctu_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ACCENT_VIOLET),
    ("TEXTCOLOR", (0,0), (-1,-1), TEXT_LIGHT),
    ("GRID", (0,0), (-1,-1), 0.25, colors.gray),
    ("FONTNAME", (0,0), (-1,-1), "SourceSans"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
]))
elements.append(ctu_table)
elements.append(Spacer(1,6*mm))

# Example Signature Techniques table
elements.append(Paragraph("Example Signature Techniques", styles["h2"]))
tech_table_data = [
    ["Technique", "Effect", "Sample Flavor"],
    ["Cursed Speech", "Command/paralyze (WIS save)", "Inumaki-style"],
    ["Ratio", "Strike weak points for increased damage", "Nanami-style"],
    ["Boogie Woogie", "Swap positions of entities", "Todo-style"],
    ["Shadow Binding", "Control enemy movement via shadows", "Megumi-inspired"],
]
tech_table = Table(tech_table_data, colWidths=[50*mm, 70*mm, 35*mm])
tech_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ACCENT_CRIMSON),
    ("TEXTCOLOR", (0,0), (-1,-1), TEXT_LIGHT),
    ("GRID", (0,0), (-1,-1), 0.25, colors.gray),
    ("FONTNAME", (0,0), (-1,-1), "SourceSans"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
]))
elements.append(tech_table)
elements.append(PageBreak())

# Sample Character Sheets (Yuji, Gojo, Nobara, Megumi)
elements.append(Paragraph("Appendix: Sample Characters", styles["h1"]))
elements.append(Paragraph("<b>Yuji Itadori (Sample PC)</b>", styles["h2"]))
yuji_text = """
Archetype: Vessel / Contract User
Level: 3
CEP: 10 + 3 + CON_mod + WIS_mod = (example)
Background: Survivor of a curse attack
Abilities: Enhanced physicals, fast healer, can host an inner curse (Sukuna analogue)
Equipment: None (relies on body and cursed energy)
Playstyle notes: Close-quarters combatant with burst CEP usage. 
"""
elements.append(Paragraph(yuji_text, styles["normal"]))
elements.append(Spacer(1,6*mm))

elements.append(Paragraph("<b>Satoru Gojo (NPC/Legendary Template)</b>", styles["h2"]))
gojo_text = """
Archetype: Domain Specialist / Unique Technique User
Level: Legendary (GM only)
Signature: Infinity-like barrier (flavored)
Notes: Use as high-level NPC with Domain Perfection and Reality Rewrite.
"""
elements.append(Paragraph(gojo_text, styles["normal"]))
elements.append(PageBreak())

# Starter Module (Level 1-3 one-shot)
elements.append(Paragraph("Starter Module: The Haunting of Higan Shrine", styles["h1"]))
elements.append(Paragraph("Adventure Summary", styles["h2"]))
adv_text = """
The players are new recruits assigned to investigate a rural shrine where villagers have been disappearing...
"""
elements.append(Paragraph(adv_text, styles["normal"]))
elements.append(Spacer(1,6*mm))
elements.append(PageBreak())

# Bestiary sample
elements.append(Paragraph("Bestiary (Sample Entries)", styles["h1"]))
elements.append(Paragraph("Grade 4: Hollowchild", styles["h2"]))
hc_text = """
HP: 12 | Damage: 1d6 | Abilities: Haunting Wail (debuff), Possess small objects.
Tactics: Harass and separate party members.
"""
elements.append(Paragraph(hc_text, styles["normal"]))
elements.append(PageBreak())

# Index placeholder
elements.append(Paragraph("Index", styles["h1"]))
index_text = "This index is a placeholder. After final edits, update page numbers and index entries."
elements.append(Paragraph(index_text, styles["normal"]))

# Build PDF with a custom onPage for header/footer
def on_page(canvas_obj, doc):
    # Draw background rectangle (subtle)
    canvas_obj.saveState()
    canvas_obj.setFillColor(OBSIDIAN)
    canvas_obj.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, stroke=0, fill=1)
    canvas_obj.restoreState()
    header_footer(canvas_obj, doc)

doc.build(elements, onFirstPage=on_page, onLaterPages=on_page)

print("PDF generation script run complete. Output file:", OUT_PDF)
