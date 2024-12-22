import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for filename in self.file_names:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    content = file.read().lower()

                    # Удаляем пунктуацию
                    content = content.translate(str.maketrans('', '', string.punctuation + ' -'))

                    # Разбиваем текст на слова
                    words = content.split()

                    # Добавляем в словарь
                    all_words[filename] = words
            except FileNotFoundError:
                all_words[filename] = []
                print(f"Файл {filename} не найден.")

        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word)

        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            result[name] = words.count(word)

        return result


finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
all_words = finder.get_all_words()
print(all_words)
positions = finder.find('искомое_слово')
print(positions)
counts = finder.count('искомое_слово')
print(counts)