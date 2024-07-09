class Solution:
    def interpret(self, command: str) -> str:
        answer = ""
        i = 0
        while (i < len(command)):
            if (command[i] == "G"):
                answer += "G"
                i += 1

            elif (command[i] == "(" and command[i + 1] == ")"):
                answer += "o"
                i += 2

            else:
                answer += "al"
                i += 4
        return answer



