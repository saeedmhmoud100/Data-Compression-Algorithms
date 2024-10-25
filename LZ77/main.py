class LZ77:
    def __init__(self, window_size, buffer_size):
        self.window_size = window_size
        self.look_ahead = buffer_size

    def compress(self, data):
        compressed_data = []
        i = 0
        while i < len(data):
            match = self.find_match(data, i)
            if match:
                offset, length = match
                compressed_data.append((offset, length, data[i + length]))
                i += length + 1
            else:
                compressed_data.append((0, 0, data[i]))
                i += 1
        return compressed_data

    def decompress(self, compressed_data):
        data = ''
        for (offset, length, char) in compressed_data:
            if length:
                start = len(data) - offset
                for i in range(length):
                    data += data[start + i]
            data += char
        return data

    def find_match(self, data, i):
        index = i
        end = min(index + self.look_ahead, len(data) - 1)
        max_start = max(index - self.window_size, 0)

        search_window = data[max_start:index]
        string_ahead = data[index]

        while True:
            new_string_ahead = string_ahead + data[index]
            if index >= end or search_window.rfind(new_string_ahead) == -1:
                break
            index += 1
            string_ahead = new_string_ahead

        position = search_window.rfind(string_ahead)
        if position != -1:
            return i - position, len(string_ahead)


def main():
    window_size = 20
    buffer_size = 5
    lz77 = LZ77(window_size, buffer_size)
    data = 'abracadabra'
    compressed_data = lz77.compress(data)
    print(compressed_data)
    decompressed_data = lz77.decompress(compressed_data)
    print(decompressed_data)


if __name__ == '__main__':
    main()

# for j in range(i + 1, end):
#     offset = 1
#     while j - offset >= i and data[j - offset] == data[j - offset - i]:
#         offset += 1
#     length = offset - 1
#     if length > best_length:
#         best_offset = i + 1 - offset
#         best_length = length
