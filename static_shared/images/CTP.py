from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm,inch
from reportlab.lib import colors, utils
from reportlab.platypus import Paragraph, Table, TableStyle, Image, Frame, Spacer, PageBreak, BaseDocTemplate, PageTemplate, SimpleDocTemplate, Flowable
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics import barcode
from reportlab.graphics.shapes import *
from reportlab.platypus.flowables import Image as GNAA
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, TA_CENTER
from reportlab.lib.colors import yellow, red, black,white,grey
from reportlab.graphics.shapes import Rect
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.shapes import *
from reportlab.lib.colors import green, gray
from reportlab.platypus import Image
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing
from svglib.svglib import svg2rlg
from PIL import Image, ImageFilter
from reportlab.graphics import renderSVG

c = Canvas("CTP.pdf",pagesize=(letter))

width, height = A4

c.setPageSize((610, 790))

styles = getSampleStyleSheet()
styleN = styles["BodyText"]
stylesN = styles["Normal"]

logo = "brugglifting.svg"
logo1 = "p2.png"
logo2 = "image2.jpg"
logo3 = "image3.svg"
logo4 = "image4.png"
logo5 = "image5.png"
logo11 ="image11.jpg"
logo12 = "image12.png"
logo13 = "a.png"
logo14 = "b.png"
logo15 = "c.png"
logo16 = "d.png"
logo7 ="image7.png"
logo8 = "image8.png"
logo9 = "image9.png"
logo10 ="image10.png"
i1 = "systemprovider.png"
i2 = "customized.png"
i3= "availability.png"
i4="ExpressService.png"
i5="InternationalStandards.png"
i6="Training_specialistWorkshop.png"
log1 = "p2.png"
log2 = "p3.png"
gra1 =  'p2strip.png'
gra2 = "p3strip.png"
ladder= "p3IMG.png"
grasvg2 ="P3STRIP.svg"
grapng2 ="p5strip.png"
f1 = "p1img1.png"
f2 = "p1.png"
f3 = "p1img3rope.png"
f4 = "p1LeadingRopeTechnology.png"
ro1 ="rope.png"
sha = "PageShadowLeftSide.png"
sha1= "PageShadowRightSide.png"

c.drawImage(f2,0*inch,0*inch,width=8.5*inch,height=5.75*inch)

c.drawImage(f1,0*inch,5.75*inch,width=8.5*inch,height=5.75*inch)

c.drawImage(f4,0.5*inch,0.5*inch,width=1.5*inch,height=0.5*inch)

c.drawImage(ro1,0.65*inch,1.5*inch,width=1.25*inch,height=9.5*inch,mask="auto")

drawing = svg2rlg(logo)
scaleFactor = 1/1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 400, 10.2*inch)

c.setFont("Helvetica-Bold",50)
c.setFillColor('#000000')
c.drawString(185, 5.85*inch, "CTP")

c.setFont("Helvetica",15)
c.setFillColor('#000000')
c.drawString(300, 5.85*inch, "COATED TRACTION ROPES")

c.showPage()

c.drawImage(logo1,0*inch,7.8*inch,width=8.5*inch,height=5*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.25*inch)

c.drawImage(gra1,0*inch,7.5*inch,width=8.5*inch,height=1.4*inch)

c.drawImage(i1,0.65*inch,6.4*inch,width=0.6*inch,height=0.6*inch)
c.drawImage(i2,0.65*inch,5.15*inch,width=0.6*inch,height=0.6*inch)
c.drawImage(i3,0.65*inch,3.9*inch,width=0.6*inch,height=0.6*inch)
c.drawImage(i4,0.65*inch,2.7*inch,width=0.6*inch,height=0.6*inch)
c.drawImage(i5,0.65*inch,1.6*inch,width=0.6*inch,height=0.6*inch)
c.drawImage(i6,0.65*inch,0.65*inch,width=0.6*inch,height=0.6*inch)

c.setFont('Helvetica-Bold', 21)
c.drawString(50, 8.1*inch, "SERVICES")

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch,  6.9*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
System Provider''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 6.65*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
We offer to you a wide assortment of elevator ropes, accessories and tools to meet all
of your requirements. We supply you with complete solutions or individually combined
components as individual or pre-assembled parts to suit your needs.''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 5.65*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Customized''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 5.4*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Our wide assortment of elevator ropes, accessories and tools provides nearly all products
required for your applications. If none of the articles depicted in the catalog solves
your problem, or if your elevator is to meet specific requirements, we will be glad to
advise you and to develop customized solutions together with you.''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 4.4*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Availability''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 4.15*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Due to our two production facilities located in Switzerland and China, as well as due to
our global network of warehouse locations, our products will be delivered to your fac-
tory or your construction site within a very short time. Please contact us if you have any
questions regarding deadlines, individual deliveries and specific projects.''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 3.15*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Express Service''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 2.9*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
In urgent cases we provide the required materials ex works within the hour and ship
it to you as quickly as possible by courier all over the world.
                        ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 2.05*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
International Standards''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 1.8*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
RUGG LIFTING is certified according to ISO 9001:2015 and ISO 14001:2015
                        ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 1.1*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Training/Specialist Workshops''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.55*inch, 0.9*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Our aim is to ensure that you will enjoy an optimal use and an increase service life of
your elevator ropes. Make use of our offering of qualified and customized training
units for your staff.''')
c.drawText(textobject)

gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "2")

c.showPage()

c.drawImage(log2,0*inch,7.8*inch,width=8.5*inch,height=5*inch)

drawing = svg2rlg(grasvg2)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,7.8*inch)

c.drawImage(grapng2,0*inch,7.5*inch,width=8.5*inch,height=0.3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

p = Paragraph('''<para fontsize=10  leading=13 align="justify">Developed as a world s first, CTP combines technological innovations into
a state of the art plastic coated rope specifically designed for the elevator
industry.  </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=4.7*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,50,6.7*inch)

