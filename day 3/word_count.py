def  words(wordstring):

    wordlist = wordstring.split()
    wordfreq = [wordlist.count(w) for w in wordlist]
    k = dict(list( zip(wordlist, wordfreq)))
    for key in k:
        if str(key).isdigit():
            k[int(key)]=k.pop(key)
    return k
#print(words('testing 1 2 testing'))


