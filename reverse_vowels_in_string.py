'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105'''
####################################################
class Solution:
	def reverseVowels(self, s: str) -> str:
		new_list_index = []
		new_list = []
		count_vowel = 0
		s_list = []
		j = -1
		for i in range(0,len(s),1):
			s_list.append(s[i])
		for i in s_list :
			j = j+1
			if (i in ('a','e','i','o','u','A','E','I','O','U')):
				count_vowel = count_vowel+1
				new_list_index.append(j)
				new_list.append(i)
		if count_vowel > 1:
			new_list.reverse()
			for l,k in zip(new_list, new_list_index) :
				s_list[k]=l
			s_list = "".join(s_list)
			return s_list
		else:
			return s