p = Paragraph('''<para fontsize=10  leading=13 align="justify">Approved for traction sheaves with a diameter of only 115 mm, CTP  ropes
have been already installed in 60,000 elevators all over the world.
Tested by means if simulation In the laboratory and under real-life conditions,
CTP  meets highest demands on function and efficiency. </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=4.7*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,50,5.8*inch)

c.drawImage(ladder,0.8*inch,2.3*inch,width=7*inch,height=3.2*inch)

c.drawImage(logo4,6.7*inch,0.85*inch,width=1*inch,height=1*inch)

c.drawImage(logo5,5.5*inch,0.85*inch,width=1*inch,height=1*inch)

gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, 7.75*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(580, 0.15*inch, "3")

c.showPage()

bg = "img1.jpg"
product = "img8.png"
wire = "img7.png"
l1 = 'img5.png'
l2= 'img6.png'
l3= 'img4.png'
log3="p4.png"
log4="p5.png"
gra3 ="p4strip.png"
gra5="p5strip.png"
box="P4fOURbOXES.png"
grasvg3 ="P4STRIP.svg"


c.drawImage(log3,0*inch,7.4*inch,width=8.5*inch,height=4*inch, )

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.25*inch)

# c.drawImage(gra3,0*inch,7.25*inch,width=8.5*inch,height=1.4*inch)
c.drawImage(grapng2,0*inch,7.375*inch,width=8.5*inch,height=0.3*inch)

drawing = svg2rlg(grasvg3 )
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,7.4*inch)

c.setFont('Helvetica-Bold', 27.5)
c.drawString(50, 7.75*inch, "CTP")

c.setFont('Helvetica', 12.5)
c.drawString(225, 7.45*inch, "COATED TRANSMISSION PRODUCTS")

c.setFont("Helvetica-Bold", 20)
# c.drawString(30,515, "CTP")
textobject = c.beginText()
textobject.setTextOrigin(2.8*inch, 6.5*inch)
textobject.setFont("Helvetica-Bold", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Steel core rope with coated transmission, 6 strands, separate lay''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(2.8*inch, 6.35*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demands on elongation, riding comfort and service life
                    ''')
c.drawText(textobject)

c.drawImage(box,4.65*inch,5.4*inch,width=0.6*inch,height=0.6*inch)
c.drawImage(box,3.65*inch,5.4*inch,width=0.6*inch,height=0.6*inch)
c.drawImage(box,2.65*inch,5.4*inch,width=0.6*inch,height=0.6*inch)
c.drawImage(box,5.65*inch,5.4*inch,width=0.6*inch,height=0.6*inch)



c.drawText(textobject)
data = [
   ['item-no', 'rope ', 'breaking load',  'weight' , "construction"],
   ['',   'mm',         'kN',         'kg/100m',     ' ',     ],
   ['73107',   '6.5',        '23.6',        '11.0',    ' ',     '6x19seal-SES(IWRC)'],
   ['10982',   '6.5',        '23.6',        '11.0',    ' ',     '6x19seal-SES(IWRC)'],


   ]

t5 =  Table(data,colWidths=[2.2* cm, 2.2* cm, 2.2 * cm,2.2* cm, 2.2* cm] ,rowHeights=5*mm)
t5.setStyle(TableStyle([
                    ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                    ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 7),
                    ('FONTSIZE', (0, 1), (-1, -1), 6),
                    ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                    ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                    ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (4, 1), (-1,-1), -40),
                    ('ALIGN', (4, 0), (-1,-1), 'LEFT'),
                    ('BACKGROUND', (1,0), (1, 1), '#DCDCDC'),
                    ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                     ]))

t5.wrapOn(c, 150, 190)
t5.drawOn(c, 2.5*inch,3.65*inch)
c.drawImage(l3,185,15,width=3.25*inch,height=2.8*inch,mask='auto')

c.drawImage(product,35,380,width=1.5*inch,height=1.5*inch,mask='auto')
c.drawImage(wire,65,0,width=0.8*inch,height=4.65*inch,mask='auto')

textobject1 = c.beginText()
textobject1.setTextOrigin(2.5*inch, 3.45*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7.5)
textobject1.textLines('''*  There is no limitation on lifting heights however experience to date is limited to installations below 150m.
                            Certified and in Production. Available in Stock length and in cut lengths.
                            Rope diameter-tolerances according to ISO 2768-1 class m (middle).
                           ''')
c.drawText(textobject1)

textobject = c.beginText()

