# 8th Coronal Loops Workshop
[![Build Status](https://travis-ci.org/wtbarnes/loops-workshop-2017-talk.svg?branch=master)](https://travis-ci.org/wtbarnes/loops-workshop-2017-talk)

Slides for my talk at the [8th Coronal Loops Workshop (2017)](http://www.astropa.unipa.it/CLW2017/CLW2017.html) in Palermo, Italy. You can view the slides [here](https://wtbarnes.github.io/loops-workshop-2017-talk/)

## Goal
Highlight observable differences between nanoflare heating models with different frequencies (if they exist) using EBTEL and a global active region model. We will primarily rely on the LOS emission measure distribution constructed from EIS line intensities and associated slopes for making determinations about the underlying heating frequency. We may also look at the time lags in each pixel of the entire active region as well as the measured line widths and doppler shifts (though these are secondary).

We want to try to understand two things: 1) what sort of observational signatures do different heating frequencies produce and 2) can these signatures be observed? In this talk, we'll tackle this question by looking at the emission measure slope though other diagnostics are possible.

## Outline
General talk overview
* Introduction
  * Problem: frequency of energy release in ARs unknown, may hold key to underlying heating mechanism(s)
  * Solution: use observables to try to constrain heating frequency
  * But: difficult to understand mapping between observed quantities and heating inputs
* Method
  * Loop hydrodynamics, specifically EBTEL (later HYDRAD) to model field-aligned plasma dynamics
  * Build up AR model from 1000 loops and map them to potential field skeleton
  * Synthesize emission and project along the LOS
  * Data products for SDO/AIA and Hinode/EIS
* Heating Model/Parameter Space
  * AR 9 from Warren et al. (NOAA 1109)
  * Use 4 (for now) different heating frequencies: 250, 750, 2500, 5000 s
  * Nanoflare energy distributed according to powerlaw of alpha=-2.5 and "charge-up time" depends linearly on event energy
* Emission Measure distribution 
  * Ground truth and inverted 
  * Per pixel per timestep
  * (**or** per pixel for time-averaged EM)
  * Look at distribution of EM slopes for each frequency for derived and "true"
  * What can these tell us?
  * Look at 1D EM distributions (true and inverted) for area highlighted by the Warren paper
* Other diagnostics--This is mostly just concluding stuff, only diagnostic I plan to talk about in depth is the EM slope
  * Doppler shifts and line widths
  * Time lag maps (a la Viall and Klimchuk 2017, in press)

## Slides
Details about what will go into each slide
