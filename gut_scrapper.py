import urllib.request
import urllib.error
from shutil import copyfile

for n in range(16037, 100000):
    gutenberg_url = "http://www.gutenberg.org/cache/epub/" + str(n) + "/pg" + str(n) + ".txt"

    print(gutenberg_url)

    tmp_name = "src/temp.txt"
    file_name = "src/" + str(n) + ".txt"

    try:
        urllib.request.urlretrieve(gutenberg_url, tmp_name)
        print("Downloading " + file_name)

        with open(tmp_name, encoding="latin-1") as datafile:
            if 'Language: English' in datafile.read():
                copyfile(tmp_name, file_name)
                print("Successfully saved " + file_name)
    except urllib.error.HTTPError as err:
        print(err.code)
