class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while (len(students) != 0):
            if (students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
            elif (students.count(sandwiches[0]) == 0):
                return len(students)

            else:
                student = students.pop(0)
                students.append(student)

        return 0
