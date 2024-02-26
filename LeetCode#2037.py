class Solution:
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        n = len(seats)
        sum = 0
        for i in range(n):
            sum += abs(seats[i] - students[i])
        return sum