textobject1 = c.beginText()
textobject1.setTextOrigin(1.95*inch, 2.6*inch)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''
                      ** E-Module tested according to DIN 18800. The specified E-Module is tested with 30-40% of MBL.
                ''')




d = c.beginPath()
# d.rect(1.95*inch,4.25*inch,0.6*inch,0.6*inch)
d.rect(2.75*inch,5.25*inch,0.6*inch,0.6*inch)
d.rect(3.55*inch,5.25*inch,0.6*inch,0.6*inch)
d.rect(4.35*inch,5.25*inch,0.6*inch,0.6*inch)
d.rect(107, 7.25*inch, 12*inch, 0.2*inch)
d.rect(-20, 7.25*inch, 1.765*inch, 0.8*inch)

# for box1
c.setFont("Helvetica-Bold", 7)
c.drawString(2.75*inch,5.75*inch, "125.000")
c.setFont("Helvetica", 7)
c.drawString(2.8*inch,5.55*inch, "N/mm2")
c.drawString(2.7*inch,5.2*inch, "E-Module **")

# for box2
c.setFont("Helvetica-Bold", 7)
c.drawString(3.8*inch,5.75*inch, "0.104")
c.setFont("Helvetica", 7)
c.drawString(3.85*inch,5.55*inch, "%")
c.drawString(3.85*inch,5.2*inch, "Elastic")
c.drawString(3.75*inch,5.05*inch, "elongation")

# for box3
c.setFont("Helvetica-Bold", 7)
c.setFillColor(colors.black)
c.drawString(4.85*inch,5.75*inch, "0.13")
c.setFont("Helvetica", 7)
c.drawString(4.9*inch,5.55*inch, "%")
c.drawString(4.7*inch,5.2*inch, "Permanent")
c.drawString(4.75*inch,5.05*inch, "elongation")

# for box4
c.setFont("Helvetica", 7)
c.drawString(5.9*inch,5.75*inch, "<75")
c.drawString(5.95*inch,5.5*inch, "m")
c.drawString(5.7*inch,5.2*inch, "Lifting height *")


gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "4")

c.showPage()

c.drawImage(log4,0*inch,7.4*inch,width=8.5*inch,height=4*inch)

c.drawImage(gra5,0*inch,7.4*inch,width=8.5*inch,height=0.3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 6.5*inch)
textobject.setFont("Helvetica", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    A world first, CTP  unites technological innovation for the highest demands.
                    This high-end rope is unbeatable in terms of function and efficiency''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 6.05*inch)
textobject.setFont("Helvetica-Bold", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Reduce your total cost by up to 40%.
                    ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 5.85*inch)
textobject.setFont("Helvetica", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    A smaller rope diameter and a smaller drive allow for a reduction of capital and operating cost.
                    ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 5.55*inch)
textobject.setFont("Helvetica-Bold", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Reduce your maintenance cost by up to 100%.
                    ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 5.35*inch)
textobject.setFont("Helvetica", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    CTP is a self-contained system which requires neither lubrication and minimal maintenance.
                    ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 5.1*inch)
textobject.setFont("Helvetica-Bold", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Enjoy a clearly improved travelling comfort
                    ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 4.9*inch)
textobject.setFont("Helvetica", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    The polymer coating eliminates or strongly absorbs vibrations, which significantly contributes to a smooth running.
                    ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 4.7*inch)
textobject.setFont("Helvetica-Bold", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Increase the service life
                    ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 4.7*inch)
textobject.setFont("Helvetica", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    As there is negligible wear between the traction sheave and the rope, the frequency of rope replacement is much reduced.
                    ''')


c.drawText(textobject1)
c.setFont("Helvetica",9)




c.drawImage(l1,130,170,width=2.5*inch,height=2.15*inch,mask='auto')
c.setFont("Helvetica-Bold", 5)

c.drawString(2.15*inch, 2.25*inch, "Diagramm der festgelegten")
c.drawString(2.15*inch, 2.1*inch, "Rillen fur CTP 6.5mm")

c.drawImage(l2,300,170, width=2.5*inch,height=2.15*inch,mask='auto')
c.drawString(4*inch, 2.25*inch, "Diagramm der festgelegten")
c.drawString(4*inch, 2.1*inch, "Rillen fur CTP 8.1mm")

textobject = c.beginText()
textobject.setTextOrigin(0.75*inch, 1.75*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Main data of traction sheave / deflection
                    ''')
c.drawText(textobject)


data = [
    ['FUR', 'Seil-@', 'Stahlseil-@',  'Reibungs-' , "Seilgeschwindigkeit","scheiben-@","Treibscheibe","Rillenform","Abelenkscheibe"],
   ['Art.-Nr', '', '',  'Koeffzient' , "max","","Material","","Material"],
   ['',   'mm',  'mm','','m/s'   ,'mm'   '',         'hulbrund@mm',     ' ',     ],
   ['10982',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],
   ['73106',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],


   ]

t5 = Table(data, colWidths=[0.75* cm, 1* cm, 1 * cm,
                            2.5* cm, 2.5* cm,2.5* cm,2.5* cm,2.5* cm, ],rowHeights=5.5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),

                    ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                    ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                    ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                    ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(0, 1), "Helvetica-Bold"),
                    ('FONTNAME', (1,0),(3,1), "Helvetica-Bold"),
                    ('FONTNAME', (4,1),(6,1), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(8,1), "Helvetica-Bold"),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                    # ('ALIGN', (1, 0), (1, 7), 'CENTER'),
                    # ('ALIGN', (2, 0), (-1, 7), 'CENTER'),
                    # ('ALIGN', (3, 0), (-1, 7), 'LEFT'),
                    # ('ALIGN', (4, 0), (-1, 7), 'LEFT'),
                    # ('ALIGN', (5, 0), (-1, 7), 'CENTER'),
                    # ('VALIGN', (5, 0), (-1, 7), 'BOTTOM'),
                    # ('LEFTPADDING', (0, 0), (-1, -1), -20),
                    #  ('LEFTPADDING', (1, 0), (-1, -1),10),
                    #  ('LEFTPADDING', (2, 0), (-1, -1), -30),
                    #  ('LEFTPADDING', (3, 0), (-1, -1), -30),
                    #  ('LEFTPADDING', (5, 0), (-1, -1), -30),
                    # ('LEFTPADDING', (4, 0), (-1, 9), -30),
                    #  ('LEFTPADDING', (5, 0), (-1, 9), -70),
                    ('BACKGROUND', (1,0), (1, 1), '#DCDCDC'),
                    ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                    ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                    # ('BACKGROUND', (1,6), (1, 7), '#DCDCDC'),
                     ]))

t5.wrapOn(c, 20, 170)
t5.drawOn(c, 0.75*inch,0.6*inch)


textobject1 = c.beginText()
textobject1.setTextOrigin(0.72*inch, 0.49*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''* Higher speeds must be tested..
                           ''')
c.drawText(textobject1)

