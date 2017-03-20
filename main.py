import Sum as s
import Comparasion as c
import time


class Input:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "r")

    def readN(self):
        self.n = self.file.readline()
        return int(self.n)

    def getB(self):
        self.file.readline()
        line = []
        for i in range(0, int(self.n)):
            line.append(self.file.readline())
        return line

    def getOtherElements(self):
        self.file.readline()
        line = self.file.readlines()
        val = []
        col = []
        diag = []
        line = [(float(element.split(", ")[0]), int(element.split(", ")[1]), int(
            element.split(", ")[2].split("\n")[0])) for element in line]
        line = sorted(line, key=lambda val: (val[1], val[2]))
        for element in line:
            value, line_index, column_index = element[0], element[1], element[2]
            if (-1 * line_index - 1) not in col:
                val.append(0)
                col.append(-1 * line_index - 1)
            if line_index == column_index:
                diag.append(value)
            else:
                col.append(column_index)
                val.append(value)
        return diag, val, col


def getInputFromText(filename):
    x = Input(filename)
    n = x.readN()
    b_vector = x.getB()
    diag, val, col = x.getOtherElements()

    return n, b_vector, diag, val, col


def main():
    n_a, b_vector_a, diag_a, val_a, col_a = getInputFromText("a.txt")
    n_b, b_vector_b, diag_b, val_b, col_b = getInputFromText("b.txt")
    n_sum, b_vector_sum, diag_sum, val_sum, col_sum = getInputFromText("aplusb.txt")
    operation = s.Sum(n_a, n_b, diag_a, diag_b, val_a, val_b, col_a, col_b, b_vector_a, b_vector_b)
    # #print (operation.addDiag())
    start_time = time.time()
    el_final, col_final = operation.addOthers()
    print(abs(time.time() - start_time))
    print(val_sum)
    print(el_final)


main()
