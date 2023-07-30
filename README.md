# Imdb_reviews

Была поставлена задача классификации 25000 отзывов на классы 1, 2, 3, 4, 7, 8, 9, 10, ассоциированные с оценкой фильма пользователями, на основе "Large Movie Review Dataset v1.0".

Представлены три блокнота решений данной задачи. 

В блокноте "bert_greenatom_2classes.ipynb" обучена модель разделения отзывов на негативные и позитивные, в "bert_greenatom_4classes.ipynb" - на классификацию отзывов на 4 группы, где 1 класс - отзывы с оценкой 1 или 2, 2 класс - с оценкой 3 или 4, 3 класс - 7 или 8, 4 класс - 9 или 10. Последний ноутбук "bert_greenatom_8classes.ipynb" содержит решение поставленной задачи, то есть классификацию отзывов на 10 классов за исключением нейтральных. Во всех случаях для решения задачи классификации использовалась трансформенная модель.

В блокноте "bag_of_words.ipynb" решается поставленная задача с применением Tfidfvectorizer, LabelPropagation из sklearn.semi_supervised и модели градиентного бустинга.

Подробное описание датасета представлено далее.
Large Movie Review Dataset v1.0

Overview

This dataset contains movie reviews along with their associated binary
sentiment polarity labels. It is intended to serve as a benchmark for
sentiment classification. This document outlines how the dataset was
gathered, and how to use the files provided. 

Dataset 

The core dataset contains 50,000 reviews split evenly into 25k train
and 25k test sets. The overall distribution of labels is balanced (25k
pos and 25k neg). We also include an additional 50,000 unlabeled
documents for unsupervised learning. 

In the entire collection, no more than 30 reviews are allowed for any
given movie because reviews for the same movie tend to have correlated
ratings. Further, the train and test sets contain a disjoint set of
movies, so no significant performance is obtained by memorizing
movie-unique terms and their associated with observed labels.  In the
labeled train/test sets, a negative review has a score <= 4 out of 10,
and a positive review has a score >= 7 out of 10. Thus reviews with
more neutral ratings are not included in the train/test sets. In the
unsupervised set, reviews of any rating are included and there are an
even number of reviews > 5 and <= 5.
