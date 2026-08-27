class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []

        for op in operations:
            if op == "+":
                points.append((points[-1] + points[-2]))
            elif op == "C":
                points.pop()
            elif op == "D":
                points.append((points[-1] * 2))
            else:
                points.append(int(op))

        return sum(points)