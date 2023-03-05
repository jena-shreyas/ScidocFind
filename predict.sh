allennlp predict \
    /path/to/model.tar.gz \
    data/CSAbstruct/test.jsonl \
    --include-package sequential_sentence_classification \
    --predictor SeqClassificationPredictor
