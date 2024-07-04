class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        transformation = set()
        for i in words:
            morseCode = ''
            for j in i:
                morseCode += morse[ord(j) - 97]
            transformation.add(morseCode)
        return len(transformation)
