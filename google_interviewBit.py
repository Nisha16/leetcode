def Kth_pascal_row(A):
    row = [1]

    for col in range(0, A):
        row.append((row[-1] * (A - col))/ (col + 1)) 

    return row       

#print Kth_pascal_row(3)

def rotateMatrix(A):
    n = len(A)
    for i in range(n):
        print "for: "
        for j in range(i+1,n):
            print "1st for :"
            A[i][j], A[j][i] = A[j][i], A[i][j]
            print A
    for i in range(n/2):
        for j in range(n):
            print "2nd for: "
            temp = A[j][n-i-1]
            A[j][n-i-1], A[j][i] = A[j][i], A[j][n-i-1]
            print "2 A: ", A

    return A


def check_difference_of_strings(word1,word2):
    word1_temp = set()
    word1 = map(str,word1)
    for i in word1:
        word1_temp.add(i)
    word2 = map(str,word2)
    count = 0
    for i in word2:
        if i not in word1_temp:
            count += 1
    if count == 1:
        return True
    else:
        return False    

print check_difference_of_strings('blue','bull')




print rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])                   
  