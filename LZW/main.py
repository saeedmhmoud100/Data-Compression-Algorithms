class LZW:
    def compressed(self,data):
        listOfCode = {}
        data_comperssed = []
        i=0
        valueOfListCode=128
        while i<len(data):
            length_match= self.match(data,listOfCode,i);
            if length_match==1:
                data_comperssed.append(ord(data[i]))
                if data[i:length_match+1+i]not in listOfCode.keys() and i!=len(data)-1:
                    listOfCode[data[i:length_match+1+i] ] = valueOfListCode
                    valueOfListCode+=1
            else:
                data_comperssed.append(listOfCode[data[i:length_match+i]])
                if data[i:length_match+1+i]not in listOfCode.keys():
                    listOfCode[data[i:length_match+1+i] ] = valueOfListCode
                    valueOfListCode+=1
            i+=length_match
        return  data_comperssed



    def match(self,data,listOfCode,i):
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

    def decompressed(self,compressedData):
        listOfCode={}
        data=chr(compressedData[0])
        i=1
        keyOfListCode=128
        while i<len(compressedData):
            index=len(data)
            start=index-1 if compressedData[i-1]<128 else index-len(listOfCode[compressedData[i-1]])
            if compressedData[i]<128:
                data+=chr(compressedData[i])
                if  compressedData[i-1]<128:
                    listOfCode,keyOfListCode=self.compare(data,listOfCode,keyOfListCode,start,index)
                else:
                    listOfCode,keyOfListCode=self.compare(data,listOfCode,keyOfListCode,start,index)

            elif compressedData[i] not in listOfCode.keys():
                if compressedData[i-1]<128:
                    data+=chr(compressedData[i-1])+chr(compressedData[i-1])
                    listOfCode,keyOfListCode=self.compare(data,listOfCode,keyOfListCode,start,index )
                else:
                    data+=listOfCode[compressedData[i-1]]+listOfCode[compressedData[i-1]][0]
                    listOfCode,keyOfListCode=self.compare(data,listOfCode,keyOfListCode,start,index)
            else:
                data+=listOfCode[compressedData[i]]
                if compressedData[i-1]<128:
                    listOfCode,keyOfListCode=self.compare(data,listOfCode,keyOfListCode,start,index)
                else:
                    listOfCode,keyOfListCode=self.compare(data,listOfCode,keyOfListCode,start,index)

            i+=1
        return data
    def compare(self,data,listOfCode,keyOfListCode,start,end):
        if data[start:end+1] not in listOfCode.values():
            listOfCode[keyOfListCode] = data[start:end+1]
            keyOfListCode+=1
        return listOfCode,keyOfListCode

def main():
    Lzw=LZW();
    while True:
        choice=int(input("choose your operation : 1/compressed data 2/decompressed data 0/ exit"))
        if choice==0:break
        elif choice==1:
            data = input("enter your data to compress it : ")
            print(Lzw.compressed(data))
        elif choice==2:
            data = input("Enter your data to decompress it: ")
            data = data.replace('[', '').replace(']', '').split(',')
            data = [int(item.strip()) for item in data]
            print(Lzw.decompressed(data))


if __name__ == '__main__':
    main()
