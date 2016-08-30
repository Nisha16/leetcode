def isInterleaved(s1, s2, s3):
 
    isInterleaved = []
    if len(s3) != len(s1)+len(s2):
        return False
    for i in range(0,len(s1)+1):
        row = []
        for j in range(0,len(s2)+1):
            if i == 0 and  j==0:
                row.append(True)
            else:
                temp = False
                if j>0:
                    temp = row[j-1] and s3[i+j-1] == s2[j-1]
                if i>0:
                     temp = temp or (previousRow[j] and s3[i+j-1] == s1[i-1])
                row.append(temp)
        previousRow = row
    return row[len(s2)]

def printIlsRecur(str1, str2, iStr, m, n, i):
 
    # Base case: If all characters of str1 and str2 have been
    # included in output string, then print the output string
    if m==0 and n==0:
        print ''join(iStr)
 
    # If some characters of str1 are left to be included, then
    # include the first character from the remaining characters
    # and recur for rest
    if m != 0:
        iStr[i] = str1[0]
        printIlsRecur(str1[1:], str2, iStr, m-1, n, i+1)
 
    # If some characters of str2 are left to be included, then
    # include the first character from the remaining characters
    # and recur for rest
    if n != 0:
        iStr[i] = str2[0]
        printIlsRecur(str1, str2[1:], iStr, m, n-1, i+1)
 
# Allocates memory for output string and uses printIlsRecur()
# for printing all interleavings
def printIls(str1, str2, m, n):
    iStr = [''] * (m+n)
 
    # print all interleavings using printIlsRecur()
    printIlsRecur(str1, str2, iStr, m, n, 0)    