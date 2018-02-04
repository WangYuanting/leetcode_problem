'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_dict={'(':')',
                   '{': '}',
                   '[' : ']'}
        temp_list=[]
        for i in s:
            if i in temp_dict.keys():
                temp_list.append(i)
            elif i in temp_dict.values() and len(temp_list)>0 and temp_list[-1] in temp_dict.keys() and i==temp_dict[temp_list[-1]]:
                temp_list.pop()
            elif i in temp_dict.values():
                temp_list.append(i)

        if temp_list==[]:
            return True
        else:
            return False

a=Solution()
b=a.isValid("([)]")
print b


def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    right_to_left_dict = {")": "(", "]": "[", "}": "{"}
    stack = []
    for cur_char in s:
        if cur_char not in right_to_left_dict:
            stack.append(cur_char)
        else:
            if not stack or right_to_left_dict[cur_char] != stack.pop():
                return False

    if stack:
        return False
    else:
        return True
isValid(1,"([)]")