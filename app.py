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
    speech = "".join(p_elems)
