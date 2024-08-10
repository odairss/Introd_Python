# A função split_words recebe uma referência para um arquivo aberto
# e retorna uma lista de listas contendo as palavras de cada linha do arquivo:

def split_words(file):
    list_words = list()
    for line in file.readlines():
        list_words.append(line.split())
    return list_words

# A função strip_words recebe uma lista de listas de palavras
# e retorna essa mesma lista eliminando pontos e vírgulas contidos nas palavras:

def strip_words(listwords):
    words_cleared = list()
    for line in listwords:
        for word in line:
            line[line.index(word)] = word.strip('.').strip(',').lower()
        words_cleared.append(line)
    return words_cleared

# A função words_no_repeated recebe uma lista de listas de palavras
# e retorna uma lista simples eliminando palavras repetidas:

def words_no_repeated(wordscleared):
    wordsnorepeated = list()
    for line in wordscleared:
        for word in line:
            if word not in wordsnorepeated:
                wordsnorepeated.append(word)
    return wordsnorepeated

# A função fill_dict recebe uma lista de listas de palavras e retorna
# um dicionário onde as chaves são as palavras e os valores são as # linhas e as colunas das ocorrências dessas palavras:
            
def fill_dict(wordscleared):
    dict_words = dict()
    for line in wordscleared:
        start = 0
        for word in line:
            if word not in dict_words:
                dict_words[word] = list()
                n = 0
                while n < len(wordscleared):
                    dict_words[word].append(list())
                    n += 1
                dict_words[word][wordscleared.index(line)].append(line.index(word))
                start = line.index(word)+1
            else:
                dict_words[word][wordscleared.index(line)].append(line.index(word, start))
                start = line.index(word,start)+1
                
    return dict_words

# a função print_words recebe um dicionário e uma lista de palavras simples
# e imprime as linhas e as colunas das ocorrências dessas palavras:

def print_words(dictwords, listwords):
    all_occurrences = ''
    for word in listwords:
        word_occurrences = word.upper() + '\n'
        for occurrences_in_line in dictwords[word]:
            if len(occurrences_in_line) != 0:
                word_occurrences += f'Ocorrências na linha: {dictwords[word].index(occurrences_in_line)}: '
                for occurrence in occurrences_in_line:
                    word_occurrences += str(occurrence) + ', '
                all_occurrences += word_occurrences.strip(', ') + '\n'
    print(all_occurrences)
                    

# a função dict_factory recebe a referência a um arquivo aberto,
# e chamando as demais funções imprime a linha e as colunas das ocorrências dessas palavras
# no arquivo:

def dict_factory(file):
    list_words = split_words(file)
    words_cleared = strip_words(list_words)
    words = fill_dict(words_cleared)
    wordsnorepeated = words_no_repeated(words_cleared)
    print_words(words, wordsnorepeated)
