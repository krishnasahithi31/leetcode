class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)!=set(word2):
            return False
        count1={}
        count2={}
        for ch in word1:
            count1[ch]=count1.get(ch,0)+1
        for ch in word2:
            count2[ch]=count2.get(ch,0)+1
        return sorted(count1.values())==sorted(count2.values())
        