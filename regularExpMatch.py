def isMatch(s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        previous = [True]
        for i in range(len(p)):
            if p[i] == '*':
                previous.append(previous[i-1])
            else:
                previous.append(False)
        print previous
        
        for letter in range(0,len(s)):
            actual = [False]
            for i in range(0, len(p)):
                if p[i]=='*':
                    temp = actual[i-1] or (previous[i+1] and (p[i-1]==s[letter] or p[i-1]=='.'))
                    print "if :", temp
                elif p[i] == '.':
                    temp = previous[i]
                    print "elif: ", temp
                else:
                    temp = previous[i] and p[i]==s[letter]
                    print "else ", temp
                actual.append(temp)
            previous = actual
        return previous[len(p)]
