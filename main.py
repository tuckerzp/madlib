#!/usr/bin/env python3

import sys

from mad_lib import MadLib

m = MadLib()

KEYS = [
    ("{noun}", m.get_noun, m.add_nouns),
    ("{pronoun}", m.get_pronoun, m.add_pronouns),
    ("{verb}", m.get_verb, m.add_verbs),
    ("{adjective}", m.get_adjective, m.add_adjectives),
    ("{adverb}", m.get_adverb, m.add_adverbs)
]


def replace_by_type(text, key, func):
    while (text.find(key) != -1):
        text = text.replace(key, func(), 1)
    return text


def parse_text(text):
    for i in range(len(KEYS)):
        text = replace_by_type(text, KEYS[i][0], KEYS[i][1])

    return text


def count_keys(text):
    for i in range(len(KEYS)):
        func = KEYS[i][2]
        func(text.count(KEYS[i][0]))


def main():
    text = sys.argv[1]

    count_keys(text)

    print(parse_text(text))


if __name__ == "__main__":
    main()
