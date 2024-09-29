'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104'''
#############################################################
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string1 = []
        j = 1
        m = 0
        if (1 <= k <= 10**4) and (1 <= len(s) <= 10**4) :
            if len(s) >= k:
                for i in range(0 , len(s),k):
                    string1 = string1 + [s[i:i + k]]
                #for j in range(0 ,round(len(s)/k) ,k):
                while j <= len(s):
                    string1[m] = string1[m][::-1]
                    j = j +(2*k)
                    m = m + 2
                return ("".join(string1))
            else :
                return s[::-1]
