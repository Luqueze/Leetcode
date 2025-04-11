class Solution(object):
    def lengthOfLastWord(self, s):
        
        counter = 0
        for i in s[::-1]:

            if i != " ":
                counter += 1
            elif counter > 0:
                break

        return counter        

            