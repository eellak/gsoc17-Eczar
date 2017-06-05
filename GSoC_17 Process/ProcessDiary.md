## gsoc17-Eczar Process Diary


**June 01-02**<br />
- Initial sketches & designs

**June 05**<br />
- Initial designs for Regular & Extra-Bold
- glyphs added: /alpha /eta /iota /omicron /rho
- **interpolation tests:** <br />
based on the original design of Eczar, and according to the /n stems of Regular & Extra Bold,
one can get the interpolation factor from some simple math:

   for i in [0, max]
   n(i+1) = n(i) + (n(max)-n(i)) * factor
