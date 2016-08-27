#Validate if a given string is numeric.
#"0" => true,,,  " 0.1 " => true,,,,,, "abc" => false,,,, "1 a" => false,,,,,, "2e10" => true

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        n = len(s)
        point = 0
        isNumeric = False
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1
            
        while i < n and s[i].isdigit():
            isNumeric = True
            i += 1
            
        while i < n and s[i] == '.':
            i += 1
            point += 1
            while i < n and s[i].isdigit():
                isNumeric = True
                i += 1
                
        if isNumeric and i < n and s[i] == 'e':
            i += 1
            isNumeric = False
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < n and s[i].isdigit():
                isNumeric = True
                i += 1
                    
        while i < n and s[i] == ' ':
            i += 1
            
        if point > 1:
            return False
            
        return isNumeric and i == n