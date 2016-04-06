import sys
from string import punctuation


def get_words(filename):
    f = open(filename, encoding='utf-8')
    word_count = {}
    for word in f.read().lower().split():
        word = word.strip(punctuation + ' ')
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


def print_words(filename):
    words = get_words(filename)
    for word, count in sorted(words.items(), key=lambda x: x[1], reverse=True):
        print('{:20} {:5}'.format(word, count))


def main():
    if len(sys.argv) != 2:
        print('Usage: python wordcount.py <file>')
        sys.exit(1)
    filename = sys.argv[1]
    print_words(filename)


if __name__ == '__main__':
    main()
