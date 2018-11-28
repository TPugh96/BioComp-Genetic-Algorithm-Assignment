class Data:
    numberOfBytes = 5
    bytes = []
    output = 0

    def __init__(self):
        self.numberOfBytes = 5
        self.bytes = []
        self.output = 0


def read_file():
    data_file = open("Data sets\data1.txt", "r")
    data_set = []

    for index, line in enumerate(data_file):
        cleaned_line = line.replace(" ", "")
        data_set.append(Data())
        byte_count = 0

        for byte in cleaned_line:
            if byte_count < data_set[index].numberOfBytes:
                data_set[index].bytes.append(int(byte))
                byte_count += 1
            else:
                data_set[index].output = int(byte)
                break
    return data_set
