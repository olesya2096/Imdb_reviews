from django.apps import AppConfig
import html
import pathlib
import os
# from fast_bert.prediction import BertClassificationPredictor
from transformers import BertForSequenceClassification

class WebappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "my_bert"
    # MODEL_PATH = pathlib.Path("model")
    # LABEL_PATH = pathlib.Path("label/")
    # BERT_PRETRAINED_PATH = pathlib.Path("bert-base-uncased")

    # model = BertForSequenceClassification.from_pretrained(
    #     "bert-base-uncased",
    #     num_labels=8,
    #     output_attentions=False,
    #     output_hidden_states=False,
    # )
    model = BertForSequenceClassification.from_pretrained("/Users/o.moiseenko/Desktop/django/deploy/my_bert/model")




