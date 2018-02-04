'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        y={'2':'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'}
        list=[]
        y, digits, list=self.add(y,digits,list)
        return list

    def add(self,y,digits,list):
        if len(digits)==0:
            return y,digits,list
        temp_str=digits[0]
        temp_list=[]
        if list==[]:
            for s in y[temp_str]:
                temp_list.append(s)
        else:
            for l in list:
                for s in y[temp_str]:
                    temp_list.append(l+s)
        return self.add(y,digits[1:],temp_list)
a=Solution()
b=a.letterCombinations('22')
print b


def letterCombinations(self, digits):
    if not len(digits):
        return []
    self.dig2let = {1: '*', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0: ' '}

    return self.create_combination(digits, [])


def create_combination(self, digits, coll):
    if len(digits) == 1:
        return list(self.dig2let[int(digits[0])])
    else:
        coll = []
        prev_coll = self.create_combination(digits[:-1], coll)
        for sub in prev_coll:
            for char in list(self.dig2let[int(digits[-1])]):
                buff = sub + char
                coll.append(buff)
        return coll