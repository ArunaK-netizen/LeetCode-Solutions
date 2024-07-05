class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        visited = set()
        for i in range(len(words)):
            if (words[i][::-1] in words and words[i] not in visited and words.index(words[i][::-1]) != words.index(
                    words[i])):
                visited.add(words[i])
                visited.add(words[i][::-1])
                count += 1
        return count
