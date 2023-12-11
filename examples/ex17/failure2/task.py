def alliteration(text):
    if not isinstance(text,str):
        return None
    else:
        words = text.split(" ")
        if(len(words) <2):
            return None
        for word in words:
            if not isinstance(word,str):
                return None
        j = 1
        max = 1
        temp = 0
        while j < len(words):
            actual = words[j]
            previous = words[j-1]
            if actual[0].lower() == previous[0].lower():
                temp+=1
                if temp >= max:
                    max = temp+1
                else:
                    temp = 0
            j+=1
    return max
 