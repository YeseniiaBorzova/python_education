"""Module with class representing Sentence and
help class SentenceIterator for iteration purposes """


class SentenceIterator:
    """Help class that responsible for iteration of the Sentence class"""
    def __init__(self, words):
        """Constructor"""
        self._words = words
        self._index = 0

    def __next__(self):
        """method responsible for loop iteration trough the object"""
        if self._index < len(self._words):
            result = self._words[self._index]
        else:
            raise StopIteration
        self._index += 1
        return result


class Sentence:
    """Class responsible for splitting a sentence into the words
    and sorting other special symbols"""
    def __init__(self, text: str):
        """Constructor"""
        self.words = []
        self.other_chars = []
        terminal_symbols = [".", "?", "!"]
        special_characters = ";:@#$%^&*()-+_=,<>/0123456789.?!"
        if text[-1] not in terminal_symbols:
            raise ValueError
        elif not isinstance(text, str):
            raise TypeError
        else:
            for symbol in text:
                if symbol in special_characters:
                    self.other_chars.append(symbol)
                    text = text.replace(symbol, '')
        self.words = text.split()

    def __repr__(self):
        """String representation of object"""
        return f"<Sentence(words={len(self.words)}, other chars={len(self.other_chars)})>"

    def __iter__(self):
        """Returns iterator object"""
        return SentenceIterator(self.words)

    def __getitem__(self, key):
        """Allows us to access words by index and use slicing"""
        if isinstance(key, slice):
            indices = range(*key.indices(len(self.words)))
            return [self.words[i] for i in indices]
        elif key > len(self.words) - 1:
            raise IndexError
        else:
            return self.words[key]

    def _words(self, i=0):
        """lazy iterator"""
        while i < len(self.words):
            yield print(self.words[i])
            i += 1


if __name__ == "__main__":
    sentence = Sentence("Hello,  ,,how 2is  ####your :day @sir?")
    print(sentence)
    print(sentence.words)
    print(sentence.other_chars)
    gen = Sentence("Hello,  ,,how 2is  ####your :day @sir?")._words()
    for word in sentence:
        print(word)
