.. FigCapsHF documentation master file, created by
   sphinx-quickstart on Fri May 19 11:03:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Example Usage
===================================================================================================================

Installation 
-------------------------------------------------------------------------------------------------------------------

Install the required requirements, clone the repository, and download the benchmark dataset.

.. code-block::

   pip install --upgrade pip
   git clone https://github.com/FigCapsHF/FigCapsHF
   pip install -r requirements.txt
   wget  https://figshare.com/ndownloader/files/41222934 -O benchmark.zip
   unzip benchmark.zip

Import the FigCaps module

.. code-block::

   from FigCapsHF import FigCapsHF
   FigCapsHF = FigCapsHF("path/to/benchmark/data")

RLHF Fine-tuning
-------------------------------------------------------------------------------------------------------------------

To train a BLIP model with RLHF while choosing a human feedback factor

.. code-block::

   #Code edits to implement a baseline are also included in train_blip.py
   #If training on CPU, add "--cpu" flag.
   python train_blip.py --mixed_precision fp16 --hf_score_type helpfulness --benchmark_path XX/benchmark

Inference
-------------------------------------------------------------------------------------------------------------------
Our RLHF Fine-tuned BLIP Model can be downloaded `here <https://drive.google.com/file/d/1BtyBkk9bZeruzjttMAzWlTDnJCzLlmpc/view?usp=share_link>`_

To generate caption for a single image

.. code-block::

   python inference.py --figure_path /path/sample.png --model_path /path/model.pth

To generate evaluation metrics on the test dataset
   
.. code-block::   

   python test_blip.py --benchmark_path /path/benchmark --model_path /path/model.pth

Visualization
-------------------------------------------------------------------------------------------------------------------

To visualize example from dataset

.. code-block::

   FigCapsHF.get_image_caption_pair(data_split = "train", image_name = "1001.0025v1-Figure5-1")


To visualize an example from the human annotated dataset and its associated annotations

.. code-block::

   FigCapsHF.get_image_caption_pair_hf(image_name = "1907.11521v1-Figure6-1")

Human Feedback Generation
-------------------------------------------------------------------------------------------------------------------

To generate human-feedback metadata for the dataset
embedding_model can be 'BERT', 'SciBERT', 'MCSE', or 'BLIP'
hf_score_type can be 'helpfulness','ocr','takeaway' or 'visual'

.. code-block::

   inferred_hf_df = FigCapsHF.infer_hf_training_set(hf_score_type = "helpfulness", embedding_model = "BERT", max_num_samples = 100, quantization_levels = 3, mapped_hf_labels = ["Bad", "Neutral", "Good"])

To generate a human-feedback score for a single figure-caption pair

.. code-block::

   hf_ds_embeddings, scores = FigCapsHF.generate_embeddings_hf_anno(hf_score_type = "helpfulness", embedding_model = "BERT")
   scoring_model = FigCapsHF.train_scoring_model(hf_ds_embeddings, scores)

   image_path = "/path/sample.png"
   caption = "the graph indicates the loss of the model over successive generations"

   embedding = FigCapsHF.generate_embeddings([image_path], [caption], embedding_model = "BERT")
   inferred_hf_score = scoring_model.predict(embedding)

