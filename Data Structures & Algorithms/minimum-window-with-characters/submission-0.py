class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        a = 0
        b = 0
        freq = {}
        window = {}
        curr = 0

        for char in t:
            freq[char] = freq.get(char,0) +1
        
        req = len(freq)
        sub = [-1,-1]
        sublength = float("Infinity")

        for b in range(len(s)):
            window[s[b]] = window.get(s[b], 0) +1

            if s[b] in freq and freq[s[b]] == window[s[b]]:
                curr += 1

            while curr == req:
                if sublength > b - a:
                    sub = [a, b]
                    sublength = b - a
                window[s[a]] -= 1
                if s[a] in freq and freq[s[a]] > window[s[a]]:
                    curr -= 1
                a += 1
        return s[sub[0]:sub[1] +1] if sublength != float("Infinity") else ""
                