textobject1 = c.beginText()
textobject1.setTextOrigin(0.75*inch, 0.38*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''Tolerances according to ISO 2768-1 class m (middle).
                           ''')
c.drawText(textobject1)

textobject1 = c.beginText()
textobject1.setTextOrigin(0.8*inch, 0.27*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines(''' The CTP  rope is only certified for usage on traction and deflector sheaves that meet the requirements outlined above.''')
c.drawText(textobject1)


gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, 7.75*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(580, 0.15*inch, "5")

c.showPage()

logo = "brugglifting.svg"

bg = "image1.jpg"
product = "image3.jpg"
b = "1.png"
am = "AM.png"
j = "D.png"
log5="p6.png"
gra6 = "p6strip.png"

c.drawImage(log5,0*inch,7.25*inch,width=9*inch,height=4*inch)
drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.25*inch)

c.drawImage(b,30,0,width=2.2*inch,height=6.8*inch,mask='auto')

c.drawImage(gra6,0*inch,7.25*inch,width=8.5*inch,height=0.85*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

c.setFont('Helvetica-Bold', 22.5)
c.drawString(50, 7.6*inch, "APAG")

c.setFont('Helvetica', 13)
c.drawString(125, 7.6*inch, "Threaded Swaged Sockets")


textobject = c.beginText()
textobject.setTextOrigin(3.2*inch, 6.5*inch)
textobject.setFont("Helvetica-Bold", 12)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Product Data''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(3*inch, 6.25*inch)
textobject.setFont("Helvetica", 9)
lyrics = ['- APAG-end connections are TUV tested and approved according to ENB1',
          '- APAG-end connections transmits 80 of minimal breaking load of traction rope',

          ]
for line in lyrics:
    textobject.textLine(". %s" %(line))

c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(3.2*inch, 5.7*inch)
textobject.setFont("Helvetica-Bold", 12)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    				 Advantages''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(3*inch, 5.475*inch)
textobject.setFont("Helvetica", 9)
lyrics = ['- simple, fast and safe end terminations ',
          '- shortened installation time, since no mounting of end connections by customers ',
          '- no special tools required ',
          '- the compact type enables a very tight arrangement of ropes ',
          '  and parallel running ropes ',
          '- simple securing against rotation ',
          '- position of pilot hole for rope end ',
          '- quiet operation because there are no individual parts ',

          ]
for line in lyrics:
    textobject.textLine(". %s" %(line))

c.drawText(textobject)
c.setFont("Helvetica-Bold", 7)

c.drawString(3.2*inch, 3.1*inch, "For use with CTP  6.5 mm")

data = [

   ['Art.-Nr', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
   ['',   '',  '','',''      'Abmessungen in mm',         '',     ' ',     ],
   ['10209',   'M 10', '13','9','7','240','150','66.0','16.6'],


   ]

t5 = Table(data, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                            1.25* cm, 1.25* cm,1.25* cm,1.25* cm,1.25* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                     ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                     ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                     ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                     ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),

                    # ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                    # ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                     ]))

t5.wrapOn(c, 30, 300)
t5.drawOn(c, 3.2*inch,2.25*inch)
c.setFont("Helvetica-Bold", 7)
c.drawString(3.2*inch, 1.7*inch, "Fur den Einsatz mit CTP 8.1mm")

data = [

   ['Art.-Nr', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
   ['',   '',  '','',''      'Abmessungen in mm',         '',     ' ',     ],
   ['10113',   'M 10', '13','9','7','240','150','66.0','16.6'],


   ]

t5 = Table(data, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                            1.25* cm, 1.25* cm,1.25* cm,1.25* cm,1.25* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                     ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                     ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                     ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                     ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),

                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                     ]))

t5.wrapOn(c, 30, 300)
t5.drawOn(c, 3.2*inch,0.9*inch)


gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "6")

c.showPage()

logo = "brugglifting.svg"
bg = "image1.jpg"
product = "image3.jpg"
b = "1.png"
am = "AM.png"
j = "D.png"
log6="p7.png"
gra7 = "p7STRIP.png"
dimg = "p7soccerimages.png"
grasvg4= "p7STRIP.svg"

c.drawImage(log6,0*inch,7.25*inch,width=8.5*inch,height=4*inch)

# c.drawImage(gra1,0*inch,7.5*inch,width=8.5*inch,height=1.7*inch)

c.drawImage(grapng2,0*inch,7.25*inch,width=8.5*inch,height=0.3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(grasvg4)
scaleFactor = 1./1.3
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,7.25*inch)

c.drawImage(dimg,70,100,width=2.8*inch,height=3*inch,mask='auto')

c.setFont('Helvetica-Bold', 18.5)
c.drawString(50, 7.6*inch, "WEDGE SOCKET")

c.setFont('Helvetica', 13)
c.drawString(210, 7.6*inch, "Symmetrical [EN 13411-7]")


gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, 7.75*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(580, 0.15*inch, "7")

textobject = c.beginText()
textobject.setTextOrigin(4.5*inch, 6.65*inch)
textobject.setFont("Helvetica-Bold", 12)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Product Data''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(4.4*inch, 6.375*inch)
textobject.setFont("Helvetica", 9)
lyrics = [' wedge socket welded, steel zinc-plated',
          ' incl. wedge, bolt and safety pins pre-assembled',
          ' wedge socket transmits 80 of minimal breaking load',
          '  of traction rope or governor rope',
          ' eylet bolt welded, steel zinc-plated',
          ' in connection with the wedge socket the eyelet bolt transmits',
          '  80 of the minimal breaking load of the elevator rope',
          ' for mounting and operation the explanations in appendix B',
          '  of the norm EN 13411-7 are valid',
          ]
for line in lyrics:
    textobject.textLine(". %s" %(line))

c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(4.5*inch, 4.65*inch)
textobject.setFont("Helvetica-Bold", 12)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Advantages''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(4.4*inch, 4.4*inch)
textobject.setFont("Helvetica", 9)
lyrics = ['- can be assembled safely and simply on-site ',
          '- springs, buffers and other accessories can',
          '  be mounted individually',
]
for line in lyrics:
    textobject.textLine(". %s" %(line))
c.drawText(textobject)

c.setFont("Helvetica-Bold", 7)
c.drawString(4.5*inch, 3.5*inch, "Fur den Einsatz mit CTP 6.5 mm")

data = [

   ['Art.-Nr','', 'Seil-@', 'd',  'd1',"L1","L2","L3"],
   ['',   '','mm',  '','',''      '',         '',     ' ',     ],
   ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
   ['64140', 'AM', '5,0-6,5','M 10', '','265','180'],
   ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']


   ]

t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                            1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                     ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                     ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                     ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                     ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                    ('BACKGROUND', (2,0),(2, 5), '#DCDCDC')
                     ]))

t5.wrapOn(c, 30, 300)
t5.drawOn(c, 4.5*inch,2.4*inch)
textobject1 = c.beginText()
textobject1.setTextOrigin(4.5*inch, 2.3*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 6)
textobject1.textLines(''' Weitere Nennfestigkeiten und/oder Durchmesser
                        Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage   ''')
c.drawText(textobject1)
c.setFont("Helvetica-Bold", 7)

c.drawString(4.5*inch, 1.9*inch, "Fur den Einsatz mit CTP 8.1mm")

data = [

   ['Art.-Nr','', 'Seil-@', 'd',  'd1',"L1","L2","L3"],
   ['',   '','mm',  '','',''      '',         '',     ' ',     ],
   ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
   ['64140', 'AM', '5,0-6,5','M 10', '','265','180'],
   ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']


   ]

t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                            1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                     ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                     ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                     ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                     ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                    ('BACKGROUND', (2,0),(2, 5), '#DCDCDC'),


                     ]))

t5.wrapOn(c, 30, 300)
t5.drawOn(c, 4.5*inch,0.8*inch)

textobject1 = c.beginText()
textobject1.setTextOrigin(4.5*inch,0.7*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines(''' Weitere Nennfestigkeiten und/oder Durchmesser
                        Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage   ''')
c.drawText(textobject1)

d = c.beginPath()
d.rect(-20, 7.25*inch, 10*inch, 0.6*inch)
d.rect(700, 7.25*inch, 12.5*inch, 0.2*inch)
c.clipPath (d, stroke=0)
# c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
c.setFont("Helvetica", 10)
c.drawString(90,450, "Anpress-Ausssengewinden")
c.setFont("Helvetica-Bold", 18)
# c.drawString(30,535, "APAG")
c.setFont("Helvetica-Bold", 18)
c.drawString(400,450, "SEILSCHLOSS")
c.setFont("Helvetica", 10)
c.drawString(530,450, "symmetrisch [EN-13411-7]")





c.showPage()


logo = "brugglifting.svg"
logo11 ="image11.jpg"
logo12 = "image12.png"
logo13 = "a.png"
logo14 = "b.png"
logo15 = "c.png"
logo16 = "d.png"
log7="p8.png"
log8="p9.png"
gra8 = "p8strip.png"
grasvg8 = "P8STRIP.svg"
table = "p8table.png"
table1 = "P8tABLEbox.svg"
table2 ="p9table.png"

c.drawImage(log7,0*inch,7.25*inch,width=8.5*inch,height=4*inch)
drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.25*inch)

# c.drawImage(gra8,0*inch,7.25*inch,width=8.5*inch,height=1.4*inch)
#
c.drawImage(grapng2,0*inch,7.25*inch,width=8.5*inch,height=0.25*inch)
#

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')
c.drawImage(table,0.5*inch,0.55*inch,width=8.25*inch,height=2.5*inch)

drawing = svg2rlg(grasvg8)
scaleFactor = 1./1.3
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,7.25*inch)

gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "8")




c.setFont('Helvetica-Bold', 20.5)
c.drawString(50, 7.6*inch, "INSPECTION MANUAL CTP")

p = Paragraph('''<para fontsize=10  leading=13 align="justify">This document shall serve as practical guidance for CTP  rope
inspections out in the field. It covers the official discard crite-
ria of the CTP   rope as well as specific fields of inspection in
a running elevator system which are most critical to rope life. </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,5.8*inch)


