from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import A5
from reportlab.lib.pagesizes import A6
from reportlab.lib.units import cm, mm,inch
from reportlab.lib import colors, utils
from reportlab.platypus import Paragraph, Table, TableStyle, Image, Frame, Spacer, PageBreak, BaseDocTemplate, PageTemplate, SimpleDocTemplate, Flowable
from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate, NextPageTemplate
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
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import ImageFont

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
pdfmetrics.registerFont(TTFont('OpenSans-Bold', '/home/cioc/Documents/ELEVATOR ROPES/opensans/truetype/OpenSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('OpenSans-Regular', '/home/cioc/Documents/ELEVATOR ROPES/opensans/truetype/OpenSans-Regular.ttf'))
# font = ImageFont.truetype('/home/cioc/Documents/ELEVATOR ROPES/opensans/truetype/OpenSans-Bold.ttf',120)

styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
ps_title2 = ParagraphStyle(styles['Normal'],\
     fontSize=18, \
    leading=25, backColor='#FEE40D', borderRadius=15,borderColor='#FEE40D',   borderWidth=1, borderPadding=10)

b1 = "b1.png"
b2 = "b2.png"
b3 = "b3.png"
b4 = "b4.png"
b5 = "b5.png"
b6 = "b6.png"
b7 = "b7.png"
l1 = "e1-01.png"
rope = "ropetech.png"
bg = "p1.png"
logo = "brugglifting.svg"
bg1 = "p2transStrip.png"
bg2 = "P6strip2.png"
bg3="P3BannerIMg.png"
a1 = "p10bg.svg"
a2 = "P2BgImg.png"
a3 = "P3Strip.svg"
f1 = "p1img1.png"
f2 = "p1img2.png"
f3 = "p1img3rope.png"
f4 = "p1LeadingRopeTechnology.png"
bgp4 = "P4BannerImg.png"
bgp5 = "P5BannerImg.png"
i1 = "P6Strip.png"
z1 = "gre1.png"
z2 = "gre1.svg"
z3 = "gre2.png"
z4 = "gre2.svg"
z9 = "PtStrip2.png"
bg7 = "P3HStrip.png"
bg8 = "P9Hbox.svg"
bg9 = "P11Hbox.svg"
bg10= "P37TransStrip.png"
bg11= "P37Hbox.svg"
bg12= "ThickRopep1.svg"
bg13= "Tickrope.png"
bg14= "P3BuildingImg.png"
bg15= "P3RemarkedBuilding.svg"
bg16= "P2SideBuildingImg.png"
bg17= "P2SideBuildingImg.svg"
bg18 = "P4SideBuilding.png"
bg19 = "buildingLines.png"
sha = "PageShadowLeftSide.png"
sha1= "PageShadowRightSide.png"
bb5= "P8Strip.png"
az1 ="P21Strip.png"
maa = "P7TransStrip.png"

width,height = A4

c = Canvas("ELEVATORROPES.pdf",pagesize=letter)

c.setPageSize((610, 790))

c.drawImage(f2,0*inch,0*inch,width=8.5*inch,height=5.75*inch)

c.drawImage(f1,0*inch,5.75*inch,width=8.5*inch,height=5.75*inch)

c.drawImage(bg13,0.7*inch,0*inch,width=1.1*inch,height=12.5*inch,mask="auto")

# c.drawImage(test,0.5*inch,0.5*inch,width=1.5*inch,height=0.5*inch)

# drawing1 = svg2rlg(bg17)
# scaleFactor = 1/1.35
# drawing1.width *= scaleFactor
# drawing1.height *= scaleFactor
# drawing1.scale(scaleFactor, scaleFactor)
# renderPDF.draw(drawing1, c, 50, 0*inch)

drawing = svg2rlg(logo)
scaleFactor = 1/1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 400, 10.1*inch)

c.drawImage(f4,0.5*inch,0.5*inch,width=1.5*inch,height=0.5*inch)

# c.setFont("Barlow Condensed",27)
c.setFont("Helvetica-Bold",27)
c.setFillColor('#000000')
c.drawString(185, 5.85*inch, "ELEVATOR")

c.setFont("OpenSans-Bold",27)
c.setFillColor('#ffffff')
c.drawString(340, 5.85*inch, "ROPES")

c.showPage()

c.drawImage(a2,0*inch,0*inch,width=8.5*inch,height=8*inch)

c.drawImage(bg,0*inch,8.1*inch,width=8.5*inch,height=3*inch,preserveAspectRatio=False)

drawing = svg2rlg(logo)
scaleFactor = 1/1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 10.2*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/0.6
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)

c.setFillColor('#696969')
# c.rect(-20,8*inch, 9.5*inch, 1.2*inch,stroke=0,fill=1)

c.drawImage(bb5,0*inch,8*inch,width=8.5*inch,height=1.2*inch,mask='auto')

c.drawImage(rope,2.75*inch,7.75*inch,width=1.5*inch,height=0.45*inch)

c.drawImage(l1,-60,3*inch,width=4*inch,height=4*inch,preserveAspectRatio=True)

c.drawImage(bg16,7.25*inch,0.25*inch,width=1.5*inch,height=4.75*inch,mask="auto")

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

# drawing = svg2rlg(bg17)
# scaleFactor = 1/0.6
# drawing.width *= scaleFactor
# drawing.height *= scaleFactor
# drawing.scale(scaleFactor, scaleFactor)
# renderPDF.draw(drawing, c, 400, 0.75*inch)

c.setFont("Helvetica-Bold",20)
c.setFillColor('#0080ff')
c.drawString(35, 8.6*inch, "GOING UP")

c.setFont("Helvetica-Bold",20)
c.setFillColor('#ffffff')
c.drawString(155, 8.6*inch, "IS OUR MOTTO.")

tp = Paragraph('<para fontsize=10 align="Justify" leading=15> Through our three production facilities located in Switzerland, the U.S.A. and China, we produce elevator ropes to service the global market. Over decades, our ropes have transported millions of passengers in a secure and comfortable way. It is especially in high-rise high speed installations that BRUGG LIFTING elevator ropes show their excellent performance,ensuring smoothness of ride, above-average lifetime and high economic efficiency.</para>',stylesN)

tp1 = Paragraph('<para fontsize=10 align="Justify" leading=17>The development of new and innovative products, the continuous improvement of existing products as well as the optimization of production processes ensures, that customers of BRUGG LIFTING can demand and expect consistently high product quality and optimum performance.</para>',stylesN)

tp2 = Paragraph('<para fontsize=10 align="Justify" leading=17>For additional flexibility and innovation BRUGG LIFTING also produce hoist and governor ropes in compliance with individual customer specifications.</para>',stylesN)

tp3 = Paragraph('<para fontsize=10 align="Justify" leading=17>Working with our global logistics and distribution partners ensures,that our products are correctly packaged, labeled and available for our customers everywhere at the right place and time  every time.</para>',stylesN)

tp4 = Paragraph('<para fontsize=10 align="Justify" leading=17>Our performance parameters are convincing.That`s why international elevator engineering groups to local small and medium-sized companies rely on BRUGG LIFTING elevator ropes.</para>',stylesN)
tpt=[[tp],[tp1],[tp2],[tp3],[tp4]]
tptab=Table(tpt ,colWidths=4.65*inch)
tptab.setStyle(TableStyle([
                    ('TOPPADDING',(0,0),(-1,-1),10)
                    # ('FONTNAME',(0,0),(0,0),'Helvetica-Bold'),
                     ]))
tptab.wrapOn(c,width,height)
tptab.drawOn(c,2.75*inch,1.6*inch)


gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "2")

c.showPage()

c.drawImage(bg3,0*inch,8.1*inch,width=8.5*inch,height=3*inch)

c.drawImage(bg7,0*inch,8*inch,width=8.5*inch,height=0.25*inch, mask="auto")

c.setFillColor('#ffffff')

# drawing = svg2rlg(bg15)
# scaleFactor = 1/1.45
# drawing.width *= scaleFactor
# drawing.height *= scaleFactor
# drawing.scale(scaleFactor, scaleFactor)
# renderPDF.draw(drawing, c, 0,0*inch)

drawing = svg2rlg(a3)
scaleFactor = 1/1.65
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,8*inch)

c.drawImage(bg19,0*inch,0.25*inch,width=7.2*inch,height=10.5*inch, mask="auto")

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

b00 =Paragraph('<para>828m</para>',stylesN)
b001 =Paragraph('<para>2.717ft</para>',stylesN)
b002 =Paragraph('<para>Burj Khalifa Dubai UAE</para>',stylesN)

b991 =Paragraph('<para>553m</para>',stylesN)
b9912 =Paragraph('<para>1.814ft</para>',stylesN)
b9913 =Paragraph('<para> CN Tower.Tornto.CDN</para>',stylesN)

b882 =Paragraph('<para>541m</para>',stylesN)
b8821 =Paragraph('<para>1.775ft</para>',stylesN)
b8822 =Paragraph('<para>One World Trade Center New York USA</para>',stylesN)

b3 =Paragraph('<para>468m</para>',stylesN)
b31 =Paragraph('<para>1.535ft</para>',stylesN)
b32 =Paragraph('<para>Oriental Pearl.Shangai.CN</para>',stylesN)

b4 =Paragraph('<para>452m</para>',stylesN)
b41 =Paragraph('<para>1.483ft</para>',stylesN)
b42 =Paragraph('<para>Petroans Tower. Kulala Lumpur.MAL</para>',stylesN)

b5 =Paragraph('<para>449m</para>',stylesN)
b51 =Paragraph('<para>1.473ft</para>',stylesN)
b52 =Paragraph('<para>Empire State Building.NewYork .USA</para>',stylesN)

b6 =Paragraph('<para>448m</para>',stylesN)
b61 =Paragraph('<para>1.470ft</para>',stylesN)
b62 =Paragraph('<para>Federation Tower. Moscow.RUS</para>',stylesN)

b7 =Paragraph('<para>412m</para>',stylesN)
b71 =Paragraph('<para>1.352ft</para>',stylesN)
b72 =Paragraph('<para>IFC .Hongkong .CN</para>',stylesN)

b8 =Paragraph('<para>351m</para>',stylesN)
b81 =Paragraph('<para>1.033ft</para>',stylesN)
b82 =Paragraph('<para>Stratosphere Tower. Las Vegas. USA</para>',stylesN)

b9 =Paragraph('<para>351m</para>',stylesN)
b91 =Paragraph('<para>1.033ft</para>',stylesN)
b92 =Paragraph('<para>Stratosphere Tower. Las Vegas. USA</para>',stylesN)

b10 =Paragraph('<para>351m</para>',stylesN)
b101 =Paragraph('<para>1.033ft</para>',stylesN)
b102 =Paragraph('<para>Stratosphere Tower. Las Vegas. USA</para>',stylesN)

b11 =Paragraph('<para>310m</para>',stylesN)
b111 =Paragraph('<para>1.017ft</para>',stylesN)
b112 =Paragraph('<para>Telekom HQ. Kuala Lumpur.MAL</para>',stylesN)

b12 =Paragraph('<para>297m</para>',stylesN)
b121 =Paragraph('<para>974ft</para>',stylesN)
b122 =Paragraph('<para>Comcast Center . Philadelphia.USA</para>',stylesN)

b13 =Paragraph('<para>288m</para>',stylesN)
b131 =Paragraph('<para>945ft</para>',stylesN)
b132 =Paragraph('<para>Plaza 66. Shangai .CN</para>',stylesN)

b14 =Paragraph('<para>284m</para>',stylesN)
b141 =Paragraph('<para>932ft</para>',stylesN)
b142 =Paragraph('<para>Tomorrow Square. Shanghai . CN</para>',stylesN)

b15 =Paragraph('<para>280m</para>',stylesN)
b151 =Paragraph('<para>919ft</para>',stylesN)
b152 =Paragraph('<para>Foreign Ministry . MOscow. RUS</para>',stylesN)

b16 =Paragraph('<para>233m</para>',stylesN)
b161 =Paragraph('<para>764ft</para>',stylesN)
b162 =Paragraph('<para>Harbourfront.Hong Kong . CN</para>',stylesN)

b17 =Paragraph('<para>225m</para>',stylesN)
b171 =Paragraph('<para>738ft</para>',stylesN)
b172 =Paragraph('<para>Torre Mayor . Mexico City. MEX</para>',stylesN)

b18 =Paragraph('<para>218m</para>',stylesN)
b181 =Paragraph('<para>715ft</para>',stylesN)
b182 =Paragraph('<para>Shang Mao Real Estate. Nnanjing. CN</para>',stylesN)

b19 =Paragraph('<para>213m</para>',stylesN)
b191 =Paragraph('<para>699ft</para>',stylesN)
b192 =Paragraph('<para>Shangria-La . Hong Kong. CN</para>',stylesN)

b20 =Paragraph('<para>177m</para>',stylesN)
b201 =Paragraph('<para>581ft</para>',stylesN)
b202 =Paragraph('<para>Millenium Tower . Vienna .A</para>',stylesN)

b21 =Paragraph('<para>169m</para>',stylesN)
b211 =Paragraph('<para>554ft</para>',stylesN)
b212 =Paragraph('<para>Shalom Center . Tele Aviv. IL</para>',stylesN)

b22 =Paragraph('<para>153m</para>',stylesN)
b221 =Paragraph('<para>502ft</para>',stylesN)
b222 =Paragraph('<para>Fairmont (Park Plaza).Dubai.UAE</para>',stylesN)

b23 =Paragraph('<para>138m</para>',stylesN)
b231 =Paragraph('<para>453ft</para>',stylesN)
b232 =Paragraph('<para>Twintower.Vienna. A</para>',stylesN)

b24 =Paragraph('<para>135m</para>',stylesN)
b241 =Paragraph('<para>443ft</para>',stylesN)
b242 =Paragraph('<para>Nurnberger Versicherung . Nuremberg . DE</para>',stylesN)


b25 =Paragraph('<para>130m</para>',stylesN)
b251 =Paragraph('<para>427ft</para>',stylesN)
b252 =Paragraph('<para>Castor. Frankfurt.DE</para>',stylesN)

b26 =Paragraph('<para>105m</para>',stylesN)
b261 =Paragraph('<para>344ft</para>',stylesN)
b262 =Paragraph('<para>Messeturm .Basel.CH</para>',stylesN)

b26 =Paragraph('<para>105m</para>',stylesN)
b261 =Paragraph('<para>344ft</para>',stylesN)
b262 =Paragraph('<para>Messeturm .Basel.CH</para>',stylesN)

b27 =Paragraph('<para>96m</para>',stylesN)
b271 =Paragraph('<para>226ft</para>',stylesN)
b272 =Paragraph('<para>Platinum Tower.Tel Aviv .IL</para>',stylesN)

data1 = [[b00,b001,b002],['','',''],['','',''],['','',''],['','',''],[b991,b9912,b9913],[b882,b8821,b8822],[b3,b31,b32],[b4,b41,b42],[b5,b51,b52],[b6,b61,b62],['','',''],[b7,b71,b72],['','',''],['','',''],[b8,b81,b82],['','',''],[b10,b101,b102],[b11,b111,b112],[b12,b121,b122],[b13,b131,b132],[b14,b141,b142],[b15,b151,b152],[b16,b161,b162],[b17,b171,b172],[b18,b181,b182],[b19,b191,b192],[',',''],[b20,b201,b202],[b21,b211,b212],[b22,b221,b222],[b23,b231,b232],[b24,b241,b242],[b25,b251,b252],['','',''],[b26,b261,b262],[b27,b271,b272]]
t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
t1.wrapOn(c,width,height)
t1.drawOn(c,4*inch,0.25*inch)

# c.drawCentredString(10*inch, 3*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 2.9*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 2.8*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 2.7*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 2.6*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 2.5*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 2.4*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 2.3*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 2.2*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 1.8*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 1.7*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 1.6*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 1.5*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 1.2*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 0.9*inch, "553m 1.814ft CN Tower.Tornto.CDN")


# c.drawImage(b2,5.5*inch,0.8*inch,width=0.5*inch,height=3.8*inch,preserveAspectRatio=True)
# c.line(5.75*inch,4.75*inch,10.75*inch,4.75*inch)
# c.drawCentredString(10*inch, 4.5*inch, "553m 1.814ft CN Tower.Tornto.CDN")
#
# c.drawImage(b3,5.9*inch,0.8*inch,width=0.75*inch,height=4.75*inch,preserveAspectRatio=True)
# c.line(6.2*inch,5.5*inch,10.75*inch,5.5*inch)
# c.drawCentredString(10*inch, 5.15*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 5.0*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 4.85*inch, "553m 1.814ft CN Tower.Tornto.CDN")
#
# c.drawImage(b4,6.25*inch,0.8*inch,width=1.25*inch,height=8*inch,preserveAspectRatio=True)
# c.line(7*inch,8*inch,10.75*inch,8*inch)
# c.drawCentredString(10*inch, 7.75*inch, "828m 2.717ft Burj Khalifa. Dubai.UAE")
# c.drawImage(b5,6.7*inch,0.8*inch,width=1.5*inch,height=5*inch,preserveAspectRatio=True)
# c.line(7.5*inch,5.75*inch,10.75*inch,5.75*inch)
# c.drawCentredString(10*inch, 5.65*inch, "553m 1.814ft CN Tower.Tornto.CDN")
#
# c.drawImage(b6,7.15*inch,0.8*inch,width=1.5*inch,height=4.5*inch,preserveAspectRatio=True)
# c.line(7.9*inch,5.3*inch,10.75*inch,5.3*inch)
#
# c.drawImage(b7,7.75*inch,0.8*inch,width=1*inch,height=3.5*inch,preserveAspectRatio=True)
# c.line(8.15*inch,4.35*inch,10.75*inch,4.35*inch)
# c.drawCentredString(10*inch, 4.1*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.drawCentredString(10*inch, 3.5*inch, "553m 1.814ft CN Tower.Tornto.CDN")
# c.line(5*inch,0.8*inch,10.75*inch,0.8*inch)
#


# c.drawImage(rope,2.1*inch,5.6*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
# black50transparent = Color( 0, 0, 0, alpha=0.5)
# c.setFillColor(black50transparent)
# c.rect(-20, 6.07*inch, 6.5*inch, 1*inch,stroke=0,fill=1)
# blue50transparent = Color( 0, 0, 255, alpha=0.75)
#
# c.setFont("Helvetica-Bold",30)
# c.setFillColor(blue50transparent)
# c.drawString(30, 6.5*inch, "GOING UP IS OUR MOTTO")

# c.setFillGray(0.5)
# c.rect(448,6.07*inch, 6*inch, 0.25*inch,stroke=0,fill=1)

gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, 7.75*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(580, 0.15*inch, "3")


c.showPage()

b1 = "b1.png"
b2 = "b2.png"
b3 = "b3.png"
b4 = "b4.png"
b5 = "b5.png"
b6 = "b6.png"
b7 = "b7.png"
l1 = "e1-01.png"
rope = "ropetech.png"
bg = "img1.jpg"
logo = "brugglifting.svg"
bull1 = "image3.svg"
bull2 = "image3.svg"
bull3 = "image3.svg"
bull4 = "image3.svg"
bull5 = "image3.svg"
bull6 = "image3.svg"
im = "e2-2.png"
iso = "e2-3.png"
sys = "SYS.svg"
isoo = "isoo.svg"
cust ="cust.svg"
exp ="exp.svg"
ava = "ava.svg"
exp = "exp.svg"
iso1 = "iso.svg"
tra = "tra.svg"
isoo = "isoo.svg"
isoc = "isoc.svg"
sqs = "sqs.svg"
iet = "iet.svg"
a1 = "P2BgImg.png"
a2 = "P3Strip.svg"

width,height = A6
# d = c.setFillColorRGB(170,180,182)
# c.linearGradient(50*mm, 100*mm, 30*mm, 30*mm,(colors.white),extend=True)

c.drawImage(a1,0*inch,0*inch,width=8.5*inch,height=8*inch)

c.drawImage(bgp4,0*inch,8.1*inch,width=8.5*inch,height=3*inch)

drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 10.2*inch)

c.setFillColor('#696969')
# c.rect(-20,8*inch, 9.5*inch, 1.2*inch,stroke=0,fill=1,mask='auto')

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

c.drawImage(bb5,0*inch,8*inch,width=8.5*inch,height=1.2*inch,mask='auto')

drawing = svg2rlg(sys)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,6.9*inch)

drawing = svg2rlg(cust)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,5.75*inch)

drawing = svg2rlg(ava)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,4.4*inch)

drawing = svg2rlg(exp)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,2.85*inch)

drawing = svg2rlg(iso1)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,1.75*inch)

drawing = svg2rlg(iso1)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,1.75*inch)

drawing = svg2rlg(tra)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,0.5*inch)

# black50transparent = Color( 0, 0, 0, alpha=0.5)
# c.setFillColor(black50transparent)
# c.rect(-20, 8.1*inch, 6.5*inch, 1*inch,stroke=0,fill=1)
# blue50transparent = Color( 0, 0, 255, alpha=0.75)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",22)
c.drawString(40, 8.5*inch, "SERVICES")
c.setFillGray(0.5)
# c.rect(448,8.1.7*inch, 6*inch, 0.25*inch,stroke=0,fill=1)


c.drawImage(bg18,7.75*inch,5.4*inch,width=0.75*inch,height=2.2*inch,mask="auto")


