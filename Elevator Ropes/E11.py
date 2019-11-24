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
a = 'A.png'
am = 'AM.png'
d = "D.png"
fp = "FP.png"
fp2 = "FP2.png"
fp3 = "FP3.png"

width, height = A4
c = Canvas("ER11.pdf",pagesize=landscape(letter))
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 570)
black50transparent = Color(0,0,0, alpha=0.5)
c.setFillColor(black50transparent)
c.rect(-20,6.07*inch, 8.5*inch, 0.75*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(20, 6.4*inch, "WEDGE SOCKET")
c.setFont("Helvetica",10)

c.drawString(190, 6.4*inch, "Symmetrical [EN 13411-7] with Eyelet Bolt [DIN 444]")

black50transparent = Color(169,169,169, alpha=0.35)
c.setFillColor(black50transparent)
c.rect(585,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)

textobject = c.beginText()
textobject.setTextOrigin(20, 5.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           Product Data
                           wedge socket welded, steel zinc-plated
                            incl. wedge, bolt and safety pins pre-assembled
                           wedge socket transmits 80% of minimal breaking load
                           of traction rope or governor rope
                           eyelet bolt welded, steel zinc-plated
                           in connection with the wedge socket the eyelet bolt transmits
                           80% of the minimal breaking load of the elevator rope
                           for mounting and operation the explanations in appendix B
                            of the norm EN 13411-7 are valid''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 5.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           Advantages
                            can be assembled safely and simply on-site
                            springs, buffers and other accessories can
                            be mounted individually
                            ''')
c.drawText(textobject)


c.drawImage(a,1*inch,1.5*inch,width=0.75*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(am,2*inch,1.7*inch,width=0.75*inch,height=2.75*inch,preserveAspectRatio=True)
c.drawImage(d,3*inch,1.65*inch,width=0.75*inch,height=2.75*inch,preserveAspectRatio=True)
c.drawImage(fp,4*inch,1.45*inch,width=0.75*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(fp2,5*inch,1.4*inch,width=0.75*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(fp3,6*inch,1.4*inch,width=0.75*inch,height=3*inch,preserveAspectRatio=True)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
rope = Paragraph('<para lindent=15 fontname = "Helvetica-Bold" fontsize =4>rope-@</para>',stylesN)
di = Paragraph('<para fontname = "Helvetica-Bold" fontsize =4>d<br/></para>',stylesN)

di1= Paragraph('<para  fontname = "Helvetica-Bold" fontsize =4>d1</para>',stylesN)
l1 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =4>L1</para>',stylesN)
l2 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =4>L2</para>',stylesN)
l3 = Paragraph('<para fontname = "Helvetica-Bold" fontsize =4>L3</para>',stylesN)

p1 = Paragraph('<para align = "LEFT" leftindent=5 fontname = "Helvetica-Bold" fontsize =7>A</para>',stylesN)
p2 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =4>mm</para>',stylesN)
p3 = Paragraph('<para align = "LEFT" leftindent=3 fontname = "Helvetica-Bold" fontsize =7>AM</para>',stylesN)
p4 = Paragraph('<para align = "LEFT" leftindent=3 fontname = "Helvetica-Bold" fontsize =7>D</para>',stylesN)
p5 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =7>FP</para>',stylesN)
p6 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =7>FP2</para>',stylesN)
p7 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =7>FP3</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =4  >64109</para>',stylesN)
rope1 = Paragraph('<para  fontname = "Helvetica" fontsize =4>5.0</para>',stylesN)
rope2 = Paragraph('<para  fontname = "Helvetica" fontsize =4>6.5</para>',stylesN)

dit = Paragraph('<para fontname = "Helvetica" fontsize =4>M10<br/></para>',stylesN)

di1t= Paragraph('<para  fontname = "Helvetica" fontsize =4></para>',stylesN)
l1t = Paragraph('<para  fontname = "Helvetica" fontsize =4>265</para>',stylesN)
l2t = Paragraph('<para  fontname = "Helvetica" fontsize =4>180</para>',stylesN)
l3t = Paragraph('<para fontname = "Helvetica" fontsize =4></para>',stylesN)
d1 = [[itemn,rope,'', di,di1,l1,l2,l3],
        ['','','','','','','','',],
      [p1,p2,'','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p3,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p4,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p5,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p6,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p7,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      ]

t1 = Table(d1,colWidths=[1.25*cm,2*cm,1*cm,1*cm,1*cm,1*cm,1*cm,1*cm],rowHeights=3.5*mm)
t1.setStyle(TableStyle([

                            ('SPAN',(1,0),(2,0)),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(0,2),(-8,-36),'#DCDCDC'),#for A
                            ('BACKGROUND',(2,3),(-8,-30),'#DCDCDC'),#for A
                             ('BACKGROUND',(0,9),(-8,-29),'#DCDCDC'),#for AM
                             ('BACKGROUND',(1,10),(-7,-23),'#DCDCDC'),#for AM
                             ('BACKGROUND',(0,16),(-8,-22),'#DCDCDC'),#for D
                              ('BACKGROUND',(1,17),(-7,-16),'#DCDCDC'),#for D
                              ('BACKGROUND',(0,23),(-8,-15),'#DCDCDC'),#for FP
                              ('BACKGROUND',(1,24),(-7,-11),'#DCDCDC'),#for FP
                              ('BACKGROUND',(0,29),(-8,-11),'#DCDCDC'),#for FP2
                              ('BACKGROUND',(1,29),(-7,-6),'#DCDCDC'),#for FP2
                              ('BACKGROUND',(0,34),(-8,-6),'#DCDCDC'),#for FP3
                              ('BACKGROUND',(1,32),(-7,-1),'#DCDCDC'),#for FP3
                               # ('BACKGROUND',(2,10),(-8,-1),'#DCDCDC'),

                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,1),(-2,-1),0.25,colors.black),

                             ('ALIGN',(1,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t1.wrapOn(c,width,height)
t1.drawOn(c,7.25*inch,0.75*inch)

textobject = c.beginText()
textobject.setTextOrigin(7.25*inch, 0.65*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                          Other sizes available upon request.
                           You will find the item numbers for all combination possibilities in the price list.
                            ''')
c.drawText(textobject)

c.showPage()
c.save()