textobject = c.beginText()
textobject.setTextOrigin(0.5*inch,  5.5*inch)
c.setFont('Helvetica-Bold', 11)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
1. Discard criteria of the CTP rope''')
c.drawText(textobject)

p = Paragraph('''<para fontsize=10  leading=13 align="justify">Brugg Lifting is applying a simple replacement criteria that
limits the use of the CTP   rope after a defined number of
cycles or trips (1) . This method of appraisal is therefore based
on the level of usage.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,4.68*inch)

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch,  5.5*inch)
c.setFont('Helvetica-Bold', 11)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
1. Discard criteria of the CTP rope''')
c.drawText(textobject)

p = Paragraph('''<para fontsize=10  leading=13 align="justify">This discard criterion forms part of all CTP   rope certifications,
which have been issued by LIFTINSTITUUT  The calculation of
maximum allowed trips is described under chapter  conditions
as follows:</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,3.8*inch)


p = Paragraph('''<para fontsize=10  leading=13 align="justify"> - The defined maximum number of trips shall be divided by
the number of pulleys which are passed most often by the
bended rope</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,3.2*inch)

c.drawImage(logo12,4.35*inch,5.75*inch,width=1.5*inch,height=1*inch)


p = Paragraph('''<para fontsize=8  leading=10 align="justify">Intact ropes in elevator shaft. Note
that there is no color change of
coating during the entire rope life.
The rope remains dark black.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=2*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,430,6*inch)




p = Paragraph('''<para fontsize=9  leading=10 align="justify">During inspection the condition of the ropes should always be
checked for any abnormal wear or damage (2) . Following is the
table showing the five typical rope issues which can occur in
an elevator system and the according actions, which must be
taken by the elevator maintenance company in such a case.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,325,4.7*inch)

p = Paragraph('''<para fontsize=9  leading=10 align="justify">(1)
	Every change of direction will be counted as a trip or cycle by the lift cont-
roller. Important:  trip  or  cycle  should NOT be confused with  starts .</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,325,4.15*inch)


