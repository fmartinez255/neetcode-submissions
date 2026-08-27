class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False # can't be true if uneven number of brackets

        pStack = []
        # optimization here would be to use a dict to hold ending and opening brackets
        # closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for bracket in list(s):
            if bracket == "[" or bracket == "{" or bracket == "(":
                pStack.append(bracket)

            else:
                if len(pStack) == 0:
                    return False
                br = pStack.pop()
                if br == "{" and bracket != "}":
                    return False
                if br == "(" and bracket != ")":
                    return False
                if br == "[" and bracket != "]":
                    return False

        return True if len(pStack) == 0 else False