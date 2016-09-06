class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""    # result string
        word = ""   # single word string
        for ch in s:
            if (ch!=' '):
                word+=ch
            if (ch==' '):
                if (len(word)!=0):
                    if (res!=""):   # add space between words
                        res = ' ' + res
                    res = word + res
                    word = ""
                
        if (len(word)!=0):  #handle the final word
            if (res!=""):
                res = ' ' + res
            res = word + res
             
        return res
