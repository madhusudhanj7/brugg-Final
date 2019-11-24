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
width, height = A4
c = Canvas("compensationrope.pdf",pagesize=landscape(letter))
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 570)
c.setFillColor('#87CEFA')
c.rect(-20,6.07*inch, 1.75*inch, 0.5*inch,stroke=0,fill=1)

c.rect(50,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)
c.rect(670,6.07*inch, 1.75*inch, 0.5*inch,stroke=0,fill=1)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(50, 6.25*inch, "8x19")
c.drawCentredString(740, 6.25*inch, "6x25")

c.setFont("Helvetica-Bold",8)

c.drawString(120, 6.15*inch, "COMPENSATION ROPES")

c.drawImage(X19,30,4.5*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(120, 5.45*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
rope = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =4>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =4>breaking load<br/>min.</para>',stylesN)
weight= Paragraph('<para leftindent=-5 fontname = "Helvetica-Bold" fontsize =4>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =4>construction</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =-10 fontname = "Helvetica" fontsize =4>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-45 fontname = "Helvetica" fontsize =4>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =4>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =-11 fontname = "Helvetica" fontsize =4>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-45 fontname = "Helvetica" fontsize =4>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =4 leftindent=-70>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
            ['',mm,inc,kN,lbs,kg,lb,''],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],




            ]


t = Table(data,colWidths=[1*cm,1*cm,0.2*cm,2*cm,1*cm,1.75*cm,1.5*cm],rowHeights=0.7*cm)
t.setStyle(TableStyle([

                             # ('LINEABELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),

                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,0),(-1,-1),0.25,colors.black),

                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 120,4*inch)
textobject = c.beginText()
textobject.setTextOrigin(120, 3.85*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.''')
c.drawText(textobject)
c.drawImage(sx25,5.75*inch,4.5*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(7*inch, 5.45*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
rope = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =4>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =4>breaking load<br/>min.</para>',stylesN)
weight= Paragraph('<para leftindent=-5 fontname = "Helvetica-Bold" fontsize =4>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =4>construction</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =-10 fontname = "Helvetica" fontsize =4>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-45 fontname = "Helvetica" fontsize =4>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =4>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =-11 fontname = "Helvetica" fontsize =4>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-45 fontname = "Helvetica" fontsize =4>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =4 leftindent=-70>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
            ['',mm,inc,kN,lbs,kg,lb,''],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],




            ]


t = Table(data,colWidths=[1*cm,1*cm,0.2*cm,2*cm,1*cm,1.75*cm,1.5*cm],rowHeights=0.7*cm)
t.setStyle(TableStyle([

                             # ('LINEABELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),

                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,0),(-1,-1),0.25,colors.black),

                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 7*inch,4*inch)




textobject = c.beginText()
textobject.setTextOrigin(7*inch, 3.85*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.''')
c.drawText(textobject)

c.setFillColor('#87CEFA')
c.rect(-20,2.5*inch, 1.75*inch, 0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(50, 2.65*inch, "8x25")
c.drawImage(x25,30,1.25*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(120, 2.2*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)
itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
rope = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =4>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =4>breaking load<br/>min.</para>',stylesN)
weight= Paragraph('<para leftindent=-5 fontname = "Helvetica-Bold" fontsize =4>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =4>construction</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =-10 fontname = "Helvetica" fontsize =4>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-45 fontname = "Helvetica" fontsize =4>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =4>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =-11 fontname = "Helvetica" fontsize =4>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-45 fontname = "Helvetica" fontsize =4>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =4 leftindent=-70>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
            ['',mm,inc,kN,lbs,kg,lb,''],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],



            ]


t = Table(data,colWidths=[1*cm,1*cm,0.2*cm,2*cm,1*cm,2*cm,1.5*cm],rowHeights=0.7*cm)
t.setStyle(TableStyle([

                             ('LINEABELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),

                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,0),(-1,-1),0.25,colors.black),
                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 120,0.75*inch)
textobject = c.beginText()
textobject.setTextOrigin(120, 0.65*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.''')
c.drawText(textobject)
c.showPage()
c.save()
