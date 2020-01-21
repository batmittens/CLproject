import random
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

my_file = open("ftales.txt")
text = my_file.read()
my_file.close()
bigram_vectorizer = CountVectorizer(ngram_range=(2,3),
                                    token_pattern=r'[A-Za-z]+', min_df=1)
analyze = bigram_vectorizer.build_analyzer()
z = analyze(text)
Counter(z).most_common()
new_lst = []
letter = input('Введите букву: ').lower()

for word in z:
    if word.lower().startswith(letter):
        if not word[-1].isalpha():
            word = word[:-1]
        new_lst.append(word)
new_list = []
for x in new_lst:
    if x not in new_list:
        new_list.append(x)
sentence = ''
for x in range(3):
    sentence = sentence + " " + random.choice(new_list)
print(sentence)
print(new_list)