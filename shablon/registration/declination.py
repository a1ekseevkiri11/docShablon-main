import pymorphy2

def get_word_genitive(word, inflect):
    morph = pymorphy2.MorphAnalyzer()
    parsed_word = morph.parse(word)[0]
    gent = parsed_word.inflect({inflect})
    print(inflect, " " ,gent)

    if gent:
        return gent.word
    else:
        return word


def get_str_genitive(str, inflect):
    words = str.split()
    genitive_words = []
    for word in words:
        genitive_word = get_word_genitive(word, inflect)
        if word[0].isupper():
            genitive_word = genitive_word.capitalize()
        else:
            genitive_word = genitive_word.lower()
        genitive_words.append(genitive_word)
    return ' '.join(genitive_words)

