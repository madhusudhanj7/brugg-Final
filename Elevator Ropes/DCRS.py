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

tss = "tss.png"
ssz = "smz.png"
dcrs1 = "dcr1.png"
dcrs2 = "dcrs2.png"
dcrs3 = "dcrs3.png"


width, height = A4
c = Canvas("DCRS.pdf",pagesize=letter)
c.drawImage(bg,0*inch,7.25*inch,width=12*inch,height=5*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 10.5*inch)
# black50transparent = Color(0,0,0, alpha=0.8)
c.setFillColor(colors.black)
c.rect(-20,8.33*inch, 9*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",13)
c.drawString(20, 8.55*inch, "DOOR CLOSING ROPE SETS ")
c.setFont("Helvetica",9)


c.drawImage(tss,-20,5*inch,width=2*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(ssz,1*inch,4.5*inch,width=1.75*inch,height=3*inch,preserveAspectRatio=True)

c.drawImage(dcrs1,0.75*inch,3*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
c.drawImage(dcrs2,0.1*inch,2*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
c.drawImage(dcrs3,1.5*inch,2*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)





textobject = c.beginText()
textobject.setTextOrigin(3*inch, 7.75*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 10)
textobject.textLines('''
                         TSS-Rope Set
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant

                         One packaging unit contains 5 ropes sets each

                         ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=5  fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)

rope0 = Paragraph('<para lindent=5  fontname = "Helvetica-Bold"fontsize =5  >mm</para>',stylesN)


itemn2 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5>77720</para>',stylesN)
rope2 = Paragraph('<para lindent=5   fontname = "Helvetica-Bold" fontsize =5>3.0</para>',stylesN)



tss1 =[[itemn,rope],
         ['',''],
         ['',''],
        ['',rope0],
        [itemn2,rope2],

]
tsst = Table(tss1,colWidths=[1.25*cm,1.35*cm],rowHeights=4*mm)
tsst.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
tsst.wrapOn(c,width,height)
tsst.drawOn(c,3*inch,5.5*inch)



textobject = c.beginText()
textobject.setTextOrigin(3*inch, 5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 10)
textobject.textLines('''
                         SMZ-Rope Set
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant

                         Advantages
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant


                         ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=5  fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)

rope0 = Paragraph('<para lindent=5  fontname = "Helvetica-Bold"fontsize =5  >mm</para>',stylesN)


itemn2 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5>77720</para>',stylesN)
rope2 = Paragraph('<para lindent=5   fontname = "Helvetica-Bold" fontsize =5>3.0</para>',stylesN)



smz1 =[[itemn,rope],
         ['',''],
         ['',''],
        ['',rope0],
        [itemn2,rope2],

]
smzt = Table(smz1,colWidths=[1.25*cm,1.35*cm],rowHeights=4*mm)
smzt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
smzt.wrapOn(c,width,height)
smzt.drawOn(c,3*inch,1*inch)
#


c.showPage()
c.save()
