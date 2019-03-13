from nltk.translate.bleu_score import corpus_bleu

class BLEU_Score():

    def find_bleu_score(self, predicted_sentences, actual_sentences):
        maximum = 0.0
        for actual_sentence in actual_sentences:
            if maximum < corpus_bleu([predicted_sentences], [actual_sentence]):
                maximum = corpus_bleu([predicted_sentences], [actual_sentence])
        return maximum

