# SciDocFind - Faceted Ranked Retrieval of Scientific Research Papers

## Abstract
- This work proposes a novel approach for faceted retrieval of scientific research papers using the CSFCube dataset for evaluation. Given a query paper Q, a facet f ∈ {background, method, result} and a set of candidate papers {C1, C2,..., Cn}, the task is to rank candidate papers similar to Q with respect to the facet f. In particular we fine-tuned the SentBERT-PP model using the PARADE dataset and observed improvement in the performance metrics when the facet being searched for is result. Additionally we also fine-tuned the SPECTER and the Sci-NCL models using a subset of the HIC dataset. For the fine-tuned SPECTER model, we observed improvement in performance metrics when the facet being searched for is method.

## Paper 
- The link for the paper is available [here](https://github.com/jena-shreyas/ScidocFind/blob/main/Reports/SciDocFind-Faceted_Ranked_Retrieval_of_Scientific_Research_Papers.pdf.pdf). 

## Instructions
- [Final_baselines_inference.ipynb]
Run this python code after uploading CSFCube-master.zip*(connecting to GPU is optional but for faster inferences it's required) to get the evaluation metrics like R-Precsion, Precision@20, and others for all the baseline models. \
A total of 7 baselines are implemented which consists of 3 abstract level baselines and 4 sentence level baselines.


- [Final_finetune_inference.ipynb]
Run this python code after uploading CSFCube-master.zip*(connecting to GPU is optional but for faster inferences it's required) to get the evaluation metrics like R-Precsion, Precision@20, and others for all the finetuned models. Three models are finetuned where one is sentence level model and two are abstract level models.

- [Final_Sentbert_PP_finetune.ipynb]
Run all cells after uploading PARADE_dataset-main.zip*.

- [Final_specter_scincl_finetune.ipynb]
Run all cells after connecting to GPU for faster performance.

- [Final_Demo.ipynb]
Run all cells after uploading CSFCube-master.zip*.

- [SciRepEval_SciBERT_classifier.ipynb]
Run all cells after connecting to GPU for faster performance.

## Acknowledgments
A big shout out to [Soni Aditya Bharatbhai](https://github.com/adityasoni9998), [Likhith Reddy Morredigari](https://github.com/likhnic) and [Rishi Raj](https://github.com/rsh-raj) for the amazing work !!

[//]: #
[jena-shreyas]: <https://github.com/jena-shreyas>
   [Final_baselines_inference.ipynb]: <https://github.com/jena-shreyas/SciDocFind/blob/main/src/Final_baselines_inference.ipynb>
   [Final_finetune_inference.ipynb]: <https://github.com/jena-shreyas/SciDocFind/blob/main/src/Final_finetune_inference.ipynb>
   [Final_Sentbert_PP_finetune.ipynb]: <https://github.com/jena-shreyas/SciDocFind/blob/main/src/Final_Sentbert_PP_finetune.ipynb>
   [Final_specter_scincl_finetune.ipynb]: <https://github.com/jena-shreyas/SciDocFind/blob/main/src/Final_specter_scincl_finetune.ipynb>
   [Final_Demo.ipynb]: <https://github.com/jena-shreyas/SciDocFind/blob/main/src/Final_Demo.ipynb>
   [SciRepEval_SciBERT_classifier.ipynb]: <https://github.com/jena-shreyas/SciDocFind/blob/main/src/SciRepEval_SciBERT_classifier.ipynb]>
