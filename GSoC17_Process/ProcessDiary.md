## gsoc17-Eczar Process Diary

**June 07**

**June 06**
- Alternate test designs for /alpha /eta /iota /rho
- Extra glyphs added: /epsilon /mu, added diacritics. Comparison of two alternate
versions with different in & out strokes, and how they read along Latin text (designs await feedback from mentor):

![FirstTests](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_Screenshots/170606_01.png?raw=true)

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
