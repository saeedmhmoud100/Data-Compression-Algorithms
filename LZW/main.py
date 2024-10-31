class LZW:
    def compressed_file(self,input_file='input.txt',output_file='output.txt'):
        compressed_data = self.compressed(open(input_file).read())
        with open(output_file, 'w') as f:
            f.write('[')
            for index in range(len(compressed_data)):
                (f.write(str(compressed_data[index])+',')) if index != len(compressed_data)-1 else f.write(str(compressed_data[index])+']')
    def decompressed_file(self,input_file='output.txt',output_file='secondOutPut.txt'):
        data = open(input_file).read()
        data = data.replace('[', '').replace(']', '').split(',')
        data = [int(item.strip()) for item in data]
        result=self.decompressed(data)
        with open(output_file, 'w') as f:
            f.write(result)
    def compressed(self,data):
        list_of_code = {}
        data_comperssed = []
        i=0
        value_of_list_code=128
        while i<len(data):
            length_match= self.match(data,list_of_code,i)
            if length_match==1:
                data_comperssed.append(ord(data[i]))
                if data[i:length_match+1+i]not in list_of_code.keys() and i!=len(data)-1:
                    list_of_code[data[i:length_match+1+i] ] = value_of_list_code
                    value_of_list_code+=1
            else:
                data_comperssed.append(list_of_code[data[i:length_match+i]])
                if data[i:length_match+1+i]not in list_of_code.keys():
                    list_of_code[data[i:length_match+1+i] ] = value_of_list_code
                    value_of_list_code+=1
            i+=length_match
        return  data_comperssed

    def match(self,data,list_of_code,i):
        index=i
        string_match= data[index]
        while True:
            if index+1<len(data):
                new_string=string_match+data[index+1]
                if new_string in list_of_code.keys():
                    index+=1
                    string_match+=data[index]
                else:
                    break
            else:
                break
        return len(string_match)

    def decompressed(self,compressed_data):
        list_of_code={}
        data=chr(compressed_data[0])
        i=1
        key_of_list_code=128
        while i<len(compressed_data):
            index=len(data)
            start=index-1 if compressed_data[i-1]<128 else index-len(list_of_code[compressed_data[i-1]])
            if compressed_data[i]<128:
                data+=chr(compressed_data[i])
                if  compressed_data[i-1]<128:
                    list_of_code,key_of_list_code=self.compare(data,list_of_code,key_of_list_code,start,index)
                else:
                    list_of_code,key_of_list_code=self.compare(data,list_of_code,key_of_list_code,start,index)

            elif compressed_data[i] not in list_of_code.keys():
                if compressed_data[i-1]<128:
                    data+=chr(compressed_data[i-1])+chr(compressed_data[i-1])
                    list_of_code,key_of_list_code=self.compare(data,list_of_code,key_of_list_code,start,index )
                else:
                    data+=list_of_code[compressed_data[i-1]]+list_of_code[compressed_data[i-1]][0]
                    list_of_code,key_of_list_code=self.compare(data,list_of_code,key_of_list_code,start,index)
            else:
                data+=list_of_code[compressed_data[i]]
                if compressed_data[i-1]<128:
                    list_of_code,key_of_list_code=self.compare(data,list_of_code,key_of_list_code,start,index)
                else:
                    list_of_code,key_of_list_code=self.compare(data,list_of_code,key_of_list_code,start,index)

            i+=1
        return data
    def compare(self,data,list_of_code,key_of_list_code,start,end):
        if data[start:end+1] not in list_of_code.values():
            list_of_code[key_of_list_code] = data[start:end+1]
            key_of_list_code+=1
        return list_of_code,key_of_list_code

def main():
    lzw=LZW()
    while True:
        choice=int(input("choose your operation : 1/compressed data 2/decompressed data 0/ exit\n"))
        if choice==0:break
        elif choice==1:
            lzw.compressed_file()
        elif choice==2:
            lzw.decompressed_file()



if __name__ == '__main__':
    main()
    # print(compressed("ABAABABBAABAABAAAABABBBBBBBB"))
    #                   ABAABABBAABAABAAAABABBBBBBBB
    # [65, 66, 65, 128, 128, 129, 131, 134, 130, 129, 66, 138, 139, 138]
