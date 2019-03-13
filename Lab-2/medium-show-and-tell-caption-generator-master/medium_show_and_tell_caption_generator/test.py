import nltk
import nltk.translate.bleu_score as bleu

import math
import numpy
import os

try:
  nltk.data.find('tokenizers/punkt')
except LookupError:
  nltk.download('punkt')


hyp = str('she read the book because she was interested in world history').split()
ref_a = str('she read the book because she was interested in world history').split()
ref_b = str('she was interested in world history because she read the book').split()

score_ref_a = bleu.sentence_bleu([ref_a], hyp)
print("Hyp and ref_a are the same: {}".format(score_ref_a))

score_ref_b = bleu.sentence_bleu([ref_b], hyp)
print("Hyp and ref_b are different: {}".format(score_ref_b))

score_ref_ab = bleu.sentence_bleu([ref_a, ref_b], hyp)
print("Hyp vs multiple refs: {}".format(score_ref_ab))