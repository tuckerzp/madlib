import sys

from mad_lib import MadLib


def parse_text(text):
    m = MadLib()
    o = []

    for t in text:
        if (t == "{noun}"):
            o.append(m.get_noun())
        elif (t == "{pronoun}"):
            o.append(m.get_pronoun())
        elif (t == "{verb}"):
            o.append(m.get_verb())
        elif (t == "{adjective}"):
            o.append(m.get_adjective())
        elif (t == "{adverb}"):
            o.append(m.get_adverb())
        else:
            o.append(t)

    return o


def main():
    text = sys.argv[1].split()

    print(text)
    parsed = parse_text(text)
    print(" ".join(parsed))


if __name__ == "__main__":
    main()
