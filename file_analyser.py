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


def read_sentiment(file):
    good_counter = 0
    bad_counter = 0
    f = open(file, 'r', encoding='utf-8')
    for word in f.read().split():
        w = word.lower()
        if w in good_words:
            good_counter += 1
        elif w in bad_words:
            bad_counter += 1
    f.close()
    result = good_counter/(good_counter+bad_counter)
    print("Good ratio: " + str(result))

    plt.figure()
    cd = {"Positive": good_counter, "Negative": bad_counter}
    plt.bar(range(len(cd)), list(cd.values()), align='center')
    plt.xticks(range(len(cd)), list(cd.keys()))
    plt.savefig("plt/plot" + str(file_number) + "v2.png", dpi=300)
    plt.close()

    res_file = open("res.txt", 'a+')
    res_file.write(str(result) + "\n")
    res_file.close()


good_words = ["good", "fine", "great", "nice", "cool", "awesome", "fine", "best", "health", "joy", "happy", "happiness"]
bad_words = ["bad", "wrong", "awful", "sick", "disease", "death", "morbid", "terrible", "fear", "anxiety", "scared",
             "worry", "worried", "cruel", "damage", "depressed", "fail", "greed", "guilty", "hideous", "hate",
             "jealous", "lose", "pain", "scary", "ugly", "threat", "vice", "stressful"]

for n in range(2007, 20000):
    file_number = n
    file_name = "src/" + str(file_number) + ".txt"
    if os.path.exists(file_name):
        print(file_name)
        read_sentiment(file_name)
