# referred to https://blog.csdn.net/qq_41667743/article/details/129627660

import random
import pandas as pd
from nltk.corpus import wordnet
stop_words=[]
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace("_", " ").lower()
            if synonym != word and synonym not in synonyms:
                synonyms.append(synonym)
    return synonyms

def synonym_replacement(sentence, n=1):
    words = sentence.split()
    words = [ i if i!= 'http' else '_http_' for i in words]
    words = [ i if i!= '@user' else '_@user_' for i in words]
    new_words = words.copy()
    random_word_list = list(set([word for word in words if word not in stop_words]))
    random.shuffle(random_word_list)
    num_replaced = 0
    for i in range(1):
        for random_word in random_word_list:
            synonyms = get_synonyms(random_word)
            if len(synonyms) >= 1:
                synonym = random.choice(synonyms)
                new_words = [synonym if word == random_word else word for word in new_words]
                num_replaced += 1
            if num_replaced >= n:
                break
        new_words = [ i if i!= '_http_' else 'http' for i in new_words]
        new_words = [ i if i!= '_@user_' else '@user' for i in new_words]
        new_sentence = ' '.join(new_words)
        # if len(words) == len(new_sentence.split()):
        #     break
    return new_sentence

print(synonym_replacement('Ramallah 🐒 : @user http'))

