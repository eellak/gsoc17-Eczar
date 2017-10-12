
#===============////////////////////===============

# to be used with Eczar Fonts :
# Link: https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/05_Exports

#===============///////PAGE01///////===============

import random

newPage("A4Landscape")
fill(0)
rect(0,0, width(), height())
fill(1)
fontSize(32)
font("Eczar-Regular_170827")

t = """Adding Greek
to the Open Source Font ‘Eczar’"""

translate(50,height()/2)
textBox(t, (0, 0-fontLineHeight()-fontLineHeight()/5, width(), fontLineHeight()*2))

fontSize(height()*1.2)

t = u'''αβγδεζηθικλμνξοπρστυφχψω'''

fill(None)
stroke(1)
strokeWidth(0.1)
save()

textBox("λ", (width()/2, fontDescender()-height()/2, width(), height()*1.2))
translate(fontXHeight()*0.2, 0)
textBox("ε", (width()/2, fontDescender()-height()/2, width(), height()*1.2))
translate(fontXHeight()*0.2, 0)
textBox("η", (width()/2, fontDescender()-height()/2, width(), height()*1.2))
translate(fontXHeight()*0.2, 0)
textBox("ζ", (width()/2, fontDescender()-height()/2, width(), height()*1.2))
translate(fontXHeight()*0.2, 0)
textBox("ρ", (width()/2, fontDescender()-height()/2, width(), height()*1.2))
translate(fontXHeight()*0.2, 0)
restore()

fontSize(14)
fill(0.5)
stroke(None)
textBox("GSoC17 | Emilios Theofanous", (0, -height()/2, width(), fontLineHeight()*2))


#===============///////PAGE02///////===============


newPage("A4Landscape")
hyphenation(True)
font("Eczar-ExtraBold_170827")
fontSize(32)
t = """Synopsis / Σύνοψη"""
save()
translate(50,height()/2)
textBox(t, (0, 0-height()/4, width()-200, height()/2))
restore()

font("Eczar-Regular_170827")
fontSize(22)

t = """The aim of the project was to offer full support for the Greek script, including polytonic, to an existing open source typeface; expanding the Google Fonts collection and create a repository for future reference for designers who are interested in designing Greek."""

translate(50,height()/2)
textBox(t, (0, 0-height()/2.8, width()-280, height()/2))


#===============///////PAGE03///////===============


newPage("A4Landscape")
t = FormattedString()
t.align("center")
t.font("Eczar-ExtraBold_170827")
t.fontSize(46)
t += "ἤρχισε νὰ πλύνῃ τὰ ροῦχα"

t.font("Eczar-Regular_170827")
t.fontSize(35.5)
t.lineHeight(36)
t +="\n"
t += "μία ακρίδα ζωγραφίζει ρεβίθια για φαΐ"

t.font("Eczar-Regular_170827")
t.fontSize(38.2)
t.lineHeight(52)
t +="\n"
t += "ΕΓΚΑΘΙΣΤΑΤΑΙ ΣΤΗ ΦΛΩΡΕΝΤΙΑ"

t.font("Eczar-ExtraBold_170827")
t.fontSize(72.5)
t.lineHeight(60)
t +="\n"
t += "ΧΡΥΣΕΣ ΓΟΒΕΣ"

t.font("Eczar-Bold_170827")
t.fontSize(52)
t.lineHeight(38)
t +="\n"
t += "τεμάχια σαπρῶν ξύλων"

t.font("Eczar-Bold_170827")
t.fontSize(33)
t.lineHeight(40)
t +="\n"
t += "εἶχε στείλει γράμμα ἀπὸ τριῶν ἐτῶν"

t.font("Eczar-Medium_170827")
t.fontSize(54.5)
t.lineHeight(51)
t +="\n"
t += "ελληνικής τυπογραφίας"

t.font("Eczar-Regular_170827")
t.fontSize(44.1)
t.lineHeight(61)
t +="\n"
t += "Ἡ γραῖα ἔκυψεν εἰς τὴν ἄκρην"

t.font("Eczar-ExtraBold_170827")
t.fontSize(100.7)
t.lineHeight(76)
t +="\n"
t += "ἀναλογισθῆ"

textBox(t, (0,-29, width(), height()))


#===============///////PAGE04///////===============


newPage("A4Landscape")
im = ImageObject("Robofont_171012.png")
im.lanczosScaleTransform(scale=0.365, aspectRatio=1)
image(im, (0,0))


#===============///////PAGE05///////===============


newPage("A4Landscape")
hyphenation(True)
font("Eczar-ExtraBold_170827")
fontSize(32)
t = """Design / Σχεδιασμός"""
save()
translate(50,height()/2)
textBox(t, (0, 0-height()/4, width()-200, height()/2))
restore()

