from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import math
import os

import tensorflow as tf

from medium_show_and_tell_caption_generator.caption_generator import CaptionGenerator
from medium_show_and_tell_caption_generator.model import ShowAndTellModel
from medium_show_and_tell_caption_generator.vocabulary import Vocabulary

from medium_show_and_tell_caption_generator.find_caption import Find_caption
from medium_show_and_tell_caption_generator.bleu_score import BLEU_Score
from medium_show_and_tell_caption_generator.rogue_score import ROGUE_Score

FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_string("model_path", "C:/Users/Kavin Kumar/Documents/GitHub/Tutorial 6 Source Code/medium-show-and-tell-caption-generator-master/model/show-and-tell.pb", "Model graph def path")
tf.flags.DEFINE_string("vocab_file", "C:/Users/Kavin Kumar/Documents/GitHub/Tutorial 6 Source Code/medium-show-and-tell-caption-generator-master/etc/word_counts.txt", "Text file containing the vocabulary.")
tf.flags.DEFINE_string("input_files", "C:/Users/Kavin Kumar/Documents/GitHub/Tutorial 6 Source Code/medium-show-and-tell-caption-generator-master/data/filtered_data/*/*.jpg",
                       "File pattern or comma-separated list of file patterns "
                       "of image files.")

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def main(_):
    model = ShowAndTellModel(FLAGS.model_path)
    vocab = Vocabulary(FLAGS.vocab_file)
    filenames = _load_filenames()

    generator = CaptionGenerator(model, vocab)

    predicted_captions = []

    for filename in filenames:
        with tf.gfile.GFile(filename, "rb") as f:
            image = f.read()
        captions = generator.beam_search(image)

        # to find the actual captions
        find_caption_object = Find_caption()
        actual_captions = find_caption_object.find_caption(os.path.basename(filename))

        for i, caption in enumerate(captions):
            # Ignore begin and end tokens <S> and </S>.
            sentence = [vocab.id_to_token(w) for w in caption.sentence[1:-1]]
            sentence = " ".join(sentence)
            predicted_captions.append(sentence)
            print(sentence)

        BLEU_Score_object = BLEU_Score()
        BLEU_rate = BLEU_Score_object.find_bleu_score(predicted_captions, actual_captions)
        print("BLUE Score for image %s: %f" % (os.path.basename(filename), BLEU_rate))

        ROGUE_Score_object = ROGUE_Score()
        ROGUE_rate = ROGUE_Score_object.find_rogue_score(predicted_captions, actual_captions)
        print("ROGUE Score for image %s: %f" % (os.path.basename(filename), ROGUE_rate))

def _load_filenames():
    filenames = []
    for file_pattern in FLAGS.input_files.split(","):
        filenames.extend(tf.gfile.Glob(file_pattern))
    logger.info("Running caption generation on %d files matching %s",
                len(filenames), FLAGS.input_files)
    return filenames


if __name__ == "__main__":
    tf.app.run()
