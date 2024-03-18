class Solution:
    def romanToInt(self, s: str) -> int:
        num={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Int=0
        for i in range(len(s)-1):
            if num[s[i]]<num[s[i+1]]:
                Int-=num[s[i]]
            else:
                Int+=num[s[i]]
        return Int+num[s[-1]]