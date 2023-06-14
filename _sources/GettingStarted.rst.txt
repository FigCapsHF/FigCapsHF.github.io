.. Figure-Captioning with Human Feedback (FigCapsHF) documentation master file, created by
   sphinx-quickstart on Fri May 19 11:03:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Retrieving the dataset
===================================================================================================================

The benchmark dataset can be downloaded from `here <https://figshare.com/ndownloader/files/41222934>`_ (8.34 GB) manually or by running the following commands

.. code-block:: 

   wget  https://figshare.com/ndownloader/files/41222934 -O benchmark.zip
   unzip benchmark.zip


The directory structure is 

.. code-block:: 

   ├── No-Subfig-Img                       #contains figure-image files for each split of the dataset
   │	├── Train
   │	├── Val
   │	└── Test
   ├── Caption-All                         #contains corresponding figure-captions and (precomputed) inferred human-feedback metadata
   │	├── Train
   │	├── Val
   │	└── Test
   ├── human-feedback.csv                  #contains human evaluations of a subset of figure image-caption pairs
   ├── arxiv-metadata-oai-snapshot.json    #arXiv paper metadata (from arXiv dataset) 
   └── List-of-Files-for-Each-Experiments  #list of figure names used in each experiment 
      ├── Single-Sentence-Caption
      │   ├── No-Subfig
      │   │   ├── Train
      │	│   ├── Val
      │	│   └── Test
      │	└── Yes-Subfig
      │       ├── Train
      │       ├── Val
      │       └── Test
      ├── First-Sentence                  #Same as in Single-Sentence-Caption
      └── Caption-No-More-Than-100-Tokens #Same as in Single-Sentence-Caption

