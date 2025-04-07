#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        soma = int(str(l1)[::-1]) + int(str(l2)[::-1])
        return int(str(soma)[::-1])




#resolution is not correct *****linked list