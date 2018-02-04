'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        temp_dict={}
        return self.count(temp_dict,n)

    def count(self,dict_in,n):
        if n==0:
            return_list=[]
            for key,value in dict_in.iteritems():
                temp_str=key
                while value>0:
                    temp_str+=')'
                    value-=1
                if temp_str not in return_list:
                    return_list.append(temp_str)
            return return_list
        dict_out={}
        if dict_in=={}:
            dict_out['(']=1
            dict_out['()'] = 0
            return self.count(dict_out,n-1)
        for key,value in dict_in.iteritems():
            dict_out[key + '()'] = value
            dict_out[key+'(']=value+1
            i=1
            while value>0:
                dict_out[key + ')'*i+'('] = value
                value-=1
                i+=1

        return self.count(dict_out,n-1)

a=Solution()
b=a.generateParenthesis(3)
print(b)


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 0:
        return [""]
    result = []
    mystr = ""
    helper(n, 0, 0, result, mystr)
    return result


def helper(n, open_count, close_count, result, mystr):
    if len(mystr) == 2 * n:
        result.append(mystr[:])
    if open_count < n:
        helper(n, open_count + 1, close_count, result, mystr + "(")

    if close_count < open_count:
        helper(n, open_count, close_count + 1, result, mystr + ")")

generateParenthesis(3)