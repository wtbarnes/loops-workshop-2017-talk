title: Constraining Nanoflare Heating Frequency with a Global Active Region Model
class: animation-fade
layout: true

<!-- This slide will serve as the base layout for all your slides -->
.bottom-bar[
  <a href="https://wtbarnes.github.io/loops-workshop-2017-talk/" style="color:#f8f8f8;">wtbarnes.github.io/loops-workshop-2017-talk</a>
  <img src="img/rice_owl_logo.transparent.png" style="float: right; height: 35px;">
]

---

class: impact
background-image: url("img/Rice_University_seal.svg.transparent.png")
background-size: contain
background-blend-mode: overlay;

# {{title}}
## Will Barnes, Stephen Bradshaw
## 8th Coronal Loops Workshop &ndash; Palermo, Italy
## 28 June 2017

---

# Outline
* Heating Frequency in AR Cores
* Forward Modeling Pipeline
* Hydrodynamic Loop Model
* Heating Parameter Space
* Diagnostics
  * True and Predicted Emission Measures
  * Emission Measure Slopes

---

# Heating Frequency in AR Cores

Motivation, past studies, what does the slope tell us

Mention our previous papers, what did they tell us

Define what we mean by a "heating frequency"

Many factors likely to obscure EM
* multiple emitting structures along the LOS
* nonequilibrium ionization
* difficulties due to inversion
* lack of spectral coverage in detectors

---

## Two primary questions:
* How does varying the heating frequency manifest itself in observable signatures?
* Are these signatures detectable?

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

* Follow approach of [Warren et al. (2012)][warren_systematic_2012]
* Use AR NOAA 1109 (#9 in Table 1) from 29 September 2010
* Model 10<sup>3</sup> individual fieldlines with two-fluid EBTEL model for ≈2&times;10<sup>4</sup> s
* Each individual strand evolves indpendently according to EBTEL model
* Calculate emission from *all* ions in the CHIANTI database (AIA)
* Synthesize *wavelength-resolved* intensity for 22 transitions (EIS)
* Repeat for four different average waiting times, $$ t_N=250,750,2500,5000\,\,\mathrm{s}$$


---
class: full,middle,center
background-image: url("img/aia_and_hmi_observations.png")
background-size: contain
---
class: middle

.col-6[
  <img src="img/contribution_fns.png" style="float:left" width="550px">
]
.col-6[

  | Ion         | Wavelength                               | Ion         | Wavelength                               |
  |:------------|:-----------------------------------------|:------------|:-----------------------------------------|
  |    S X      |            264.2306                      |    Si X     |            258.374                       |
  |    Fe X     |            184.537                       |    Fe XII   |              195.119                     |
  |    Fe IX    |              188.493                     |    Fe IX    |              197.854                     |
  |    Fe XII   |              192.394                     |    Fe XVI   |              262.976                     |
  |    Fe XI    |             180.401                      |    S XIII   |               256.6852                   |
  |    Ca XV    |             200.9719                     |    Fe XV    |             284.163                      |
  |    Fe XIII  |               202.044                    |    Fe XIV   |              264.7889                    |
  |    Fe XIII  |               203.826                    |    Ca XVI   |              208.585                     |
  |    Fe XIV   |              270.5208                    |    Fe XI    |             188.216                      |
  |    Ca XVII  |                192.8532                  |    Si VII   |               275.3612                   | 
  |    Ca XIV   |              193.8661                    |    Ar XIV   |              194.401                     |   
]

---

# Heating Parameter Space

.col-6[
* Each strand heated independently
* Preferentially heat electrons
* Triangual pulses with duration `\(\tau=200\,\,\mathrm{s}\)`
* Total input energy per strand set by $$E = \frac{(\epsilon B)^2}{8\pi}$$ 
* Event energies chosen from a power-law distribution with `\(\alpha=-2.5\)`
* `\(t_{N,i}\propto E_i\)` such that larger events require a longer "winding time"
]

.col-6[
<img src="img/wait_time_distribution.png" style="float:left" width="550px">
]

???
`\(B\)` is determined from the field extrapolation and `\(\epsilon=0.1\)`

---

# Dynamic Results
Show some movies of concurrent AIA and EIS measurements, e.g. AIA in a particular channel for all 4 heating frequencies and 
a spectra from EIS for one of the channels

Play gifs side by side

Save this for last as it will likely take the longest

---

# Diagnostics
* Calculate the *true* emission measure from simulated thermodynamic quantities, $$\mathrm{EM}(T) = \int_{\mathrm{LOS}}\mathrm{d}h\,n^2(h,T)$$ 
* Bin in temperature `\(5.6<\log{T}<7.0\)` with width `\(\Delta\log{T}=0.05\)`
* Calculate *predicted* emission measure from the regularized inversion code of [Hannah and Kontar (2012)][hannah_differential_2012]
  * Assume 25% uncertainty on our intensities to balance acceptable `\(\chi^2\)` and smoothness
  * Apply to single-pixel **and** full AR
* Fit power-law to cool side such that `\(\mathrm{EM}\sim T^a\)`
  * Fit between 1 MK and 4 MK (3 MK) for true (predicted) emission measure
  * Only fit to pixels where `\(\mathrm{EM}(T)>10^{25}\)` and acceptable fit `\(R^2>0.95\)`

???
Integrated intensities for all 22 spectral lines as observed by EIS

HK12 gives us error bars in both temperature and emission measure

---

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
[warren_systematic_2012]: http://adsabs.harvard.edu/abs/2012ApJ...759..141W
[hannah_differential_2012]: http://adsabs.harvard.edu/abs/2012A%26A...539A.146H

