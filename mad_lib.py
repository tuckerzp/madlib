class MadLib:
    '''
    Stores all words used.
    '''

    def __init__(self):
        # generate a list of nouns.
        self.nouns = [
            "man", "woman", "teacher", "John", "Mary",
            "home", "office", "town", "countryside", "America"
        ]

        # generate a list of pronouns.
        self.pronouns = [
            "anybody", "anyone", "anything", "each", "either", "everybody", "everyone",
            "everything", "neither", "nobody", "no one", "nothing", "one", "somebody", "someone", "something"
        ]

        # generate a list of verbs.
        self.verbs = [
            "question", "add", "itch", "reach", "allow", "jog", "rinse", "bake", "jump",
            "run", "bang", "scatter", "call", "kick", "stay", "chase", "knit"
        ]

        # generate a list of adjectives.
        self.adjectives = [
            "abundant", "delightful", "high", "nutritious", "square", "adorable",
            "dirty", "hollow", "obedient", "steep", "agreeable", "drab", "hot",
            "obnoxious", "sticky"
        ]

        # generate a list of adverbs.
        self.adverbs = [
            "actually", "famously", "jaggedly", "perfectly", "smoothly", "almost",
            "far", "jealously", "playfully", "softly", "always", "fast", "joyfully",
            "politely", "solidly"
        ]

    def get_noun(self):
        return self.nouns.pop()

    def get_pronoun(self):
        return self.nouns.pop()

    def get_verb(self):
        return self.verbs.pop()

    def get_adjective(self):
        return self.adjectives.pop()

    def get_adverb(self):
        return self.adverbs.pop()
