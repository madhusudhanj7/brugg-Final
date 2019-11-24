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
c = Canvas("HRS.pdf",pagesize=letter)
c.drawImage(bg,0*inch,8.25*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)
c.setFillColor('#87CEFA')
c.rect(-20,8.33*inch, 2.5*inch, 0.75*inch,stroke=0,fill=1)

c.rect(150,8.33*inch, 12*inch, 0.25*inch,stroke=0,fill=1)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(50, 8.55*inch, "HRS")
c.setFont("Helvetica-Bold",8)

c.drawString(190, 8.4*inch, "HOIST ROPES")

c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(190, 7.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)



c.setFillColor('#87CEFA')
c.rect(190,6.85*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(192, 7.25*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           125,000
                             N/mm2
                           18.1x10^6
                            psi''')
c.drawText(textobject)
c.drawString(192, 6.7*inch, "E-Module**")

c.setFillColor('#87CEFA')
c.rect(240,6.85*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(242, 7.25*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           0.104
                             %
                            1.2
                           in/100ft        ''')
c.drawText(textobject)
c.drawString(242, 6.7*inch, "Elastic")

c.setFillColor('#87CEFA')
c.rect(290,6.85*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(292, 7.25*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           0.13
                             %''')
c.drawText(textobject)
c.drawString(292, 6.7*inch, "permenant")

c.setFillColor('#87CEFA')
c.rect(340,6.85*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject0 = c.beginText()
textobject0.setTextOrigin(342, 7.25*inch)
c.setFillColor(colors.black)
textobject0.setFont("Helvetica", 7)
textobject0.textLines('''
                           < 425
                             m
                            <14000
                              ft ''')
c.drawText(textobject0)
c.drawString(342, 6.7*inch, "lifting height*")

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =7 >item number</para>',stylesN)
rope = Paragraph('<para lindent=5 fontname = "Helvetica-Bold" fontsize =7>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =7>breaking load<br/>min.</para>',stylesN)
weight= Paragraph('<para leftindent=10 fontname = "Helvetica-Bold" fontsize =7>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =7>construction</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =7 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =30 fontname = "Helvetica" fontsize =7>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =7>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =3 fontname = "Helvetica" fontsize =7>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =7>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-30 fontname = "Helvetica" fontsize =7>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =7>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =7>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =30 fontname = "Helvetica" fontsize =7>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =7>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =2 fontname = "Helvetica" fontsize =7>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =7>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-35 fontname = "Helvetica" fontsize =7>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =7 leftindent=-70>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
            ['',mm,inc,kN,lbs,kg,lb,''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            

            ]

t = Table(data,colWidths=[1.5*cm,1.5*cm,1.5*cm,2*cm,1.75*cm,2.25*cm,3*cm],rowHeights=0.55*cm)
t.setStyle(TableStyle([

                            ('LINEABELOW',(0,2),(-2,-2),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),
                            ('FONTSIZE',(0,1),(-2,-1),20),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,0),(-1,-1),0.25,colors.black),
                             ('ALIGN',(0,0),(-1,-1),'LEFT'),
                            # ('ALIGN',())
                            ('VALIGN',(0,0),(0,-4),'BOTTOM')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 190,3*inch)
textobject = c.beginText()
textobject.setTextOrigin(190, 2.85*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.''')
c.drawText(textobject)

c.showPage()



# For SCX9


# c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# c.setFillColor('#87CEFA')
# c.rect(-20,6.07*inch, 2.5*inch, 0.75*inch,stroke=0,fill=1)
#
# c.rect(150,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)
#
# c.setFillColor(colors.white)
# c.setFont("Helvetica-Bold",8)
# c.drawString(190, 6.15*inch, "HOIST ROPES")
# c.setFillColor('#87CEFA')
# c.rect(-20,6.07*inch, 2.5*inch, 0.75*inch,stroke=0,fill=1)
#
# c.rect(150,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)
#
# c.setFillColor(colors.white)
# c.setFont("Helvetica-Bold",20)
# c.drawCentredString(50, 6.35*inch, "HRS")
# c.setFont("Helvetica-Bold",8)
#
# c.drawString(190, 6.15*inch, "HOIST ROPES")
#
# c.drawImage(hrs,30,4*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)
# c.setFillColor(colors.black)
#
# textobject = c.beginText()
# textobject.setTextOrigin(190, 5.45*inch)
# c.setFillColor(colors.black)
# textobject.setFont("Helvetica", 7)
# textobject.textLines('''
#                            and number of trips, also under difficult  highest demandas
#                            on breaking force, elongation  elongation number of trips,
#                            also under difficult instalation''')
# c.drawText(textobject)
#
#
#
# c.setFillColor('#87CEFA')
# c.rect(190,4.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
# textobject = c.beginText()
# textobject.setTextOrigin(192, 4.6*inch)
# c.setFillColor(colors.black)
# textobject.setFont("Helvetica", 7)
# textobject.textLines('''
#                            125,000
#                              N/mm2
#                            18.1x10^6
#                             psi''')
# c.drawText(textobject)
# c.drawString(192, 4*inch, "E-Module**")
#
# c.setFillColor('#87CEFA')
# c.rect(240,4.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
# textobject = c.beginText()
# textobject.setTextOrigin(242, 4.6*inch)
# c.setFillColor(colors.black)
# textobject.setFont("Helvetica", 7)
# textobject.textLines('''
#                            0.104
#                              %
#                             1.2
#                            in/100ft        ''')
# c.drawText(textobject)
# c.drawString(242, 4*inch, "Elastic")
#
#
# c.setFillColor('#87CEFA')
# c.rect(290,4.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
# textobject = c.beginText()
# textobject.setTextOrigin(292, 4.6*inch)
# c.setFillColor(colors.black)
# textobject.setFont("Helvetica", 7)
# textobject.textLines('''
#                            0.13
#                              %''')
# c.drawText(textobject)
# c.drawString(292, 4*inch, "permenant")
#
# c.setFillColor('#87CEFA')
# c.rect(340,4.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
# textobject0 = c.beginText()
# textobject0.setTextOrigin(342, 4.6*inch)
# c.setFillColor(colors.black)
# textobject0.setFont("Helvetica", 7)
# textobject0.textLines('''
#                            < 425
#                              m
#                             <14000
#                               ft ''')
# c.drawText(textobject0)
# c.drawString(342, 4*inch, "lifting height*")
#
# itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =7 >item number</para>',stylesN)
# rope = Paragraph('<para lindent=5 fontname = "Helvetica-Bold" fontsize =7>rope-@</para>',stylesN)
# brk = Paragraph('<para leftindent = -20 fontname = "Helvetica-Bold" fontsize =7>breaking load<br/>min.</para>',stylesN)
# weight= Paragraph('<para leftindent=25 fontname = "Helvetica-Bold" fontsize =7>weight</para>',stylesN)
# con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =7>construction</para>',stylesN)
#
#
#
# # i = Paragraph('<para> </para>',stylesN)
# mm = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =7 underlineGap = 1>mm</para>',stylesN)
# inc = Paragraph('<para leftindent =30 fontname = "Helvetica" fontsize =7>in</para>',stylesN)
# kN= Paragraph('<para leftindent =40 fontname = "Helvetica" fontsize =7>kN</para>',stylesN)
# lbs = Paragraph('<para leftindent =20 fontname = "Helvetica" fontsize =7>lbs</para>',stylesN)
# kg = Paragraph('<para fontname = "Helvetica" fontsize =7>kg/100m</para>',stylesN)
# lb = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =7>lb/ft</para>',stylesN)
# # c = Paragraph('<para> </para>',stylesN)
# i = Paragraph('<para fontname = "Helvetica" fontsize =7>10699 </para>',stylesN)
# mm1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =7>6.0</para>',stylesN)
# inc1 = Paragraph('<para leftindent =30 fontname = "Helvetica" fontsize =7>5/16</para>',stylesN)
# kN1= Paragraph('<para leftindent =40 fontname = "Helvetica" fontsize =7>42.7</para>',stylesN)
# lbs1 = Paragraph('<para leftindent =20 fontname = "Helvetica" fontsize =7>9.599</para>',stylesN)
# kg1 = Paragraph('<para fontname = "Helvetica" fontsize =7>26.9</para>',stylesN)
# lb1 = Paragraph('<para  leftindent =-15 fontname = "Helvetica" fontsize =7>0.181</para>',stylesN)
# con1 = Paragraph('<para fontname = "Helvetica" fontsize =7 leftindent=-70>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)
#
#
#
#
# data = [[itemn,'',rope,'',brk,weight,'',con],
#             ['',mm,inc,kN,lbs,kg,lb,''],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
#
#             ]
#
# t = Table(data,colWidths=[1.75*cm,1.5*cm,1.5*cm,2.25*cm,2.5*cm,2.5*cm,3.25*cm],rowHeights=0.55*cm)
# t.setStyle(TableStyle([
#
#                             ('LINEABELOW',(0,2),(-2,-2),0.25,colors.black),
#                             ('SPAN',(2,0),(2,0)),
#                             ('SPAN',(3,0),(2,0)),
#                             ('FONTSIZE',(0,1),(-2,-1),20),
#                             ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
#                             ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
#                             ('LEFTPADDING',(2,0),(-1,-1),-20),
#
#
#                             ('LINEBELOW',(0,0),(-1,-1),0.25,colors.black),
#                             # ('ALIGN',(0,0),(-1,-1),'LEFT'),
#
#                             ('VALIGN',(0,0),(-1,-1),'MIDDLE')
#                        ]))
#
# t.wrapOn(c, width,height)
# t.drawOn(c, 190,0.75*inch)
#
#
#
# c.showPage()
c.save()
