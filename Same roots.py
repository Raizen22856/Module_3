def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        a = root_word
        b = other_words
        d = a.lower()
        c = [g.lower() for g in b]
        if d in c[i]:
            same_words.append(b[i])
        elif c[i] in d:
            same_words.append(b[i])
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)