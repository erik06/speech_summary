import requests
import bs4
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter


def main():
    url = "http://www.analytictech.com/mb021/mlk.htm"
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    p_elems = [element.text for element in soup.find_all("p")]
    speech = " ".join(p_elems)
    speech = speech.replace("mowing", "knowing")
    speech = re.sub("\s+", " ", speech)
    speech_edit = re.sub("[^a-zA-Z]", " ", speech)
    speech_edit = re.sub("\s+", " ", speech_edit)

    while True:
        max_words = input("Enter max words per sentence for summary: ")
        num_sents = input("Enter number of sentences for summary: ")
        if max_words.isdigit() and num_sents.isdigit():
            break
        else:
            print("\nInput must be whole numbers.\n")

    speech_edit_no_stop = remove_stop_words(speech_edit)
    word_freq = get_word_freq(speech_edit_no_stop)
    sent_scores = score_sentances(speech, word_freq, max_words)

    counts = Counter(sent_scores)
    summary = counts.most_common(int(num_sents))
    print("\nSUMMARY:")
    for i in summary:
        print(i[0])
