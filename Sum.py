class Sum:
    def __init__(self, n_a, n_b, diag_a, diag_b, val_a, val_b, col_a, col_b, b_vector_a, b_vector_b):
        self.n_a = n_a
        self.n_b = n_b
        self.diag_a = diag_a
        self.diag_b = diag_b
        self.val_a = val_a
        self.val_b = val_b
        self.col_a = col_a
        self.col_b = [int(x) for x in col_b]
        self.b_vector_a = b_vector_a
        self.b_vector_b = b_vector_b

    def addDiag(self):
        diagSUM = []
        for i in range(0, self.n_a):
            diagSUM.append(float(self.diag_a[i]) + float(self.diag_b[i]))
        return diagSUM

    def getValuesByLine(self, line, vec):
        element = []
        nr = 0
        nr_elements = len(vec)
        for i in range(1, nr_elements):
            if vec[i] != 0:
                element.append(vec[i])
            elif nr < line - 1:
                element.clear()
                nr += 1
            else:
                return element
        return []

    def getColumsByLine(self, line, vec):
        for i in vec[vec.index(line) + 1:len(vec)]:
            if i < 0:
                return vec[vec.index(line) + 1:vec.index(i)]
        return []

    def addOthers(self):
        el_final = []
        col_final = []
        for i in self.col_b:
            if i < 0:
                el_final.append(0)
                col_final.append(i)
                elements_b = self.getValuesByLine(abs(i), self.val_b)
                columns_b = self.getColumsByLine(i, self.col_b)
                elements_a = self.getValuesByLine(abs(i), self.val_a)
                columns_a = self.getColumsByLine(i, self.col_a)
                l1 = 0
                l2 = 0
                while l1 < len(columns_a) and l2 < len(columns_b):
                    if columns_a[l1] > columns_b[l2]:
                        el_final.append(elements_b[l2])
                        col_final.append(columns_b[l2])
                        l2 += 1
                    elif columns_a[l1] < columns_b[l2]:
                        el_final.append(elements_a[l1])
                        col_final.append(columns_a[l1])
                        l1 += 1
                    else:
                        el_final.append(elements_a[l1] + elements_b[l2])
                        col_final.append(columns_a[l1])
                        l1 += 1
                        l2 += 2
                while l1 < len(columns_a):
                    el_final.append(elements_a[l1])
                    col_final.append(columns_a[l1])
                    l1 += 1
                while l2 < len(columns_b):
                    el_final.append(elements_b[l2])
                    col_final.append(columns_b[l2])
                    l2 += 1
                el_final.append(0)
                col_final.append(i - 1)
        print(el_final)
        print(col_final)