font("Eczar-Regular_170827")
fontSize(22)

t = """For the design of the Greek letterforms, the project started with various explorations on letterforms with characteristics inspired from the existing Latin and Devanagari, yet unique to the Greek as the script demands special treatment due to its historic origins and constructional ductus. 

Attention was paid in the counters, as their shape could be transferred from the Latin to the Greek round letters and provide better balance and rhythm between the supported scripts."""
save()
translate(50,height()/2)
textBox(t, (0, 0-height()/2.8, width()-280, height()/2))
restore()


#===============///////PAGE06///////===============


newPage("A4Landscape")

hyphenation(True)
im = ImageObject("GlyphBuilder_170702.png")
im.lanczosScaleTransform(scale=0.177, aspectRatio=1)
image(im, (width()/3.8, height()/2.4))

font("Eczar-Regular_170827")
fontSize(22)

t = """





Polytonic support was also added, making the typeface even more versatile, as it can now be used not only for contemporary multilingual webpages / publications but also i.e. for academic reasons, research papers quoting ancient Greek, webpages with poetry set in polytonic etc."""
save()
translate(50,height()/2)
textBox(t, (0, 0-height()/2.8, width()-280, height()/2))
restore()


#===============///////PAGE07///////===============


newPage("A4Landscape")

t = FormattedString()
t.tracking(12)
t.fontSize(55)
t.lineHeight(54)

t.font("Eczar-Regular_170827")
t += "Α"

t.font("Eczar-Medium_170827")
t += "ΒΓ"

t.font("Eczar-SemiBold_170827")
t += "ΔΕ"
t.font("Eczar-Bold_170827")
t += "ΖΗ"
t.font("Eczar-ExtraBold_170827")
t += "ΘΙ"

t.font("Eczar-Regular_170827")
t += "\n"
t += "Κ"

t.font("Eczar-Medium_170827")
t += "Λ"

t.font("Eczar-SemiBold_170827")
t += "ΜΝ"

t.font("Eczar-Bold_170827")
t += "ΞΟ"

t.font("Eczar-ExtraBold_170827")
t += "ΠΡ"

t.font("Eczar-Regular_170827")
t += "\n"
t += "Σ"

t.font("Eczar-Medium_170827")
t += "ΤΥ"

t.font("Eczar-SemiBold_170827")
t += "ΦΧ"

t.font("Eczar-Bold_170827")
t += "Ψ"

t.font("Eczar-ExtraBold_170827")
t += "Ω"

t.font("Eczar-Regular_170827")
t += "\n"
t += "αά"

t.font("Eczar-Medium_170827")
t += "βγ"

t.font("Eczar-SemiBold_170827")
t += "δε"

t.font("Eczar-Bold_170827")
t += "έζ"

t.font("Eczar-ExtraBold_170827")
t += "ηή"

t.font("Eczar-Regular_170827")
t += "\n"
t += "θιί"

t.font("Eczar-Medium_170827")
t += "ϊΐ"

t.font("Eczar-SemiBold_170827")
t += "κλ"

t.font("Eczar-Bold_170827")
t += "μν"

t.font("Eczar-ExtraBold_170827")
t += "ξοό"

t.font("Eczar-Regular_170827")
t += "\n"
t += "πρ"

t.font("Eczar-Medium_170827")
t += "σς"

t.font("Eczar-SemiBold_170827")
t += "τυ"

t.font("Eczar-Bold_170827")
t += "ύϋ"

t.font("Eczar-ExtraBold_170827")
t += "ΰφ"

t.font("Eczar-Regular_170827")
t += "\n"
t += "χψ"

t.font("Eczar-Medium_170827")
t += "ω"

t.font("Eczar-SemiBold_170827")
t += "ώ"    

textBox(t, (50,-80, width(), height()))

t = FormattedString()
t.fontSize(13)
t.lineHeight(13.1)

t.font("Eczar-Regular_170827")
t += "Τελευταῖον ἐπῆρε καὶ τὸν ἄνδρα της, καὶ τῆς εἶχον μείνει μόνον δύο υἱοί, ξενιτευμένοι τώρα· ὁ εἷς εἶχεν ὑπάγει, τῆς εἶπον, εἰς τὴν Αὐστραλίαν, καὶ δὲν εἶχε στείλει γράμμα ἀπὸ τριῶν ἐτῶν· αὐτὴ δὲν ἤξευρε τί εἶχεν ἀπογίνει· ὁ ἄλλος ὁ μικρότερος ἐταξίδευε μὲ τὰ καράβια ἐντὸς τῆς Μεσογείου, καὶ κάποτε τὴν ἐνθυμεῖτο ἀκόμη. Τῆς εἶχε μείνει καὶ μία κόρη, ὑπανδρευμένη τώρα, μὲ μισὴν δωδεκάδα παιδιά."

