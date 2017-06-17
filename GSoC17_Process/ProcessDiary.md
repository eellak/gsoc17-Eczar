## **gsoc17-Eczar Process Diary**

**June17**


**June 16**
- Implementation of feedback
- Change of Greek Capitals, that share same design with Latin, to components

**June 15**

**Feedback from Mentor was provided (you can view the pdf [here](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/00_Feedback/170615-IVfeedback.pdf)). Suggestions include:**
- to keep the terminals from v02 and implement them on the skeleton of v03
- make stronger and more prominent the corner element and the sharp strokes
to match the latin better
- fix some widths (check: /omicron, /rho, /alpha)


![IVfeedback1](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170615-IVfeedback1.png?raw=true)
![IVfeedback2](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170615-IVfeedback2.png?raw=true)

**June 14**
- Version 03 of initial test designs uploaded
- **First (Skype) meeting with mentor**
- Test print doc, created with Drawbot Extention for RoboFont, with the 3 versions: (you can download the pdf [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170614.pdf))

![TestPrintDoc170614](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170614.png?raw=true)

**June 13**
- Revision and cleanup for v01 and v02, based on v03
- Changed 'font info', adding individual names based on date and version in UFO files for better test install from RoboFont

**June 10**
- Cleanup of previous versions
- Glyphs added: /alpha /epsilon /iota /rho (designs await feedback from mentor).

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
