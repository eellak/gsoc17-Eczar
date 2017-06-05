# For DrawBot Extention in Robofont
# Draft coding for preview - code needs optimization

newPage("A4")
f1, f2 = AllFonts()

g1 = f1["alpha"]
g2 = f2["alpha"]
space = 1.2

save()
translate(50,700)
scale(0.1)

r1 = g1 + (g2 - g1) * 0.25
drawGlyph(g1)
translate(space*g1.width)
drawGlyph(r1)
translate(space*r1.width)


r2 = r1 + (g2 - r1) * 0.33
drawGlyph(r2)
translate(space*r2.width)

r3 = r2 + (g2 - r2) * 0.5
drawGlyph(r3)
translate(space*r3.width)
       
drawGlyph(g2)
restore()

save()
g1 = f1["iota"]
g2 = f2["iota"]

translate(50,600)
scale(0.1)
r1 = g1 + (g2 - g1) * 0.25
drawGlyph(g1)
translate(space*g1.width)
drawGlyph(r1)
translate(space*r1.width)


r2 = r1 + (g2 - r1) * 0.33
drawGlyph(r2)
translate(space*r2.width)

r3 = r2 + (g2 - r2) * 0.5
drawGlyph(r3)
translate(space*r3.width)
       
drawGlyph(g2)
restore()

save()
g1 = f1["omicron"]
g2 = f2["omicron"]

translate(50,500)
scale(0.1)
r1 = g1 + (g2 - g1) * 0.25
drawGlyph(g1)
translate(space*g1.width)
drawGlyph(r1)
translate(space*r1.width)


r2 = r1 + (g2 - r1) * 0.33
drawGlyph(r2)
translate(space*r2.width)

r3 = r2 + (g2 - r2) * 0.5
drawGlyph(r3)
translate(space*r3.width)
       
drawGlyph(g2)
restore()

save()
g1 = f1["rho"]
g2 = f2["rho"]

translate(50,400)
scale(0.1)
r1 = g1 + (g2 - g1) * 0.25
drawGlyph(g1)
translate(space*g1.width)
drawGlyph(r1)
translate(space*r1.width)


r2 = r1 + (g2 - r1) * 0.33
drawGlyph(r2)
translate(space*r2.width)

r3 = r2 + (g2 - r2) * 0.5
drawGlyph(r3)
translate(space*r3.width)
       
drawGlyph(g2)
restore()

save()
g1 = f1["a"]
g2 = f2["a"]

translate(50,300)
scale(0.1)
r1 = g1 + (g2 - g1) * 0.25
drawGlyph(g1)
translate(space*g1.width)
drawGlyph(r1)
translate(space*r1.width)


r2 = r1 + (g2 - r1) * 0.33
drawGlyph(r2)
translate(space*r2.width)

r3 = r2 + (g2 - r2) * 0.5
drawGlyph(r3)
translate(space*r3.width)
       
drawGlyph(g2)
restore()

save()
g1 = f1["o"]
g2 = f2["o"]

translate(50,200)
scale(0.1)
r1 = g1 + (g2 - g1) * 0.25
drawGlyph(g1)
translate(space*g1.width)
drawGlyph(r1)
translate(space*r1.width)


r2 = r1 + (g2 - r1) * 0.33
drawGlyph(r2)
translate(space*r2.width)

r3 = r2 + (g2 - r2) * 0.5
drawGlyph(r3)
translate(space*r3.width)
       
drawGlyph(g2)
restore()

font("SourceCodePro-Light")
fontSize(6)
textBox("Emilios Theofanous / GSoC17 - Adding Greek to the Open-Source Type Family Eczar / DraftInterpolationTests170605 ", (50, 0, width(), 30), align="left")

saveImage("InterpolationTests170605.png")
