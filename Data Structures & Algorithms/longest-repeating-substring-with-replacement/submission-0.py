class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_count=0
        max_length=0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]]=1
            max_count=max(max_count,count[s[right]])

            length=right-left+1
            if length-max_count>k:
                count[s[left]]-=1
                left+=1
            length=right-left+1

            max_length=max(max_length,length)
        return max_length
        