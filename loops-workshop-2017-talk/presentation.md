title: Constraining Nanoflare Heating Frequency with a Global Active Region Model
class: animation-fade
layout: true

<!-- This slide will serve as the base layout for all your slides -->
.bottom-bar[
  <img src="../img/rice_owl_logo.transparent.png" style="float: right; width: 35px;">
]

---

class: impact
background-image: url("../img/Rice_University_seal.svg.transparent.png")
background-size: contain
background-blend-mode: overlay;

# {{title}}
## Will Barnes, Stephen Bradshaw
## 8th Coronal Loops Workshop &ndash; Palermo, Italy
## 28 June 2017

---

# Heating Frequency in AR Cores

Motivation, past studies, what does the slope tell us

Mention our previous papers, what did they tell us

Define what we mean by a "heating frequency"

Two primary questions:
* ## What are the signatures of these different heating frequencies?
* ## Are these signatures detectable?
---

## Making points

Look how you can make *some* points:
--

- Create slides with your **favorite text editor**
--

- Focus on your **content**, not the tool
--

- You can finally be **productive**!

---

# Forward Modeling Global Active Regions
Give details about synthesizar code, what we do

It would be nice to provide a flow chart of the code, e.g. using networkx or something like that

---

# Hydrodynamic Loop Model
Two-fluid EBTEL model of [Barnes et al. (2016a)][barnes_inference_2016a],

\begin{align}
\frac{dp\_e}{dt} =& \frac{\gamma - 1}{L}(\psi\_{TR} - (\mathcal{R}\_{TR} + \mathcal{R}\_C)) + k\_Bn\nu\_{ei}(T\_i - T\_e) + (\gamma - 1)Q\_e \\\\
\frac{dp\_i}{dt} =& -\frac{\gamma - 1}{L}\psi\_{TR} + k\_Bn\nu\_{ei}(T\_e - T\_i) + (\gamma - 1)Q\_i \\\\
\frac{dn}{dt} =& \frac{c\_2(\gamma - 1)}{c\_3\gamma Lk\_BT\_e}(\psi\_{TR} - F\_{ce,0} - \mathcal{R}\_{TR}) \\\\
p\_e =& k\_BnT\_e,\quad p\_i = k\_BnT\_i
\end{align}

Heat electrons or ions *dynamically* and model *spatially-averaged coronal* quantities

---

# Experiment Details


What active region we are looking at

What heating frequencies and energy distribution, show them (shown in previous slide)

What results were synthesized, lines, channels, etc.
---

# Heating Parameter Space

---

# Dynamic Results
Show some movies of concurrent AIA and EIS measurements, e.g. AIA in a particular channel for all 4 heating frequencies and 
a spectra from EIS for one of the channels

Play gifs side by side

---

# Diagnostics
Emission measure distributions for idealized case for all four heating frequencies, i.e. density squared integrated along LOS

Apply DEM inversion method to synthesized time-averaged intensities. Show 2D maps of EM for different frequencies and maps of EM slope. Do this for inverted and ground truth EM

Compare distribution of EM slope values for two methods for all heating frequencies, show Warren result superimposed

Look at 1D distribution for area studied by Warren et al., show ground truth

---

# Conclusions

---

## 12-column grid layout

Use to the included **grid layout** classes to split content easily:
.col-6[
  ### Left column

  - I'm on the left
  - It's neat!
]
.col-6[
  ### Right column

  - I'm on the right
  - I love it!
]

## Learn the tricks

See the [wiki](https://github.com/gnab/remark/wiki) to learn more of what you can do with .alt[Remark.js]

---

## Syntax highlighting

You can also add `code` to your slides:
```html
<div class="impact">Some HTML code</div>
```

## CSS classes

You can use .alt[shortcut] syntax to apply .big[some style!]

...or just <span class="alt">HTML</span> if you prefer.

[barnes_inference_2016a]: http://adsabs.harvard.edu/abs/2016arXiv160804776B

