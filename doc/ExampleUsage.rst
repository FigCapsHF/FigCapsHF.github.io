.. FigCapsHF documentation master file, created by
   sphinx-quickstart on Fri May 19 11:03:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Example Usage
===================================================================================================================
This is an example of fine-tuning a ViT+GPT2 model for Figure-Captioning, using HuggingFace, on our RLHF dataset.

First, we download the dataset and dependencies, and clone our `repo <https://github.com/rayt98/RLHF>`_ for helper functions

.. code-block:: 

   pip install --upgrade pip
   git clone https://github.com/rayt98/RLHF.git
   pip install -r requirements.txt
   cd RLHF
   wget https://figshare.com/ndownloader/files/40317607 -O dataset.zip
   unzip dataset.zip
   mv "metadata.jsonl" "benchmark/No-Subfig-Img/train"

Second, we can train the model using HuggingFace 

.. code-block::

   python train.py

Third, we can perform inference to generate a caption for a scientific figure

.. code-block::
   
   python inference.py PATH/TO/YOUR/sample.png

