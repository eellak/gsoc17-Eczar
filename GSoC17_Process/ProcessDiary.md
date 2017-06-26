## **gsoc17-Eczar Process Diary**

**June25**
- Added anchors to base glyphs that accept diacritics
- Proper built of diacritics. [Glyph Builder](https://github.com/typemytype/GlyphConstruction) from [Frederic Berlaen](https://github.com/typemytype) was used.
- Glyphs added: /anoteleia /tonos.case /dieresistonos /iotadieresis /iotadieresisandtonos /upsilondieresis /upsilondieresisandtonos /Alphawithtonos /Epsilowithtonos /Etawithtonos /Iotawithtonos /Iotadieresis /Omicronwithtonos (designs await feedback from mentor)
- Test print doc, created with Drawbot Extention for RoboFont, with the latest characters: (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170625.pdf))

![PrintDoc170625_pg1](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170625_pg1.png?raw=true)
![PrintDoc170625_pg2](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170625_pg2.png?raw=true)

**June 24**
- Glyphs added: /upsilon /upsilonwithtonos /chi /psi /omega /omegawithtonos (designs await feedback from mentor)
- Test print doc
- Corrections

**June 23**
- Implementation of feedback
- Tighter spacing
- UFO cleanup
- Glyphs added: /xi /phi (designs await feedback from mentor)

**June 22**

**Feedback from Mentor was provided (you can view the pdf [here](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/00_Feedback/220615-IVfeedback.pdf)). Suggestions include:**

- widening of /beta
- more prominent corner elements on several letters
- minor weight fixes

![IVfeedback_170622](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/220615-IVfeedback.png?raw=true)

**June21**

**Skype meeting with organization GFOSS and mentor.** Conversation regarding the first evaluation process, the timeline and completion of its goals.

**Skype meeting with mentor.** Conversation regarding the design and suggestions:
- on spacing, which is currently slightly loose
- on starting with some interpolation tests for the current design before the first evaluation
- implement basic kerning for some critical glyphs

**June20**
- Glyphs added: /beta /zeta (designs await feedback from mentor)
- Revisions
- Test print doc, created with Drawbot Extention for RoboFont, with the latest characters: (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170620.pdf))

![PrintDoc170620_pg1](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170620_pg1.png?raw=true)
![PrintDoc170620_pg2](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170620_pg2.png?raw=true)

**June19**
- Glyphs added: /gamma /delta /theta /kappa /lamda /nu /pi /sigma /finalsigma /tau (designs await feedback from mentor)
- Revised spacing
- Test prints

**June17**
- Test prints after feedback
- Revision on design of /alpha /mu /rho to fix colour

**June 16**
- Implementation of feedback
- Change of Greek Capitals, that share same design with Latin, to components

**June 15**

**Feedback from Mentor was provided (you can view the pdf [here](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/00_Feedback/170615-IVfeedback.pdf)). Suggestions include:**
- to keep the terminals from v02 and implement them on the skeleton of v03
- make stronger and more prominent the corner element and the sharp strokes
to match the latin better
- fix some widths (check: /omicron, /rho, /alpha)


![IVfeedback1_170615](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170615-IVfeedback1.png?raw=true)
![IVfeedback2_170615](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170615-IVfeedback2.png?raw=true)

**June 14**
- Version 03 of initial test designs uploaded
- **First (Skype) meeting with mentor**
- Test print doc, created with Drawbot Extention for RoboFont, with the 3 versions: (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170614.pdf))

![PrintDoc170614](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170614.png?raw=true)

**June 13**
- Revision and cleanup for v01 and v02, based on v03
- Changed 'font info', adding individual names based on date and version in UFO files for better test install from RoboFont

**June 10**
- Cleanup of previous versions
- Glyphs added: /alpha /epsilon /iota /rho (designs await feedback from mentor)

**The variations between the three versions, lie on the exploration of these elements:**
- different terminals, for example in v01 and v02 they follow an upwards exit, with v02 being more angular, while in v03, they follow a downwards exit (shown in red).
- on how much continuous or interrupted the ductus is, more prominent on the different constructions of /eta and /mu (shown in yellow)
- on the construction of loops, for example in v03, the design follows more closely a loop found in the devanagari script of Eczar (shown in purple)
- for v03 a sharper stroke ending is implement, following the endings found in the devanagari script of Eczar (shown in light blue)

![ExploartionsBetweenVersions](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170610_ExploartionsBetweenVersion.png?raw=true)

**June 07**
- Initial designs for a third version, with more design elements implement to match the Latin
- Glyphs added: /eta, /mu (designs await feedback from mentor)

**June 06**
- Alternate test designs for /alpha /eta /iota /rho
- Extra glyphs added: /epsilon /mu, added diacritics. Comparison of two alternate
versions with different in & out strokes, and how they read along Latin text (designs await feedback from mentor):

![FirstTests](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170606_01.png?raw=true)

**June 05**
- Initial designs for Regular & Extra-Bold
- First glyphs added: /alpha /eta /iota /omicron /rho
- **Interpolation tests:** (created with Drawbot Extention for RoboFont)
based on the original design of Eczar, and according to the /n stems of Regular & Extra Bold,
one can get the interpolation factor with some simple math:

   for i in [0, max]

   n(i+1) = n(i) + (n(max)-n(i)) * factor

   Initial designs examples for some of the Greek glyphs, (awaiting feedback from mentor), you can view the pdf [here](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/InterpolationTests/InterpolationTests170605.pdf).

![InterpolationTests170605](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/InterpolationTests/InterpolationTests170605.png?raw=true)

**June 01-02**
- Initial sketches & designs
