class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        retries = 0

        while True:
            if retries == len(students):
                break

            if len(students) == 0 and len(sandwiches) == 0:
                break

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                retries = 0

            else:
                students.append(students.pop(0))
                retries += 1

        return len(students)