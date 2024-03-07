def split_words(file):
    list_words = list()
    for line in file.readlines():
        list_words.append(line.split())
    return list_words

def strip_words(listwords):
    words_cleared = list()
    for line in listwords:
        for word in line:
            line[line.index(word)] = word.strip('.').strip(',').lower()
        words_cleared.append(line)
    return words_cleared

def words_no_repeated(wordscleared):
    wordsnorepeated = list()
    for line in wordscleared:
        for word in line:
            if word not in wordsnorepeated:
                wordsnorepeated.append(word)
    return wordsnorepeated

def fill_dict(wordscleared):
    dict_words = dict()
    count = 0
    for line in wordscleared:
        for wordcleared in line:
            if wordcleared not in dict_words:
                dict_words[wordcleared] = [count, line.index(wordcleared), 1]
            else:
                dict_words[wordcleared][2] += 1
        count += 1
    return dict_words

def print_words(dictwords, listwords):
    count = 1
    print('Nº  |    PALAVRA    | LINHA | COLUNA | OCORRÊNCIAS ')
    print('-'*51)
    for word in listwords:
        print(str(count).center(3) + ' |' + word.center(15) + '|' + str(dictwords[word][0]).center(7) + '|' + str(dictwords[word][1]).center(8) + '|' + str(dictwords[word][2]).center(13))
        count += 1
    
def dict_factory(file):
    list_words = split_words(file)
    words_cleared = strip_words(list_words)
    words = fill_dict(words_cleared)
    wordsnorepeated = words_no_repeated(words_cleared)
    print_words(words, wordsnorepeated)
