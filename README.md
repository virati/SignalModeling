# SignalModeling
Signal modeling in the context of neuroscience (lots of notebooks)
Interact with the notebooks here: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/virati/signalmodeling)

## Overview
This is a repo for various signal modeling exercises. Let me know if anything is helpful or unclear and I'll do my best to extend/fix it!

## Introduction
**Signal Modeling** is, in my view, the first step before dynamical modeling. We have to know something about the measurement process, how it reflects and/or warps the underlying generative process, before we can actually get at the underlying generative process.

A quick example:

When we do a fourier transform, we have an implicit signal model - bandlimited. When that signal model's assumptions are broken, we see things like "aliasing". Check out [This notebook]() for a hands on exercise with this idea.
Nothing about the fourier transform takes into account the generative processes that give rise to the signal. That's *the next step*. If we know we're dealing with a mechanical oscillator, that tells us, very quickly, that we're limited in our frequencies, in the context of our measurement modality.

Etc. etc. (more to come!)
