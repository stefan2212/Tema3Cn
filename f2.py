n = 0
def from_file_cols(filename):
    triplets = []
    b = []
    with open(filename, "r") as f:
        global n
        p = lambda x, y, z: (float(x), int(y), int(z))
        n = int(f.readline())
        f.readline()
        for i in range(n):
            b.append(float(f.readline()))
        f.readline()
        for l in f:
            l = l[:-1]
            val, i, j = p(*l.split(","))
            triplets.append((val, i, j))
    triplets = sorted(triplets, key=lambda value: (value[1], value[2]))
    vals = []
    ind_cols = []
    last_line = -1
    for l in triplets:
        val, i, j = l
        while i > last_line:
            last_line += 1
            vals.append(0)
            ind_cols.append(last_line)
        vals.append(val)
        ind_cols.append(j)
    return vals, ind_cols, b


def transform_to_lines(vals, ind_cols):
    ind_lines = []
    new_vals = []
    ind_cols_new = list(ind_cols)
    vals_new = list(vals)
    for it1 in range(0, n):
        new_vals.append(0)
        ind_lines.append(it1)
        for it in range(len(ind_cols_new)):
            if ind_cols_new[it] == it1 and vals_new[it] != 0:
                new_vals.append(vals_new[it])
                new_it = it
                while vals_new[new_it] != 0:
                    new_it -= 1
                ind_lines.append(ind_cols_new[new_it])
    return new_vals, ind_lines


def a_mul_x(vals, ind_cols):
    result_vector = [0 for i in range(0, 2017)]
    x = [i for i in range(2017, -1, -1)]
    current_line = -1
    for it in range(len(ind_cols)):
        if vals[it] == 0:
            current_line = ind_cols[it]
        else:
            result_vector[current_line] += vals[it] * x[ind_cols[it]]
    return result_vector


def a_plus_b(vals_a, ind_cols_a, vals_b, ind_cols_b):
    final_a_plus_b_val = []
    final_a_plus_b_ind = []
    it = 0
    """ se porneste cu vectorul b """
    while it < len(vals_b):
        if vals_b[it] == 0:
            current_line = ind_cols_b[it]
            it2 = 0
            found_line_in_a_plus_b = True
            """ cautam linia corespunzatoare din b in vectorul a """
            while it2 < len(ind_cols_a):
                """ se verifica daca linia din a contine elemente nenule """
                if vals_a[it2] == 0 and ind_cols_a[it2] == current_line:
                    break
                if vals_a[it2] == 0 and ind_cols_a[it2] > current_line:
                    found_line_in_a_plus_b = False
                    break
                it2 += 1
            """ daca linia din a contine elemente nenule, atunci se aduna cei doi vectori"""
            if found_line_in_a_plus_b:
                new_line_vals = [0]
                new_line_ind_cols = [current_line]
                i, j = it2 + 1, it + 1
                while i < len(vals_a) and j < len(vals_b) and vals_a[i] != 0 and vals_b[j] != 0:
                    if ind_cols_b[j] < ind_cols_a[i]:
                        new_line_ind_cols.append(ind_cols_b[j])
                        new_line_vals.append(vals_b[j])
                        j += 1
                    else:
                        if ind_cols_b[j] > ind_cols_a[i]:
                            new_line_ind_cols.append(ind_cols_a[i])
                            new_line_vals.append(vals_a[i])
                            i += 1
                        else:
                            if ind_cols_b[j] == ind_cols_a[i]:
                                if vals_a[i] + vals_b[j] != 0:
                                    new_line_ind_cols.append(ind_cols_a[i])
                                    new_line_vals.append(vals_a[i] + vals_b[j])
                                i += 1
                                j += 1
                while i < len(vals_a) and vals_a[i] != 0:
                    new_line_ind_cols.append(ind_cols_a[i])
                    new_line_vals.append(vals_a[i])
                    i += 1
                while j < len(vals_b) and vals_b[j] != 0:
                    new_line_ind_cols.append(ind_cols_b[j])
                    new_line_vals.append(vals_b[j])
                    j += 1
                it = j
            else:
                new_line_vals = [0]
                new_line_ind_cols = [current_line]
                j = it2 + 1
                while j < len(vals_b) and vals_b[j] != 0:
                    new_line_ind_cols.append(ind_cols_b[j])
                    new_line_vals.append(vals_b[j])
                    j += 1
            final_a_plus_b_ind.extend(new_line_ind_cols)
            final_a_plus_b_val.extend(new_line_vals)
        else:
            it += 1
    return final_a_plus_b_val, final_a_plus_b_ind


def a_ori_b(vals_a, ind_cols_a, vals_b, ind_lines_b):
    final_a_ori_b_val = []
    final_a_ori_b_ind = []
    it = 0
    while it < len(vals_a):
        if vals_a[it] == 0:
            current_line = ind_cols_a[it]
            it2 = 0
            final_a_ori_b_ind.append(current_line)
            final_a_ori_b_val.append(0)
            while it2 < len(vals_b):
                current_element = 0
                current_column = ind_lines_b[it2]
                i, j = it + 1, it2 + 1
                while i < len(vals_a) and j < len(vals_b) and vals_a[i] != 0 and vals_b[j] != 0:
                    if ind_lines_b[j] < ind_cols_a[i]:
                        j += 1
                    else:
                        if ind_lines_b[j] > ind_cols_a[i]:
                            i += 1
                        else:
                            current_element += vals_a[i] * vals_b[j]
                            i += 1
                            j += 1
                if current_element != 0:
                    final_a_ori_b_ind.append(current_column)
                    final_a_ori_b_val.append(current_element)
                while j < len(vals_b) and vals_b[j] != 0:
                    j += 1
                it2 = j
        it += 1
    return final_a_ori_b_val, final_a_ori_b_ind


vals_a, ind_a, b_a = from_file_cols("a.txt")
vals_b, ind_b, b_b = from_file_cols("b.txt")
print(vals_b)
print(ind_b)
vals_t, ind_t = transform_to_lines(vals_b, ind_b)


"""#### A x B ####"""
print(vals_t)
print(ind_t)
vals_a_ori_b_file, ind_a_ori_b_file, b_aorib = from_file_cols("aorib.txt")
vals_a_ori_b, ind_a_ori_b = a_ori_b(vals_a, ind_a, vals_t, ind_t)
print(vals_a_ori_b)
print(ind_a_ori_b)

"""#### A + B ####"""
vals_a_plus_b_file, ind_a_plus_b_file, b_aplusb = from_file_cols("aplusb.txt")
vals_a_plus_b, ind_a_plus_b = a_plus_b(vals_a, ind_a, vals_b, ind_b)


"""### AxX & BxX & (A+B)xX & (AxB)xX"""
a_ori_x = a_mul_x(vals_a, ind_a)
b_ori_x = a_mul_x(vals_b, ind_b)
a_plus_b_ori_x = a_mul_x(vals_a_plus_b, ind_a_plus_b)
a_ori_b_ori_x = a_mul_x(vals_a_ori_b, ind_a_ori_b)

