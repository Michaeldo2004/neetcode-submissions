class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            currString = i + "##!##"
            string += currString
        return string


    def decode(self, s: str) -> List[str]:
        x = s.split("##!##")
        x.pop()
        return x

