# gsoc17-Eczar


## Final Report
You can visit the **Final Report gist** for the project with more details on the process and design decisions [here](https://gist.github.com/thynem/034ee86ea3da707eb6e46ee230c59aed).

You can also take a look at the **daily process diary**, with thoughts on design, feedback from mentor, process screenshots and updates [here](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/ProcessDiary.md).

View the project on [Google Summer of Code website.](https://summerofcode.withgoogle.com/organizations/4825634544025600/#6608201922379776)


## Synopsis

**The Project took place during the Google Summer of Code 2017.**

**It’s aim was to offer full support for the Greek script, including polytonic**, to an existing open source typeface. Eczar was selected, an open-source type family designed by Vaibhav Singh, produced by David Březina, and published by [Rosetta Type Foundry](https://rosettatype.com).
You can view the original Github repository of the project [here](https://github.com/rosettatype/Eczar).


![Sample170827](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/Sample170827.png?raw=true)


A few words about the selected typeface: Eczar has a strong personality, with five weights from Regular to Extra-Bold and can be used to set text from body copy to display.
These characteristics were transferred to the Greek script as well, with the intention of providing a contemporary open source typeface with Greek support.

At the moment, not many serif fonts that support Greek are available from Google Fonts; as a result many Greek websites, that load their fonts from Google Fonts, lack of unique brand and personality. The same can be said for non-profit organizations that depend on open source projects for their daily production tasks.
By adding polytonic support, the typeface becomes even more versatile, and can be used not only for multilingual webpages but also i.e. for academic reasons, for publishing houses that prefer polytonic text etc.
The goal of this project is to expand the Google Fonts collection with support for the Greek script and create a repository for future reference for designers that are interested in adding Greek support in their fonts.

**A pdf file with all the character sets and sample texts can be found [here](https://github.com/eellak/gsoc17-Eczar/raw/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170827.pdf).**

A small pangram animation, from Regular to ExtraBold and back, demonstrating the changes of the final design that occur as weight is added:

![EczarRegularToExtraBoldAnimation170816](https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/03_ScreenshotsForProcessDiary/EczarRegularToExtraBoldAnimation170816.gif?raw=true)

---

## Deliverables

- **The Final UFO files can be found [here](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/01_UFO)**

- **The exported OTF & TTF files can be found [here](https://github.com/eellak/gsoc17-Eczar/tree/master/GSoC17_Process/05_Exports)**

---

## Timeline’s Summary:

**May 30 – June 29**<br />
Uppercase, lowercase and polytonic for Regular Weight

**June 30**<br />
**Phase 1 Evaluation**

**July 3 – July 27**<br />
Uppercase, lowercase and polytonic for Extra-Bold Weight, kerning and initial interpolation tests.

**July 28**<br />
**Phase 2 Evaluation**

**July 31 – August 28**<br />
Fix interpolation compatibility issues, completion of the 5 weights, documentation.


**August 29**<br />
**Finish**

You can find the detailed, week by week, **timeline** for the project [here](https://github.com/eellak/gsoc17-Eczar/blob/master/TIMELINE.md).



---

### GSoC Mentors:

* Alexios Zavras
* Diomidis Spinellis
* Irene Vlachou | [GitHub](https://github.com/irenevl) | [Twitter](https://twitter.com/irene_vlachou)

### Student:

* Emilios Theofanous | EsadType, Amiens | [GitHub](https://github.com/thynem) | [Twitter](https://twitter.com/emilios__)

### Organization:

[Open Technologies Alliance - GFOSS](https://summerofcode.withgoogle.com/organizations/4825634544025600/)

---

## License

The fonts and related code are licensed under [Open Font License](https://github.com/rosettatype/eczar/tree/master/LICENSE.txt). See `LICENSE.txt` for licensing information.
