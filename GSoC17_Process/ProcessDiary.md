## gsoc17-Eczar Process Diary

**June 15** <br />
** Feedback from Mentor was provided, suggestions include:**
- to keep the terminals from V02 and implement them on the skeleton of v03
- make stronger and more prominent the corner element and the sharp strokes
to match the latin better
- fix some widths (check: /omicron, /rho, /alpha)

![FirstTests](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170615-IVfeedback1.png?raw=true)
![FirstTests](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170615-IVfeedback2.png?raw=true)

**June 14**
- Version 03 of initial test designs uploaded
- Test doc with the 3 versions
- Skype meeting with Mentor

**June 10**
-


**June 07**
- Initial designs for a third version, with more elements from the Latin

**June 06**
- Alternate test designs for /alpha /eta /iota /rho
- Extra glyphs added: /epsilon /mu, added diacritics. Comparison of two alternate
versions with different in & out strokes, and how they read along Latin text (designs await feedback from mentor):

![FirstTests](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/170606_01.png?raw=true)

**June 05**
- Initial designs for Regular & Extra-Bold
- First glyphs added: /alpha /eta /iota /omicron /rho
- **Interpolation tests:**
based on the original design of Eczar, and according to the /n stems of Regular & Extra Bold,
one can get the interpolation factor with some simple math:

   for i in [0, max]

   n(i+1) = n(i) + (n(max)-n(i)) * factor

   Initial designs examples for some of the Greek glyphs (awaiting feedback from mentor):
![InterpolationTests170605](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/InterpolationTests/InterpolationTests170605.png?raw=true)

**June 01-02**
- Initial sketches & designs
