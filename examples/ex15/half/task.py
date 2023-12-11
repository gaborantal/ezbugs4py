def hossz_stat(text):
    lista=text.split(" ")
    length=0
    words=0
    longer=0
    for szo in lista:
        length= length+len(szo)
        words= words+1
    for word_ in lista:
        if int(length/words)< len(word_):
            longer=longer+1
    ret=[int(length/words), longer]
    return ret
