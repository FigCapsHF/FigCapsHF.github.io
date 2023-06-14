.. Figure-Captioning with Human Feedback (FigCapsHF) documentation master file, created by
   sphinx-quickstart on Fri May 19 11:03:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the documentation for Figure-Captioning with Human Feedback benchmark dataset!
===================================================================================================================

To enable the generation of high-quality figure captions, we introduce **FigCaps-HF**, a new framework for figure-caption generation that can incorporate domain expert feedback in generating captions optimized for reader preferences. 
Our framework comprises of 1) an automatic method for evaluating quality of figure-caption pairs, 2) a novel reinforcement learning with human feedback (RLHF) method to optimize a generative figure-to-caption model for reader preferences.

We release a large-scale benchmark dataset with human feedback on figure-caption pairs to enable further evaluation and development of RLHF techniques for this problem.

Contents
===================================================================================================================
.. toctree::
   :maxdepth: 1

   GettingStarted
   ExampleUsage
   api_doc
