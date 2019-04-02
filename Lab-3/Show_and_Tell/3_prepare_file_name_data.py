import string


# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r', encoding="utf8")
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


# extract descriptions for images
def load_descriptions(doc):
    mapping = dict()
    filenames = []
    # process lines
    for line in doc.split('\n'):
        # split line by white space
        tokens = line.split()
        if len(line) < 2:
            continue
        # take the first token as the image id, the rest as the description
        image_id, image_desc = tokens[0], tokens[1:]
        # remove filename from image id
        image_id = image_id.split('.')[0] + '.jpg'
        filenames.append(image_id)
    return filenames


filename = 'data/sports_caption.txt'
# load descriptions
doc = load_doc(filename)
# parse descriptions
filenames = load_descriptions(doc)

filenames = list(set(filenames))

train_percentage = .15
dev_percentage = .20
test_percentage = .25

f1 = open('data/train_file_name.txt', 'w')
f2 = open('data/dev_file_name.txt', 'w')
f3 = open('data/test_file_name.txt', 'w')

for i in range(0,len(filenames)):

    if i < train_percentage * len(filenames):
        f1.write(filenames[i]+'\n')

    elif i < dev_percentage * len(filenames):
        f2.write(filenames[i]+'\n')

    elif i < test_percentage * len(filenames):
        f3.write(filenames[i] + '\n')