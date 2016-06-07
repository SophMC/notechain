from collections import Counter
import re


def word_count(phrase):
    return Counter(re.findall(r"[\w]+", phrase.lower().replace('_', ' ')))