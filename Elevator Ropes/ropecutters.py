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

width, height = A4
c = Canvas("ropecutter.pdf",pagesize=letter)
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
c.drawCentredString(138, 8.55*inch, "ROPE CUTTERS")

textobject = c.beginText()
textobject.setTextOrigin(380, 7.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Rope Cutters
                         ''')
c.drawText(textobject)


c.drawImage(i16,60,6.4*inch,width=3*inch,height=1.75*inch)

c.drawImage(i17,50,3.7*inch,width=3.4*inch,height=1.75*inch)


textobject = c.beginText()
textobject.setTextOrigin(380, 5.4*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Hydraulic Rope Cutters
                           ''')
c.drawText(textobject)


itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> rope @</para>',stylesN)
weight = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> weight</para>',stylesN)
length =Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> length<br/>cutters</para>',stylesN)

itemn0 = Paragraph('<para  fontname = "Helvetica" fontsize =6  ></para>',stylesN)
ropemm = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> mm</para>',stylesN)
weightkg = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> kg</para>',stylesN)
lengthmm =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> mm</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77790</para>',stylesN)
ropemm1 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>upto 12 </para>',stylesN)
weightkg1 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> 1.5</para>',stylesN)
lengthmm1 =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>500</para>',stylesN)





rc =[[itemn,rope,weight,length],
         ['','',''],
         ['','',''],
        [itemn0,ropemm,weightkg,lengthmm],
        [itemn1,ropemm1,weightkg1,lengthmm1],


]
rct = Table(rc,colWidths=[1.25*cm,1.75*cm,2.25*cm],rowHeights=4*mm)
rct.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-3,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
rct.wrapOn(c,width,height)
rct.drawOn(c,5.2*inch,6.9*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> rope @</para>',stylesN)
weight = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> weight</para>',stylesN)
length =Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> length<br/>cutters</para>',stylesN)

itemn0 = Paragraph('<para  fontname = "Helvetica" fontsize =6  ></para>',stylesN)
ropemm = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> mm</para>',stylesN)
weightkg = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> kg</para>',stylesN)
lengthmm =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> mm</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77790</para>',stylesN)
ropemm1 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>upto 12 </para>',stylesN)
weightkg1 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> 1.5</para>',stylesN)
lengthmm1 =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>500</para>',stylesN)

rc =[[itemn,rope,weight,length],
         ['','',''],
         ['','',''],
        [itemn0,ropemm,weightkg,lengthmm],
        [itemn1,ropemm1,weightkg1,lengthmm1],


]
rct = Table(rc,colWidths=[1.25*cm,1.75*cm,2.25*cm],rowHeights=4*mm)
rct.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-3,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
rct.wrapOn(c,width,height)
rct.drawOn(c,5.2*inch,4.4*inch)

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
c.drawCentredString(98, 8.55*inch, "PACKAGING")

c.drawImage(i18,20,6.85*inch,width=1.4*inch,height=1.15*inch)

c.drawImage(i19,145,6.1*inch,width=1.4*inch,height=1.35*inch)

c.drawImage(i20,35,5*inch,width=2*inch,height=1.2*inch)

c.drawImage(i21,60,3*inch,width=2.75*inch,height=1.75*inch)

c.drawImage(i22,35,1.3*inch,width=2*inch,height=1.6*inch)

c.drawImage(i23,165,0.2*inch,width=1.65*inch,height=1.5*inch)

textobject = c.beginText()
textobject.setTextOrigin(308, 7.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        When selecting the packaging, BRUGG LIFTING pays attention to the
                        best transport protection possible. Our ropes are protected in the best
                        possible  way  during  the  transport  with  special  packaging  materials
                        against corrosion and mechanical damaging.

                        BRUGG  LIFTING is  committed  to  handle  ressources  with  great  care.
                        That  is  why  our  ropes,  whenever  possible,  are  delivered  on  sturdy
                        returnable reels and drums that can be reused.
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 4.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          Cross Drums
                           capacity according to rope diameter
                           from 100m (16mm) to 400m (6,5mm)
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 4.3*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          Round Reels
                          /width: 300 600mm / 320 530mm
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 3.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          Coils
                          up to 50m or 30kg
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 3.3*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          XJ Wooden Reels 100 x 65 cm
                          capacity according to rope diameter
                          from 1000m HRS ( 16mm) or 1132kg reel weight
                          up to 4100m HRS ( 8mm) or 1118kg reel weight
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 2.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        System Deliveries on Pallets
                        consisting  of  rope/ end  terminations/ accessories/
                        mounting materia
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 1.75*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        System Deliveries in Sturdy Cardboard Box
                        System Deliveries in Sturdy Cardboard Box
                         ''')
c.drawText(textobject)
c.showPage()
c.save()
