def alliteration(strseg: str):
    if isinstance(strseg, str):
        if(len(strseg)==0):
            return None
        str2= strseg.lower()
        str1=list()
        str1=str2.split(' ')
        print(str1[0][0])
        print(len(str1))
        if(len(str1)<2):
            return None
        elif(len(str1)==2):
            if(str1[0][0]==str1[1][0]):
                return 2
            else:
                return 1
    else:
        return None
