.. FigCapsHF documentation master file, created by
   sphinx-quickstart on Fri May 19 11:03:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Example Usage
===================================================================================================================

Download our dataset from <https://figshare.com/s/c034fd77bea9475319cb>

To reproduce our experiments using our helper functions, first clone and import the FigCaps module

.. code-block::

   git clone https://github.com/FigCapsHF/FigCapsHF
   from FigCapsHF import FigCapsHF
   FigCapsHF = FigCapsHF("path/to/benchmark/data")

To train a BLIP model with RLHF while choosing a human feedback factor

.. code-block::

   python train_blip.py --mixed_precision fp16 --hf_score_type helpfulness --benchmark_path XX/benchmark

To run inference on an image using a particular model

.. code-block::

   python inference.py --figure_path /path/test_image.png --model_path /path/model.pth


To visualize example from dataset

.. code-block::

   FigCapsHF.get_image_caption_pair(data_split = "train", image_name = "1001.0025v1-Figure5-1")


To visualize an example from the human annotated dataset and its associated annotations

.. code-block::

   FigCapsHF.get_image_caption_pair_hf(image_name = "1907.11521v1-Figure6-1")

To generate dataset like the experiment 
embedding_model can be 'BERT', 'SciBERT', 'MCSE', or 'BLIP'
hf_score_type can be 'helpfulness','ocr','takeaway' or 'visual'

.. code-block::

   inferred_hf_df = FigCapsHF.infer_hf_training_set(hf_score_type = "helpfulness", embedding_model = "BERT", max_num_samples = 100, quantization_levels = 3, mapped_hf_labels = ["Bad", "Neutral", "Good"])

To score a single user specified figure-caption pair 

.. code-block::

   hf_ds_embeddings, scores = FigCapsHF.generate_embeddings_hf_anno(hf_score_type = "helpfulness", embedding_model = "BERT")
   scoring_model = FigCapsHF.train_scoring_model(hf_ds_embeddings, scores)

   image_path = "/path/1907.11521v1-Figure6-1.png"
   caption = "the graph indicates the loss of the model over successive generations"

   embedding = FigCapsHF.generate_embeddings([image_path], [caption], embedding_model = "BERT")
   inferred_hf_score = scoring_model.predict(embedding)

