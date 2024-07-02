class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        print(seats, students)
        operations = 0
        for i in range(len(seats)):
            operations += abs(seats[i] - students[i])
        return operations
