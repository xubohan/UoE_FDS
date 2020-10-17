import queue

class BufferedInput:
    def __init__(self, filename, memory):
        self.reader = open(filename, 'r', encoding='utf-8')
        self.buffer = self.reader.readlines(memory)
        self.memory = memory
        self.pos = 0

    def readline(self):
        if self.buffer == []:
            return ''
        else:
            result = self.buffer[self.pos]
            self.pos += 1
            if self.pos == len(self.buffer):
                self.buffer = self.reader.readlines(self.memory)
                self.pos = 0
            return result

    def close(self):
        self.reader.close()


class BufferedOutput:
    def __init__(self, filename, size):
        self.writer = open(filename, 'w', encoding='utf-8')
        self.buffer = ['' for i in range(size)]
        self.lines = size
        self.pos = 0

    def writeline(self, str):
        self.buffer[self.pos] = str
        self.pos += 1
        if self.pos == self.lines:
            self.writer.writelines(self.buffer)
            self.pos = 0

    def flush(self):  # flushes buffer and close file
        self.writer.writelines(self.buffer[0:self.pos])
        self.writer.close()


def readnumbers(filename):
    reader = BufferedInput(filename, 20)
    temp = []
    while True:
        line = reader.readline()
        if not line:
            break
        line_split = line.split('N:')
        line_file = line.split('I:')
        if line_split[0] == '':
            temp.append(line_split[1].replace('\n', ''))
        elif line_file[0] == '':
            temp.extend(readnumbers(line_file[1].replace('\n', '')))
    reader.close()
    return temp
# print('%s contains: %s' % (filename, temp))

def readnumbersQueue(filename):
    reader = BufferedInput(filename, 20)
    temp = queue.LL_Queue()
    while True:
        line = reader.readline()
        if not line:
            break
        line_split = line.split('N:')
        line_file = line.split('I:')
        if line_split[0] == '':
            temp.push(line_split[1].replace('\n', ''))
        elif line_file[0] == '':
            readnumbersQueue(line_file[1].replace('\n', ''))
    reader.close()
    return temp

if __name__ == '__main__':
    pass
