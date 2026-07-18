from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        aux = deque([])
        for c in s:
            if c in ['(','{','['] :
                aux.append(c)
            else :
                if not len(aux) :return False
                if c == ')' and aux[-1] == '(' or c=='}' and aux[-1] == '{' or c==']' and aux[-1]=="[":
                    aux.pop()
                else :
                    return False
        return not len(aux)