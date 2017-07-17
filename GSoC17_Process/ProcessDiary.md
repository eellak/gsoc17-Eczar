## **gsoc17-Eczar Process Diary**

**July1 17**
- UFO cleanups & latest versions uploaded at github

**July 16**
- Revisions
- Test print doc, created with DrawBot Extension for RoboFont. It includes the ExtraBold lowercase and text set in ExtraBold & Regular for comparison (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170716.pdf))

![PrintDoc170716_pg1](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170716_pg1.png?raw=true)
![PrintDoc170716_pg2](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170716_pg2.png?raw=true)

**July 14**
- Glyphs added in ExtraBold: /dieresistonos /upsilon /upsilondieresisandtonos /upsilondieresis /upsilonwithtonos /phi /chi /psi /omega /omegawithtonos (designs await feedback from mentor).

Lowercase for ExtraBold is now complete. A small pangram animation, from Regular to ExtraBold and back, created with the RoboFont Extension ‘Mutator Animator’ by Mathieu Réguer:

![EczarRegularToExtraBoldAnimation170716](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/EczarRegularToExtraBoldAnimation170716.gif?raw=true)

**July 13**

- Glyphs added in ExtraBold: /zeta /kappa /xi /pi /finalsigma /sigma /tau (designs await feedback from mentor).
- Revisions
- Test prints

**July 12**
- Glyphs added in ExtraBold: /beta /gamma /delta /theta /lamda /nu (designs await feedback from mentor).

**July 10-11**

Initial designs for the ExtraBold weight -based on the current Regular- and fixes for interpolation compatibility. Regarding the design itself, as the weight increases, the axis rotates to an almost horizontal one (designs await feedback from mentor).

- Revised design for /chi
- Added components for the Greek Capitals that share same design with Latin to the ExtraBold
- Glyphs added in ExtraBold: /Alpha /Beta /Epsilon /Zeta /Eta /Iota /Kappa /Lamda /Mu /Nu /Omicron /Rho /Tau /Chi /tonos /alpha /alphawithtonos /epsilon /epsilonwithtonos /eta /etawithtonos /iota /iotawithtonos /mu /omicron /omicronwithtonos /rho
- Added anchors to existing glyphs for diacritics
- Fix of a unicode error in Glyph Construction file for diacritics and added the correct glyph \Omicronlenisacute
- UFO update in github
- I have also prepared a small animation of the weight, from Regular to ExtraBold and back, for better view of the changes that occur as the weight changes. It was created with the RoboFont Extension ‘Mutator Animator’ by Mathieu Réguer.

![EczarRegularToExtraBoldAnimation170712](https://raw.githubusercontent.com/eellak/gsoc17-Eczar/42dff7e798ca08d3dcb4d16036779076602ae6be/GSoC17_Process/03_ScreenshotsForProcessDiary/EczarRegularToExtraBoldAnimation170712.gif)


**July02**
- Revisions
- UFO cleanup & latest version uploaded at github
- Test print doc, created with DrawBot Extension for RoboFont. This one includes all the latest characters, with texts set in Monotonic and Polytonic as well: (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170702.pdf))

![PrintDoc170702_pg1](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170702_pg1.png?raw=true)
![PrintDoc170702_pg2](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170702_pg2.png?raw=true)
![PrintDoc170702_pg3](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170702_pg3.png?raw=true)
![PrintDoc170702_pg4](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170702_pg4.png?raw=true)

**July01**
- Complete polytonic, lowercase and uppercase, I will not mention all the 230+ glyphs with their name, however I have prepared:

**[.txt and .glyphConstruction files](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/04_Diacritics) so anyone can use them in order to build the needed characters with diacritics for Greek Monotonic & Basic Polytonic**

- You can find the files [here](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/04_Diacritics)
- Anchors are used on the base glyphs for the position of diacritics
- I have also added the unicode value to each one
- I used [Glyph Builder](https://github.com/typemytype/GlyphConstruction), however you can use these files as you prefer

![GlyphBuilder](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/GlyphBuilder_170702.png?raw=true)

**June30**

**First Evaluation Results, all good :)**
- Beginning of writing proper code for the build of polytonic


**June28**
- Glyphs added: /kaisymbol
- New design for /Upsilon, with a more ‘traditional’ look
- Diacritics for polytonic
- Glyphs added: /iotaadscript /lenis /gr:tilde /dieresistilde /lenisgrave /lenisacute /lenistilde /aspergrave /asperacute /aspertilde /dieresisgrave /dieresisacute /gr:grave /gr:acut /asper and for the uppercase /iotaadscript.case /lenis.case /lenisgrave.case /lenisacute.case /lenistilde.case /aspergrave.case /asperacute.case /aspertilde.case /gr:grave.case /gr:acute.case /asper.case.
- /breve & /macron are the same as the Latin ones.

**June27**

**First Evaluation**

**Feedback from Mentor was provided, via email conversation, suggestions include:**

- narrower /alpha /kappa /epsilon /theta /upsilon
- longer horizontal stroke of /tau
- /phi counter should be corrected, it needs more balance and should be closer to the stress of /omicron
- wider /chi
- general note: the junction of /epsilon /beta /omega and /xi seems that it needs a bit of work, maybe the triangular shape isn’t perfect so we should make a note to revise it again after we see how it behaves in heavier weights
- Implementation of feedback, with some revisions on the junctions and characters that share similar characteristics, with yellow the new version.

![Feedback170627](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/Feedback170627.png?raw=true)

**June26**
- Glyphs added: /Gamma /Delta /Theta /Lamda /Xi /Pi /Sigma /Phi /Psi /Omega /Omegawithtonos (designs await feedback from mentor). With these added, we have the complete monotonic character set, lowercase & uppercase.
- Test print docs

**June25**
- Added anchors to base glyphs that accept diacritics
- Proper built of diacritics. [Glyph Builder](https://github.com/typemytype/GlyphConstruction) from [Frederik Berlaen](https://github.com/typemytype) was used.
- Glyphs added: /anoteleia /tonos.case /dieresistonos /iotadieresis /iotadieresisandtonos /upsilondieresis /upsilondieresisandtonos /Alphawithtonos /Epsilowithtonos /Etawithtonos /Iotawithtonos /Iotadieresis /Omicronwithtonos (designs await feedback from mentor)
- Test print doc, created with DrawBot Extension for RoboFont, with the latest characters: (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170625.pdf))

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
- Test print doc, created with DrawBot Extension for RoboFont, with the latest characters: (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170620.pdf))

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
- Test print doc, created with DrawBot Extension for RoboFont, with the 3 versions: (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170614.pdf))

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
- **Interpolation tests:** (created with DrawBot Extension for RoboFont)
based on the original design of Eczar, and according to the /n stems of Regular & Extra Bold,
one can get the interpolation factor with some simple math:

   for i in [0, max]

   n(i+1) = n(i) + (n(max)-n(i)) * factor

   Initial designs examples for some of the Greek glyphs, (awaiting feedback from mentor), you can view the pdf [here](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/InterpolationTests/InterpolationTests170605.pdf).

![InterpolationTests170605](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/InterpolationTests/InterpolationTests170605.png?raw=true)

**June 01-02**
- Initial sketches & designs
