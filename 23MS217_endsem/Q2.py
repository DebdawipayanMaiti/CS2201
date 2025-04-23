# Method:-1 not completed
# database of sentences
sentences = ['The paneer pasanda was simply awesome', 'I loved the aloo biriyani', 'paneeeeeeeeeer', 'Overall I liked the paneer pasanda although the texture and aroma have room for improvement', 'Superlike', 'Loved paneer pasanda', 'Paneer pasanda was not good']


# Function for splitting and lowering 
def preprocess(sentence):
    return sentence.lower().split()
# Function for making word context map.dictionary containing words and its words containg in that sentence
def build_contexts(sentences):
    word_contexts = {}  # word and its other words in sentence
    word_sentence_map = {}# word containing in sentence of index
    for idx, sentence in enumerate(sentences):
        words = preprocess(sentence)
        for word in words:
            if word in word_sentence_map:
                word_sentence_map[word].append(idx)
            else:
                word_sentence_map[word] = [idx]
    for word, indices in word_sentence_map.items():
        # Only include words that occur in exactly one sentence
        if len(indices) == 1:
            sent_idx = indices[0]
            words_in_sentence = set(preprocess(sentences[sent_idx]))
            context = words_in_sentence - {word}
            word_contexts[word] = context
    return word_sentence_map


positive = ['good', 'very good', 'awesome', 'liked', 'superliked', 'loved', 'yummy']
negative = ['bad', 'not good', 'disliked', 'tasteless', 'yucky']
good_review = 0
bad_review = 0

for i in build_contexts(sentences):
    if 
    

 
# print(build_contexts(sentences))

# Method:-2 (not completed)

check = input("Enter the prompt: ")
for i in range(len(dataset)):
    s = set(dataset[i].split(" "))
    if len(set)