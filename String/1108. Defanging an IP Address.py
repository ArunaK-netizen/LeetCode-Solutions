class Solution:
    def defangIPaddr(self, address: str) -> str:

        defangIP = ""
        for i in address:
            if (i == "."):
                defangIP += "[.]"
            else:
                defangIP += i
        return defangIP

