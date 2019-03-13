from PyRouge.pyrouge import Rouge


class ROGUE_Score():

    def find_rogue_score(self, predicted_sentences, actual_sentences):
        r = Rouge()
        maximum = 0.0
        for actual_sentence in actual_sentences:
            for predicted_sentence in predicted_sentences:
                t = float(r.rouge_l([predicted_sentence], [actual_sentence])[0])
                if t > maximum:
                    maximum = r.rouge_l([predicted_sentence], [actual_sentence])[0]

        return maximum

