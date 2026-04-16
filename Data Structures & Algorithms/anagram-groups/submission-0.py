class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord("a")] += 1
            freq_dict[tuple(freq)].append(word)
        return [x for x in freq_dict.values()]

        