class Prod:
    def __init__(self,n_a, n_b, diag_a, diag_b, val_a, val_b, col_a, col_b, b_vector_a, b_vector_b):
        self.n_a = n_a
        self.n_b = n_b
        self.diag_a = diag_a
        self.diag_b = diag_b
        self.val_a = val_a
        self.val_b = val_b
        self.col_a = col_a
        self.col_b = col_b
        self.b_vector_a = b_vector_a
        self.b_vector_b = b_vector_b

    def mul(self):
        final_a_ori_b_val = []
        final_a_ori_b_ind = []
        it = 0
        while it < len(self.val_a):
            if self.val_a[it] == 0:
                current_line = self.col_a[it]
                it2 = 0
                final_a_ori_b_ind.append(current_line)
                final_a_ori_b_val.append(0)
                while it2 < len(self.val_a):
                    current_element = 0
                    current_column = self.col_b[it2]
                    i, j = it + 1, it2 + 1
                    while i < len(self.val_a) and j < len(self.val_a) and self.val_a[i] != 0 and self.val_a[j] != 0:
                        if self.col_b[j] < self.col_a[i]:
                            j += 1
                        else:
                            if self.col_b[j] > self.col_a[i]:
                                i += 1
                            else:
                                current_element += self.val_a[i] * self.val_b[j]
                                i += 1
                                j += 1
                    if current_element != 0:
                        final_a_ori_b_ind.append(current_column)
                        final_a_ori_b_val.append(current_element)
                    while j < len(self.val_b) and self.val_b[j] != 0:
                        j += 1
                    it2 = j
            it += 1
        return final_a_ori_b_val, final_a_ori_b_ind

    def a_mul_x(self,vals, ind_cols):
        result_vector = [0 for i in range(0, 2017)]
        x = [i for i in range(2017, -1, -1)]
        current_line = -1
        for it in range(len(ind_cols)):
            if vals[it] == 0:
                current_line = ind_cols[it]
            else:
                result_vector[current_line] += vals[it] * x[ind_cols[it]]
        return result_vector