p = Paragraph('''<para fontsize=9  leading=10 align="justify">(2)
	The abnormal wear or damages presented below could be caused by
overloading, unequal rope tension, severe shock, loading, torsional un-
balance, bad rope alignment, etc. The maximum number of broken wires
defined in the instructions is based on standards (UNE-EN, ISO, DIN) as
well as on verification by testing samples.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,325,3.15*inch)


# p1 = ['Beschreibung der Kunststoffummantelung']
#
#
# c.setFillColor('#EEE8AA')
# c.rect(18, 0.68*inch, 8*inch, 2.4*inch,stroke=0,fill=1)
#
# c.drawString(30,150,'Ablegekriterien')


# textobject = c.beginText()
# textobject.setTextOrigin(0.4*inch,  2.9*inch)
# c.setFont('Helvetica-Bold', 9)
# c.setFillColorRGB(0,0,0)
# textobject.textLines('''
# Ablegekriterien''')
# c.drawText(textobject)
#
#
# # Headers
# hdescrpcion = Paragraph('''<para align = "RIGHT">|</para>''', stylesN)
# hpartida = Paragraph('<para fontsize=7 align = "CENTER"><b>A</b></para>', stylesN)
# h1 = Paragraph('''<para align = "LEFT">|</para>''', stylesN)
# hcandidad = Paragraph('<para fontsize=7 align = "CENTER" leftindent = -5 align="LEFT"><b>B</b></para>', stylesN)
# h2 = Paragraph('''|''', stylesN)
# hprecio_unitario = Paragraph('<para fontsize=7 leftindent = -40 align="LEFT"><b>C</b></para>', stylesN)
# h3 = Paragraph('''<para  leftindent = -130 align = "CENTER">|</para>''', stylesN)
# hprecio_total = Paragraph('<para fontsize=7 align="CENTER" leftindent = -140 align="CENTER"><b>D</b></para>', stylesN)
# h4 = Paragraph('''<para  align = "LEFT" leftindent = -70>|</para>''', stylesN)
# hprecio_empty1 = Paragraph(''+''' ''', stylesN)
# hprecio_empty2 = Paragraph(''+''' ''', stylesN)
#
#
# descrpcion = Paragraph('<para fontsize=5><b>Problem</b></para>', styleN)
# partida = Paragraph('<para fontsize=5>Beschadigung der <br\>Kunststoffummantelung</para>', styleN)
# candidad = Paragraph('<para fontsize=5>Drahbruch</para>', styleN)
# precio_unitario = Paragraph('<para fontsize=4>Massive Bruche von Drahten</para>', styleN)
# precio_total = Paragraph('<para fontsize=4>Litzenbrunch</para>', styleN)
# precio_empty1 = Paragraph('<para fontsize=4>Seil aus der Rille</para>', styleN)
# precio_empty2 = Paragraph('<para fontsize=4> Image1 </para>', styleN)
# # precio_empty3 = Paragraph('<para fontsize=4> Image2 </para>', styleN)
#
#
# descrpcio = Paragraph('<para fontsize=5><b>Beschreibung</b></para>', styleN)
# partid = Paragraph('<para fontsize=4>Kunststoffummantelung ist so <br/>abgenutzt, dass der mettallische</para>', styleN)
# candida = Paragraph('<para fontsize=4>Mehr als 10 Drahte ragen<br/>aus dem TPU-Mantel</para>', styleN)
# precio_unitari = Paragraph('<para fontsize=4>Mehr als 3 Drahte ragen aus   dem</para>', styleN)
# precio_tota = Paragraph('<para fontsize=4>spezifischer Seilbruch</para>', styleN)
# precio_empty = Paragraph('<para fontsize=4>Seil ist aus seiner<br/>ursprunglichen Rille</para>', styleN)
# # precio_empty = Paragraph('<para fontsize=4> Image1 </para>', styleN)
#
#
# descrpci = Paragraph('<para fontsize=5><b>Korrektur-massnahme</b></para>', styleN)
# parti = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
# candid = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
# precio_unitar = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
# precio_tot = Paragraph('<para fontsize=4>Bericht anBericht an<br/>Brugg Lifting senden.</para>', styleN)
# precio_empt = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
# precio_empt = Paragraph('<para fontsize=4> Image1 </para>', styleN)
#
#
# descrpc = Paragraph('<para fontsize=5><b>Zeitskala</b></para>', styleN)
# part = Paragraph('<para fontsize=4>< 2 Monate</para>', styleN)
# candi = Paragraph('<para fontsize=4>2 Monate</para>', styleN)
# precio_unita = Paragraph('<para fontsize=4>umgehend</para>', styleN)
# precio_to = Paragraph('<para fontsize=4>umgehend</para>', styleN)
# precio_emp = Paragraph('<para fontsize=4>umgehend</para>', styleN)
# # precio_emp = Paragraph('<para fontsize=4> Image1 </para>', styleN)
#
#
# data= [[hdescrpcion, hpartida,h1,hcandidad,h2,hprecio_unitario,h3, hprecio_total,h4, hprecio_empty1,hprecio_empty2],
#        [descrpcion, partida, candidad, precio_unitario, precio_total,precio_empty1],
#        [descrpcio,partid,candida,precio_unitari,precio_tota,precio_empty],
#        [descrpci,parti,candid,precio_unitar,precio_tot,precio_empt],
#        [descrpc,part,candi,precio_unita,precio_to,precio_emp]]
#
# table = Table(data, colWidths=[1.6 * cm, 2.5 * cm, 2 * cm,
#                                2.25* cm, 2.5 * cm, 2*cm,1*cm,1.45*cm],rowHeights =12*mm)
#
# table.setStyle(TableStyle([
#                             ('LINEABOVE',(0,1),(-1,1),0.25,colors.black),
#                             ('SPAN',(2,0),(2,0)),
#                             ('LINEBELOW',(0,1),(5,4),0.25,colors.black),
#                             ('LINEBELOW',(0,4),(-1,-1),0.25,colors.black),
#                             ('FONTSIZE', (0, 1), (-1, -1), 5),
#                        ]))
#
# table.wrapOn(c, width, height)
# table.drawOn(c, 17, 60, cm)

# c.drawImage(logo13,6.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
# c.drawImage(logo14,6.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
# c.drawImage(logo15,7.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
# c.drawImage(logo16,7.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)




p = c.beginPath()
p.rect(-20, 7.25*inch, 4*inch, 0.9*inch)
p.rect(268, 7.25*inch, 8*inch, 0.2*inch)

c.clipPath(p, stroke=0)
# c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
c.setFont('Helvetica-Bold', 17)
c.setFillColor(colors.black)
c.drawString(20,465,"CTP PRUFHANDBUCH")


c.showPage()


c.drawImage(log8,0*inch,7.25*inch,width=8.5*inch,height=4*inch)

c.drawImage(gra1,0*inch,7.25*inch,width=8.5*inch,height=0.3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

# c.drawImage(table,0.5*inch,0.55*inch,width=8.25*inch,height=2.5*inch)

# drawing = svg2rlg(table1)
# scaleFactor = 1/2.25
# drawing.width *= scaleFactor
# drawing.height *= scaleFactor
# drawing.scale(scaleFactor, scaleFactor)
# renderPDF.draw(drawing, c, 30,4.25*inch)

c.drawImage(table2,0*inch,0.55*inch,width=4.15*inch,height=2.5*inch)

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch,  6.75*inch)
c.setFont('Helvetica-Bold', 10)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
2. Elevator specifications''')
c.drawText(textobject)

p = Paragraph('''<para fontsize=10  leading=13 align="justify">Only with the help of specific elevator data are we able to
analyze the rope regarding traction capabilities, bending
fatigue performance, etc. Therefore in case of support please
contact your Brugg Lifting representative.  </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,5.85*inch)

