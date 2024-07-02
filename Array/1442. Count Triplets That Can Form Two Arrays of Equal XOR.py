class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0

        for i in range(n):
            xor_sum = 0
            for k in range(i, n):
                xor_sum ^= arr[k]
                if xor_sum == 0 and k > i:
                    count += (k - i)

        return count


