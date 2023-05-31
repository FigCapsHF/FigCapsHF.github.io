.. FigCapsHF documentation master file, created by
   sphinx-quickstart on Fri May 19 11:03:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Example Usage
===================================================================================================================
This is an example of fine-tuning a BLIP model for Figure-Captioning, using HuggingFace's Dataset Class, on our RLHF dataset.

First, we download the dataset and dependencies, and clone our `repo <https://github.com/rayt98/RLHF>`_ for helper functions

.. code-block:: 

   pip install --upgrade pip
   git clone https://github.com/TODO/RLHF.git
   cd RLHF
   pip install -r requirements.txt
   wget https://figshare.com/ndownloader/files/40317607 -O dataset.zip
   unzip dataset.zip
   ./cp.sh

Here we are using BLIP as a sample model for training using Pytorch's native DataLoader library combined with Huggingface's dataset class. User can provide arguments for their desired functionality as shown in the script below. To change the the number of epochs and learning rate, modify config variable in train_blip.py.

.. code-block::

   python train_blip.py --f16 --output_dir output
   
   
（after downloading and setting up the dataset) To predict a scientific caption from an scientific image
.. code-block::
   ./pred.sh
   cd BLIP

Use this `link <https://drive.google.com/file/d/1FZh95Xeyt3RlaYs_TeeiiSPwYvAuGogQ/view?usp=share_link>`_ to download our pre-trained model, and place it under directory BLIP, and use the following script to do an inference on the sample.png

.. code-block::   
   python inference.py sample.png
   
If running on a CPU, the expected inference result on the sample.png is [the results of comparing oa and noa in terms of mean of error.] (on seed 42)

