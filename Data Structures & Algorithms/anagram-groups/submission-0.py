class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counter = defaultdict(list)
        for str in strs:
            count = [0]*26
            for let in str:
                count[ord(let) - ord('a')]+=1
            counter[tuple(count)].append(str)
        
        return list(counter.values())