import sys

from mad_lib import MadLib


def replace_by_type(text, key, func):
    while (text.find(key) != -1):
        text = text.replace(key, func(), 1)
    return text


def parse_text(text):
    m = MadLib()

    KEYS = [("{noun}", m.get_noun), ("{pronoun}", m.get_pronoun),
            ("{verb}", m.get_verb), ("{adjective}", m.get_adjective),
            ("{adverb}", m.get_adverb)]

    for i in range(len(KEYS)):
        text = replace_by_type(text, KEYS[i][0], KEYS[i][1])

    return text


def main():
    text = sys.argv[1]

    print(parse_text(text))


if __name__ == "__main__":
    main()
