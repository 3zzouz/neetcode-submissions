from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        aux = deque([])
        ops = ['+','-','*','/']
        for c in tokens:
            if c not in ops :
                aux.append(c)
            else:
                el2 = int(aux.pop())
                el1 = int(aux.pop())
                if c == '+':
                    res = el1 + el2
                elif c == '-':
                    res = el1 - el2
                elif c == "*":
                    res = el1 * el2
                else:
                    res = int(el1 / el2)
                aux.append(res)
        return int(aux[0])
                