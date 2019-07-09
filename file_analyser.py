import matplotlib.pyplot as plt
import os.path
from collections import OrderedDict


def read_file(file):
    word_counter = 0
    wordcount = {}
    f = open(file, 'r', encoding='utf-8')
    for word in f.read().split():
        w = word.lower()
        word_counter += 1
        # lowercase the word
        if w not in wordcount:
            wordcount[w] = 1
        else:
            wordcount[w] += 1
    for k, v in list(wordcount.items()):
        if v < int(word_counter/333):
            wordcount.pop(k)
    plt.figure()
    sorted_wc = OrderedDict(sorted(wordcount.items(), key=lambda x: x[1], reverse=True))
    plt.bar(range(len(sorted_wc)), list(sorted_wc.values()), align='center')
    plt.xticks(range(len(sorted_wc)), list(sorted_wc.keys()), rotation='vertical')
    plt.savefig("plt/plot" + str(file_number) + ".png", dpi=300)
    plt.close()


for n in range(500, 16000):
    file_number = n
    file_name = "src/" + str(file_number) + ".txt"
    if os.path.exists(file_name):
        print(file_name)
        read_file(file_name)
