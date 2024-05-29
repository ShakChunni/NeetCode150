class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for s in strs:
            sorted_strings = '.'.join(sorted(s))
            anagram_groups[sorted_strings].append(s)
        return list(anagram_groups.values())
            