tp = Paragraph('<para fontsize=12 leftindent=13  ><b>System Provider</b></para>',stylesN)
tp2 = Paragraph('<para fontsize=10  align="Justify" leading=15> We offer to you a wide assortment of elevator ropes, accessories and tools to meet all of your requirements. We supply you with complete solutions or individually combined components as individual or pre-assembled parts to suit your needs.</para>',stylesN)
tpt=[[tp],[tp2]]
tptab=Table(tpt,colWidths=6*inch)
tptab.setStyle(TableStyle([
                            ('LEFTPADDING',(0,1),(-1,-1),20),
                            ('TOPPADDING',(0,0),(-1,-1),10),
                       ]))
tptab.wrapOn(c,width,height)
tptab.drawOn(c,1.7*inch, 6.75*inch)

tp = Paragraph('<para fontsize=12 leftindent=13  ><b>Customized</b></para>',stylesN)
tp2 = Paragraph('<para fontsize=10  align="Justify" leading=18><br/> Our wide assortment of elevator ropes, accessories and tools provides nearly all products required for your applications. If none of the articles depicted in the catalog solvesyour problem, or if your elevator is to meet specific requirements, we will be glad to advise you and to develop customized solutions together with you.</para>',stylesN)
tpt=[[tp],[tp2]]
tptab=Table(tpt,colWidths=6*inch)
tptab.setStyle(TableStyle([
                            ('TOPPADDING',(0,1),(-1,-1),-10),
                            ('LEFTPADDING',(0,1),(-1,-1),20),
                       ]))
tptab.wrapOn(c,width,height)
tptab.drawOn(c,1.7*inch, 5.3*inch)


tp = Paragraph('<para fontsize=12 leftindent=13  ><b>Availability</b></para>',stylesN)
tp2 = Paragraph('<para fontsize=10 align="Justify" leading=18 >Due to our three production facilities located in Switzerland and China, as well as due toour global network of warehouse locations, our products will be delivered to your factory or your construction site within a very short time. Please contact us if you have anyquestions regarding deadlines, individual deliveries and specific projects.</para>',stylesN)
tpt=[[tp],[tp2]]
tptab=Table(tpt,colWidths=6*inch)
tptab.setStyle(TableStyle([
                            ('TOPPADDING',(0,1),(-1,-1),8),
                            ('LEFTPADDING',(0,1),(-1,-1),20),
                       ]))
tptab.wrapOn(c,width,height)
tptab.drawOn(c,1.7*inch, 3.9*inch)


tp = Paragraph('<para fontsize=12 leftindent=13  ><b>Express Service</b></para>',stylesN)
tp2 = Paragraph('<para fontsize=10 align="Justify" leading=18 >In urgent cases we provide the required materials ex works within the hour and ship it to you as quickly as possible by courier all over the world.</para>',stylesN)
tpt=[[tp],[tp2]]
tptab=Table(tpt,colWidths=6*inch)
tptab.setStyle(TableStyle([
                            ('TOPPADDING',(0,1),(-1,-1),8),
                            ('LEFTPADDING',(0,1),(-1,-1),20),
                       ]))
tptab.wrapOn(c,width,height)
tptab.drawOn(c,1.7*inch, 2.9*inch)

tp = Paragraph('<para fontsize=12 leftindent=13  ><b>International Standards</b></para>',stylesN)
tp2 = Paragraph('<para fontsize=10 align="Justify" leading=18 >All of our products meet the valid international standards.<br/> BRUGG LIFTING is certified according to ISO 9001:2008 and ISO 14001:2004.</para>',stylesN)
tpt=[[tp],[tp2]]
tptab=Table(tpt,colWidths=6*inch)
tptab.setStyle(TableStyle([
                            ('TOPPADDING',(0,1),(-1,-1),8),
                            ('LEFTPADDING',(0,1),(-1,-1),20),
                       ]))
tptab.wrapOn(c,width,height)
tptab.drawOn(c,1.7*inch, 1.75*inch)

tp = Paragraph('<para fontsize=12 leftindent=13  ><b>Training/Specialist Workshops</b></para>',stylesN)
tp2 = Paragraph('<para fontsize=10 align="Justify" leading=18 >Our aim is to ensure that you will enjoy an optimal use and an increase service life of your elevator ropes. Make use of our offering of qualified and customized training units for your staff.</para>',stylesN)
tpt=[[tp],[tp2]]
tptab=Table(tpt,colWidths=6*inch)
tptab.setStyle(TableStyle([
                            ('TOPPADDING',(0,1),(-1,-1),8),
                            ('LEFTPADDING',(0,1),(-1,-1),20),
                       ]))
tptab.wrapOn(c,width,height)
tptab.drawOn(c,1.7*inch, 0.25*inch)


gm934 = Paragraph('<para></para>',stylesN)
gmn934 = Paragraph('<para></para>',stylesN)

data =  [[gm934,gmn934]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                     ]))
t.wrapOn(c,width, height)
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "4")


c.showPage()

# Second page

# c.linearGradient(50*mm, 400*mm, 30*mm, 30*mm, '#A3ABAF',extend=True)

c.drawImage(a1,0*inch,0*inch,width=8.5*inch,height=8.2*inch)

c.drawImage(bgp5,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(bg7,0*inch,8*inch,width=8.5*inch,height=0.25*inch,mask='auto')

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(a2)
scaleFactor = 1/1.65
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,8*inch)

drawing = svg2rlg(isoc)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,2*inch)

drawing = svg2rlg(sqs)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 50,0.75*inch)

drawing = svg2rlg(iet)
scaleFactor = 1./1.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 2*inch,0.75*inch)

blue50transparent = Color( 0, 0, 255, alpha=0.75)


c.drawImage(im,0,5*inch,width=3.75*inch,height=3*inch,preserveAspectRatio=True)



# c.drawImage(isoo,30,1*inch,width=1.7*inch,height=1.7*inch,preserveAspectRatio=True)

gm = Paragraph('<para fontsize=8  leading=10>Going up is our Motto</para>',stylesN)
n = Paragraph('<para fontsize=8  leading=10>2</para>',stylesN)
gm1 = Paragraph('<para fontsize=8  leading=10>Services</para>',stylesN)
gmn1 = Paragraph('<para fontsize=8  leading=10>4</para>',stylesN)
gm2 = Paragraph('<para fontsize=8  leading=10>Ropes at Glance</para>',stylesN)
gmn2 = Paragraph('<para fontsize=8  leading=10>6</para>',stylesN)

gm3 = Paragraph('<para fontsize=8  leading=10>Rope Comparision</para>',stylesN)
gmn3 = Paragraph('<para fontsize=8  leading=10>8</para>',stylesN)

gm4 = Paragraph('<para fontsize=8  leading=10>Rope Comparision . i-Line</para>',stylesN)
gmn4 = Paragraph('<para fontsize=8  leading=10>9</para>',stylesN)

gm5 = Paragraph('<para fontsize=8  leading=10><b>Elevator Ropes.Accessories</b></para>',stylesN)
gmn5 = Paragraph('<para fontsize=8  leading=10>10</para>',stylesN)

gm6 = Paragraph('<para fontsize=8  leading=10>Hoist Ropes</para>',stylesN)
gm7 = Paragraph('<para fontsize=8 leftindent = 15 leading=10>HRS</para>',stylesN)
gmn7 = Paragraph('<para fontsize=8  leading=10>12</para>',stylesN)

gm8 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>DP9</para>',stylesN)
gmn8 = Paragraph('<para fontsize=8  leading=10>13</para>',stylesN)
gm9 = Paragraph('<para fontsize=8 leftindent = 15  leading=10>MCX9</para>',stylesN)
gmn9 = Paragraph('<para fontsize=8  leading=10>15</para>',stylesN)

gm10 = Paragraph('<para fontsize=8 leftindent = 15  leading=8>SCX9</para>',stylesN)
gmn10 = Paragraph('<para fontsize=8  leading=8>14</para>',stylesN)

gm11 = Paragraph('<para fontsize=8 leftindent = 15  leading=10>8x19</para>',stylesN)
gmn11 = Paragraph('<para fontsize=8  leading=10>16</para>',stylesN)

gm12 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>TSR</para>',stylesN)
gmn12 = Paragraph('<para fontsize=8  leading=10>17</para>',stylesN)
gm13 = Paragraph('<para fontsize=8  leading=10>Compensation Ropes</para>',stylesN)
gm14 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>8x19.8x25</para>',stylesN)
gmn14 = Paragraph('<para fontsize=8  leading=10>18</para>',stylesN)
gm15 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>6x25</para>',stylesN)
gmn15 = Paragraph('<para fontsize=8  leading=10>19</para>',stylesN)
gm16 = Paragraph('<para fontsize=8  leading=10>Governor Ropes</para>',stylesN)
gm17 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>6x19.8x19</para>',stylesN)
gmn17 = Paragraph('<para fontsize=8  leading=10>20</para>',stylesN)

gm18 = Paragraph('<para fontsize=8  leading=10>Designations and Classifications</para>',stylesN)
gmn18 = Paragraph('<para fontsize=8  leading=10>21</para>',stylesN)

gm19 = Paragraph('<para fontsize=8   leftindent = 15 leading=10>APAG Threaded Swaged Sockets</para>',stylesN)
gmn19 = Paragraph('<para fontsize=8  leading=10>22</para>',stylesN)

gm20 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>Eyelet Bolt with Swaged Thimble</para>',stylesN)
gmn20 = Paragraph('<para fontsize=8  leading=10>23</para>',stylesN)

gm21 = Paragraph('<para fontsize=8   leftindent = 15 leading=10>Wedge Socket Symmetrical</para>',stylesN)
gmn21 = Paragraph('<para fontsize=8  leading=10>24</para>',stylesN)

gm22 = Paragraph('<para fontsize=8 leftindent = 15  leading=10>Wedge Socket ASymmetrical</para>',stylesN)
gmn22 = Paragraph('<para fontsize=8  leading=10>26</para>',stylesN)

gm23 = Paragraph('<para fontsize=8 leftindent = 15 leading=10>Elastomer Buffers</para>',stylesN)
gmn23 = Paragraph('<para fontsize=8  leading=10>28</para>',stylesN)

gm24 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>Spring</para>',stylesN)
gmn24 = Paragraph('<para fontsize=8  leading=10>29</para>',stylesN)

gm25 = Paragraph('<para fontsize=8  leading=10>Door Closing Rope Sets</para>',stylesN)
gmn25 = Paragraph('<para fontsize=8  leading=10>30</para>',stylesN)

gm25 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>Door Closing Rope Flex . Rope clamp</para>',stylesN)
gmn25 = Paragraph('<para fontsize=8  leading=10>31</para>',stylesN)
gm26 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>RPM Rope Performance Measurement Device</para>',stylesN)
gmn26 = Paragraph('<para fontsize=8  leading=10>31</para>',stylesN)

gm27 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>GDC Grove Depth Comparator</para>',stylesN)
gmn27 = Paragraph('<para fontsize=8  leading=10>33</para>',stylesN)


gm29 = Paragraph('<para fontsize=8 leftindent = 15 leading=10>RWG Rope Wear Gauge</para>',stylesN)
gmn29 = Paragraph('<para fontsize=8  leading=10>33</para>',stylesN)
gm30 = Paragraph('<para fontsize=8  leftindent = 15 leading=10>VT-Lube Lubricant</para>',stylesN)
gmn30 = Paragraph('<para fontsize=8  leading=10>34</para>',stylesN)
gm31 = Paragraph('<para fontsize=8 leftindent = 15 leading=10>Rope Cutters</para>',stylesN)
gmn31 = Paragraph('<para fontsize=8  leading=10>34</para>',stylesN)
gm32 = Paragraph('<para fontsize=8 leftindent = 15 leading=10>Packaging</para>',stylesN)
gmn32 = Paragraph('<para fontsize=8  leading=10>35</para>',stylesN)
gm33 = Paragraph('<para fontsize=8  leading=10><b>Support</b></para>',stylesN)
gmn33 = Paragraph('<para fontsize=8  leading=10>38</para>',stylesN)
gm34 = Paragraph('<para fontsize=8  leading=10>Contacts</para>',stylesN)
gmn34 = Paragraph('<para fontsize=8  leading=10>39</para>',stylesN)

data =  [[gm,n],[gm1,gmn1],[gm2,gmn2],[gm3,gmn3],[gm4,gmn4],['',''],[gm5,gmn5],[gm6],[gm7,gmn7],[gm8,gmn8],[gm10,gmn10],[gm9,gmn9],[gm11,gmn11],[gm12,gmn12],[gm13],[gm14,gmn14],[gm15,gmn15],[gm16],[gm17,gmn17],[gm18,gmn18],[gm19,gmn19],[gm20,gmn20],[gm21,gmn21],[gm22,gmn22],[gm23,gmn23],[gm24,gmn24],[gm25,gmn25],[gm26,gmn26],[gm27,gmn27],[gm29,gmn29],[gm30,gmn30],[gm31,gmn31],[gm32,gmn32],['',''],[gm33,gmn33],[gm34,gmn34]]

t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                    ('LINEBELOW',(0,0),(-1,-1),0.1,colors.white),
                    ('FONTSIZE', (0, 0), (-1, -1), 7),
                    ('FONTNAME',(0,6),(-2,-32),'Helvetica-Bold'),
                    # ('ALIGN',(0,8),(-2,-23),'CENTER'),
                    # ('LEFTPADDING',(0,8),(-2,-23),-30),
                    ('ALIGN',(0,13),(-2,-16),'CENTER'),
                    # ('LEFTPADDING',(0,15),(-2,-17),-40),
                    ('ALIGN',(0,19),(-2,-10),'CENTER'),
                    # ('LEFTPADDING',(0,18),(-2,-11),-40),
                    ('ALIGN',(0,20),(-2,-3),'LEFT'),
                    # ('LEFTPADDING',(0,20),(-2,-3),17),
                    ('FONTNAME',(0,35),(-2,-2),'Helvetica-Bold'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                     ]))

t.wrapOn(c,width, height)
t.drawOn(c, 4.75*inch,0.3*inch)


# gm934 = Paragraph('<para></para>',stylesN)
# gmn934 = Paragraph('<para></para>',stylesN)
#
# data =  [[gm934,gmn934]]
#
# t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
# t.setStyle(TableStyle([
#                     ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
#                      ]))
# t.wrapOn(c,width, height)
# t.drawOn(c, 7.75*inch,0.2*inch)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",10)
c.drawString(580, 0.15*inch, "5")


c.showPage()

logo = "brugglifting.svg"
bg = "img1.jpg"
hrs = "hrs1.png"
scx9 = "scx9.png"
mcx9 = "mcx92.png"
sc8 = "hrs.jpg"
dp9 = "dp92.png"
X19 = "exn.png"
tsr = "tsr.png"
x25 = "exf.png"
sx25 = "scf.png"
x119 = "exnn.png"
X191 = "tr.png"
i1 = "P6Strip.png"
i2= "P6strip2.png"
b1= "P6BannerImg.png"
b2= "P7BannerImg.png"
bgp4 = "P4BannerImg.png"

width,height= A4


c.drawImage(b1,0*inch,8*inch,width=8.5*inch,height=3*inch)
c.drawImage(i1,-0*inch,8*inch,width=8.5*inch,height=1*inch,mask='auto')

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 10.2*inch)



c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(30, 8.4*inch, "ROPES AT A GLANCE")

c.setFillColor(colors.white)
c.setFont("Helvetica",11)
c.drawString(300, 8.05*inch, "HOIST ROPES")



