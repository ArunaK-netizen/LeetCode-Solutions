class solution:
    def maxfrequencyelements(self, nums: list[int]) -> int:
        frequencies = dict(counter(nums))
        values = frequencies.values()
        maxfreq = max(values)
        count = 0
        for i in frequencies:
            if (frequencies[i] == maxfreq):
                count += frequencies[i]
        return count
