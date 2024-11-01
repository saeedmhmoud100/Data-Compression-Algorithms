




class LZ78:
    def __init__(self):
        self.dictionary = {}
        self.index = 1
        self.output = []

    def compress(self, data):
        data = list(data)
        while data:
            for i in range(len(data)):
                if ''.join(data[:i + 1]) not in self.dictionary:
                    self.dictionary[''.join(data[:i + 1])] = self.index
                    self.output.append((self.dictionary[''.join(data[:i+1])], data[i]))
                    print(self.output)
                    self.index += 1
                    data = data[i + 1:]
                    break
                else:
                    self.output.append((0, data[0]))
                    data = data[1:]
        return self.output

    def decompress(self, data):
        for i in data:
            if i[0] == 0:
                self.output.append(i[1])
            else:
                self.output.append(self.output[i[0]] + i[1])
        return ''.join(self.output)



def main():
    lz78 = LZ78()
    data = 'abracadabra'
    compressed_data = lz78.compress(data)
    print(compressed_data)
    decompressed_data = lz78.decompress(compressed_data)
    print(decompressed_data)

if __name__ == '__main__':
    main()