# c.setFillColor('#EEE8AA')
# c.rect(30, 3.35*inch, 3.9*inch, 2.25*inch,stroke=0,fill=1)

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 5.4*inch)
c.setFont('Helvetica-Bold', 10)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Safety Instructions
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 5.2*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Most of these inspections must be performed on a
running elevator (in maintenance mode) Do never
perform below listed measurements without trained an
authorized elevator personnel. Be sure to be secured
at all times when standing on top of the lift car.
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 4.15*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
CTP ropes should not be operated if oil or water is on
the surface of the rope. If water or oil is on the surface
of the rope and then comes into contact with the traction
sheave, it will reduce traction capability and cause slippage.
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(4.9*inch,  6.75*inch)
c.setFont('Helvetica-Bold', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
3. Visual inspection''')
c.drawText(textobject)

p = Paragraph('''<para fontsize=10  leading=13 align="justify">In addition external factors that could have a negative impact
on the rope shall be evaluated. Before doing detailed mea-
surements we recommend to first visually check the outside
appearance of the rope. Particular attention must be paid to
the rope coating: </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,325,5.69*inch)


textobject = c.beginText()
textobject.setTextOrigin(4.5*inch, 5.45*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)



dat = [
'Broken wires piercing out of the coating material',
'Irregularities regarding rope coating surface',
'Scratches, tear or fractures on the rope coating',
'Abrasion of the coating',
'Dust, oil, water etc. on the rope coating',
'Rope kinks',
]

for i in dat:
    textobject.textLines("- %s"%(i))

c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(4.5*inch, 4.2*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
The following points should also be evaluated:
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(4.5*inch, 3.8*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)

data = [
'Rope touching elevator parts or shaft',
'Ropes touching each other due to electro-static charge',
'Rope vibration during operation',
'Insufficient alignment of traction sheave',
]

for i in data:
    textobject.textLines("- %s"%(i))

c.drawText(textobject)


p = Paragraph('''<para fontsize=10  leading=13 align="justify">Whenever possible pictures of the rope should be taken
during inspection (also in the case of intact ropes). Also
traction sheave, diverting pulley and end terminations
should be photographed. </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,325,2.3*inch)

gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, 7.75*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(580, 0.15*inch, "9")


c.showPage()


logo11 ="image11.jpg"
logo = "brugglifting.svg"
logo6 = "image6.jpeg"
logo7 ="image7.png"
logo8 = "image8.png"
logo9 = "image9.png"
logo10 ="image10.png"
log9="p10.png"
gra10="P10STRIP.svg"

c.drawImage(log9,0*inch,7.25*inch,width=8.5*inch,height=4*inch)
drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.25*inch)

# c.drawImage(gra10,0*inch,7.25*inch,width=8.5*inch,height=1.4*inch)

c.drawImage(grapng2,0*inch,7.25*inch,width=8.5*inch,height=0.25*inch)
#

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(gra10)
scaleFactor = 1./1.3
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,7.25*inch)


textobject = c.beginText()
textobject.setTextOrigin(0.5*inch,  6.75*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
4.Inspection of fleet angle''')
c.drawText(textobject)

c.setFont('Helvetica-Bold', 21.5)
c.drawString(50, 7.5*inch, "INSPECTION MANUAL CTP")

gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "10")


p = Paragraph('''<para fontsize=10  leading=13 align="justify">The allowable fleet angle is 0.5 . For the CTP   8.1 this angle
can be increased up to a maximum of 1.0  as long as the
number of trips is reduced limited to 2 400 000 and divided
by the number of pulleys passing the most bended part of
the rope (this does NOT apply for the CTP   6.5). Fleet angle
allowed (in accordance with our certificate) is 0.5 . If the fleet
angle is too big it will induce torsion into the rope. This effect
also applies to conventional ropes but is even more pronounced
in the CTP   rope.  </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,5*inch)


p = Paragraph('''<para fontsize=10  leading=13 align="justify">The most critical positions are when the cabin is at the top
floor (maximum fleet angle between cabin and tractions
sheave deflecting pulley) and when the cabin is at the lowest
floor (maximum fleet angle between counter weight and
traction sheave deflecting pulley). It is fairly difficult to directly
measure the fleet angle between rope and sheave. For this
reason we recommend an indirect more practical way of
measuring the fleet angle (please see below).  </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,3.2*inch)


