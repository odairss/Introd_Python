def split_words(file):
    list_words = list()
    for line in file.readlines():
        list_words += line.split()
    return list_words

def strip_words(listwords):
    words_cleared = list()
    for word in listwords:
        words_cleared.append(word.strip('.').strip(',').lower())
    return words_cleared

def words_no_repeated(wordscleared):
    wordsnorepeated = list()
    for word in wordscleared:
        if word not in wordsnorepeated:
            wordsnorepeated.append(word)
    return wordsnorepeated

def fill_dict(words):
    dict_words = dict()
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    return dict_words

def print_words(dictwords, listwords):
    count = 1
    for word in listwords:
        print(str(count) + ' - ' + word + ': ' + str(dictwords[word]))
        count += 1
    
def dict_factory(file):
    list_words = split_words(file)
    words_cleared = strip_words(list_words)
    words = fill_dict(words_cleared)
    wordsnorepeated = words_no_repeated(words_cleared)
    print_words(words, wordsnorepeated)
