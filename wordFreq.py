import csv
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk import ngrams
from collections import Counter
import nltk
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
import re

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

banWords = ['also', 'back', 'even', 'get', 'help', 'know', 'let', 'like', 'make', 'need',
            'one', 'please', 'since', 'sure', 'though', 'told', 'want', 'would']

def preprocess(sentence):
    sentence = str(sentence)
    sentence = sentence.lower()
    sentence = sentence.replace('{html}',"")
    # print(len(sentence))
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', sentence)
    # print(len(cleantext))
    rem_url=re.sub(r'http\S+', ' ',cleantext)
    rem_num = re.sub('[0-9]+', ' ', rem_url)
    # print(len(rem_num))
    tokens = re.sub('[^A-Za-z0-9]+', ' ', rem_num)
    # print(len(tokens))
    word_tokens = word_tokenize(tokens)
    filtered_words = [w for w in word_tokens if len(w) > 2 if not w in stopwords.words('english')]
    filtered_words = [w for w in filtered_words if not w in banWords]
    # print(len(filtered_words))
    # stem_words=[stemmer.stem(w) for w in filtered_words]
    # lemma_words=[lemmatizer.lemmatize(w) for w in stem_words]
    return filtered_words

def word_frequency(data):
    filteredWords = preprocess(data)
    counted = Counter(filteredWords)
    counted_2 = Counter(ngrams(filteredWords,2))
    counted_3 = Counter(ngrams(filteredWords,3))
    word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
    word_pairs =pd.DataFrame(counted_2.items(),columns=['pairs','frequency']).sort_values(by='frequency',ascending=False)
    trigrams =pd.DataFrame(counted_3.items(),columns=['trigrams','frequency']).sort_values(by='frequency',ascending=False)
    return word_freq,word_pairs,trigrams

with open('otherNullPosts.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

newData = [item for sublist in data for item in sublist]

data1, data2, data3 = word_frequency(newData)

data1.to_pickle("other_data1.pkl")
data2.to_pickle("other_data2.pkl")
data3.to_pickle("other_data3.pkl")