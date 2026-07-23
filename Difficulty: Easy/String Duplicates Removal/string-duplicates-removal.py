class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    st=""
	    for i in s:
	        if i not in st:
	            st+=i
	        else:
	            continue
	    return st
	    