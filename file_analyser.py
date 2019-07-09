import matplotlib.pyplot as plt
import os.path


def read_file(file):
    word_counter = 0
    wordcount = {}
    f = open(file, 'r', encoding='utf-8')
    for word in f.read().split():
        word_counter += 1
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for k, v in list(wordcount.items()):
        if v < int(word_counter/333):
            wordcount.pop(k)
    plt.figure()
    plt.bar(range(len(wordcount)), list(wordcount.values()), align='center')
    plt.xticks(range(len(wordcount)), list(wordcount.keys()), rotation='vertical')
    plt.savefig("plt/plot" + str(file_number) + ".png", dpi=300)
    plt.close()


for n in range(1, 16000):
    file_number = n
    file_name = "src/" + str(file_number) + ".txt"
    if os.path.exists(file_name):
        print(file_name)
        read_file(file_name)