p = Paragraph('''<para fontsize=10  leading=13 align="justify">To get a rough estimate on the fleet angle measure follo-
wing points(illustratedon an elevator with 1:1 suspension): </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,2.6*inch)


p = Paragraph('''<para fontsize=10  leading=13 align="justify">Distance from traction sheave to end termination on lift
car (when cabin is at the very top)</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,2.1*inch)


p = Paragraph('''<para fontsize=10  leading=13 align="justify">Distance from rope to rope at rope termination on elevator
cabin and on traction sheave. Distance from rope to rope on
traction sheave (groove to-groove distance) and on rope
termination on counter weight </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,1.2*inch)

p = Paragraph('''<para fontsize=10  leading=13 align="justify">Distance from traction sheave to end termination on
counter weight (when cabin is at the very bottom) </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,0.7*inch)

c.drawImage(logo7,4.8*inch,1.1*inch,width=1.75*inch,height=4.5*inch)

c.drawImage(logo8,6.9*inch,4.7*inch,width=1.25*inch,height=2.25*inch)
textobject = c.beginText()
textobject.setTextOrigin(4.6*inch, 3.1*inch)
c.setFont('Helvetica', 5)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Schragzugwinkel zwischen
Scheibe und Seil
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(6.8*inch, 0.7*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Brugg Rillenlehre
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.6*inch, 0.7*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Seilspannungsmessgerat Brugg RPM
''')
c.drawText(textobject)

p = c.beginPath()
p.rect(0.3*inch,1.2*inch, 0.1*inch, 0.1*inch)
p.rect(0.3*inch,1.8*inch,0.1*inch, 0.1*inch)
p.rect(0.3*inch,2.3*inch, 0.1*inch, 0.1*inch)
p.rect(-20, 7.25*inch, 4*inch, 0.9*inch)
p.rect(268, 7.25*inch, 8*inch, 0.2*inch)

c.clipPath(p, stroke=0)
# c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)

c.setFont('Helvetica', 7)
c.drawString(23,87,"3")

c.setFont('Helvetica', 7)
c.drawString(23,130,"2")

c.setFont('Helvetica', 7)
c.drawString(23,167,"1")

c.setFont('Helvetica-Bold', 17)
c.drawString(20,465,"CTP PRUFHANDBUCH")

c.showPage()

logo11 ="image11.jpg"
logo = "brugglifting.svg"
logo6 = "image6.jpeg"
logo7 ="image7.png"
logo8 = "image8.png"
logo9 = "image9.png"
logo10 ="image10.png"
log10 ="p11.png"
gra9 = "P10STRIP.svg"
gra10 = "P11STRIP.svg"
gra11 = "p11strip.png"
lp ="P38BG.png"

c.drawImage(log10,0*inch,7.25*inch,width=8.5*inch,height=4*inch)

c.drawImage(gra1,0*inch,7.25*inch,width=8.5*inch,height=0.3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch,  6.7*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
5. Inspection of groove shape
(traction sheave and diverting pulley)''')
c.drawText(textobject)


p = Paragraph('''<para fontsize=10  leading=13 align="justify"> Evenif traction sheave and diverting pulley grooves are
manufactured according to drawing (radius for CTP   6.5 :
3.4   3.65 mm, radius for CTP   8.1  4.3mm), we strongly
recommend to check the shape with the specially designed
Brugg groove gauge Brugg Lifting provides a custom made
gauge which includes the 45  (30    45  for CTP   6.5)
opening angle as specified in our CTP   certificate. </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,5.1*inch)



textobject = c.beginText()
textobject.setTextOrigin(4.5*inch,  6.7*inch)
c.setFont('Helvetica-Bold', 12)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
5.Seilspannung''')
c.drawText(textobject)


p = Paragraph('''<para fontsize=10  leading=13 align="justify">Even though rope tension is often measured by hand (by
plucking the rope and judging by  feeling ) this method is
far from accurate. Comparing spring buffers with each other
is more precise   to a certain extent but not all elevators are
equipped with such springs. The most reliable way of measuring
rope tension is by measuring the tension on the rope itself.
There are various tools for measuring tension commercially
available. Brugg Lifting recommend our own specialist tool
the Brugg RPM.  </para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,320,5*inch)

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 4.85*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Furthermore check the groove surface for following defects:
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 4.5*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen
''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 4*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen der Treibscheibe und
''')
c.drawText(textobject)

c.drawImage(logo9,0.75*inch,1.5*inch,width=3.15*inch,height=2*inch)

textobject = c.beginText()
textobject.setTextOrigin(1.5*inch, 1.25*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Brugg groove gauge.
''')
c.drawText(textobject)

c.drawImage(logo10,4.5*inch,1.5*inch,width=3.25*inch,height=3.3*inch)

textobject = c.beginText()
textobject.setTextOrigin(4.75*inch, 1.25*inch)
c.setFont('Helvetica', 9)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Rope tension device Brugg RPM
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.9*inch, 0.75*inch)
c.setFont('Helvetica', 6)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Creation date 09/2017
Subject to changes. Nonbinding indication of measures. No warranty for printing errors or errors.
Design, realization: www.schaefer-design.com
''')

c.drawText(textobject)

gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, 7.75*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(580, 0.15*inch, "11")

c.showPage()

c.drawImage(lp,0*inch,0*inch,width=12*inch,height=12*inch)

c.showPage()
c.save()
