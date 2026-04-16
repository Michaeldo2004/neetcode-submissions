class Solution:

    def encode(self, strs: List[str]) -> str: # O(n)
        string = ""
        for i in strs:
            string += str(len(i)) + "#" + i
        return string


    def decode(self, s: str) -> List[str]:
        lists = []
        pointer = 0
        while pointer < len(s):
            num = pointer
            while s[num] != "#":
                num += 1
            
            stringNum = int(s[pointer:num]) 
            # after '#' to the next n#
            lists.append(s[num + 1: num + stringNum + 1])
            # update pointer to next n#
            pointer = num + 1 + stringNum

        return lists

             

