class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        answer = ""
        mapping = {}
        count = 0
        for i in range(len(key)):
            if (key[i] in mapping):
                continue
            else:
                if (key[i] != " "):
                    mapping[key[i]] = count
                    count += 1

        for i in range(len(message)):
            if (message[i] != " "):
                answer += chr(mapping[message[i]] + 97)
            else:
                answer += " "
        return answer

