def compressed(data):
    listOfCode = {}
    data_comperssed = []
    i=0
    keyOfListCode=128
    while i<len(data):
        length_match=match(data,listOfCode,i);
        if length_match==1:
            data_comperssed.append(ord(data[i]))
            if data[i:length_match+1+i]not in listOfCode.keys() and i!=len(data)-1:
                listOfCode[data[i:length_match+1+i] ] = keyOfListCode
                keyOfListCode+=1
        else:
            data_comperssed.append(listOfCode[data[i:length_match+i]])
            if data[i:length_match+1+i]not in listOfCode.keys():
                listOfCode[data[i:length_match+1+i] ] = keyOfListCode
                keyOfListCode+=1
        i+=length_match
    return  data_comperssed



def match(data,listOfCode,i):
    index=i
    string_match= data[index]
    while True:
        if index+1<len(data):
            new_string=string_match+data[index+1]
            if new_string in listOfCode.keys():
                index+=1
                string_match+=data[index]
            else:
                break
        else:
            break
    return len(string_match)


print(compressed("ABAABABBAABAABAAAABABBBBBBBB"))

