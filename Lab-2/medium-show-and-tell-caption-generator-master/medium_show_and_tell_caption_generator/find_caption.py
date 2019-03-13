import re


class Find_caption():

    def find_caption(self, file_name):
        captions = []
        with open(
                "C:/Users/Kavin Kumar/Documents/GitHub/Tutorial 6 Source Code/medium-show-and-tell-caption-generator-master/data/caption.token",
                encoding="utf8") as search:
            pattern = re.compile(file_name)
            for line in search:
                line = line.rstrip()
                if pattern.match(line) != None:
                    line = re.sub('[0-9]+.jpg#[0-9]\t', '', line)
                    captions.append(line)

        return captions