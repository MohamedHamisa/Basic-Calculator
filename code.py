class Solution:
    def calculate(self, s: str):
        def calc(i):
            p, n, op = 0, 0, 1
            while i < len(s) and s[i] != ')':
                if s[i] == '(':    i, n = calc(i+1)
                elif s[i] in '+-': p, n, op = p + op*n, 0, [-1, 1][s[i]=='+']
                elif s[i] != ' ':  n = 10*n + int(s[i])
                i += 1
            return i, p + op*n
        return calc(0)[1]n 







