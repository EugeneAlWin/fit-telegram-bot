class Dictionary:
    def __init__(self, dictionary: dict):
        """Modification of the base class dict."""
        self.dictionary: dict = dictionary

    def pop(self, params: list[str]):
        for i in params:
            try:
                self.dictionary.pop(i)
            except KeyError:
                continue
        return self

    def clear(self):
        self.dictionary.clear()
        return self

    def update(self, updict: dict):
        self.dictionary.update(updict)
        return self

    def get_dictionary(self):
        return self.dictionary
