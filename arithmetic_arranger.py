class arithmetic_arranger():
    def __init__(self, lista, flag=False):
        self.flag = flag
        self.rawdata = lista
        self.key = 1
        self.list_num1 = []
        self.list_opre = []
        self.list_num2 = []
        self.list_size = []
        self.list_offset1 = []
        self.list_offset2 = []
        self.list_total = []
        self.list_offset3 = []

    def process_the_item(self, item):
        res = item.split()
        if len(res) > 3 or len(res) == 0:
            print('rawdata error')
            self.key = 0
            quit()
        else:
            num1 = res[0]
            opre = res[1]
            num2 = res[2]
            if opre != '+' and opre != '-':
                print(r"Error: Operator must be ' + '  or  ' - ' .")
                self.key = 0
                quit()
            elif len(num1) > 4 or len(num2) > 4:
                print('Error: Numbers cannot be more than four digits.')
                self.key = 0
                quit()
            else:
                try:
                    int(num1)
                except ValueError:
                    print('Error: Numbers must only contain digits.')
                    self.key = 0
                    quit()
                try:
                    int(num2)
                except ValueError:
                    print('Error: Numbers must only contain digits.')
                    self.key = 0
                    quit()
            s1 = lambda x, y: x if x > y else y
            size = s1(len(num1), len(num2)) + 2
            offset1 = size - len(num1)
            offset2 = size - len(num2)
            if opre == '+':
                total = int(num1) + int(num2)
            else:
                total = int(num1) - int(num2)
            offset3 = size - len(str(total))
            if self.key:
                return num1, opre, num2, size, offset1, offset2, total, offset3

    def process_rawdata(self):
        if len(self.rawdata) > 5:
            print('Error: Too many problems.')
            self.key = 0
            quit()
        else:
            for item in self.rawdata:
                num1, opre, num2, size, offset1, offset2, total, offset3 = self.process_the_item(item)
                self.list_num1.append(num1)
                self.list_opre.append(opre)
                self.list_num2.append(num2)
                self.list_size.append(size)
                self.list_offset1.append(offset1)
                self.list_offset2.append(offset2)
                self.list_total.append(total)
                self.list_offset3.append(offset3)

    def print_answer(self):
        if self.key:
            txt1 = ''
            for i in range(len(self.list_num1)):
                for j in range(self.list_offset1[i]):
                    txt1 += ' '
                txt1 += str(self.list_num1[i])
                txt1 += '    '
            print(txt1)
            txt2 = ''
            for m in range(len(self.list_num1)):
                txt2 += str(self.list_opre[m])
                for n in range(self.list_offset2[m] - 1):
                    txt2 += ' '
                txt2 += str(self.list_num2[m])
                txt2 += '    '
            print(txt2)
            txt3 = ''
            for p in range(len(self.list_size)):
                for q in range(self.list_size[p]):
                    txt3 += '-'
                txt3 += '    '
            print(txt3)
            if self.flag :
                txt4 = ''
                for x in range(len(self.list_offset3)):
                    for y in range(self.list_offset3[x]):
                        txt4 += ' '
                    txt4 += str(self.list_total[x])
                    txt4 += '    '
                print(txt4)

    def count(self):
        self.process_rawdata()
        self.print_answer()



