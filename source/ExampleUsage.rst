.. FigCapsHF documentation master file, created by
   sphinx-quickstart on Fri May 19 11:03:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Example Usage
===================================================================================================================

Download the dataset from <https://figshare.com/ndownloader/files/40317607>

.. code-block::

   wget https://figshare.com/ndownloader/files/40317607 -O dataset.zip
   unzip dataset.zip

To use our helper functions, first download and import the FigCaps module

.. code-block::

   #To-do : change link to module 
   git clone https://github.com/FigCapsHF/FigCaps
   from FigCapsHF import FigCapsHF
   FigCapsHF = FigCapsHF("path/to/benchmark/data")

To visualize example from dataset

.. code-block::

   data_split = "train"
   image_name = "1001.0025v1-Figure5-1"
   FigCapsHF.get_image_caption_pair(data_split, image_name)


To visualize an example from the human annotated dataset and its associated annotations

.. code-block::

   image_name = "1907.11521v1-Figure6-1"
   FigCapsHF.get_image_caption_pair_hf(image_name)

To generate dataset like the experiment 

.. code-block::

   hf_score_type = "helpfulness"
   model_name = "BERT"
   MCSE_path = None
   max_num_samples = 100 
   quantization_levels = 5
   mapped_hf_labels = ["Very#Want to generate dataset like the experiment 
   Bad", "Bad", "Neutral", "Good", "Very Good"]

   result_df = FigCapsHF.infer_hf_training_set(hf_score_type, model_name, MCSE_path, max_num_samples, quantization_levels, mapped_hf_labels)

To score a single user specified figure-caption pair 

.. code-block::

   hf_ds_embeddings, scores = FigCapsHF.generate_embeddings_hf_anno(hf_score_type,model_name, MCSE_path = MCSE_path)
   scoring_model = FigCapsHF.train_scoring_model(hf_ds_embeddings,scores)
   image_path = "/Users/prateekagarwal/Desktop/Benchmark/No-Subfig-Img/train/1907.11521v1-Figure6-1.png"
   caption = "the graph indicates the loss of the model over successive generations"
   model_name = "BERT"
   embedding = FigCapsHF.generate_embeddings([image_path], [caption], model_name)
   inferred_hf_score = scoring_model.predict(embedding)



.. This is an example of fine-tuning a BLIP model for Figure-Captioning, using HuggingFace's Dataset Class, on our RLHF dataset.

.. First, we download the dataset and dependencies, and clone our `repo <https://github.com/rayt98/RLHF>`_ for helper functions


..    pip install --upgrade pip
..    git clone https://github.com/FigCapsHF/FigCaps.git
..    cd RLHF
..    pip install -r requirements.txt
..    wget https://figshare.com/ndownloader/files/40317607 -O dataset.zip
..    unzip dataset.zip
..    ./cp.sh

.. Here we are using BLIP as a sample model for training using Pytorch's native DataLoader library combined with Huggingface's dataset class. User can provide arguments for their desired functionality as shown in the script below. To change the the number of epochs and learning rate, modify config variable in train_blip.py.


..    python train_blip.py --f16 --output_dir output
   
   
.. (after downloading and setting up the dataset) To predict a scientific caption from an scientific image

..    ./pred.sh
..    cd BLIP

.. Use this `link <https://drive.google.com/file/d/1FZh95Xeyt3RlaYs_TeeiiSPwYvAuGogQ/view?usp=share_link>`_ to download our pre-trained model, and place it under directory BLIP, and use the following script to do an inference on the sample.png


..    python inference.py sample.png
   