c.drawImage(hrs,20,6.75*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=7><bullet>&bull;</bullet><b>Steel Core Rope</b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>9 Strands</b></para>',stylesN)
ad3 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>Parallel Lay</b></para>',stylesN)

a = [[ad1],[ad2],[ad3]]
at=Table(a,colWidths=9.5*cm)
at.wrapOn(c,width,height)
at.drawOn(c,125,7*inch)

c.setFillColor('#109ED9')
c.rect(230,6.9*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="Justify"fontsize=17 leading=10 color=white><b>HRS</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,7.2*inch)

c.setFillColor('#7EBBEA')
c.rect(335,6.9*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>125,000</b> <br/> N/mm2<br/><b>1.81x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,320,6.85*inch)
#
#
c.setFillColor('#A4C4E4')
c.rect(400,6.9*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.104</b> <br/> %<br/><b>1.2</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,385,6.85*inch)
#
#
c.setFillColor('#B8D6F5')
c.rect(465,6.9*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.13</b> <br/> %<br/><b>1.6</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,450,6.85*inch)
#
#
#
c.setFillColor('#DCE7FE')
c.rect(530,6.9*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=7 leading=10><b><425</b> <br/> m<br/><b><1400</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,516,6.85*inch)


# For DP9
c.drawImage(dp9,20,5.5*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>Polypropylene<br/> Fiber Core</b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>9 Strands</b></para>',stylesN)
ad3 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>Parallel Lay</b></para>',stylesN)

a = [[ad1],[ad2],[ad3]]
at=Table(a)
at.wrapOn(c,width,height)
at.drawOn(c,125,5.6*inch)

c.setFillColor('#FEE40D')
c.rect(230,5.8*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="Justify"fontsize=17 leading=10 color=white><b>DP9</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2*cm,rowHeights=1*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,6.1*inch)

c.setFillColor('#F3EB76')
c.rect(335,5.8*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>115.000</b> <br/> N/mm2<br/><b>1.67x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,320,5.75*inch)
#
#
c.setFillColor('#FDF18B')
c.rect(400,5.8*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.112</b> <br/> %<br/><b>1.35</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,385,5.75*inch)
#
#
c.setFillColor('#F7F5BC')
c.rect(465,5.8*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.25</b> <br/> %<br/><b>3</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,450,5.75*inch)
#
#
#
c.setFillColor('#FFF6D7')
c.rect(530,5.8*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=7 leading=10><b><250</b> <br/> m<br/><b><800</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,516,5.75*inch)

# For SCX9
c.drawImage(scx9,20,4.1*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Steel Core Rope </b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>9 Strands</b></para>',stylesN)
ad3 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>Seperate Lay</b></para>',stylesN)

a = [[ad1],[ad2],[ad3]]
at=Table(a)
at.wrapOn(c,width,height)
at.drawOn(c,125,4.5*inch)

c.setFillColor('#83BCDD')
c.rect(230,4.4*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="Justify"fontsize=17 leading=10 color=white><b>SCX9</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,4.7*inch)

c.setFillColor('#AAC1E3')
c.rect(335,4.4*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>120,000</b> <br/> N/mm2<br/><b>17.4x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,320,4.4*inch)
#
#
c.setFillColor('#B3D2ED')
c.rect(400,4.4*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.108</b> <br/> %<br/><b>1.3</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,385,4.4*inch)
#
#
c.setFillColor('#C7DDF1')
c.rect(465,4.4*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.16</b> <br/> %<br/><b>2</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,450,4.4*inch)
#
#
#
c.setFillColor('#DBEBF7')
c.rect(530,4.4*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=7 leading=10><b><325</b> <br/> m<br/><b><1000</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,516,4.4*inch)


#For MCX9

c.drawImage(mcx9,20,2.75*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>Polypropylene<br/> Fiber Core</b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>9 Strands</b></para>',stylesN)
ad3 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>Parallel Lay</b></para>',stylesN)

a = [[ad1],[ad2],[ad3]]
at=Table(a)
at.wrapOn(c,width,height)
at.drawOn(c,125,2.9*inch)

c.setFillColor('#F8BA13')
c.rect(230,3.1*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="Justify"fontsize=17 leading=10 color=white><b>MCX9</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2.25*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,3.4*inch)

c.setFillColor('#F9C780')
c.rect(335,3.1*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>110.000</b> <br/> N/mm2<br/><b>16x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,320,3.1*inch)
#
#
c.setFillColor('#F7D69E')
c.rect(400,3.1*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.120</b> <br/> %<br/><b>1.5</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,385,3.1*inch)
#
#
c.setFillColor('#FDE2B7')
c.rect(465,3.1*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.30</b> <br/> %<br/><b>4</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,450,3.1*inch)
#
#
#
c.setFillColor('#FFEBD1')
c.rect(530,3.1*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=7 leading=10><b><200</b> <br/> m<br/><b><650</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,516,3.1*inch)
# For 8X19


c.drawImage(X19,20,1.5*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>SisalFiber Core</b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>8 Strands</b></para>',stylesN)


a = [[ad1],[ad2]]
at=Table(a)
at.wrapOn(c,width,height)
at.drawOn(c,125,2*inch)

c.setFillColor('#FEFEFE')
c.rect(230,1.9*inch, 1.25*inch, 0.6*inch,stroke=1,fill=1)
ad5 = Paragraph('<para  align="Justify"fontsize=17 leading=10 color=black><b>8X19</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2.25*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,2.2*inch)

c.setFillColor('#FFFFFF')
c.rect(335,1.9*inch, 0.6*inch, 0.6*inch,stroke=1,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>110.000</b> <br/> N/mm2<br/><b>16x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,320,1.9*inch)
#
#
c.setFillColor('#FFFFFF')
c.rect(400,1.9*inch, 0.6*inch, 0.6*inch,stroke=1,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.122</b> <br/> %<br/><b>1.5</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,385,1.9*inch)
#
#
c.setFillColor('#FFFFFF')
c.rect(465,1.9*inch, 0.6*inch, 0.6*inch,stroke=1,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.26</b> <br/> %<br/><b>4</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,450,1.9*inch)
#
#
#
c.setFillColor('#FFFFFF')
c.rect(530,1.9*inch, 0.6*inch, 0.6*inch,stroke=1,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=7 leading=10><b><200</b> <br/> m<br/><b><650</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,516,1.9*inch)

# For TSR

c.drawImage(tsr,20,0.25*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>Steel Core Rope</b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=10><bullet>&bull;</bullet><b>6 Strands</b></para>',stylesN)
ad3 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Zinc-Plated</b></para>',stylesN)
ad4 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>Seperate Lay</b></para>',stylesN)

a = [[ad1],[ad2],[ad3],[ad4]]
at=Table(a,rowHeights=4*mm)
at.wrapOn(c,width,height)
at.drawOn(c,125,0.5*inch)


c.setFillColor('#5D6970')
c.rect(230,0.7*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="center"fontsize=17 leading=10 color=white><b>TSR</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2.25*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,1*inch)

c.setFillColor('#C6CACD')
c.rect(335,0.7*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>125.,000</b> <br/> N/mm2<br/><b>18.1x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,320,0.7*inch)
#
#
c.setFillColor('#D1D6D8')
c.rect(400,0.7*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.104</b> <br/> %<br/><b>1.25</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,385,0.7*inch)
#
#
c.setFillColor('#DCE0E3')
c.rect(465,0.7*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.5</b> <br/> %<br/><b>6.0</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,450,0.7*inch)

c.setFillColor('#E9E9E9')
c.rect(530,0.7*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=7 leading=10><b><175</b> <br/> m<br/><b><550</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,516,0.7*inch)

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


c.drawImage(b2,0*inch,8*inch,width=8.5*inch,height=3*inch)
c.drawImage(x119,20,6.5*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
# c.drawImage(i2,0*inch,8*inch,width=8.5*inch,height=0.35*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

c.drawImage(maa,0*inch,8*inch,width=8.5*inch,height=0.25*inch,mask='auto')

c.setFillColor('#3C434B')
c.drawString(230, 3.3*inch, "GOVERNOR  ROPES")
c.drawImage(X191,5.5*inch,3.75*inch,width=3.5*inch,height=3.75*inch,mask='auto')
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>Plypropylene Core </b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=10><bullet>&bull;</bullet><b>8 Strands .Seale</b></para>',stylesN)


c.setFillColor(colors.white)
c.setFont("Helvetica",12)
c.drawString(242, 8.1*inch, "COMPENSATION ROPES")

a = [[ad1],[ad2]]
at=Table(a,rowHeights=4*mm)
at.wrapOn(c,width,height)
at.drawOn(c,125,7*inch)

c.setFillColor('#586063')
c.rect(230,6.9*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="center"fontsize=17 leading=10 color=white><b>8x19</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2*cm,rowHeights=1*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,7.1*inch)

c.drawImage(x25,20,5.1*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>Plypropylene Core </b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=10><bullet>&bull;</bullet><b>8 Strands .Seale</b></para>',stylesN)

a = [[ad1],[ad2]]
at=Table(a,rowHeights=4*mm)
at.wrapOn(c,width,height)
at.drawOn(c,125,5.6*inch)

c.setFillColor('#586063')
c.rect(230,5.5*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="center"fontsize=17 leading=10 color=white><b>8x25</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2*cm,rowHeights=1*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,5.75*inch)

c.drawImage(sx25,20,3.75*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>Plypropylene Core </b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=10><bullet>&bull;</bullet><b>8 Strands .Seale</b></para>',stylesN)

a = [[ad1],[ad2]]
at=Table(a,rowHeights=4*mm)
at.wrapOn(c,width,height)
at.drawOn(c,125,4.2*inch)

c.setFillColor('#586063')
c.rect(230,4*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="center"fontsize=17 leading=10 color=white><b>6x25</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2*cm,rowHeights=1*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,4.25*inch)

c.setFillColor('#D2D7DB')
c.rect(230,3.25*inch, 12*inch, 0.25*inch,stroke=0,fill=1)

c.drawImage(X19,20,1.5*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>SisalFiber Core</b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>8 Strands</b></para>',stylesN)

a = [[ad1],[ad2]]
at=Table(a)
at.wrapOn(c,width,height)
at.drawOn(c,125,2*inch)

c.setFillColor('#586063')
c.rect(230,1.9*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="center"fontsize=17 leading=10 color=white><b>6x19</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2.25*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,2.2*inch)

c.setFillColor('#C6CACD')
c.rect(335,1.9*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>105.000</b> <br/> N/mm2<br/><b>15.2x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,320,1.9*inch)
#
c.setFillColor('#CCD1D6')
c.rect(400,1.9*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.084</b> <br/> %<br/><b>1.0</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,385,1.9*inch)
#
c.setFillColor('#DADBDD')
c.rect(465,1.9*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.22</b> <br/> %<br/><b>2.64</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,450,1.9*inch)

# c.setFillColor('#87CEFA')
# c.rect(530,1.9*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
# tp4 = Paragraph('''<para align="center"  fontsize=7 leading=10><b><200</b> <br/> m<br/><b><650</b><br/>ft</para>''',stylesN)
# tpt4 = [[tp4]]
# tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
# tp44.wrapOn(c,width,height)
# tp44.drawOn(c,516,1.9*inch)


c.drawImage(tsr,20,0.25*inch,width=1.2*inch,height=1.2*inch,preserveAspectRatio=True)
ad1 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Wire Rope with <br/>Steel Core Rope</b></para>',stylesN)
ad2 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=10><bullet>&bull;</bullet><b>6 Strands</b></para>',stylesN)
ad3 = Paragraph('<para leftindent=15 align="justify" fontsize=8 leading=10><bullet>&bull;</bullet><b>Zinc-Plated</b></para>',stylesN)
ad4 = Paragraph('<para leftindent=15 align="justify"fontsize=8 leading=7><bullet>&bull;</bullet><b>Seperate Lay</b></para>',stylesN)

a = [[ad1],[ad2],[ad3],[ad4]]
at=Table(a,rowHeights=4*mm)
at.wrapOn(c,width,height)
at.drawOn(c,125,0.5*inch)


c.setFillColor('#586063')
c.rect(230,0.7*inch, 1.25*inch, 0.6*inch,stroke=0,fill=1)
ad5 = Paragraph('<para  align="center"fontsize=17 leading=10 color=white><b>8x19</b></para>',stylesN)
hr = [[ad5]]
hrt = Table(hr,colWidths=2.25*cm)
hrt.wrapOn(c,width,height)
hrt.drawOn(c,245,1*inch)

c.setFillColor('#C6CACD')
c.rect(335,0.7*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>125.,000</b> <br/> N/mm2<br/><b>18.1x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,320,0.7*inch)
#
#
c.setFillColor('#CCD1D6')
c.rect(400,0.7*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.104</b> <br/> %<br/><b>1.25</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,385,0.7*inch)
#
#
c.setFillColor('#DADBDD')
c.rect(465,0.7*inch, 0.6*inch, 0.6*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.5</b> <br/> %<br/><b>6.0</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,450,0.7*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica",12)
c.drawString(242,3.3*inch, "GOVERNOR ROPES")


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



c.showPage()

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
b1= "P8BannerImg.png"
b2= "P8Strip.svg"
b3= "P9BannerImg.png"
b4= "P9Strip.svg"
b5= "P8Strip.png"
b6= "P9strip.svg"
b7= "P3HStrip.png"

width, height = A4
c.drawImage(b1,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(b5,0*inch,8.25*inch,width=8.5*inch,height=1*inch,mask='auto')

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.25*inch)


c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(138, 8.65*inch, "ROPE COMPARISON")

textobject = c.beginText()
textobject.setTextOrigin(40, 7.9*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Elastic Elongation
                         ''')
c.drawText(textobject)

c.drawImage(i3,40,4.2*inch,width=3.5*inch,height=3.5*inch)

c.drawImage(i4,43,0.5*inch,width=3.75*inch,height=3*inch)

ad1 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Elongation of the  rope occurring whenever a rope is loaded. When the load is removed, the rope is restored to its initial state</para>',stylesN)
ad2 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>E xample: With a DP9 rope, a load of 8.3 % of the minimum breaking force results in an elastic elongation of ca. 0.109 % of the length of the rope (with a length of 100 m, this is equivalent to 109 mm)</para>',stylesN)
ad3 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Elevator ropes from BRUGG LIFTING are especially characterized by a very low elastic elongation</para>',stylesN)

a = [[ad1],[ad2],[ad3]]
at=Table(a,colWidths=9.5*cm)
at.wrapOn(c,width,height)
at.drawOn(c,4.5*inch,5.1*inch)

ad1 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Elongation of the rope occurring until the rope has settled as a result of operation. This elongation is expected to occur at about 2% of the estimated rope service life</para>',stylesN)
ad2 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>The graphic compares the permanent elongation of the different types of suspension ropes</para>',stylesN)
ad3 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Elevator ropes from BRUGG LIFTING are especially characterized by a very low permanent elongation</para>',stylesN)

a = [[ad1],[ad2],[ad3]]
at=Table(a,colWidths=9.5*cm)
at.wrapOn(c,width,height)
at.drawOn(c,4.5*inch,1.5*inch)

textobject = c.beginText()
textobject.setTextOrigin(40, 3.7*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Permanent Elongation
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
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "8")



c.showPage()


c.drawImage(b3,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
# For HRS

c.drawImage(bg7,0*inch,8.25*inch,width=8.5*inch,height=0.25*inch,mask='auto')

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(bg8)
scaleFactor = 1/1.95
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,8.25*inch)

i = Paragraph('<para color=white fontsize=18><b>ROPE COMPARISON.<span color=rgb(0,157,224)><b> i</b></span>LINE</b></para>',stylesN)
di = [[i]]
dti = Table(di)
dti.wrapOn(c,width,height)
dti.drawOn(c,30,8.85*inch)


textobject = c.beginText()
textobject.setTextOrigin(40, 7.9*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Minimum Breaking Load
                         ''')
c.drawText(textobject)

c.drawImage(i5,40,4.7*inch,width=4*inch,height=3*inch)

c.drawImage(i6,370,1.3*inch,width=2*inch,height=2.5*inch)

c.drawImage(i7,535,0.7*inch,width=1*inch,height=3*inch)

ad1 = Paragraph('<para leftindent=10 align="justify" fontsize=10 leading=15><bullet>&bull;</bullet>MBL represents the minimum load that can be applied to a rope before it breakse</para>',stylesN)
ad2 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>The graphic compares the minimum breaking load of the different types of suspension ropes</para>',stylesN)
ad3 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Reference: 100 % = 8x19 suspension rope with natural fiber core</para>',stylesN)

a = [[ad1],[ad2],[ad3]]
at=Table(a,colWidths=9.5*cm)
at.wrapOn(c,width,height)
at.drawOn(c,4.5*inch,6.25*inch)

id =Paragraph('<para fontsize=15 spaceAfter=2><span color=rgb(0,157,224)><b>i</b></span><b>Line & Color Coding</b><br/></para>',stylesN)
id1 =Paragraph('<para fontsize=10 leading=13 align="justify">Correctly installed hoist ropes increase the service life and the safety.They improve the riding comfort and avoid downtimes. Independent of the construction and the producer, every hoist rope is susceptible to untwisting during the installation.</para>',stylesN)
id2 =Paragraph('<para fontsize=10 leading=13 align="justify">With the help of the i-LINE, which is applied to our hoist ropes by BRUGG LIFTING already during the production, untwisted hoist ropes can be detected easily and fast, located and adjusted correctly.</para>',stylesN)

idd = [[id],'',[id1],[id2]]
idt = Table(idd,colWidths=10*cm)
idt.wrapOn(c,width,height)
idt.drawOn(c,40,1.75*inch)

ad = Paragraph('<para  align="justify" fontsize=14 leading=15><b>Advantages of the <span color=rgb(0,157,224)><b>i</b></span>LINE</b></para>',stylesN)
ad1 = Paragraph('<para leftindent=13 align="justify" fontsize=10 leading=15><bullet>&bull;</bullet>simple and correct installation</para>',stylesN)
ad2 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>safe installation aid</para>',stylesN)
ad3 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>optimizes product performance</para>',stylesN)
ad4 = Paragraph('<para leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>colour code for the identification of the rope type</para>',stylesN)


a = [[ad],[ad1],[ad2],[ad3],[ad4]]
at=Table(a,colWidths=9.5*cm)
at.wrapOn(c,width,height)
at.drawOn(c,40,0.2*inch)


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

i1 = "i1.png"
i2 = "i2.png"
b1 = "b1.png"
b2 = "b2.png"
b3 = "b3.png"
b4 = "b4.png"
b5 = "b5.png"
b6 = "b6.png"
b7 = "b7.png"
l1 = "e1-01.png"
d = "ropetech.png"
bg = "img1.jpg"
logo = "brugglifting.svg"
e1= "P10Strip.png"
e2= "P10Bannerimg.png"
e3= "P11Strip.png"
e4 = "P11Strip.svg"
e5 = "P10bgGred.png"
e6 = "P11img3.png"
e7 = "P10BruggLiftingCom.png"
bgp11 = "p11BannerImg.png"

width,height=A4

c.drawImage(e5,0*inch,0*inch,width=8.5*inch,height=8.25*inch)

c.drawImage(e2,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
c.drawImage(e1,0*inch,8.25*inch,width=8.5*inch,height=0.9*inch,mask='auto')

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.2*inch)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(30, 8.55*inch, "ELEVATOR ROPES . ACCESSORIES")
c.setFillGray(0.5)
# c.rect(448,8.5*inch, 6*inch, 0.25*inch,stroke=0,fill=1)

p = Paragraph('''<para fontsize=10  leading=12 align="justify">BRUGG LIFTING elevator ropes are a symbol of the highest quality.<br/><br/>To ensure that our customers can rely on the consistent excellent quality of our products, we control all our manufacturing processes very tightly and continuously validate the quality of our products with a sophisticated system. Already the wire material is selected by us with the greatest care. We purchase our raw materials exclusively from suppliers that permanently meet our high standards. Further essential factors for the high product quality are modern production technologies
and especially the experience of many years of our qualified skilled workers.In order to guarantee a complete production quality we use the most modern measuring and monitoring techniques in our production lines.After that all our products are subjected to fatigue tests and property analysis with statistical evaluation at our in-house test facility. <br/><br/> As a customer you benefit from the products that stand out due to the very best values concerning elongation, breaking load, smoothness of ride and service ife. Thus BRUGG LIFTING elevator ropes symbolize the highest economic value  and a cost performance ratio that convinces again and again.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,3.35*inch)

c.drawImage(i1,4.4*inch,3.75*inch,width=3.4*inch,height=3.75*inch)

# c.drawImage(z9,0*inch,8.1*inch,width=8.5*inch,height=0.3*inch)

# drawing = svg2rlg(z2)
# scaleFactor = 1/1.85
# drawing.width *= scaleFactor
# drawing.height *= scaleFactor
# drawing.scale(scaleFactor, scaleFactor)
# renderPDF.draw(drawing, c, 0,8.1*inch)

textobject = c.beginText()
textobject.setTextOrigin(2*inch, 0.4*inch)
textobject.setFont("Helvetica-Bold", 50)
textobject.setFillColorRGB(255,255,255)
textobject.textLines('''
                        brugglifting.com
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
t.drawOn(c, -2.8*inch,0.2*inch)

c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",10)
c.drawString(20, 0.15*inch, "10")





c.showPage()

c.drawImage(e5,0*inch,0*inch,width=8.5*inch,height=8.25*inch)

# c.linearGradient(10*mm, 180*mm, 30*mm, 30*mm, (colors.white,colors.gray),extend=True)
c.drawImage(e6,30,0.6*inch,width=6.5*inch,height=3*inch)

c.drawImage(i2,4.5*inch,2.5*inch,width=3.1*inch,height=3.5*inch)

c.drawImage(bgp11,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(bg7,0*inch,8.25*inch,width=8.5*inch,height=0.25*inch,mask='auto')

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(bg9)
scaleFactor = 1/2.17
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

p = Paragraph('''<para fontsize=10  leading=15 align="justify">As system supplier we have the corresponding end termi-nations, buffer systems and accessories for all elevator
ropes in our range of products.<br/><br/> Most items are available from inventory, allowing short delivery times and state of the art logistics.<br/><br/> We are specialized in the development and manufacture of threaded swaged end fittings and are also able to provide customized end terminations.
</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,30,5.5*inch)


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
f1= "P12bannerImg.png"
f2= "P12Strip.png"
a1 = "P12Strip.svg"

width, height = A4

c.drawImage(f1,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

# c.rect(-20,8.33*inch, 2.5*inch, 0.75*inch,stroke=0,fill=1)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.25*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(35, 8.6*inch, "HRS")

c.setFont("Helvetica",12)
c.setFillColor('#ffffff')
c.drawString(250, 8.35*inch, "HOIST ROPES")


p = Paragraph('''<para fontsize=9><b>Steel Core Rope, 9 Strands, Parallel Lay</b></para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.75*inch)

p = Paragraph('''<para fontsize=8>For highest demands on  breaking force,elongation adn number of trips.Recommended for round grooves with an undercut angle of < 85.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.4*inch)



c.setFillColor('#7EBBEA')
c.rect(195,6.5*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=8 leading=9><b>125,000</b> <br/> N/mm2<br/><b>1.81x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,182,6.55*inch)
tph1= Paragraph('''<para fontsize=7 align="center">E-Module**</para>''',stylesN)
tpht1=[[tph1]]
tphtt1=Table(tpht1,colWidths=1*inch)
tphtt1.wrapOn(c,width,height)
tphtt1.drawOn(c,185,6.25*inch)

c.setFillColor('#A4C4E4')
c.rect(260,6.5*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=8 leading=9><b>0.104</b> <br/> %<br/><b>1.2</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,247,6.55*inch)
tph2= Paragraph('''<para fontsize=7 align="center">Elastic<br/> elongation</para>''',stylesN)
tpht2=[[tph2]]
tphtt2=Table(tpht2,colWidths=1*inch)
tphtt2.wrapOn(c,width,height)
tphtt2.drawOn(c,250,6.1*inch)

c.setFillColor('#B8D6F5')
c.rect(325,6.5*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=8 leading=9><b>0.13</b> <br/> %<br/><b>1.6</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,312,6.55*inch)
tph3= Paragraph('''<para fontsize=7 align="center">Permenant<br/> Elongation</para>''',stylesN)
tpht3=[[tph3]]
tphtt3=Table(tpht3,colWidths=1*inch)
tphtt3.wrapOn(c,width,height)
tphtt3.drawOn(c,315,6.1*inch)


c.setFillColor('#DCE7FE')
c.rect(390,6.5*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=8 leading=9><b><425</b> <br/> m<br/><b><1400</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,378,6.55*inch)
tph4= Paragraph('''<para fontsize=7 align="center">Lifting height*</para>''',stylesN)
tpht4=[[tph4]]
tphtt4=Table(tpht4,colWidths=1*inch)
tphtt4.wrapOn(c,width,height)
tphtt4.drawOn(c,381,6.25*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/>min.<br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-15 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)


i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)


tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10702','9.0','-','56.3','12.657','35.5','0.239','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10705','10.0','-','68.0','15.287','42.8','0.288','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10708','11.0','7/16','83.4','18.749','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],


]
tabf=Table(tabl_f,colWidths=[1.7*cm,1.2*cm,1.2*cm,2.3*cm,1.95*cm,1.7*cm,1.2*cm,2.2*cm],rowHeights=6*mm)
tabf.setStyle(TableStyle([

                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(2,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),6),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-35),

                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),

                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,190,2.25*inch)

tp = Paragraph('<para fontsize=8>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,190,1.8*inch)


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
c.drawString(20, 0.15*inch, "12")



c.showPage()

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
a1 = "P13Strip.svg"
a2 = "P13DP9Rope.png"
bgp13 = "p13Banner.png"
bgp14 = "P14Banner.png"

width, height = A4

c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

c.drawImage(bgp13,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

# c.rect(480,8.33*inch, 2.5*inch, 0.75*inch,stroke=0,fill=1)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#000000')
c.drawString(520, 8.6*inch, "DP9")

c.setFont("Helvetica",12)
c.setFillColor('#000000')
c.drawString(250, 8.35*inch, "HOIST ROPES")


c.setFont("Helvetica-Bold",8)


p = Paragraph('''<para fontsize=8 fontname="Helvetica-Bold"><b>Wire Rope with Polypropylene Fiber Core, 9 Strands, Parallel Lay</b></para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=4.25*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.85*inch)

p = Paragraph('''<para fontsize=8 >For high demands on breaking force, elongation and number of trips.<br/>
                 Recommended for conical grooves and undercut round grooves.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.5*inch)

c.setFillColor('#F3EB76')
c.rect(195,6.6*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=8 leading=9><b>115.000</b> <br/> N/mm2<br/><b>1.67x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,182,6.6*inch)
tph1= Paragraph('''<para fontsize=7 align="center">E-Module**</para>''',stylesN)
tpht1=[[tph1]]
tphtt1=Table(tpht1,colWidths=1*inch)
tphtt1.wrapOn(c,width,height)
tphtt1.drawOn(c,185,6.25*inch)

c.setFillColor('#FDF18B')
c.rect(260,6.6*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=8 leading=9><b>0.112</b> <br/> %<br/><b>1.35</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,247,6.6*inch)
tph2= Paragraph('''<para fontsize=7 align="center">Elastic<br/> elongation</para>''',stylesN)
tpht2=[[tph2]]
tphtt2=Table(tpht2,colWidths=1*inch)
tphtt2.wrapOn(c,width,height)
tphtt2.drawOn(c,250,6.1*inch)

c.setFillColor('#F7F5BC')
c.rect(325,6.6*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=8 leading=9><b>0.25</b> <br/> %<br/><b>3</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,312,6.6*inch)
tph3= Paragraph('''<para fontsize=7 align="center">Permenant<br/> Elongation</para>''',stylesN)
tpht3=[[tph3]]
tphtt3=Table(tpht3,colWidths=1*inch)
tphtt3.wrapOn(c,width,height)
tphtt3.drawOn(c,315,6.1*inch)


c.setFillColor('#FFF6D7')
c.rect(390,6.6*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=8 leading=9><b><250</b> <br/> m<br/><b><800</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,378,6.6*inch)
tph4= Paragraph('''<para fontsize=7 align="center">Lifting height*</para>''',stylesN)
tpht4=[[tph4]]
tphtt4=Table(tpht4,colWidths=1*inch)
tphtt4.wrapOn(c,width,height)
tphtt4.drawOn(c,381,6.25*inch)


itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/>min.<br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-15 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)

i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)


tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10702','9.0','-','56.3','12.657','35.5','0.239','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10705','10.0','-','68.0','15.287','42.8','0.288','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10708','11.0','7/16','83.4','18.749','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],


]
tabf=Table(tabl_f,colWidths=[1.5*cm,1*cm,1*cm,2.1*cm,1.75*cm,1.5*cm,1*cm,2*cm],rowHeights=4.75*mm)
tabf.setStyle(TableStyle([

                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(2,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),6),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-35),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),

                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,190,3.45*inch)

tp = Paragraph('<para fontsize=6>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,190,3*inch)

tp1 = Paragraph('<para fontsize=6>* The defined lifting height is based on an elevator with a 1:1 suspension and only indicative.<br/>It does not replace the exact calculation according to the system specifications.<br/>**E-Module tested according to DIN 18800.The specified E-Module is tested with 30-40% of MBL.</para>',stylesN)
tp1t=[[tp1]]
tptab1=Table(tp1t)
tptab1.wrapOn(c,width,height)
tptab1.drawOn(c,188,0.5*inch)

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
c.drawString(580, 0.15*inch, "13")



c.showPage()

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
a1 = "P14Banner.png"
a2 = "P14Strip.svg"

width, height = A4

c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

c.drawImage(bgp14,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.2*inch)
c.setFillColor('#83BCDD')
# c.rect(480,8.33*inch, 2.5*inch, 0.75*inch,stroke=0,fill=1


drawing = svg2rlg(a2)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.setFont("Helvetica-Bold",8)

# c.drawString(195, 8.4*inch, "HOIST ROPES")
# c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

p = Paragraph('''<para fontsize=9><b>Steel Core Rope, 9 Strands, Parallel Lay</b></para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=4.25*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.82*inch)

p = Paragraph('''<para fontsize=8>For highest demands on breaking force, elongation and number of trips,<br/> also under difficult installation conditions.<br/> Recommended for round grooves with an undercut angle of <= 85.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=4.25*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.3*inch)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(35, 8.6*inch, "SCX9")

c.setFont("Helvetica",12)
c.setFillColor('#ffffff')
c.drawString(250, 8.35*inch, "HOIST ROPES")

c.setFillColor('#AAC1E3')
c.rect(195,6*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" leading=10 fontsize=8><b>125,000</b> <br/> N/mm2<br/><b>1.81x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,182,6*inch)
tph1= Paragraph('''<para fontsize=7 align="center">E-Module**</para>''',stylesN)
tpht1=[[tph1]]
tphtt1=Table(tpht1,colWidths=1*inch)
tphtt1.wrapOn(c,width,height)
tphtt1.drawOn(c,185,5.75*inch)

c.setFillColor('#B3D2ED')
c.rect(260,6*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center" leading=10  fontsize=8><b>0.104</b> <br/> %<br/><b>1.2</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,247,6*inch)
tph2= Paragraph('''<para fontsize=7 align="center">Elastic<br/> elongation</para>''',stylesN)
tpht2=[[tph2]]
tphtt2=Table(tpht2,colWidths=1*inch)
tphtt2.wrapOn(c,width,height)
tphtt2.drawOn(c,250,5.6*inch)

c.setFillColor('#C7DDF1')
c.rect(325,6*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center" leading=10   fontsize=8><b>0.13</b> <br/> %<br/><b>1.6</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,312,6*inch)
tph3= Paragraph('''<para fontsize=7 align="center">Permenant<br/> Elongation</para>''',stylesN)
tpht3=[[tph3]]
tphtt3=Table(tpht3,colWidths=1*inch)
tphtt3.wrapOn(c,width,height)
tphtt3.drawOn(c,315,5.6*inch)


c.setFillColor('#DBEBF7')
c.rect(390,6*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center" leading=10  fontsize=8><b><425</b> <br/> m<br/><b><1400</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,378,6*inch)
tph4= Paragraph('''<para fontsize=7 align="center">Lifting height*</para>''',stylesN)
tpht4=[[tph4]]
tphtt4=Table(tpht4,colWidths=1*inch)
tphtt4.wrapOn(c,width,height)
tphtt4.drawOn(c,381,5.75*inch)


itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/>min.<br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-15 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)


i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)


tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10702','9.0','-','56.3','12.657','35.5','0.239','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10705','10.0','-','68.0','15.287','42.8','0.288','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10708','11.0','7/16','83.4','18.749','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],


]
tabf=Table(tabl_f,colWidths=[1.7*cm,1.2*cm,1.2*cm,2.3*cm,1.95*cm,1.7*cm,1.2*cm,2.2*cm],rowHeights=6*mm)
tabf.setStyle(TableStyle([

                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(2,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),6),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-35),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,190,2.25*inch)

tp = Paragraph('<para fontsize=6>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,190,1.8*inch)

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
c.drawString(20, 0.15*inch, "14")



c.showPage()

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
a2 = "P15BannerImg.png"
a3 = "P15Strip.svg"

width, height = A4

c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

c.drawImage(a2,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')
# c.rect(480,8.33*inch, 2.5*inch, 0.75*inch,stroke=0,fill=1)

drawing = svg2rlg(a3)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

p = Paragraph('''<para fontsize=9><b>Steel Core Rope, 9 Strands, Parallel Lay</b></para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.75*inch)

p = Paragraph('''<para fontsize=8>For highest demands on  breaking force,elongation adn number of trips.<br/>Recommended for round grooves with an undercut angle of < 85.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.4*inch)

c.setFillColor('#F9C780')
c.rect(195,6.1*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=7 leading=10><b>110.000</b> <br/> N/mm2<br/><b>16x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,182,6.1*inch)
tph1= Paragraph('''<para fontsize=7 align="center">E-Module**</para>''',stylesN)
tpht1=[[tph1]]
tphtt1=Table(tpht1,colWidths=1*inch)
tphtt1.wrapOn(c,width,height)
tphtt1.drawOn(c,185,5.85*inch)

c.setFillColor('#F7D69E')
c.rect(260,6.1*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.120</b> <br/> %<br/><b>1.5</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,247,6.1*inch)
tph2= Paragraph('''<para fontsize=7 align="center">Elastic<br/> elongation</para>''',stylesN)
tpht2=[[tph2]]
tphtt2=Table(tpht2,colWidths=1*inch)
tphtt2.wrapOn(c,width,height)
tphtt2.drawOn(c,250,5.7*inch)

c.setFillColor('#FDE2B7')
c.rect(325,6.1*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center"  fontsize=7 leading=10><b>0.30</b> <br/> %<br/><b>4</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,312,6.1*inch)
tph3= Paragraph('''<para fontsize=7 align="center">Permenant<br/> Elongation</para>''',stylesN)
tpht3=[[tph3]]
tphtt3=Table(tpht3,colWidths=1*inch)
tphtt3.wrapOn(c,width,height)
tphtt3.drawOn(c,315,5.7*inch)


c.setFillColor('#FFEBD1')
c.rect(390,6.1*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=7 leading=10><b><200</b> <br/> m<br/><b><650</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,378,6.1*inch)
tph4= Paragraph('''<para fontsize=7 align="center">Lifting height*</para>''',stylesN)
tpht4=[[tph4]]
tphtt4=Table(tpht4,colWidths=1*inch)
tphtt4.wrapOn(c,width,height)
tphtt4.drawOn(c,381,5.85*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/>min.<br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-15 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)

i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)

tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10702','9.0','-','56.3','12.657','35.5','0.239','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10705','10.0','-','68.0','15.287','42.8','0.288','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10708','11.0','7/16','83.4','18.749','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],


]
tabf=Table(tabl_f,colWidths=[1.5*cm,1*cm,1*cm,2.1*cm,1.75*cm,1.5*cm,1*cm,2*cm],rowHeights=5*mm)
tabf.setStyle(TableStyle([

                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(2,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),6),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-35),
                            ('VALIGN', (0, 0),(-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,190,3.5*inch)

tp = Paragraph('<para fontsize=7>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,190,3.05*inch)

tp1 = Paragraph('<para fontsize=7>* The defined lifting height is based on an elevator with a 1:1 suspension and only indicative.<br/>It does not replace the exact calculation according to the system specifications.<br/>**E-Module tested according to DIN 18800.The specified E-Module is tested with 30-40% of MBL.</para>',stylesN)
tp1t=[[tp1]]
tptab1=Table(tp1t)
tptab1.wrapOn(c,width,height)
tptab1.drawOn(c,188,0.5*inch)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#000000')
c.drawString(520, 8.6*inch, "MCX9")

c.setFont("Helvetica",12)
c.setFillColor('#000000')
c.drawString(250, 8.35*inch, "HOIST ROPES")

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
c.drawString(580, 0.15*inch, "15")



c.showPage()

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
a1= "P16BannerImg1.png"
a2=  "P16Strip.svg"

width, height = A4

c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

c.drawImage(a1,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.2*inch)
c.setFillColor(colors.white)

drawing = svg2rlg(a2)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.26*inch)


p = Paragraph('''<para fontsize=9><b>Wire Rope with Sisal Fiber Core, 8 Strands</b></para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.95*inch)

p = Paragraph('''<para fontsize=8>For high demands on elongation also under difficult installation conditions.<br/>Recommended for all groove shapes.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.4*inch)


c.setFillColor(colors.white)
c.rect(195,6.6*inch, 0.65*inch, 0.65*inch,stroke=1,fill=1)
tp1 = Paragraph('''<para align="center" fontsize=8 leading=10><b>125,000</b> <br/> N/mm2<br/><b>1.81x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,182,6.6*inch)
tph1= Paragraph('''<para fontsize=8 align="center">E-Module**</para>''',stylesN)
tpht1=[[tph1]]
tphtt1=Table(tpht1,colWidths=1*inch)
tphtt1.wrapOn(c,width,height)
tphtt1.drawOn(c,185,6.25*inch)

c.setFillColor(colors.white)
c.rect(260,6.6*inch, 0.65*inch, 0.65*inch,stroke=1,fill=0)
tp2 = Paragraph('''<para align="center"  fontsize=8 leading=10><b>0.104</b> <br/> %<br/><b>1.2</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,247,6.6*inch)
tph2= Paragraph('''<para fontsize=8 align="center">Elastic<br/> elongation</para>''',stylesN)
tpht2=[[tph2]]
tphtt2=Table(tpht2,colWidths=1*inch)
tphtt2.wrapOn(c,width,height)
tphtt2.drawOn(c,250,6.1*inch)

c.setFillColor(colors.white)
c.rect(325,6.6*inch, 0.65*inch, 0.65*inch,stroke=1,fill=0)
tp3 = Paragraph('''<para align="center"  fontsize=8 leading=10><b>0.13</b> <br/> %<br/><b>1.6</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,312,6.6*inch)
tph3= Paragraph('''<para fontsize=8 align="center">Permenant<br/> Elongation</para>''',stylesN)
tpht3=[[tph3]]
tphtt3=Table(tpht3,colWidths=1*inch)
tphtt3.wrapOn(c,width,height)
tphtt3.drawOn(c,315,6.1*inch)


c.setFillColor(colors.white)
c.rect(390,6.6*inch, 0.65*inch, 0.65*inch,stroke=1,fill=1)
tp4 = Paragraph('''<para align="center"  fontsize=8 leading=10><b><425</b> <br/> m<br/><b><1400</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch,rowHeights=1*mm)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,378,6.6*inch)
tph4= Paragraph('''<para fontsize=8 align="center">Lifting height*</para>''',stylesN)
tpht4=[[tph4]]
tphtt4=Table(tpht4,colWidths=1*inch)
tphtt4.wrapOn(c,width,height)
tphtt4.drawOn(c,381,6.25*inch)


c.setFont("Helvetica-Bold",28)
c.setFillColor('#000000')
c.drawString(35, 8.6*inch, "8x19")

c.setFont("Helvetica",12)
c.setFillColor('#000000')
c.drawString(250, 8.35*inch, "HOIST ROPES")


itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/>min.<br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-15 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)


i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)


tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10702','9.0','-','56.3','12.657','35.5','0.239','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10705','10.0','-','68.0','15.287','42.8','0.288','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10708','11.0','7/16','83.4','18.749','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],

]
tabf=Table(tabl_f,colWidths=[1.6*cm,1.1*cm,1.1*cm,2.2*cm,1.85*cm,1.6*cm,1.1*cm,2.1*cm],rowHeights=6*mm)
tabf.setStyle(TableStyle([
                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(2,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),6),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-35),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,190,1.5*inch)

tp = Paragraph('<para fontsize=8>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,190,1*inch)


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
c.drawString(20, 0.15*inch, "16")

c.showPage()

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
a2 = "P17Bannerimg.png"
a3 = "P17Strip.svg"

width, height = A4

c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

c.drawImage(a2,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(a3)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.setFillColor(colors.white)

c.setFont("Helvetica-Bold",8)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(520, 8.6*inch, "TSR")

c.setFont("Helvetica",12)
c.setFillColor('#ffffff')
c.drawString(250, 8.35*inch, "HOIST ROPES")

p = Paragraph('''<para fontsize=9><b>Steel Core Rope, 6 Strands, Zinc-Plated, Separate Lay</b></para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.7*inch)

p = Paragraph('''<para fontsize=8>For high demands on small traction sheaves.<br/>Suitable for conical grooves of => 45..</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,190,7.3*inch)

c.setFillColor('#C8C8C8')
c.rect(195,6.45*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" leading=9 fontsize=6><b>125,000</b> <br/> N/mm2<br/><b>1.81x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,180,6.42*inch)
tph1= Paragraph('''<para fontsize=7 align="center">E-Module**</para>''',stylesN)
tpht1=[[tph1]]
tphtt1=Table(tpht1,colWidths=1*inch)
tphtt1.wrapOn(c,width,height)
tphtt1.drawOn(c,180,6.1*inch)

c.setFillColor('#D0D0D0')
c.rect(260,6.45*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center" leading=9  fontsize=6><b>0.104</b> <br/> %<br/><b>1.2</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,243,6.42*inch)
tph2= Paragraph('''<para fontsize=7 align="center">Elastic<br/> elongation</para>''',stylesN)
tpht2=[[tph2]]
tphtt2=Table(tpht2,colWidths=1*inch)
tphtt2.wrapOn(c,width,height)
tphtt2.drawOn(c,245,5.95*inch)


c.setFillColor('#D3D3D3')
c.rect(325,6.45*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center" leading=9   fontsize=6><b>0.13</b> <br/> %<br/><b>1.6</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,308,6.42*inch)
tph3= Paragraph('''<para fontsize=7 align="center">Permenant<br/> Elongation</para>''',stylesN)
tpht3=[[tph3]]
tphtt3=Table(tpht3,colWidths=1*inch)
tphtt3.wrapOn(c,width,height)
tphtt3.drawOn(c,310,5.95*inch)


c.setFillColor('#D8D8D8')
c.rect(390,6.45*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp4 = Paragraph('''<para align="center" leading=9  fontsize=6><b><425</b> <br/> m<br/><b><1400</b><br/>ft</para>''',stylesN)
tpt4 = [[tp4]]
tp44 = Table(tpt4,colWidths=1*inch)
tp44.wrapOn(c,width,height)
tp44.drawOn(c,372,6.42*inch)
tph4= Paragraph('''<para fontsize=7 align="center">Lifting height*</para>''',stylesN)
tpht4=[[tph4]]
tphtt4=Table(tpht4,colWidths=1*inch)
tphtt4.wrapOn(c,width,height)
tphtt4.drawOn(c,379,6.1*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/>min.<br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-15 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)

i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)

tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)']
]
tabf=Table(tabl_f,colWidths=[1.5*cm,1*cm,1*cm,2.1*cm,1.75*cm,1.5*cm,1*cm,2*cm],rowHeights=6*mm)
tabf.setStyle(TableStyle([
                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(2,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),6),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-35),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,190,4.25*inch)

tp = Paragraph('<para fontsize=7>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,190,3.8*inch)

tp1 = Paragraph('<para fontsize=7>* The defined lifting height is based on an elevator with a 1:1 suspension and only indicative.<br/>It does not replace the exact calculation according to the system specifications.<br/>**E-Module tested according to DIN 18800.The specified E-Module is tested with 30-40% of MBL.</para>',stylesN)
tp1t=[[tp1]]
tptab1=Table(tp1t)
tptab1.wrapOn(c,width,height)
tptab1.drawOn(c,188,0.5*inch)

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
c.drawString(580, 0.15*inch, "17")


c.showPage()

logo = "brugglifting.svg"
bg = "P18BannerImg.png"
bg1 = "P19BannerImg.png"
hrs = "hrs.jpg"
scx9 = "hrs.jpg"
sc8 = "hrs.jpg"
dp9 = "hrs.jpg"
X19 = "hrs.jpg"
tsr = "hrs.jpg"
x25 = "hrs.jpg"
sx25 = "hrs.jpg"
a1 = "P18Strip.svg"
a2 = "P19Strip.svg"
a3 = "P18Strip2.svg"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 10.2*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

# c.drawImage(a3,0*inch,4.25*inch,width=2*inch,height=1*inch)

drawing = svg2rlg(a3)
scaleFactor = 1/2.2
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 4.25*inch)

c.drawImage(X19,30,6.5*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor('#3C434B')

p = Paragraph('''<para fontsize=9><b>Wire Rope with Polypropylene Core, 8 Strands, Seale</b></para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,165,7.7*inch)

p = Paragraph('''<para fontsize=8>FCompensation ropes are used to balance the weight of <br/> hoist ropes and travelling cables in an elevator.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,165,7.3*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="right"   fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/><br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-25 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center" leftindent=-20   fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)

i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)

tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)']
]

tabf=Table(tabl_f,colWidths= [1.6*cm,1.6*cm,1.1*cm,2.2*cm,1.85*cm,1.6*cm,1.1*cm,2.1*cm],rowHeights=5.5*mm)
tabf.setStyle(TableStyle([

                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(1,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),7),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-30),
                            ('LEFTPADDING',(5,0),(-1,-1),-50),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,165,6*inch)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(35, 8.6*inch, "8x19")

c.setFont("Helvetica",12)
c.setFillColor('#ffffff')
c.drawString(250, 8.35*inch, "COMPONSATION ROPES")

tp = Paragraph('<para fontsize=7>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,165,5.5*inch)

c.drawImage(x25,30,2.25*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(35, 4.65*inch, "8x25")

p = Paragraph('''<para fontsize=9><b>Wire Rope with Polypropylene Core, 8 Strands, Filler</b></para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,165,3.7*inch)

p = Paragraph('''<para fontsize=8>Compensation ropes are used to balance the weight of<br/> hoist ropes and travelling cables in an elevator.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,165,3.3*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/><br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-25 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center" leftindent=-20   fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)

i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)

tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)']
]

tabf=Table(tabl_f,colWidths= [1.65*cm,1.65*cm,1.15*cm,2.25*cm,1.9*cm,1.65*cm,1.15*cm,2.15*cm],rowHeights=5*mm)
tabf.setStyle(TableStyle([

                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(1,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),7),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-30),
                            ('LEFTPADDING',(5,0),(-1,-1),-50),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,160,1.75*inch)

tp = Paragraph('<para fontsize=7>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,155,1.25*inch)


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
c.drawString(20, 0.15*inch, "18")




c.showPage()









c.drawImage(bg1,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(a2)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(520, 8.6*inch, "6x25")

c.drawImage(X19,30,6.5*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor('#3C434B')

p = Paragraph('''<para fontsize=8><b>Wire Rope with Polypropylene Core, 6 Strands,Filler</b><br/>Compensation ropes are used to balance the weight of<br/>
hoist ropes and travelling cables in an elevator.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,155,7.25*inch)
itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/><br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-25 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center" leftindent=-20   fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)

i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)

tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)']
]

tabf=Table(tabl_f,colWidths= [1.6*cm,1.6*cm,1.1*cm,2.2*cm,1.85*cm,1.6*cm,1.1*cm,2.1*cm],rowHeights=6*mm)
tabf.setStyle(TableStyle([
                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(1,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),7),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-30),
                            ('LEFTPADDING',(5,0),(-1,-1),-50),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,160,6*inch)

tp = Paragraph('<para fontsize=7>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,155,5.5*inch)


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
c.drawString(580, 0.15*inch, "19")




c.showPage()







logo = "brugglifting.svg"
bg = "P20BannerImg.png"
bg1 = "P21BannerImg.png"
hrs = "hrs.jpg"
scx9 = "hrs.jpg"
sc8 = "hrs.jpg"
dp9 = "hrs.jpg"
X19 = "hrs.jpg"
tsr = "hrs.jpg"
x25 = "hrs.jpg"
sx25 = "hrs.jpg"
ex = "ex.png"
a1="P20Strip.svg"
a2="P21Strip.svg"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 10.25*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

drawing = svg2rlg(a3)
scaleFactor = 1/2.75
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 4.25*inch)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(35, 8.6*inch, "6x19")

c.setFont("Helvetica",12)
c.setFillColor('#ffffff')
c.drawString(250, 8.35*inch, "GOVERNOR ROPES")

c.drawImage(X19,30,6.5*inch,width=1*inch,height=1*inch)
c.setFillColor('#3C434B')

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(35, 4.5*inch, "8x19")

p = Paragraph('''<para fontsize=9><b>Wire Rope with Polypropylene Core, 6 Strands, Seale</b><br/>Compensation ropes are used to balance the weight of<br/>
hoist ropes and travelling cables in an elevator.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,155,7.25*inch)

c.setFillColor('#D8D8D8')
c.rect(160,6.4*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" leading=10 fontsize=8><b>125,000</b> <br/> N/mm2<br/><b>1.81x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,146,6.4*inch)
tph1= Paragraph('''<para fontsize=8 align="center">E-Module**</para>''',stylesN)
tpht1=[[tph1]]
tphtt1=Table(tpht1,colWidths=1*inch)
tphtt1.wrapOn(c,width,height)
tphtt1.drawOn(c,145,6*inch)

c.setFillColor('#DCDCDC')
c.rect(220,6.4*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center" leading=10  fontsize=8><b>0.104</b> <br/> %<br/><b>1.2</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,206,6.4*inch)
tph2= Paragraph('''<para fontsize=8 align="center">Elastic<br/> elongation</para>''',stylesN)
tpht2=[[tph2]]
tphtt2=Table(tpht2,colWidths=1*inch)
tphtt2.wrapOn(c,width,height)
tphtt2.drawOn(c,205,5.9*inch)

c.setFillColor('#E0E0E0')
c.rect(280,6.4*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center" leading=10   fontsize=8><b>0.13</b> <br/> %<br/><b>1.6</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,266,6.4*inch)
tph3= Paragraph('''<para fontsize=8 align="center">Permenant<br/> Elongation</para>''',stylesN)
tpht3=[[tph3]]
tphtt3=Table(tpht3,colWidths=1*inch)
tphtt3.wrapOn(c,width,height)
tphtt3.drawOn(c,265,5.9*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="right"   fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/>min.<br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-25 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center" leftindent=-20   fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)

i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)

tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)']
]

tabf=Table(tabl_f,colWidths= [1.6*cm,1.6*cm,1.1*cm,2.2*cm,1.85*cm,1.6*cm,1.1*cm,2.1*cm],rowHeights=5.5*mm)
tabf.setStyle(TableStyle([
                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(1,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),7),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-30),
                            ('LEFTPADDING',(5,0),(-1,-1),-50),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,160,4.75*inch)

tp = Paragraph('<para fontsize=8>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,155,4.25*inch)

c.drawImage(x25,30,1.75*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
p = Paragraph('''<para fontsize=9><b>Wire Rope with Polypropylene Core, 8 Strands, Seale</b><br/>Compensation ropes are used to balance the weight of<br/>
hoist ropes and travelling cables in an elevator.</para>''',stylesN)
p1 =[[p]]
p11 = Table(p1,colWidths=3.75*inch)
p11.wrapOn(c,width,height)
p11.drawOn(c,155,3.25*inch)

c.setFillColor('#D0D0D0')
c.rect(160,2.4*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp1 = Paragraph('''<para align="center" leading=10 fontsize=8><b>125,000</b> <br/> N/mm2<br/><b>1.81x10 <super rise=2
size=6>6</super></b><br/>psi</para>''',stylesN)
tpt1 = [[tp1]]
tp11 = Table(tpt1,colWidths=1*inch,rowHeights=10*mm)
tp11.wrapOn(c,width,height)
tp11.drawOn(c,146,2.4*inch)
tph1= Paragraph('''<para fontsize=7 align="center">E-Module**</para>''',stylesN)
tpht1=[[tph1]]
tphtt1=Table(tpht1,colWidths=1*inch)
tphtt1.wrapOn(c,width,height)
tphtt1.drawOn(c,145,2.1*inch)

c.setFillColor('#D3D3D3')
c.rect(220,2.4*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp2 = Paragraph('''<para align="center" leading=10  fontsize=8><b>0.104</b> <br/> %<br/><b>1.2</b><br/>in/100ft</para>''',stylesN)
tpt2 = [[tp2]]
tp22 = Table(tpt2,colWidths=1*inch,rowHeights=1*mm)
tp22.wrapOn(c,width,height)
tp22.drawOn(c,206,2.4*inch)
tph2= Paragraph('''<para fontsize=7 align="center">Elastic<br/> elongation</para>''',stylesN)
tpht2=[[tph2]]
tphtt2=Table(tpht2,colWidths=1*inch)
tphtt2.wrapOn(c,width,height)
tphtt2.drawOn(c,205,1.9*inch)

c.setFillColor('#D8D8D8')
c.rect(280,2.4*inch, 0.65*inch, 0.65*inch,stroke=0,fill=1)
tp3 = Paragraph('''<para align="center" leading=10   fontsize=8><b>0.13</b> <br/> %<br/><b>1.6</b><br/>in/100ft</para>''',stylesN)
tpt3 = [[tp3]]
tp33 = Table(tpt3,colWidths=1*inch)
tp33.wrapOn(c,width,height)
tp33.drawOn(c,266,2.4*inch)
tph3= Paragraph('''<para fontsize=7 align="center">Permenant<br/> Elongation</para>''',stylesN)
tpht3=[[tph3]]
tphtt3=Table(tpht3,colWidths=1*inch)
tphtt3.wrapOn(c,width,height)
tphtt3.drawOn(c,265,1.9*inch)

c.setFont("Helvetica-Bold",28)
c.setFillColor('#ffffff')
c.drawString(35, 3.8*inch, "8x19")

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =8 >item<br/> number</para>',stylesN)
rope = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =8>rope-@ <br/></para>',stylesN)
brk = Paragraph('<para align="center" fontname = "Helvetica-Bold" fontsize =8>breaking load<br/>min.<br/></para>',stylesN)
weight= Paragraph('<para align="center" leftindent=-25 fontname = "Helvetica-Bold" fontsize =8>weight</para>',stylesN)
con = Paragraph('<para align="center" leftindent=-20   fontname = "Helvetica-Bold" fontsize =8>construction</para>',stylesN)

i = Paragraph('<para  fontname = "Helvetica" fontsize =8> </para>',stylesN)
mm1 = Paragraph('<para fontname = "Helvetica" fontsize =8>mm</para>',stylesN)
inc1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>in</para>',stylesN)
kN1= Paragraph('<para   fontname = "Helvetica" fontsize =8>kN</para>',stylesN)
lbs1 = Paragraph('<para leftindent=5 fontname = "Helvetica" fontsize =8>lbs</para>',stylesN)
kg1 = Paragraph('<para  fontname = "Helvetica" fontsize =8>kg/100m</para>',stylesN)
lb1 = Paragraph('<para   fontname = "Helvetica" fontsize =8>lb/ft</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =8 leftindent=-70></para>',stylesN)

tabl_f = [[itemn,rope,'',brk,'',weight,'',con],['','','','','','','',''],
            [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)'],
            ['10699','8.0','5/16','42.7','9.599','26.9','0.181','9x19S-PWRC 1570 U sZ.(RRL)']

]

tabf=Table(tabl_f,colWidths= [1.5*cm,1.5*cm,1*cm,2.1*cm,1.75*cm,1.5*cm,1*cm,2*cm],rowHeights=5*mm)
tabf.setStyle(TableStyle([
                            ('LINEABELOW',(0,2),(-1,-3),0.25,colors.black),
                            ('SPAN',(1,0),(1,0)),
                            ('SPAN',(2,0),(2,0)),
                            ('FONTSIZE',(0,1),(-1,-1),7),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(4,0),(-1,-1),-30),
                            ('LEFTPADDING',(5,0),(-1,-1),-50),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                       ]))
tabf.wrapOn(c,width,height)
tabf.drawOn(c,160,0.6*inch)

tp = Paragraph('<para fontsize=7>Further nominal strengths and/or diameters (including imperial dimensions) on request.<br/> Rope diameter-tolerances according to EN12385-5 / ISO 4344.</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,155,0.2*inch)

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
c.drawString(20, 0.15*inch, "20")

c.showPage()

c.drawImage(bg1,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

c.setFont("Helvetica-Bold",10)

c.drawImage(az1,0*inch,8.25*inch,width=8.5*inch,height=0.3*inch,mask='auto')

# drawing = svg2rlg(a2)
# scaleFactor = 1/1.25
# drawing.width *= scaleFactor
# drawing.height *= scaleFactor
# drawing.scale(scaleFactor, scaleFactor)
# renderPDF.draw(drawing, c, 0, 8.25*inch)

c.drawImage(ex,80,5.1*inch,width=2.5*inch,height=2.5*inch,preserveAspectRatio=True)

tp = Paragraph('<para fontsize=9>Desingation and Classification of wire ropes(EN 12385-2 formerly ISO 17893)</para>',stylesN)
tpt=[[tp]]
tptab=Table(tpt)
tptab.wrapOn(c,width,height)
tptab.drawOn(c,4*inch,7.5*inch)

c.setFillColor('#D0D0D0')
c.rect(4.5*inch,6.75*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)

c.setFillColor('#D3D3D3')
c.drawCentredString(4.57*inch,6.77*inch,"A")

tr = Paragraph('<para fontSize=8 ><b >Rope nominal Diameter in mm</b><br/>(see coresponding table for each )</para>',stylesN)
trt=[[tr]]
trtab=Table(trt)
trtab.wrapOn(c,width,height)
trtab.drawOn(c,4.75*inch,6.55*inch)

c.setFillColor('#D8D8D8')
c.rect(4.5*inch,6.3*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor('#3C434B')
c.drawCentredString(4.57*inch,6.33*inch,"B")
tr = Paragraph('<para fontSize=8 ><b >Rope Construction</b><br/></para>',stylesN)
trt=[[tr]]
trtab=Table(trt)
trtab.wrapOn(c,width,height)
trtab.drawOn(c,4.75*inch,6.25*inch)

tr = Paragraph('<para fontSize=8 ><b >Construction and Lay Direction</b><br/></para>',stylesN)
trt=[[tr]]
trtab=Table(trt)
trtab.wrapOn(c,width,height)
trtab.drawOn(c,4.75*inch,6*inch)

c.setFillColor('#DCDCDC')
c.rect(4.5*inch,6.05*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor('#3C434B')
c.drawCentredString(4.57*inch,6.08*inch,"C")
data1 = [['-','simple lay strand',''],
        ['' , 'example for strand construction','7 d.h.(1-6)'],
        ['s' , 'seale parallel lay',''],
        ['' , 'example for strand construction','19S d.h. (1-9-9)'],
        ['W','Warrington parallel lay',''],
        ['' , 'example for strand construction','19W d.h. (1-6-6+6)'],
        ['F' , 'Filler parallel lay',''],
        ['' , 'example for strand construction','21F d.h. (1-5-5F-10)'],
        ['' , '','25F d.h. (1-6-6F-12)'],
        ['WS' , 'combined (warrington seale) parallel lay',''],
        ['' , 'example for strand construction','31WS d.h. (1-6-6+6-12)'],
]

r = Table(data1,colWidths=[0.75*cm,3.25*cm,2*cm],rowHeights=4*mm)
r.setStyle(TableStyle([
                    ('FONTSIZE',(0,0),(-1,-1),7),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                             ('LEFTPADDING',(2,0),(-1,-1),50),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
r.wrapOn(c,width,height)
r.drawOn(c,4.75*inch,4.25*inch)

c.setFillColor('#DCDCDC')
c.rect(4.5*inch,3.9*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor('#3C434B')
c.drawCentredString(4.57*inch,3.93*inch,"D")

tr = Paragraph('<para fontSize=8 ><b >Construction of Core</b><br/></para>',stylesN)
trt=[[tr]]
trtab=Table(trt)
trtab.wrapOn(c,width,height)
trtab.drawOn(c,4.75*inch,3.85*inch)

data2 = [['Single layer rope with fibre core FC',''],
        ['NFC' , 'natural fibre core'],
        ['SFC' , 'synthetic fibre core'],
        ['' , ''],
        ['Single layer rope with fibre core WC',''],
        ['WSC' , 'wire strand core'],
        ['IWRC' , 'independant wire rope core',''],
        ['' , ''],
        ['Rope with parallel lay'],
        ['PWRC' , 'parallel wire rope core',''],
]

s = Table(data2,colWidths=17*mm,rowHeights=3*mm)
s.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                            ('LEFTPADDING',(2,0),(-1,-1),20),('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
s.wrapOn(c,width,height)
s.drawOn(c,4.75*inch,2.7*inch)

c.setFillColor('#DCDCDC')
c.rect(4.5*inch,2.4*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor('#3C434B')
c.drawCentredString(4.57*inch,2.43*inch,"E")

tr = Paragraph('<para fontSize=8 ><b >Nominal Tensile Grade of wires in N/mm2</b><br/></para>',stylesN)
trt=[[tr]]
trtab=Table(trt)
trtab.wrapOn(c,width,height)
trtab.drawOn(c,4.75*inch,2.35*inch)



c.setFillColor('#DCDCDC')
c.rect(4.5*inch,2.1*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor('#3C434B')
c.drawCentredString(4.57*inch,2.12*inch,"F")
tr = Paragraph('<para fontSize=8 ><b >Surface Finish of Wires</b><br/></para>',stylesN)
trt=[[tr]]
trtab=Table(trt)
trtab.wrapOn(c,width,height)
trtab.drawOn(c,4.75*inch,2.05*inch)

data3 = [['U','bright'],
        ['B' , 'zinc coated (classB)'],
]

u = Table(data3,colWidths=17*mm,rowHeights=3*mm)
u.setStyle(TableStyle([
                    ('FONTSIZE',(0,0),(-1,-1),7),
                    ('LEFTPADDING',(1,0),(-1,-1),7),
                    ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
u.wrapOn(c,width,height)
u.drawOn(c,4.75*inch,1.75*inch)

c.setFillColor('#DCDCDC')
c.rect(4.5*inch,1.5*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor('#3C434B')
c.drawCentredString(4.57*inch,1.53*inch,"G")
tr = Paragraph('<para fontSize=8 ><b >Type and Direction of Lay</b><br/></para>',stylesN)
trt=[[tr]]
trtab=Table(trt)
trtab.wrapOn(c,width,height)
trtab.drawOn(c,4.75*inch,1.43*inch)


data3 = [['z','right lay (strand)'],
        ['s','left lay (strand)'],
        ['Z','right lay (rope)'],
        ['S','left lay (rope)'],
        ['sZ(RRL)','regular lay,right hand'],
        ['zS(RLL)','rregular lay,left-hand'],
]

u = Table(data3,colWidths=17*mm,rowHeights=3.5*mm)
u.setStyle(TableStyle([
                    ('FONTSIZE',(0,0),(-1,-1),7),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
u.wrapOn(c,width,height)
u.drawOn(c,4.75*inch,0.6*inch)

c.setFont("Helvetica",12)
c.setFillColor('#ffffff')
c.drawString(250, 8.35*inch, "ABBREVIATED DESIGNATIONS")

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
c.drawString(580, 0.15*inch, "21")



c.showPage()

logo = "brugglifting.svg"
bg = "P22BannerImg.png"
product = "image3.jpg"
b = "1.png"
a1 = "P22Strip.svg"

c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1.0/1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,10.25*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.drawImage(b,30,0,width=1.5*inch,height=7.75*inch,mask='auto')

p1  =Paragraph('<para fontsize=20 color=white><b>APAG</b></para>',stylesN)
p2  =Paragraph('<para fontsize=12 color=white>Threaded Swaged Sockets</para>',stylesN)
d1 = [[p1,p2]]
dt1 = Table(d1,colWidths=[3*cm,7*cm])
dt1.setStyle(TableStyle([


                            ('LEFTPADDING',(1,0),(-1,-1),-20),
                            ('BOTTOMPADDING',(1,0),(-1,-1),-5)

                       ]))
dt1.wrapOn(c,width,height)
dt1.drawOn(c,30,8.6*inch)

p3 = Paragraph('<para><b>Product Data</b><br/></para>',stylesN)
p4 = Paragraph('<para><bullet>&bull;</bullet>APAG-end connections are TV tested and approved according to TRA  EN81.</para>',stylesN)
p5 = Paragraph('<para><bullet>&bull;</bullet>APAG-end connections transmits 80 of minimal breaking load of traction rope</para>',stylesN)
d2 =[[p3],[p4],[p5]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,2.5*inch,7.4*inch)
p6 = Paragraph('<para><b>Advantages</b><br/></para>',stylesN)
p7 = Paragraph('<para><bullet>&bull;</bullet>simple, fast and safe end termination</para>',stylesN)
p8 = Paragraph('<para><bullet>&bull;</bullet>shortened installation time, since no mounting of end connections by customers</para>',stylesN)
p9 = Paragraph('<para><bullet>&bull;</bullet>no special tools required</para>',stylesN)
p10 = Paragraph('<para align="justify" leftindent=10><bullet>&bull;</bullet>the compact type enables a very tight arrangement of ropes <br/>and parallel running ropes</para>',stylesN)
p11 = Paragraph('<para align="justify"><bullet>&bull;</bullet>simple securing against rotation</para>',stylesN)
p12 = Paragraph('<para align="justify"><bullet>&bull;</bullet>position of pilot hole for rope end</para>',stylesN)
p13 = Paragraph('<para align="justify"><bullet>&bull;</bullet>quiet operation because there are no individual parts</para>',stylesN)
d3 =[[p6],[p7],[p8],[p9],[p10],[p11],[p12],[p13]]
dt3 = Table(d3)
dt3.wrapOn(c,width,height)
dt3.drawOn(c,2.5*inch,5*inch)









itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >item<br/> number</para>',stylesN)
rope = Paragraph('<para   align="center"fontname = "Helvetica-Bold" fontsize =5>rope-@</para>',stylesN)

d1= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d1</para>',stylesN)
d2= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d2</para>',stylesN)
d3= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d3</para>',stylesN)
d4= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d4</para>',stylesN)

li1 = Paragraph('<para lindent=-50 fontname = "Helvetica-Bold" fontsize =5>  L1</para>',stylesN)
li2 = Paragraph('<para lindent=-50 fontname = "Helvetica-Bold" fontsize =5>  L2</para>',stylesN)
li3 = Paragraph('<para lindent=-50 fontname = "Helvetica-Bold" fontsize =5>  L3</para>',stylesN)
li4 = Paragraph('<para lindent=-50 fontname = "Helvetica-Bold" fontsize =5>  L4</para>',stylesN)

li5 = Paragraph('<para lindent=-35 fontname = "Helvetica" fontsize =5>dimensions in mm</para>',stylesN)
li6 = Paragraph('<para fontname = "Helvetica"  align="center" fontsize =5> mm</para>',stylesN)


itemn0 = Paragraph('<para  fontname = "Helvetica" fontsize =5  >10112</para>',stylesN)
rope0 = Paragraph('<para align="center"  fontname = "Helvetica" fontsize =5>6.0</para>',stylesN)

d10= Paragraph('<para    fontname = "Helvetica" fontsize =5> M 10</para>',stylesN)
d20= Paragraph('<para    fontname = "Helvetica" fontsize =5>  13</para>',stylesN)
d30= Paragraph('<para    fontname = "Helvetica" fontsize =5>  9.0</para>',stylesN)
d40= Paragraph('<para    fontname = "Helvetica" fontsize =5>  7</para>',stylesN)

li10 = Paragraph('<para lindent=-50 fontname = "Helvetica" fontsize =5>  240</para>',stylesN)
li20 = Paragraph('<para lindent=-50 fontname = "Helvetica" fontsize =5>  150</para>',stylesN)
li30 = Paragraph('<para lindent=-50 fontname = "Helvetica" fontsize =5>  66.0</para>',stylesN)
li40 = Paragraph('<para lindent=-50 fontname = "Helvetica" fontsize =5>  16.6</para>',stylesN)


apag1 = [
        [itemn,rope,d1,d2,d3,d4,'',li1,li2,li3,li4],
        ['','','','','','','','','','',''],
            ['','','','','','','','','','',''],
        ['',li6,'','','','',li5,'','','',''],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
   ]
# colWidths=[1.25* cm, 1.25* cm, 1 * cm,
                            # 1* cm, 1* cm,1* cm,1.5* cm,1* cm,1*cm,1*cm ]
apagt = Table(apag1, colWidths=[1.55* cm, 1.55* cm, 1.3 * cm,1.3* cm, 1.3* cm,1.3* cm,1.8* cm,1.3* cm,1.3*cm,1.3*cm],rowHeights=3.5*mm)
apagt.setStyle(TableStyle([
                     # ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     # ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,2),(-3,-1),0.25,colors.black),
                     ('BACKGROUND', (1, 0), (-10, -1), '#DCDCDC'),
                     ('FONTSIZE', (0, 0), (-1, -1), 5),

                     ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                     ('VALIGN', (0, 0), (-1, -1), 'TOP'),

                     ]))

apagt.wrapOn(c, 30, 300)
apagt.drawOn(c, 2.55*inch,0.3*inch)

textobject1 = c.beginText()
textobject1.setTextOrigin(2.5*inch, 0.2*inch)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''
                     Other sizes avaliable upon request.


''')

c.drawText(textobject1)





# c.setFont("Helvetica", 10)
# c.drawString(90,8.4*inch, "Threaded Swaged Sockets")
# c.setFont("Helvetica-Bold", 18)
# c.drawString(30,8.4*inch, "APAG")
# c.setFont("Helvetica-Bold", 18)

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
c.drawString(20, 0.15*inch, "22")





c.showPage()

logo = "brugglifting.svg"
bg = "P23BannerImg.png"
eye = "eye.png"
a1 = "P23Strip.svg"

width,height = A4

c.drawImage(bg,0*inch, 8.25*inch, width=8.5*inch, height=3*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

c.setFillColor(colors.white)
p1  =Paragraph('<para fontsize=20 color=white><b>EYELET BOLT</b></para>',stylesN)
p2  =Paragraph('<para fontsize=12 color=white>with Swaged Thimble</para>',stylesN)
d1 = [[p1,p2]]
dt1 = Table(d1,colWidths=[7.6*cm,7*cm])
dt1.setStyle(TableStyle([

                            ('LEFTPADDING',(1,0),(-1,-1),-60),
                            ('BOTTOMPADDING',(1,0),(-1,-1),-5)

                       ]))
dt1.wrapOn(c,width,height)
dt1.drawOn(c,30,8.6*inch)

p3 = Paragraph('<para><b>Product Data</b><br/></para>',stylesN)
p4 = Paragraph('<para><bullet>&bull;</bullet>eyelet bolt steel St 37,zinc-plated</para>',stylesN)
p7 = Paragraph('<para><b>Advantages</b><br/></para>',stylesN)
p5 = Paragraph('<para><bullet>&bull;</bullet>simple, fast and safe end terminations</para>',stylesN)
p51 = Paragraph('<para><bullet>&bull;</bullet>no special tools required</para>',stylesN)
p52 = Paragraph('<para><bullet>&bull;</bullet>simple securing against twisting</para>',stylesN)

d2 =[[p3],[p4],'',[p7],[p5],[p51],[p52]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,3.5*inch,6.25*inch)


c.drawImage(eye, 10, 0, width=2 * inch, height=7 * inch, mask='auto')



itemn = Paragraph(
    '<para align="center"   fontname = "Helvetica-Bold"fontsize =5  >item number</para>', stylesN)
rope = Paragraph(
    '<para  align="center" fontname = "Helvetica-Bold" fontsize =5>rope-@</para>', stylesN)

d1 = Paragraph(
    '<para align="center"    fontname = "Helvetica-Bold" fontsize =5>  d1</para>', stylesN)
d2 = Paragraph(
    '<para align="center"     fontname = "Helvetica-Bold" fontsize =5>  d2</para>', stylesN)
d3 = Paragraph(
    '<para  align="center"   fontname = "Helvetica-Bold" fontsize =5>  d3</para>', stylesN)
li1 = Paragraph(
    '<para  align="center" lindent=10 fontname = "Helvetica-Bold" fontsize =5>  L1</para>', stylesN)
li2 = Paragraph(
    '<para  align="center"  lindent=10 fontname = "Helvetica-Bold" fontsize =5>  L2</para>', stylesN)
load = Paragraph(
    '<para align="center" fontname = "Helvetica-Bold" fontsize =5>  breaking <br/>load</para>', stylesN)

li5 = Paragraph(
    '<para align="center" lindent=-20 fontname = "Helvetica" fontsize =5>dimensions in mm</para>', stylesN)
li6 = Paragraph('<para align = "center"fontname = "Helvetica" fontsize =5> mm</para>', stylesN)
li7 = Paragraph('<para align="center"fontname = "Helvetica" fontsize =5> kN</para>', stylesN)

itemn0 = Paragraph(
    '<para align="center"  fontname = "Helvetica"fontsize =5  >64250</para>', stylesN)
rope0 = Paragraph(
    '<para  align="center" fontname = "Helvetica" fontsize =5>6.0</para>', stylesN)

d10 = Paragraph(
    '<para   align="center"  fontname = "Helvetica" fontsize =5>  M 12</para>', stylesN)
d20 = Paragraph(
    '<para   align="center"   fontname = "Helvetica" fontsize =5>  26.0</para>', stylesN)
d30 = Paragraph(
    '<para align="center"    fontname = "Helvetica" fontsize =5>  50.0</para>', stylesN)
li10 = Paragraph(
    '<para  align="center" lindent=10 fontname = "Helvetica" fontsize =5> 260</para>', stylesN)
li20 = Paragraph(
    '<para align="center"  lindent=10 fontname = "Helvetica" fontsize =5>  60</para>', stylesN)
load0 = Paragraph(
    '<para  align="center"fontname = "Helvetica" fontsize =5>  33.7</para>', stylesN)


apag1 = [
        [itemn, rope, d1, d2, d3, li1, li2, load],
        ['', '', '', '', '', '', '', '', '', '', ''],
        ['', li6, '', '', li5, '', '', li7],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],
        [itemn0, rope0, d10, d20, d30, li10, li20, load0],



]

apagt = Table(apag1, colWidths=[1.25 * cm, 1.25 * cm, 1.25 * cm,
                                1.25 * cm, 1.25 * cm, 1.25 * cm, 1.5 * cm, 1.5 * cm], rowHeights=4 * mm)
apagt.setStyle(TableStyle([
    # ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
    # ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
    ('LINEBELOW', (0, 1), (-4, -1), 0.25, colors.black),
    ('BACKGROUND', (1, 0), (-10, -1), '#DCDCDC'),
    ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),

]))

apagt.wrapOn(c, 30, 300)
apagt.drawOn(c, 3.5 * inch, 0.5 * inch)




l1 = Paragraph('<para fontsize = 7>Other sizes avaliable upon request.</para>',stylesN)
lt1 = [[l1]]
ltt=Table(lt1)
ltt.wrapOn(c,width,height)
ltt.drawOn(c,3.5*inch,0.25*inch)
textobject1 = c.beginText()
textobject1.setTextOrigin(2.5*inch, 0.4*inch)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''
                     Other sizes avaliable upon request.


''')


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
c.drawString(580, 0.15*inch, "23")



c.showPage()

logo = "brugglifting.svg"
bg = "P24BannerImg.png"
bg1 = "P25BannerImg.png"
a = 'A.png'
am = 'AM.png'
d = "D.png"
fp = "FP.png"
fp2 = "FP2.png"
fp3 = "FP3.png"
a1="P24Strip.svg"
a2="P25Strip.svg"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)


p1  =Paragraph('<para fontsize=20 color=white><b>WEDGE SOCKET</b></para>',stylesN)
p2  =Paragraph('<para fontsize=12 color=white>Symmetrical [EN 13411-7] with Eyelet Bolt [DIN 444]</para>',stylesN)
d1 = [[p1,p2]]
dt1 = Table(d1,colWidths=[7.5*cm, 9*cm])
dt1.setStyle(TableStyle([


                            ('LEFTPADDING',(1,0),(-1,-1),-30),
                            ('BOTTOMPADDING',(1,0),(-1,-1),-5)

                       ]))
dt1.wrapOn(c,width,height)
dt1.drawOn(c,30,8.6*inch)



p3 = Paragraph('<para><b>Product Data</b><br/></para>',stylesN)
p4 = Paragraph('<para><bullet>&bull;</bullet>wedge socket welded, steel zinc-plated</para>',stylesN)
p7 = Paragraph('<para><bullet>&bull;</bullet>incl. wedge, bolt and safety pins pre-assembled</para>',stylesN)
p5 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>wedge socket transmits 80 % of minimal breaking load <br/>of traction rope or governor rope</para>',stylesN)
p51 = Paragraph('<para><bullet>&bull;</bullet>eyelet bolt welded, steel zinc-plated</para>',stylesN)
p52 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>in connection with the wedge socket the eyelet bolt transmits <br/>80 % of the minimal breaking load of the elevator rope</para>',stylesN)
p53 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>for mounting and operation the explanations in appendix B <br/> of the norm EN 13411-7 are valid</para>',stylesN)

d2 =[[p3],[p4],[p7],[p5],[p51],[p52],[p53]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,40,5.75*inch)


p51 = Paragraph('<para><b>Advantages</b></para>',stylesN)
p52 = Paragraph('<para><bullet>&bull;</bullet>can be assembled safely and simply on-site</para>',stylesN)
p53 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>springs, buffers and other accessories can <br/> be mounted individually</para>',stylesN)

d2 =[[p51],[p52],[p53]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,5.1*inch,7.1*inch)

# c.setFillColor(colors.white)
# c.setFont("Helvetica-Bold",20)
# c.drawString(20, 6.4*inch, "WEDGE SOCKET")
# c.setFont("Helvetica",10)
#
# c.drawString(190, 6.4*inch, "Symmetrical [EN 13411-7] with Eyelet Bolt [DIN 444]")
#
# black50transparent = Color(169,169,169, alpha=0.35)
# c.setFillColor(black50transparent)
# c.rect(585,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)



c.drawImage(a,2.5*inch,1.5*inch,width=1*inch,height=3.5*inch,preserveAspectRatio=True)
c.drawImage(am,4*inch,1.7*inch,width=1*inch,height=3.25*inch,preserveAspectRatio=True)
c.drawImage(d,5.5*inch,1.65*inch,width=1*inch,height=3.25*inch,preserveAspectRatio=True)
c.drawImage(fp,7*inch,1.45*inch,width=1*inch,height=3.5*inch,preserveAspectRatio=True)


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
c.drawString(20, 0.15*inch, "24")


c.showPage()


c.drawImage(bg1,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(a2)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

black50transparent = Color(0,0,0, alpha=0.5)


c.drawImage(fp2,1.25*inch,1.75*inch,width=1*inch,height=3.4*inch,preserveAspectRatio=True)
c.drawImage(fp3,2.75*inch,1.75*inch,width=1*inch,height=3.4*inch,preserveAspectRatio=True)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=15 fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)
di = Paragraph('<para fontname = "Helvetica-Bold" fontsize =6>d<br/></para>',stylesN)

di1= Paragraph('<para  fontname = "Helvetica-Bold" fontsize =6>d1</para>',stylesN)
l1 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =6>L1</para>',stylesN)
l2 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =6>L2</para>',stylesN)
l3 = Paragraph('<para fontname = "Helvetica-Bold" fontsize =6>L3</para>',stylesN)

p1 = Paragraph('<para align = "LEFT" leftindent=5 fontname = "Helvetica-Bold" fontsize =7>A</para>',stylesN)
p2 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =6>mm</para>',stylesN)
p3 = Paragraph('<para align = "LEFT" leftindent=3 fontname = "Helvetica-Bold" fontsize =6>AM</para>',stylesN)
p4 = Paragraph('<para align = "LEFT" leftindent=3 fontname = "Helvetica-Bold" fontsize =6>D</para>',stylesN)
p5 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =6>FP</para>',stylesN)
p6 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =6>FP2</para>',stylesN)
p7 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =6>FP3</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >64109</para>',stylesN)
rope1 = Paragraph('<para  fontname = "Helvetica" fontsize =6>5.0</para>',stylesN)
rope2 = Paragraph('<para  fontname = "Helvetica" fontsize =6>6.5</para>',stylesN)

dit = Paragraph('<para fontname = "Helvetica" fontsize =4>M10<br/></para>',stylesN)

di1t= Paragraph('<para  fontname = "Helvetica" fontsize =6></para>',stylesN)
l1t = Paragraph('<para  fontname = "Helvetica" fontsize =6>265</para>',stylesN)
l2t = Paragraph('<para  fontname = "Helvetica" fontsize =6>180</para>',stylesN)
l3t = Paragraph('<para fontname = "Helvetica" fontsize =6></para>',stylesN)
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

t1 = Table(d1,colWidths=[1.25*cm,2*cm,1*cm,1*cm,1*cm,1*cm,1*cm,1*cm],rowHeights=4.5*mm)
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
t1.drawOn(c,4.5*inch,1.35*inch)

textobject = c.beginText()
textobject.setTextOrigin(4.5*inch, 1.2*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 6)
textobject.textLines('''
                          Other sizes available upon request.
                           You will find the item numbers for all combination possibilities in the price list.
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
c.drawString(580, 0.15*inch, "25")



c.showPage()

logo = "brugglifting.svg"
bg = "P26BannerImg.png"
bg1 = "P27BannerImg.png"
a = 'A.png'
am = 'AM.png'
d = "D.png"
fp = "FP.png"
fp2 = "FP2.png"
fp3 = "FP3.png"
a1 = "P26Strip.svg"
a2 = "P27Strip.svg"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')


p1  =Paragraph('<para fontsize=20 color=white><b>WEDGE SOCKET</b></para>',stylesN)
p2  =Paragraph('<para fontsize=12 color=white>Asymmetrical [EN 13411-6] with Eyelet Bolt [DIN 444]</para>',stylesN)
d1 = [[p1,p2]]
dt1 = Table(d1,colWidths=[7.5*cm,10*cm])
dt1.setStyle(TableStyle([

                            ('LEFTPADDING',(1,0),(-1,-1),-30),
                            ('BOTTOMPADDING',(1,0),(-1,-1),-5)

                       ]))
dt1.wrapOn(c,width,height)
dt1.drawOn(c,30,8.6*inch)



p3 = Paragraph('<para><b>Product Data</b><br/></para>',stylesN)
p4 = Paragraph('<para><bullet>&bull;</bullet>wedge socket welded, steel zinc-plated</para>',stylesN)
p7 = Paragraph('<para><bullet>&bull;</bullet>incl. wedge, bolt and safety pins pre-assembled</para>',stylesN)

p51 = Paragraph('<para><bullet>&bull;</bullet>eyelet bolt welded, steel zinc-plated</para>',stylesN)
p52 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>in connection with the wedge socket the eyelet bolt<br/> transmits 80 % of the minimal breaking load of the traction <br/> - or governor rope</para>',stylesN)


d2 =[[p3],[p4],[p7],[p51],[p52]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,40,6.5*inch)


p51 = Paragraph('<para><b>Advantages</b></para>',stylesN)
p52 = Paragraph('<para><bullet>&bull;</bullet>can be assembled safely and simply on-site</para>',stylesN)
p53 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>springs, buffers and other accessories can <br/> be mounted individually</para>',stylesN)
p54 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>for mounting and operation the explanations<br/> in appendix B of the norm EN 13411-6 are valid</para>',stylesN)

d2 =[[p51],[p52],[p53],[p54]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,5.1*inch,6.75*inch)


c.drawImage(a,2.5*inch,1.5*inch,width=1*inch,height=3.5*inch,preserveAspectRatio=True)
c.drawImage(am,4*inch,1.7*inch,width=1*inch,height=3.25*inch,preserveAspectRatio=True)
c.drawImage(d,5.5*inch,1.65*inch,width=1*inch,height=3.25*inch,preserveAspectRatio=True)
c.drawImage(fp,7*inch,1.45*inch,width=1*inch,height=3.5*inch,preserveAspectRatio=True)


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
c.drawString(20, 0.15*inch, "26")



c.showPage()


c.drawImage(bg1,0*inch,8.25*inch,width=8.5*inch,height=3*inch)


black50transparent = Color(0,0,0, alpha=0.5)



c.drawImage(fp2,1.25*inch,1.75*inch,width=1*inch,height=3.4*inch,preserveAspectRatio=True)
c.drawImage(fp3,2.75*inch,1.75*inch,width=1*inch,height=3.4*inch,preserveAspectRatio=True)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')


drawing = svg2rlg(a2)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=15 fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)
di = Paragraph('<para fontname = "Helvetica-Bold" fontsize =6>d<br/></para>',stylesN)

di1= Paragraph('<para  fontname = "Helvetica-Bold" fontsize =6>d1</para>',stylesN)
l1 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =6>L1</para>',stylesN)
l2 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =6>L2</para>',stylesN)
l3 = Paragraph('<para fontname = "Helvetica-Bold" fontsize =6>L3</para>',stylesN)

p1 = Paragraph('<para align = "LEFT" leftindent=5 fontname = "Helvetica-Bold" fontsize =7>A</para>',stylesN)
p2 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =6>mm</para>',stylesN)
p3 = Paragraph('<para align = "LEFT" leftindent=3 fontname = "Helvetica-Bold" fontsize =6>AM</para>',stylesN)
p4 = Paragraph('<para align = "LEFT" leftindent=3 fontname = "Helvetica-Bold" fontsize =6>D</para>',stylesN)
p5 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =6>FP</para>',stylesN)
p6 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =6>FP2</para>',stylesN)
p7 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =6>FP3</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >64109</para>',stylesN)
rope1 = Paragraph('<para  fontname = "Helvetica" fontsize =6>5.0</para>',stylesN)
rope2 = Paragraph('<para  fontname = "Helvetica" fontsize =6>6.5</para>',stylesN)

dit = Paragraph('<para fontname = "Helvetica" fontsize =4>M10<br/></para>',stylesN)

di1t= Paragraph('<para  fontname = "Helvetica" fontsize =6></para>',stylesN)
l1t = Paragraph('<para  fontname = "Helvetica" fontsize =6>265</para>',stylesN)
l2t = Paragraph('<para  fontname = "Helvetica" fontsize =6>180</para>',stylesN)
l3t = Paragraph('<para fontname = "Helvetica" fontsize =6></para>',stylesN)
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

t1 = Table(d1,colWidths=[1.25*cm,2*cm,1*cm,1*cm,1*cm,1*cm,1*cm,1*cm],rowHeights=4.5*mm)
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
t1.drawOn(c,4.5*inch,1.2*inch)


tb1  = Paragraph('<para fontsize=6> *The head of the screw is not according to DIN 444. Other sizes avaliable upon request.<br/>You will find the item numbers for all comination possibilities in the price list.</para>',stylesN)
t11  = [[tb1]]
tt1 = Table(t11)
tt1.wrapOn(c,width,height)
tt1.drawOn(c,4.5*inch,0.5*inch)


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
c.drawString(580, 0.15*inch, "27")




c.showPage()

logo = "brugglifting.svg"
bg = "P28BannerImg.png"
spring = "es.png"
a1 = "P28Strip.svg"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 10.2*inch)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)


c.setFillColor('#3C434B')
c.rect(-20,8.33*inch, 12*inch, 0.6*inch,stroke=0,fill=1)
p1  =Paragraph('<para fontsize=20 color=white><b>ELASTOMER BUFFERS</b></para>',stylesN)
p2  =Paragraph('<para fontsize=12 color=white>for Rope Attachment</para>',stylesN)
d1 = [[p1,p2]]
dt1 = Table(d1,colWidths=[13*cm,9*cm])
dt1.setStyle(TableStyle([


                            ('LEFTPADDING',(1,0),(-1,-1),-120),
                            ('BOTTOMPADDING',(1,0),(-1,-1),-5)

                       ]))
dt1.wrapOn(c,width,height)
dt1.drawOn(c,30,8.6*inch)


p3 = Paragraph('<para><b>Product Data</b><br/></para>',stylesN)
p4 = Paragraph('<para><bullet>&bull;</bullet>polyurethane elastomer with cells</para>',stylesN)
p7 = Paragraph('<para><bullet>&bull;</bullet>Suitable for APAG, eyelet boly,wedge socket symmetrical and asymmetrical</para>',stylesN)



d2 =[[p3],[p4],[p7],'']
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,3.5*inch,7.1*inch)


p51 = Paragraph('<para><b>Advantages</b></para>',stylesN)
p52 = Paragraph('<para><bullet>&bull;</bullet>excellent buffering properties at minimum overall height </para>',stylesN)
p53 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>transverse elongation</para>',stylesN)
p54 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>also applicable on the counterweight side as rope length compensation</para>',stylesN)
p55 = Paragraph('<para align="justify" lindent=10><bullet>&bull;</bullet>grese- and resistant</para>',stylesN)

d2 =[[p51],[p52],[p53],[p54],[p55]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,3.5*inch,6*inch)


c.setFillColor(colors.white)

c.drawImage(spring,20,3.5*inch,width=3*inch,height=4*inch,preserveAspectRatio=True)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
tread = Paragraph('<para align="center"  fontname = "Helvetica-Bold" fontsize =6>for <br/>tread</para>',stylesN)

di1= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =6>  d1</para>',stylesN)
di2 = Paragraph('<para lindent=-45 fontname = "Helvetica-Bold" fontsize =6>  d2<br/></para>',stylesN)
di3 = Paragraph('<para lindent=-65 fontname = "Helvetica-Bold" fontsize =6>  d3<br/></para>',stylesN)
li1 = Paragraph('<para lindent=-70 fontname = "Helvetica-Bold" fontsize =6>  L1</para>',stylesN)
li2 = Paragraph('<para lindent=-70 fontname = "Helvetica-Bold" fontsize =6>  L2</para>',stylesN)
sprate = Paragraph('<para lindent=-70 fontname = "Helvetica-Bold" fontsize =6>max. <br/>stat.<br/>weight</para>',stylesN)
spf = Paragraph('<para   lindent=-70  fontname = "Helvetica-Bold" fontsize =6>  max.<br/>pressure<br/>force</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  ></para>',stylesN)
tread1 = Paragraph('<para align="center" fontname = "Helvetica" fontsize =6>mm</para>',stylesN)
di11= Paragraph('<para  fontname = "Helvetica" fontsize =6></para>',stylesN)
di21 = Paragraph('<para   lindent=-48 fontname = "Helvetica" fontsize =6>dimensions in mm<br/></para>',stylesN)
di31 = Paragraph('<para fontname = "Helvetica" fontsize =6><br/></para>',stylesN)
li11 = Paragraph('<para  fontname = "Helvetica" fontsize =6></para>',stylesN)
li21 = Paragraph('<para  fontname = "Helvetica" fontsize =6></para>',stylesN)
sprate1 = Paragraph('<para  lindent=-70 fontname = "Helvetica" fontsize =6>kg</para>',stylesN)
spf1 = Paragraph('<para lindent=-70 fontname = "Helvetica" fontsize =6>kN</para>',stylesN)

itemn12 = Paragraph('<para  fontname = "Helvetica"fontsize =6 >77658 </para>',stylesN)
tread12 = Paragraph('<para align="center"  fontname = "Helvetica" fontsize =6>M12</para>',stylesN)
di112= Paragraph('<para   fontname = "Helvetica" fontsize =6>50</para>',stylesN)
di212 = Paragraph('<para  lindent=-45 fontname = "Helvetica" fontsize =6>13<br/></para>',stylesN)
di312 = Paragraph('<para   lindent=-65 fontname = "Helvetica" fontsize =6>22<br/></para>',stylesN)
li112 = Paragraph('<para   lindent=-70 fontname = "Helvetica" fontsize =6>28</para>',stylesN)
li122 = Paragraph('<para   lindent=-70 fontname = "Helvetica" fontsize =6>28</para>',stylesN)
sprate12 = Paragraph('<para  lindent=-70 fontname = "Helvetica" fontsize =6>170</para>',stylesN)
spf12 = Paragraph('<para lindent=-70 fontname = "Helvetica" fontsize =6>6.867</para>',stylesN)


spring1 = [[itemn,tread,di1,di2,di3,li1,li2,sprate,spf],
        ['','','','','','','','',],
        ['','','','','','','','',],
        [itemn1,tread1,di11,di21,di31,li11,li21,sprate1,spf1],
        [itemn12,tread12,di112,di212,di312,li112,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,li112,sprate12,spf12],

        [itemn12,tread12,di112,di212,di312,li112,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,li112,sprate12,spf12],
]
springt =Table(spring1,colWidths=[1.4*cm,1*cm,2.65*cm,1.9*cm,1*cm,1*cm,1*cm,1*cm,1.5*cm],rowHeights=4.25*mm)
springt.setStyle(TableStyle([
                            ('LINEBELOW',(0,2),(-3,-1),0.25,colors.black),
                            # ('BACKGROUND',(1,0),(-7,-4),'#DCDCDC'),
                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                             ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('BACKGROUND',(1,0),(-8,-1),'#DCDCDC'),
                       ]))
springt.wrapOn(c,width,height)
springt.drawOn(c,3.5*inch, 2.5*inch)


t5 = Paragraph('<para fontsize=6 align="justify">* with collar. If not expressly desired differently. we supply rope   attachments with a buffer always with a <br/> collar. in case of  several buffers always the top one with collar.</para>',stylesN)
t15  = [[t5]]
tt  = Table(t15)
tt.wrapOn(c,width,height)
tt.drawOn(c,3.5*inch,2*inch)
# textobject = c.beginText()
# textobject.setTextOrigin(3.5*inch, 2.3*inch)
# c.setFillColor('#3C434B')
# textobject.setFont("Helvetica", 7)
# textobject.textLines('''
#                         * with collar. If not expressly desired differently. we supply rope   attachments with a buffer always with a
#                           collar. in case of  several buffers always the top one with collar''')
# c.drawText(textobject)

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
c.drawString(20, 0.15*inch, "28")





c.showPage()

logo = "brugglifting.svg"
bg = "P29BannerImg.png"

spring = "spring.png"
a1 = "P29steip.svg"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')


# For HRS

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

# black50transparent = Color(0,0,0, alpha=0.8)
c.setFillColor('#3C434B')
c.rect(-20,8.33*inch, 4*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(35, 8.6*inch, "SPRING ")
c.drawImage(spring,20,3.5*inch,width=3.2*inch,height=4*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 7.9*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 8)
textobject.textLines('''
                          Product Data
                          ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3.6*inch, 7.75*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                        steel spring, bright
                        cylindical type
                        suitable for APAG, eyelet bolt, wedge socket
                        symmetrical and asymmetrical
                          ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 7*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 8)
textobject.textLines('''
                         Advantages
                         ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(3.6*inch, 6.85*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                        improved riding comfort
                        ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
tread = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =6>for <br/>tread</para>',stylesN)

di1= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =6>  d1</para>',stylesN)
di2 = Paragraph('<para lindent=-45 fontname = "Helvetica-Bold" fontsize =6>  d2<br/></para>',stylesN)
di3 = Paragraph('<para lindent=-65 fontname = "Helvetica-Bold" fontsize =6>  d3<br/></para>',stylesN)
li1 = Paragraph('<para lindent=-70 fontname = "Helvetica-Bold" fontsize =6>  L1</para>',stylesN)
sprate = Paragraph('<para lindent=-70 fontname = "Helvetica-Bold" fontsize =6>spring <br/>rate</para>',stylesN)
spf = Paragraph('<para   lindent=-70  fontname = "Helvetica-Bold" fontsize =6>  spring<br/>force</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  ></para>',stylesN)
tread1 = Paragraph('<para  fontname = "Helvetica" fontsize =6>mm</para>',stylesN)
di11= Paragraph('<para  fontname = "Helvetica" fontsize =6></para>',stylesN)
di21 = Paragraph('<para   lindent=-48 fontname = "Helvetica" fontsize =6>dimensions in mm<br/></para>',stylesN)
di31 = Paragraph('<para fontname = "Helvetica" fontsize =6><br/></para>',stylesN)
li11 = Paragraph('<para  fontname = "Helvetica" fontsize =6></para>',stylesN)
sprate1 = Paragraph('<para  lindent=-70 fontname = "Helvetica" fontsize =6>N/mm2</para>',stylesN)
spf1 = Paragraph('<para lindent=-70 fontname = "Helvetica" fontsize =6>kN</para>',stylesN)

itemn12 = Paragraph('<para  fontname = "Helvetica"fontsize =6 >77658 </para>',stylesN)
tread12 = Paragraph('<para   fontname = "Helvetica" fontsize =6>M12</para>',stylesN)
di112= Paragraph('<para   fontname = "Helvetica" fontsize =6>50</para>',stylesN)
di212 = Paragraph('<para  lindent=-45 fontname = "Helvetica" fontsize =6>13<br/></para>',stylesN)
di312 = Paragraph('<para   lindent=-65 fontname = "Helvetica" fontsize =6>22<br/></para>',stylesN)
li112 = Paragraph('<para   lindent=-70 fontname = "Helvetica" fontsize =6>28</para>',stylesN)
sprate12 = Paragraph('<para  lindent=-70 fontname = "Helvetica" fontsize =6>33</para>',stylesN)
spf12 = Paragraph('<para lindent=-70 fontname = "Helvetica" fontsize =6>170</para>',stylesN)
req = Paragraph('<para  lindent=-5 fontname = "Helvetica" fontsize =6>on request</para>',stylesN)
sub = Paragraph('<para   fontname = "Helvetica" fontsize =6>substitute for 64469 of 64470</para>',stylesN)

spring1 = [[itemn,tread,di1,di2,di3,li1,sprate,spf],
        ['','','','','','','','',],
        ['','','','','','','','',],
        [itemn1,tread1,di11,di21,di31,li11,sprate1,spf1],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [req,tread12,di112,di212,di312,li112,sprate12,spf12],
        ['','',sub,'','','','',''],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
]
springt =Table(spring1,colWidths=[1.4*cm,1.4*cm,2.65*cm,1.9*cm,1.4*cm,1.4*cm,1.4*cm,1.4*cm,1.5*cm],rowHeights=4.25*mm)
springt.setStyle(TableStyle([
                            ('LINEBELOW',(0,2),(-3,-1),0.25,colors.black),
                            ('BACKGROUND',(1,0),(-7,-4),'#DCDCDC'),
                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                             ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('BACKGROUND',(1,11),(-7,-1),'#DCDCDC'),
                       ]))
springt.wrapOn(c,width,height)
springt.drawOn(c,3.5*inch, 2.5*inch)

# textobject = c.beginText()
# textobject.setTextOrigin(3.5*inch, 2.3*inch)
# c.setFillColor('#3C434B')
# textobject.setFont("Helvetica", 7)
# textobject.textLines('''
#                         * with collar. If not expressly desired differently. we supply rope   attachments with a buffer always with a
#                           collar. in case of  several buffers always the top one with collar''')
# c.drawText(textobject)

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
c.drawString(580, 0.15*inch, "29")


c.showPage()

logo = "brugglifting.svg"
bg = "P30BannerImg.png"
tss = "tss.png"
ssz = "smz.png"
dcrs1 = "dcr1.png"
dcrs2 = "dcrs2.png"
dcrs3 = "dcrs3.png"
a1 = "P30Strip.svg"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.4
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 10.25*inch)
# black50transparent = Color(0,0,0, alpha=0.8)

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)


c.setFillColor('#3C434B')
c.rect(-20,8.33*inch, 9*inch, 0.6*inch,stroke=0,fill=1)

p1  =Paragraph('<para fontsize=20 color=white><b>DOOR CLOSING ROPE SETS</b></para>',stylesN)

d1 = [[p1]]
dt1 = Table(d1,colWidths=[12*cm,9*cm])
dt1.setStyle(TableStyle([


                            ('LEFTPADDING',(1,0),(-1,-1),-120),
                            ('BOTTOMPADDING',(1,0),(-1,-1),-5)

                       ]))
dt1.wrapOn(c,width,height)
dt1.drawOn(c,30,8.6*inch)

c.drawImage(tss,-20,5*inch,width=2*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(ssz,1*inch,4.5*inch,width=1.75*inch,height=3*inch,preserveAspectRatio=True)

c.drawImage(dcrs1,0.75*inch,3*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
c.drawImage(dcrs2,0.1*inch,2*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
c.drawImage(dcrs3,1.5*inch,2*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)

p3 = Paragraph('<para fontsize=7><b>TSS-Rope Set</b><br/></para>',stylesN)
p4 = Paragraph('<para align="justify" fontsize=7 lindent=10><bullet>&bull;</bullet>1 FLEX door closing rope, 3500 mm length, with one-sided pressed <br/>APAG - external thread to adjust the correct rope tension</para>',stylesN)
p7 = Paragraph('<para fontsize=7><bullet>&bull;</bullet>1 clamping ring to fasten a rope end at a fixed point</para>',stylesN)
p8 = Paragraph('<para fontsize=7><bullet>&bull;</bullet>1 rope clamp and 1 thimble to mount the loose rope end</para>',stylesN)
p9 = Paragraph('<para fontsize=7> One packaging unit contains 5 rope sets each.</para>',stylesN)



d2 =[[p3],[p4],[p7],[p8],'',[p9]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,3.5*inch,6.5*inch)




itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=5  fontname = "Helvetica" fontsize =6>rope-@</para>',stylesN)

rope0 = Paragraph('<para lindent=5  fontname = "Helvetica"fontsize =6  >mm</para>',stylesN)


itemn2 = Paragraph('<para  fontname = "Helvetica"fontsize =6>77720</para>',stylesN)
rope2 = Paragraph('<para lindent=5   fontname = "Helvetica" fontsize =6>3.0</para>',stylesN)

item3 = Paragraph('<para  fontname = "Helvetica"fontsize =6>77721</para>',stylesN)
rope3 = Paragraph('<para lindent=5   fontname = "Helvetica" fontsize =6>4.0</para>',stylesN)

tss1 =[[itemn,rope],
         ['',''],
         ['',''],
        ['',rope0],
        [itemn2,rope2],
        [item3,rope3]

]
tsst = Table(tss1,colWidths=[1.45*cm,1.55*cm],rowHeights=4*mm)
tsst.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
tsst.wrapOn(c,width,height)
tsst.drawOn(c,3.6*inch,5.2*inch)

p13 = Paragraph('<para fontsize=7><b>SMZ-Rope Set</b><br/></para>',stylesN)
p14 = Paragraph('<para align="justify" fontsize=7 lindent=10><bullet>&bull;</bullet>1 thread for easy installation DO-IT-LINE to adjust the correct rope tension</para>',stylesN)
p17 = Paragraph('<para fontsize=7><bullet>&bull;</bullet>1 clamping ring to fasten a rope end at a fixed point</para>',stylesN)
p18 = Paragraph('<para fontsize=7><bullet>&bull;</bullet>1 rope clamp and 1 thimble to mount the loose rope end</para>',stylesN)
p19 = Paragraph('<para fontsize=7> One packaging unit contains 5 rope sets each.</para>',stylesN)
p20 = Paragraph('<para fontsize=7> The SMZ-rope set does not contain a door closing rope.<br/>This can be ordered seperately.</para>',stylesN)


p21 = Paragraph('<para fontsize=7><b>Advantages</b><br/></para>',stylesN)
p22 = Paragraph('<para align="justify" fontsize=7 lindent=10><bullet>&bull;</bullet>fast and simple installation</para>',stylesN)
p23 = Paragraph('<para fontsize=7><bullet>&bull;</bullet>suitable for most elevator door-closing sysytems</para>',stylesN)
p24 = Paragraph('<para fontsize=7><bullet>&bull;</bullet>reduces downimes</para>',stylesN)
p25 = Paragraph('<para fontsize=7><bullet>&bull;</bullet> Complete set - all parts are included</para>',stylesN)
p26 = Paragraph('<para fontsize=7> <bullet>&bull;</bullet>not much warehousing required</para>',stylesN)

d2 =[[p13],[p14],[p17],[p18],'',[p19],[p20],[p21],[p22],[p23],[p24],[p25],[p26]]
dt2 =Table(d2)
dt2.wrapOn(c,width,height)
dt2.drawOn(c,3.5*inch,1.5*inch)


# textobject = c.beginText()
# textobject.setTextOrigin(3.5*inch, 3.5*inch)
# c.setFillColor('#3C434B')
# textobject.setFont("Helvetica-Bold", 7)
# textobject.textLines('''
#                          Advantages
#                           ''')
# c.drawText(textobject)
#
# textobject = c.beginText()
# textobject.setTextOrigin(3.6*inch, 3.35*inch)
# c.setFillColor('#3C434B')
# textobject.setFont("Helvetica", 7)
# textobject.textLines('''
#                          fast and simple installation
#                          suitable for most elevator door-closing systems
#                          reduces downtimes
#                          complete set  all parts are included
#                          not much warehousing required
#
#
#                          ''')
# c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=5  fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)

rope0 = Paragraph('<para lindent=5  fontname = "Helvetica-Bold"fontsize =5  >mm</para>',stylesN)


itemn2 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5>77744</para>',stylesN)
rope2 = Paragraph('<para lindent=5   fontname = "Helvetica-Bold" fontsize =5>3.0</para>',stylesN)

itemn3 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5>77745</para>',stylesN)
rope3 = Paragraph('<para lindent=5   fontname = "Helvetica-Bold" fontsize =5>4.0</para>',stylesN)

smz1 =[[itemn,rope],
         ['',''],
         ['',''],
        ['',rope0],
        [itemn2,rope2],
        [itemn3,rope3]
]
smzt = Table(smz1,colWidths=[1.45*cm,1.55*cm],rowHeights=4*mm)
smzt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
smzt.wrapOn(c,width,height)
smzt.drawOn(c,3.6*inch,0.25*inch)
#

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
c.drawString(20, 0.15*inch, "30")



c.showPage()

logo = "brugglifting.svg"
bg = "P31BannerImg.png"

hrs = 'hrs.jpg'
clamp = "rclamp.png"
a1 = "P31Strip.svg"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)


c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(20, 8.6*inch, "DOOR CLOSING ROPE FLEX. ROPE CLAMP")

e1 = Paragraph('<para fontsize=7><b>Steel Core Rope,6 Strands, Seperate Lay</b><br/> Special design for door drives. Due to very fine strands especially suitable for deflec<br/>tor sheaves. Excellent service life with regard to high bending load.</para>',stylesN)
e11 = [[e1]]
et1 = Table(e11)
et1.wrapOn(c,width,height)
et1.drawOn(c,2.6*inch,7.5*inch)

c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

c.setFillColor('#D8D8D8')
c.rect(190,6.9*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
e2 = Paragraph('<para fontsize=7><b>110.000</b><br/>N/mm2</para>',stylesN)
e12 = [[e2]]
et2 = Table(e12)
et2.wrapOn(c,width,height)
et2.drawOn(c,2.65*inch,6.9*inch)
e3 = Paragraph('<para fontsize=6>E-Module**</para>',stylesN)
e13 = [[e3]]
et3 = Table(e13)
et3.wrapOn(c,width,height)
et3.drawOn(c,2.6*inch,6.6*inch)

c.setFillColor('#DCDCDC')
c.rect(240,6.9*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
e4 = Paragraph('<para align="justify" fontsize=7><b>0.138</b><br/>%</para>',stylesN)
e14 = [[e4]]
et4 = Table(e14)
et4.wrapOn(c,width,height)
et4.drawOn(c,3.35*inch,6.9*inch)
e5 = Paragraph('<para fontsize=6>Elastic <br/> elongation</para>',stylesN)
e15 = [[e5]]
et5 = Table(e15)
et5.wrapOn(c,width,height)
et5.drawOn(c,3.3*inch,6.45*inch)

c.setFillColor('#E0E0E0')
c.rect(290,6.9*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
e6 = Paragraph('<para align="justify" fontsize=7><b>0.25</b><br/>%</para>',stylesN)
e16 = [[e6]]
et6 = Table(e16)
et6.wrapOn(c,width,height)
et6.drawOn(c,4.1*inch,6.9*inch)
e7 = Paragraph('<para fontsize=6>Permenant <br/> elongation</para>',stylesN)
e17 = [[e7]]
et7 = Table(e17)
et7.wrapOn(c,width,height)
et7.drawOn(c,4*inch,6.45*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >item number</para>',stylesN)
rope = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =5>rope-@</para>',stylesN)
brk = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =5>breaking load<br/></para>',stylesN)

weight= Paragraph('<para lindent = -15 fontname = "Helvetica-Bold" fontsize =5>weight</para>',stylesN)
con = Paragraph('<para lindent = -25 fontname = "Helvetica-Bold" fontsize =5>construction</para>',stylesN)
min = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =5>min.</para>',stylesN)

mm0 = Paragraph('<para  fontname = "Helvetica" fontsize =5 underlineGap = 1>mm</para>',stylesN)

kN= Paragraph('<para fontname = "Helvetica" fontsize =5>kN</para>',stylesN)

kg = Paragraph('<para lindent =-15 fontname = "Helvetica" fontsize =5>kg/100m</para>',stylesN)

# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =5>10699 </para>',stylesN)
mm1 = Paragraph('<para  fontname = "Helvetica" fontsize =5>6.0</para>',stylesN)

kN1= Paragraph('<para  fontname = "Helvetica" fontsize =5>42.7</para>',stylesN)
kg1 = Paragraph('<para lindent = -15 fontname = "Helvetica" fontsize =5>26.9</para>',stylesN)

con1 = Paragraph('<para lindent = -30 fontname = "Helvetica" fontsize =5>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




dcrsf1 = [[itemn,rope,brk,weight,con],
        ['','',min,'',''],
            ['',mm0,kN,kg,''],
             [i,mm1,kN1,kg1,con1],
             [i,mm1,kN1,kg1,con1],
             [i,mm1,kN1,kg1,con1],




            ]


dcrsft = Table(dcrsf1,colWidths=[1.45*cm,1.45*cm,2.2*cm,2.2*cm,2.2*cm],rowHeights=5*mm)
dcrsft.setStyle(TableStyle([




                            ('BACKGROUND',(1,0),(-4,-1),'#DCDCDC'),



                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),

                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

dcrsft.wrapOn(c, width,height)
dcrsft.drawOn(c, 190,5.1*inch)

e7 = Paragraph('<para fontsize=7><bullet>&bull;</bullet> zinc coated</para>',stylesN)
e8 = Paragraph('<para fontsize=7><bullet>&bull;</bullet>for mounting and operation the explanations of the norm EN 13411-5 are valid</para>',stylesN)
e9 = Paragraph('<para fontsize=7><b>Rope Clamp</b></para>',stylesN)

e11 = Paragraph('<para fontsize=7><b>Advantages</b></para>',stylesN)
e10 = Paragraph('<para fontsize=7><bullet>&bull;</bullet> can be assembled safely and simply on-site</para>',stylesN)
e = [[e9],[e7],[e8],[e11],[e10]]
de = Table(e)
de.wrapOn(c,width,height)
de.drawOn(c,2.6*inch,3.75*inch)



c.drawImage(clamp,30,2*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)
itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >item number</para>',stylesN)
rope = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>rope-@*</para>',stylesN)

di= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d</para>',stylesN)
li1 = Paragraph('<para lindent=-20 fontname = "Helvetica-Bold" fontsize =5>  L1</para>',stylesN)
li2 = Paragraph('<para lindent=-20 fontname = "Helvetica-Bold" fontsize =5>  L2</para>',stylesN)
rq = Paragraph('<para   lindent=-20  fontname = "Helvetica-Bold" fontsize =5>  max.<br/>required torque</para>',stylesN)
loop = Paragraph('<para fontname = "Helvetica-Bold" fontsize =5>rode clamp/<br/>loop</para>',stylesN)


itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =5  ></para>',stylesN)
rope1 = Paragraph('<para  fontname = "Helvetica" fontsize =5>mm</para>',stylesN)

di1= Paragraph('<para  fontname = "Helvetica" fontsize =5></para>',stylesN)

li11 = Paragraph('<para lindent=-10 fontname = "Helvetica" fontsize =5>dimensions in mm</para>',stylesN)
li21 = Paragraph('<para  fontname = "Helvetica" fontsize =5></para>',stylesN)
rq1 = Paragraph('<para  lindent=-20 fontname = "Helvetica" fontsize =5>Nm</para>',stylesN)
loop1 = Paragraph('<para  fontname = "Helvetica" fontsize =5>pcs</para>',stylesN)



itemn11 = Paragraph('<para  fontname = "Helvetica"fontsize =5  >49459</para>',stylesN)
rope11 = Paragraph('<para  fontname = "Helvetica" fontsize =5>5.0</para>',stylesN)

di11= Paragraph('<para  fontname = "Helvetica" fontsize =5>M5</para>',stylesN)

li111 = Paragraph('<para lindent=-20 fontname = "Helvetica" fontsize =5>25</para>',stylesN)
li211 = Paragraph('<para lindent=-20 fontname = "Helvetica" fontsize =5>12</para>',stylesN)
rq11 = Paragraph('<para  lindent=-20 fontname = "Helvetica" fontsize =5>2.0</para>',stylesN)
loop11 = Paragraph('<para  fontname = "Helvetica" fontsize =5>3</para>',stylesN)
dcrsf2 =[[itemn,rope,di,li1,li2,rq,loop],
         ["",'','','','','',''],
         ["",'','','','','',''],

         [itemn1,rope1,di1,li11,li21,rq1,loop1],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11]]
dcrsft = Table(dcrsf2,colWidths=[1.25*cm,1.25*cm,1.75*cm,1.75*cm,1.25*cm,0.75*cm,1.25*cm],rowHeights=4*mm)

dcrsft.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

dcrsft.wrapOn(c,width,height)
dcrsft.drawOn(c,190,1*inch)

textobject = c.beginText()
textobject.setTextOrigin(190,0.85*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                         * Corresponds to the maximum rope diameter.
                           For interim sizes of the rope diameter the next-largest clamp size is to be used



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
c.drawString(580, 0.15*inch, "31")



c.showPage()

logo = "brugglifting.svg"
bg = "P32BAnner.png"

rpm1 = "rpm1.png"
rpm2 = "rpm2.png"
a1="P32Strip.png"

width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(a1,0*inch,8.25*inch,width=8.5*inch,height=0.9*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(logo)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 10.25*inch)
# black50transparent = Color(0,0,0, alpha=0.8)
c.setFillColor('#3C434B')
c.rect(-20,8.33*inch, 9*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(35, 8.6*inch, "RPM ")
c.setFont("Helvetica",12)
c.drawString(90, 8.6*inch, "Rope Performance Measurement Device")

c.drawImage(rpm1,30,0*inch,width=3*inch,height=8.2*inch)


textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 7.8*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 9)
textobject.textLines('''
                         The RPM Rope performance measurement device makes it easier for
                         you to check the rope tension during the installation, the inspection
                         and the maintenance of elevators.
 ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 7*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 9)
textobject.textLines('''
                        Advantages
                        ''')
c.drawText(textobject)

c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(3.6*inch, 6.8*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 9)
textobject.textLines('''
                        quick, easy and precise determination of rope diameter and tension
                        comparison and measurement of the rope tensions e.g. within a rope set
                        determination of the weight of cabin, counterweights etc.
                        easy documentation, query and comparison of the last 94 measuring
                        results through storage in the device
                        high precision of rope tension measurement of + / - 5%
                        and diameter measurement of + /- 1%
                        versatile through battery-supplied operation (1 x 9 V battery)
                        handy device: just 330 x 230 x 50 mm (12.9 x 9.1 x 2.0 in),
                        weight only 2.6 kg (5,73 lb)
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 4.5*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 9)
textobject.textLines('''
                         keep the tension under control
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 4.35*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 9)
textobject.textLines('''
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant
                         ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)

rope0 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >mm</para>',stylesN)
rope1 = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>in</para>',stylesN)

itemn2 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5>70020</para>',stylesN)
rope2 = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>8-22</para>',stylesN)
rope3 = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>5/16-7/18</para>',stylesN)


rpm =[[itemn,rope],
         ['',''],
         ['',''],
        ['',rope0,rope1],
        [itemn2,rope2,rope3],

]
rpmt = Table(rpm,colWidths=[1.25*cm,1.25*cm],rowHeights=4*mm)
rpmt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
rpmt.wrapOn(c,width,height)
rpmt.drawOn(c,3.5*inch,2.5*inch)
c.drawImage(rpm2,5.25*inch,0.75*inch,width=2.75*inch,height=2.75*inch,preserveAspectRatio=True)

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
c.drawString(20, 0.15*inch, "32")




c.showPage()

logo = "brugglifting.svg"
bg = "P33Banner.png"
bg1 = "P34Banner.png"
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
a1 = "P33Strip.svg"
a2 = "P34Strip.svg"



width, height = A4
c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
# For HRS

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(60, 8.55*inch, "GDC")

c.setFillColor(colors.white)
c.setFont("Helvetica",12)
c.drawCentredString(160,8.55*inch, "Grove Depth Comparator")

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(270, 8.55*inch, ". RWG")

c.setFillColor(colors.white)
c.setFont("Helvetica",12)
c.drawCentredString(365, 8.55*inch, "Rope Wear Gauge")


textobject = c.beginText()
textobject.setTextOrigin(315, 7.7*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        GDC Groove Depth Comparator
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 7.5*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        The GDC enables you to precisely measure and compare sheave groove
                        variations.  It  serves  to  early  detect  worn-out  drive  sheaves  and  may
                        thus help to increase the service life of ropes.
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 6.8*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 6.6*inch)
c.setFillColor('#3C434B')
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


c.drawImage(i24,60,3.6*inch,width=2.25*inch,height=4.25*inch)

c.drawImage(i25,50,0.6*inch,width=3.4*inch,height=2.55*inch)


textobject = c.beginText()
textobject.setTextOrigin(315, 3.35*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        RWG Rope Wear Gauge
                           ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 3.15*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        Within seconds, the precision gauge enables you to check, whether
                        the minimum nominal diameter of the rope is below the target.
                        If below limit, the rope must be replaced
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 2.55*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                           ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 2.35*inch)
c.setFillColor('#3C434B')
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
c.drawString(580, 0.15*inch, "33")





c.showPage()

c.drawImage(bg1,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./1.8
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)

drawing = svg2rlg(a2)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')


c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(90, 8.55*inch, "VT-LUBE")
c.drawImage(i26,60, 5.4*inch,width=1.75*inch,height=2*inch)

c.setFillColor(colors.white)
c.setFont("Helvetica",12)
c.drawCentredString(200, 8.55*inch, "Rope Care Lubricant")

textobject = c.beginText()
textobject.setTextOrigin(308, 7.7*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        VT-Lube
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 7.5*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        This rope care lubricant was especially developed for the
                        relubrication of elevator ropes
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 6.9*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 6.7*inch)
c.setFillColor('#3C434B')
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




c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(5*inch, 8.55*inch, ". ROPE CUTTERS")

textobject = c.beginText()
textobject.setTextOrigin(4.4*inch, 3.9*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 10)
textobject.textLines('''
                        Rope Cutters
                         ''')
c.drawText(textobject)

c.drawImage(i16,50,3.4*inch,width=2.75*inch,height=1.25*inch)

c.drawImage(i17,50,1.7*inch,width=2.75*inch,height=1.25*inch)

textobject = c.beginText()
textobject.setTextOrigin(4.4*inch, 2.25*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 10)
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

itemn2 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >07535</para>',stylesN)
ropemm2 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>upto 12 </para>',stylesN)
weightkg2 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> 2.3</para>',stylesN)
lengthmm2 =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>600</para>',stylesN)


rc =[[itemn,rope,weight,length],
         ['','',''],
         ['','',''],
        [itemn0,ropemm,weightkg,lengthmm],
        [itemn1,ropemm1,weightkg1,lengthmm1],
        [itemn2,ropemm2,weightkg2,lengthmm2]

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
rct.drawOn(c,4.4*inch,2.8*inch)


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

itemn2 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >07535</para>',stylesN)
ropemm2 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>upto 12 </para>',stylesN)
weightkg2 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> 2.3</para>',stylesN)
lengthmm2 =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>600</para>',stylesN)

rc =[[itemn,rope,weight,length],
         ['','',''],
         ['','',''],
        [itemn0,ropemm,weightkg,lengthmm],
        [itemn1,ropemm1,weightkg1,lengthmm1],
        [itemn2,ropemm2,weightkg2,lengthmm2]

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
rct.drawOn(c,4.4*inch,1.2*inch)

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
c.drawString(20, 0.15*inch, "34")

c.showPage()

logo = "brugglifting.svg"
bg = "P35Banner.png"
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
a1 = "P35Strip.svg"

width, height = A4

c.drawImage(bg,0*inch,8.25*inch,width=8.5*inch,height=3*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

drawing = svg2rlg(a1)
scaleFactor = 1/1.25
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0, 8.25*inch)

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
textobject.setTextOrigin(308, 7.75*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 9)
textobject.textLines('''
                        When selecting the packaging, BRUGG LIFTING pays attention to the
                        best transport protection possible. Our ropes are protected in the best
                        possible  way  during  the  transport  with special  packaging materials
                        against corrosion and mechanical damaging.

                        BRUGG  LIFTING is committed  to handle  ressources with great  care.
                        That  is  why  our  ropes,  whenever possible, are delivered  on  sturdy
                        returnable reels and drums that can be reused.
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 5.25*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 9)
textobject.textLines('''
                          Cross Drums
                          ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 5.1*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                           capacity according to rope diameter
                           from 100m (16mm) to 400m (6,5mm)
                         ''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(308, 4.5*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 9)
textobject.textLines('''
                          Round Reels
                          ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 4.35*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          /width: 300 600mm / 320 530mm
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 3.9*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 9)
textobject.textLines('''
                          Coils
                          ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 3.75*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          up to 50m or 30kg
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 3.4*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 9)
textobject.textLines('''
                          XJ Wooden Reels 100 x 65 cm

                          ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 3.25*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          capacity according to rope diameter
                          from 1000m HRS ( 16mm) or 1132kg reel weight
                          up to 4100m HRS ( 8mm) or 1118kg reel weight
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 2.5*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 8)
textobject.textLines('''
                        System Deliveries on Pallets
                             ''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(308, 2.35*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        consisting  of  rope/ end  terminations/ accessories/
                        mounting materia
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 1.8*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica-Bold", 9)
textobject.textLines('''
                        System Deliveries in Sturdy Cardboard Box
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 1.65*inch)
c.setFillColor('#3C434B')
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        L/W/H: 80x60x80cm / 120x60x80cm
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
c.drawString(580, 0.15*inch, "35")


c.showPage()

i1 = "i1.png"
i2 = "i2.png"
b1 = "b1.png"
b2 = "b2.png"
b3 = "b3.png"
b4 = "b4.png"
b5 = "b5.png"
b6 = "b6.png"
b7 = "b7.png"
l1 = "e1-01.png"
i8 = "i8.png"
i9 = "i9.png"
i10 = "i10.png"
i11 = "i11.png"
i12 = "i12.png"
i13 = "i13.png"
i14 = "i14.png"
i15 = "i15.png"

a1 = "P36Banner.png"
a2 = "P37Banner.png"
a3 = "P37Strip.svg"
a4 = "P36Strip.svg"
a5 = "P36Strip.png"
a6 = "P37Strip.png"

rope = "ropetech.png"
bg = "img1.jpg"
logo = "brugglifting.svg"
lp ="P38BG.png"
wm = "P37Banner.png"

width,height = A4

c.drawImage(a1,0*inch,8.1*inch,width=8.5*inch,height=3*inch)
drawing = svg2rlg(logo)
scaleFactor = 1./1.5
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 10.2*inch)
# c.drawInlineImage(rope,8*inch,5.5*inch,width=1*inch,height=1.4*inch,preserveAspectRatio=True)

c.drawImage(a5,0*inch,8.1*inch,width=8.5*inch,height=1*inch,mask="auto")

c.drawImage(sha1,8.15*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

q1  = Paragraph('<para fontsize=20 align="justify" color = white > <b>WE SUPPORT YOU.</b><span color=rgb(0,157,224)><b>WORLDWIDE</b></span></para>',stylesN)
t= [[q1]]
tq = Table(t)
tq.wrapOn(c,width,height)
tq.drawOn(c,30,8.6*inch)

c.drawImage(i8,25,5.5*inch,width=2*inch,height=2.5*inch)

c.drawImage(i9,25,2.75*inch,width=2.5*inch,height=2.5*inch)

c.drawImage(i10,58,0.4*inch,width=1.5*inch,height=1.75*inch)

p1  = Paragraph('<para fontsize=11 align="justify"> <b>brugglifting.com.</b> The compact informative homepage</para>',stylesN)
w1  = Paragraph('<para fontsize=11 align="justify" leading=13> Our Homepage provides you with vivid depictions of our entire product range. You can intuitively make preselections to meet your individual requirements and find your BRUGG LIFTING contacts all over the world with just a click. For the latest information, just visit our start page.</para>',stylesN)

p2  = Paragraph('<para fontsize=11 align="justify" > <b>RLP . </b>Calculate the service life  of your ropes</para>',stylesN)
w2  = Paragraph('<para fontsize=11 align="justify" leading=13> Login in to our service life calculator on our wevsite and enter the data of your ropes tp calculate their service life..</para>',stylesN)

p3  = Paragraph('<para fontsize=11 align="justify" > <b>Instructions for Use . </b>Important tips for rope handling</para>',stylesN)
w3  = Paragraph('<para fontsize=11 align="justify" leading=13> Login in to our service life calculator on our wevsite and enter the data of your ropes tp calculate their service life..</para>',stylesN)

p4  = Paragraph('<para fontsize=11 align="justify" > <b>User Reference Guide . </b>About the handling our ropes</para>',stylesN)
w4  = Paragraph('<para fontsize=11 align="justify" leading=13>Make use of our extenxive know-hoe rope handling. A quick Link on our website thakes you to our User Reference Guide where you both find comprehensive technical details and tips and may retrieve the requested information via a targeted ful-text Search You may store all data as a PDF file.</para>',stylesN)

tp = [[p1],[w1],[''],[p2],[w2],[''],[''],[''],[''],[p3],[w3],[''],[''],[''],[''],[''],[p4],[w4]]
tpt = Table(tp,colWidths=12.25*cm)
tpt.wrapOn(c,width,height)
tpt.drawOn(c,3.25*inch, 1.25*inch)

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
c.drawString(20, 0.15*inch, "36")

c.showPage()

c.drawImage(wm,0*inch,8.1*inch,width=8.5*inch,height=3*inch)

# drawing = svg2rlg(a3)
# scaleFactor = 1/1.25
# drawing.width *= scaleFactor
# drawing.height *= scaleFactor
# drawing.scale(scaleFactor, scaleFactor)
# renderPDF.draw(drawing, c, 0, 8*inch)

c.drawImage(z9,0*inch,8.1*inch,width=8.5*inch,height=0.3*inch)

c.drawImage(bg7,0*inch,8.1*inch,width=8.5*inch,height=0.25*inch)

drawing = svg2rlg(z2)
scaleFactor = 1/1.97
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 0,8.1*inch)

c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')


textobject = c.beginText()
textobject.setTextOrigin(2*inch, 0.4*inch)
textobject.setFont("Helvetica-Bold", 50)
textobject.setFillColorRGB(192,192,192)
textobject.textLines('''
                        brugglifting.com
                      ''')
c.drawText(textobject)

c.drawInlineImage(rope,3.25*inch,7.45*inch,width=1.75*inch,height=1.4*inch,preserveAspectRatio=True)

d1 = Paragraph('<para><img src="P37Swis.png" valign="middle" /></para>',stylesN)
d2 = Paragraph('<para fontsize=10 leftindent=-65><b> SWITZERLAND</b></para>',stylesN)
d3 = Paragraph('<para fontsize=8 leading=17 leftindent=24><b>BRUGG LIFTING</b><br/>Wydenstrasse 36<br/>5242 Birr<br/> Switzerlad<br/> T +41 (0)56 464 42 42<br/> F +41(0)56 464 42 84<br/>info.lifting@brugg.com<br/>brugglifting.com</para>',stylesN)
dt=[[d1,d2],[d3]]
dtt =Table(dt,colWidths=[5*cm,3.5*cm])
dtt.setStyle(TableStyle([
                                ('TOPPADDING',(0,0),(-1,-1),20),
                       ]))
dtt.wrapOn(c,width,height)
dtt.drawOn(c,30, 4.75*inch)

d1 = Paragraph('<para><img src="P37Swis.png" valign="middle" /></para>',stylesN)
d2 = Paragraph('<para fontsize=10 leftindent=-65><b> SWITZERLAND</b></para>',stylesN)
d3 = Paragraph('<para  align="Justify"fontsize=8 leading=17 leftindent=20><b>BRUGG LIFTING</b><br/>Chemin de Foret 12<br/>1024 Ecublens<br/> Switzerlad<br/> T +41 (0)21 634 20 21<br/> F +41(0)21 635 09 71<br/>vente.lifting@brugg.co<br/>brugglifting.com</para>',stylesN)
dt=[[d1,d2],[d3]]
dtt =Table(dt,colWidths=[5*cm,3.5*cm])
dtt.setStyle(TableStyle([
                                ('TOPPADDING',(0,0),(-1,-1),20),
                       ]))
dtt.wrapOn(c,width,height)
dtt.drawOn(c,3.1*inch, 4.75*inch)

d1 = Paragraph('<para><img src="P37USA.png" valign="middle" /></para>',stylesN)
d2 = Paragraph('<para fontsize=10 leftindent=-65><b>USA</b></para>',stylesN)
d3 = Paragraph('<para fontsize=8 leading=17 leftindent=22><b>Brugg Wire Rope LLC</b><br/>3411 Turkey Mountain Road NE<br/>US-Rome,GA 30161<br/> T +1 706 314 29 82<br/> F +1 706 235 60 35<br/>lifting.usa@brugg.com<br/>brugglifting.com</para>',stylesN)
dt=[[d1,d2],[d3]]
dtt =Table(dt,colWidths=[5*cm,3.5*cm])
dtt.setStyle(TableStyle([
                                ('TOPPADDING',(0,0),(-1,-1),20),
                       ]))
dtt.wrapOn(c,width,height)
dtt.drawOn(c,5.75*inch, 4.75*inch)

d1 = Paragraph('<para><img src="P37China.png" valign="middle" /></para>',stylesN)
d2 = Paragraph('<para fontsize=10 leftindent=-65><b>CHINA</b></para>',stylesN)
d3 = Paragraph('<para fontsize=8 leading=17 leftindent=22><b>BRUGG LIFTING</b><br/>Plant 1, Nr.88 jingling East Road<br/>Suzhou Industrial Park<br/> jiangsu Province,215121<br/>P.R. China<br/>T +86 512 6299 0779<br/> F +86 512 6299 0774<br/>lifting.cn@brugg.com<br/>brugglifting.cn</para>',stylesN)
dt=[[d1,d2],[d3]]
dtt =Table(dt,colWidths=[5*cm,3.5*cm])
dtt.setStyle(TableStyle([
                                ('TOPPADDING',(0,0),(-1,-1),20),
                       ]))
dtt.wrapOn(c,width,height)
dtt.drawOn(c,30, 1.65*inch)

d1 = Paragraph('<para><img src="P37Worldwide.png" valign="middle" /></para>',stylesN)
d2 = Paragraph('<para fontsize=10 leftindent=-65><b> WORLDWIDE</b></para>',stylesN)
d3 = Paragraph('<para  align="Justify"fontsize=8 leading=17 leftindent=22> Our quality products are  available from more than 20 distributing partners         around the world.</para>',stylesN)
dt=[[d1,d2],[d3]]
dtt =Table(dt,colWidths=[5*cm,3.5*cm])
dtt.setStyle(TableStyle([
                                ('TOPPADDING',(0,0),(-1,-1),20),
                       ]))
dtt.wrapOn(c,width,height)
dtt.drawOn(c,3.1*inch, 3*inch)

textobject = c.beginText()
textobject.setTextOrigin(40, 1.1*inch)
c.setFillColor('#C0C0C0')
textobject.setFont("Helvetica-Bold",57)
textobject.textLines('''
                        brugglifting.com
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(40, 0.75*inch)
c.setFillColor('#C0C0C0')
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                        Creation date 10 / 2018
                        Subject to changes. Nonbinding indication of measures. No warranty for printing errors or errors.
                        If not agreed otherwise, our general conditions of sale and delivery are valid.
                        We thank  OSMAAufzuge for the provision of the photos on the following pages 9, 13
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
c.drawString(580, 0.15*inch, "37")

c.showPage()

c.drawImage(lp,0*inch,0*inch,width=8.5*inch,height=12*inch)

c.showPage()
c.setPageSize((2000, 1000))
c.save()
