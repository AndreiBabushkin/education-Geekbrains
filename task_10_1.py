class Matrix:
    def __init__(self, *argv):
        for i in argv:
            self.list = i

    def __add__(self, other):
        result = []
        for list_1 in range(len(self.list)):
            new_list = []
            for integer in range(len(self.list[list_1])):
                new_list.append(self.list[list_1][integer] + other.list[list_1][integer])
            result.append(new_list)
        return Matrix(result)

    def __str__(self):
        string_ret = ''
        for idx in self.list:
            string_ret += ' '.join(map(str, idx)) + '\n'
        return string_ret

m = Matrix([[31, 22], [37, 43], [3, 5]])
m1 = Matrix([[3, 5, 21], [28, -12, -4], [93, 65, 1024]])
m2 = Matrix([[-6, 5, 21, 65], [8, 2, -14, 52], [88, 25, 64, 87]])
print(m)
print(m1)
print(m2)

print(m1 + m2)



