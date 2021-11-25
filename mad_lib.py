import requests

URL = 'http://192.168.1.167:5000'


class MadLib:
    '''
    Stores all words used.
    '''

    def __init__(self):
        self.nouns = []

        self.pronouns = []

        self.verbs = []

        self.adjectives = []

        self.adverbs = []

    def add_nouns(self, number):
        self.nouns = self.nouns + \
            requests.get(F'{URL}/noun/{str(number)}').json()

    def get_noun(self):
        return self.nouns.pop()

    def add_pronouns(self, number):
        self.pronouns = self.pronouns + \
            requests.get(F'{URL}/pronoun/{str(number)}').json()

    def get_pronoun(self):
        return self.pronouns.pop()

    def add_verbs(self, number):
        self.verbs = self.verbs + \
            requests.get(F'{URL}/verb/{str(number)}').json()

    def get_verb(self):
        return self.verbs.pop()

    def add_adjectives(self, number):
        self.adjectives = self.adjectives + \
            requests.get(F'{URL}/adjective/{str(number)}').json()

    def get_adjective(self):
        return self.adjectives.pop()

    def add_adverbs(self, number):
        self.adverbs = self.adverbs + \
            requests.get(F'{URL}/adverb/{str(number)}').json()

    def get_adverb(self):
        return self.adverbs.pop()
