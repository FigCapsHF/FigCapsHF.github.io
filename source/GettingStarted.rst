.. Figure-Captioning with Human Feedback (FigCapsHF) documentation master file, created by
   sphinx-quickstart on Fri May 19 11:03:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Retrieving the dataset
===================================================================================================================

The benchmark dataset can be downloaded from `here <https://figshare.com/ndownloader/files/41222934>`_ manually or by running the following commands

.. code-block:: 

   wget  https://figshare.com/ndownloader/files/41222934 -O benchmark.zip
   unzip benchmark.zip


The directory structure is 

.. code-block:: 

  benchmark
  ├── arxiv-metadata-oai-snapshot.json
  ├── human-feedback.csv 
  ├── Caption-All
  │   ├── test
  │   ├── train
  │   └── val
  ├── List-of-Files-for-Each-Experiment
  │   ├── Caption-No-More-Than-100-Tokens
  │   ├── First-Sentence
  │   └── Single-Sentence-Caption
  ├── No-Subfig-Img
  │   ├── test
  │   ├── train
  │   └── val       
  ├── README.md  

