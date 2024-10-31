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


# print(compressed("ABAABABBAABAABAAAABABBBBBBBB"))
#                   ABAABABBAABAABAAAABABBBBBBBB
# [65, 66, 65, 128, 128, 129, 131, 134, 130, 129, 66, 138, 139, 138]

def decompressed(compressedData):
    listOfCode={}
    data=""
    i=0
    keyOfListCode=128
    index=0
    while i<len(compressedData):
        index=len(data)
        if compressedData[i]<128:
            data+=chr(compressedData[i])
            if i!=0 and compressedData[i-1]<128:
                if data[index-1:1+index]not in listOfCode.values()  :
                    listOfCode[keyOfListCode] = data[index-1:1+index]
                    keyOfListCode+=1
            elif i!=0:
                if data[index-len(listOfCode[compressedData[i-1]]):1+index]not in listOfCode.values()  :
                    listOfCode[keyOfListCode] = data[index-len(listOfCode[compressedData[i-1]]):1+index]
                    keyOfListCode+=1

        elif compressedData[i] not in listOfCode.keys():
            if compressedData[i-1]<128:
                data+=chr(compressedData[i-1])+chr(compressedData[i-1])
                if data[index - 1:1 + index] not in listOfCode.values() :
                    listOfCode[keyOfListCode] = data[index - 1:index + 1]
                    keyOfListCode+=1
            else:
                data+=listOfCode[compressedData[i-1]]+listOfCode[compressedData[i-1]][0]
                if data[index - (len(listOfCode[compressedData[i-1]])):index + 1] not in listOfCode.values() :

                    listOfCode[keyOfListCode] = data[index - (len(listOfCode[compressedData[i-1]])):index + 1]
                    keyOfListCode+=1
        else:
            data+=listOfCode[compressedData[i]]
            if compressedData[i-1]<128:
                if data[index-1:index+1] not in listOfCode.values()  :
                    listOfCode[keyOfListCode]=data[index-1:index+1]
                    keyOfListCode += 1
            else:
                if data[index-len(listOfCode[compressedData[i-1]]):index+1] not in listOfCode.values() :
                    listOfCode[keyOfListCode]=data[index-(len(listOfCode[compressedData[i-1]])):index+1]
                    keyOfListCode += 1

        i+=1
    return data
# print(compressed("sobhi mohamed sobhi"))
print(decompressed([115, 111, 98, 104, 105, 32, 109, 111, 104, 97, 109, 101, 100, 32, 128, 130, 105]))
