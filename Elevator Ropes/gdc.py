from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm,inch
from reportlab.lib import colors, utils
from reportlab.platypus import Paragraph, Table, TableStyle, Image, Frame, Spacer, PageBreak, BaseDocTemplate, PageTemplate, SimpleDocTemplate, Flowable
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.graphics import barcode, renderPDF
from reportlab.graphics.shapes import *
from reportlab.platypus.flowables import Image as GNAA
from reportlab.lib.pagesizes import letter,landscape
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.lib.colors import yellow, red, black,white,grey
from reportlab.graphics.shapes import Rect
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red, yellow, green, gray, white
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.platypus import Image
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PIL import Image, ImageFilter
from svglib.svglib import svg2rlg
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderSVG
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.colors import Color, black, blue, red


styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
logo = "brugglifting.svg"
bg = "img1.jpg"
hrs = "hrs.jpg"
scx9 = "hrs.jpg"
sc8 = "hrs.jpg"
dp9 = "hrs.jpg"
X19 = "hrs.jpg"
tsr = "hrs.jpg"
x25 = "hrs.jpg"
sx25 = "hrs.jpg"
i3 = "i3.png"
i4 = "i4.png"
i5 = "i5.png"
i6 = "i6.png"
i7 = "i7.png"
i16 = "i16.png"
i17 = "i17.png"
i18 = "i18.png"
i19 = "i19.png"
i20 = "i20.png"
i21 = "i21.png"
i22 = "i22.png"
i23 = "i23.png"
i24 = "i24.png"
i25 = "i25.png"
i26 = "i26.png"

width, height = A4
c = Canvas("gdc.pdf",pagesize=letter)
c.drawImage(bg,0*inch,8.25*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)
c.setFillColor('#696969')
c.rect(-20,8.33*inch, 17*inch, 0.75*inch,stroke=0,fill=1)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(70, 8.55*inch, "GDC")

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",14)
c.drawCentredString(180, 8.55*inch, "Grove Depth Comparator")

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(300, 8.55*inch, ". RWG")

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",14)
c.drawCentredString(400, 8.55*inch, "Rope Wear Gauge")


textobject = c.beginText()
textobject.setTextOrigin(315, 7.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        GDC Groove Depth Comparator
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 7.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        The GDC enables you to precisely measure and compare sheave groove
                        variations.  It  serves  to  early  detect  worn-out  drive  sheaves  and  may
                        thus help to increase the service life of ropes.
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 6.8*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 6.6*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        Applicable for all common groove shapes
                        Very easy handling
                        Measurement in 1/100mm or 1/1000 inch
                        Measuring accuracy 5/1000mm or 5/10000 inch
                        Total weight of 190 g
                        Switching between metric and imperial system
                         ''')
c.drawText(textobject)


c.drawImage(i24,60,3.6*inch,width=2.6*inch,height=4.25*inch)

c.drawImage(i25,50,0.6*inch,width=3.4*inch,height=2.55*inch)


textobject = c.beginText()
textobject.setTextOrigin(315, 3.35*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        RWG Rope Wear Gauge
                           ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 3.15*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        Within seconds, the precision gauge enables you to check, whether
                        the minimum nominal diameter of the rope is below the target.
                        If below limit, the rope must be replaced
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 2.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                           ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 2.35*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                         Robust design in aluminum with anodized surface
                         Application in seconds
                         Weight of only 100 g
                         Applicable for diameters from 8 2 mm or 3/8 3/4 inch
                         Precise finish
                         ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
size = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> size</para>',stylesN)
ver = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> version</para>',stylesN)

itemn0 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77768</para>',stylesN)
size0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>8-19 mm</para>',stylesN)
ver0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> metric</para>',stylesN)

ver0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> metric</para>',stylesN)



gdc =[[itemn,size,ver],
         ['','',''],
         ['','',''],
        [itemn0,size0,ver0],
        [itemn0,size0,ver0],

]
gdct = Table(gdc,colWidths=[1.25*cm,1.75*cm,1.75*cm],rowHeights=4*mm)
gdct.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-2,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
gdct.wrapOn(c,width,height)
gdct.drawOn(c,4.4*inch,4.3*inch)



itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
size = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> size</para>',stylesN)
mes = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> unit of <br/>Measurement</para>',stylesN)

itemn0 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77768</para>',stylesN)
size0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>8-19 mm</para>',stylesN)
mes0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>metric</para>',stylesN)



rwg =[[itemn,size,mes],
         ['','',''],
         ['','',''],
        [itemn0,size0,mes0],
        [itemn0,size0,mes0],

]
rwgt = Table(rwg,colWidths=[1.25*cm,1.75*cm,2.25*cm],rowHeights=4*mm)
rwgt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-2,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
rwgt.wrapOn(c,width,height)
rwgt.drawOn(c,4.4*inch,0.8*inch)








c.showPage()

c.drawImage(bg,0*inch,8.25*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)
c.setFillColor('#696969')
c.rect(-20,8.33*inch, 5.5*inch, 0.75*inch,stroke=0,fill=1)


c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(98, 8.55*inch, "VT-LUBE")
c.drawImage(i26,60, 5.4*inch,width=1.75*inch,height=2*inch)


c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",14)
c.drawCentredString(220, 8.55*inch, "Rope Care Lubricant")



textobject = c.beginText()
textobject.setTextOrigin(308, 7.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        VT-Lube
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 7.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        This rope care lubricant was especially developed for the
                        relubrication of elevator ropes
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 6.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 6.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        excellent penetration quality causes optimum friction reduction
                        in the rope
                        excellent  creep quality enables even lubricant distribution on
                        and in the rope
                        excellent corrosion protection
                        suitable for high rope speed through very good adhesive quality
                        neutral quality towards synthetic materials
                        (no swelling of plastic parts)
                         ''')
c.drawText(textobject)



itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
content = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >content</para>',stylesN)

itemns = Paragraph('<para  fontname = "Helvetica"fontsize =6  ></para>',stylesN)
content0 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >mm</para>',stylesN)

itemns1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77738</para>',stylesN)
content1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >5</para>',stylesN)

vtl = [[itemn,content],
        ['',''],
        ['',''],
        [itemns,content0],
        [itemns1,content1]

]

vtlt = Table(vtl,colWidths=[1.25*cm,1.75*cm],rowHeights=4*mm)
vtlt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

vtlt.wrapOn(c,width,height)
vtlt.drawOn(c,4.4*inch,4.5*inch)


c.showPage()
c.save()