t.font("Eczar-Medium_170827")
t += "\n"
t += "   Πλησίον αὐτῆς, ἡ γρια-Λούκαινα ἐθήτευε τώρα, εἰς τὸ γῆράς της, καὶ δι’ αὐτὴν ἐπήγαινε τὸν κατήφορον, τὸ μονοπάτι, διὰ νὰ πλύνῃ τὰ χράμια καὶ ἄλλα διάφορα σκουτιὰ εἰς τὸ κῦμα τὸ ἁλμυρόν, καὶ νὰ τὰ ξεγλυκάνῃ στὸ Γλυφονέρι."

t.font("Eczar-SemiBold_170827")
t += "\n"
t += "   Ἡ γραῖα ἔκυψεν εἰς τὴν ἄκρην χθαμαλοῦ, θα- λασσοφαγωμένου βράχου, καὶ ἤρχισε νὰ πλύνῃ τὰ ροῦχα. Δεξιά της κατήρχετο ὁμαλώτερος, πλαγιαστός, ὁ κρημνὸς τοῦ γηλόφου, ἐφ’ οὗ ἦτο τὸ Κοιμητήριον, καὶ εἰς τὰ κλίτη τοῦ ὁποίου ἐκυλίοντο ἀενάως πρὸς τὴν θάλασσαν τὴν πανδέγμονα τεμάχια σαπρῶν ξύλων ἀπὸ ξεχώματα, ἤτοι ἀνακομιδὰς ἀνθρωπίνων σκελετῶν, λείψανα ἀπὸ χρυσὲς γόβες ἢ χρυσοκέντητα"

t.font("Eczar-Bold_170827")
t += " ὑποκάμισα νεαρῶν γυναικῶν, συνταφέντα ποτὲ μαζί των, βόστρυχοι ἀπὸ κόμας ξανθάς, καὶ ἄλλα τοῦ θανάτου λάφυρα. Ὑπεράνω τῆς κεφαλῆς της, ὀλίγον πρὸς τὰ δεξιά, ἐντὸς μικρᾶς κρυπτῆς λάκκας, παραπλεύρως τοῦ Κοιμητηρίου, εἶχε καθίσει νεαρὸς βοσκός, ἐπιστρέφων μὲ τὸ μικρὸν κοπάδι"

t.font("Eczar-ExtraBold_170827")
t += " του ἀπὸ τοὺς ἀγρούς, καί, χωρὶς ν’ ἀναλογισθῇ τὸ πένθιμον τοῦ τόπου, εἶχε βγάλει τὸ σουραύλι ἀπὸ τὸ μαρσίπιόν του, καὶ ἤρχισε νὰ μέλπῃ φαιδρὸν ποιμενικὸν ᾆσμα. Τὸ μυρολόγι τῆς γραίας ἐκόπασεν εἰς τὸν θόρυβον τοῦ αὐλοῦ, καὶ οἱ ἐπιστρέφοντες ἀπὸ"

textBox(t, (width()/1.45,-80, width()/2.65, height()))


#===============///////PAGE08///////===============


newPage("A4Landscape")
fill(0)
rect(0,0, width(), height())
fill(1)
fontSize(32)
font("Eczar-Regular_170827")

t = """https://github.com/eellak/gsoc17-Eczar
"""

translate(50,height()/2)
textBox(t, (0, 0-fontLineHeight()+fontLineHeight()/3, width(), fontLineHeight()))

fontSize(14)
fill(0.5)
stroke(None)
t= """GSoC17 
Mentors: Alexios Zavras, Diomidis Spinellis, Irene Vlachou
Student: Emilios Theofanous / EsadType, Amiens
Organization: Open Technologies Alliance - GFOSS

Eczar is an open-source type family published by Rosetta Type Foundry"""
textBox(t, (0, -height()/2.5, width(), fontLineHeight()*6))


#===============///////PAGE09///////===============


newPage("A4Landscape")
font("Eczar-Regular_170827")
fontSize(height()*1.2)
fill(0)
rect(0,0, width(), height())
t = u'''αβγδεζηθικλμνξοπρστυφχψω'''

fill(None)
stroke(1)
strokeWidth(0.1)
save()
for i in range (24):
    textBox(random.choice(t), (-fontXHeight()/5, fontDescender(), width(), height()*1.2))
    translate(fontXHeight()*0.2, 0)
restore()

fill(1)  
textBox("ά", (-fontXHeight()/4.5, fontDescender(), width(), height()*1.2))


#===============///////SAVING///////===============

saveImage("GSoC17_MentorSummit_Theofanous_00.pdf")