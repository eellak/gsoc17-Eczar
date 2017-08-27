## **GSoC17 - Eczar | Final Report**

**This is the Final Report for the work done for the project GSoC17-Eczar.**

Student: Emilios Theofanous | [GitHub](https://github.com/thynem) | [Twitter](https://twitter.com/emilios__)


---
### **Summary with the project’s links**

- [Repository of the project](https://github.com/eellak/gsoc17-Eczar)
- [Daily Process Diary](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/ProcessDiary.md)
- [Helpful files for the construction of Greek polytonic](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/04_Diacritics)
- [UFO files](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/01_UFO)
- [OTF & TTF files](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/05_Exports)

---

### **Introduction**

**The Project took place during the Google Summer of Code 2017.**

- **It’s aim was to offer full support for the Greek script, including polytonic**, to an existing open source typeface. Eczar was selected, an open-source type family designed by Vaibhav Singh, produced by David Březina, and published by [Rosetta Type Foundry](https://rosettatype.com).
You can view the original Github repository of the project [here](https://github.com/rosettatype/Eczar).

A few words about the selected typeface: Eczar has a strong personality, with five weights from Regular to Extra-Bold and can be used to set text from body copy to display.
These characteristics were transferred to the Greek script as well, with the intention of providing a contemporary open source typeface with Greek support.

At the moment, not many serif fonts that support Greek are available from Google Fonts; as a result many Greek websites, that load their fonts from Google Fonts, lack of unique brand and personality. The same can be said for non-profit organizations that depend on open source projects for their daily production tasks.
By adding polytonic support, the typeface becomes even more versatile, and can be used not only for multilingual webpages but also i.e. for academic reasons, for publishing houses that prefer polytonic text etc.
The goal of this project is to expand the Google Fonts collection with support for the Greek script and create a repository for future reference for designers that are interested in adding Greek support in their fonts.


### **Process**

One can browse the [Daily Diary I kept during the GSoC17 here](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/ProcessDiary.md), and take a look at the process of the designs, and more importantly the feedback from the mentor, Greek typeface designer Irene Vlachou. The feedback provided might not be universal and applicable on every design, but viewing it in context with the current design process, then valuable conclusions regarding proportions, relations between letters, spacing etc can be extracted and be applied to other designs.

The original week by week, **timeline** for the project can be found [here](https://github.com/eellak/gsoc17-Eczar/blob/master/TIMELINE.md).


### **Design**

![Sample170827](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/Sample170827.png?raw=true)


Eczar already supported Latin and Devanagari. Devanagari are designed with an axis mirrored in relation to the Latin; this provided a good basis for certain shapes that could be mirrored into the Greek design, rendering a balanced outcome for all the supported scripts.

For the design of the Greek letterforms, the project started with various explorations on letterforms with characteristics inspired from the existing Latin, yet unique to the Greek as the script demands special treatment due to its historic origins and constructional ductus.
Attention was paid in the counters, as their shape could be transferred from the Latin to the Greek round letters and provide better balance and rhythm between Latin and Greek.

For the ExtraBold weight, the decision to rotate the axis to an almost horizontal was made, as this provided easier handling on the addition of weight, especially for letters with horizontal loops such as /beta and /epsilon.

Most of the Greek capitals occur in Latin as well, so these ones were copied; the others were designed to match the rest of the set.

For the polytonic, the appropriate diacritics were designed and for their construction you can be informed from [here](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/04_Diacritics).
I have created files with the appropriate unicode values:
` glyphWithDiacritic = baseGlyph + diacritic @position | Unicode Value `
After the build, manual check is always advised as some the diacritics will need adjustments.

A small pangram animation, from Regular to ExtraBold and back, demonstrating the changes of the final design that occur as weight is added:

![EczarRegularToExtraBoldAnimation170816](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/EczarRegularToExtraBoldAnimation170816.gif?raw=true)


At the end, over 300 glyphs were added per weight.
That is for full coverage of monotonic & polytonic.
Mentor Irene Vlachou has a helpful repository with the [Greek character set](https://github.com/irenevl/Google-Greek-Sets).

### **Deliverables**

- The Final UFO files can be found [here](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/01_UFO)

- The exported OTF & TTF files can be found [here](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/05_Exports)

---

### GSoC Mentors:

* Alexios Zavras
* Diomidis Spinellis
* Irene Vlachou | [GitHub](https://github.com/irenevl) | [Twitter](https://twitter.com/irene_vlachou)

### Student:

* Emilios Theofanous | [GitHub](https://github.com/thynem) | [Twitter](https://twitter.com/emilios__)

### Organization:

[Open Technologies Alliance - GFOSS](https://summerofcode.withgoogle.com/organizations/4825634544025600/)

---

## License

The fonts and related code are licensed under [Open Font License](https://github.com/rosettatype/eczar/tree/master/LICENSE.txt). See `LICENSE.txt` [here](https://github.com/eellak/gsoc17-Eczar/blob/master/LICENSE.txt) for licensing information.
