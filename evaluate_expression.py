
def evalRPN(A):
    l=[]
    for str in A:
        if (str in ["+","-","*","/"]):
            a = l.pop()
            b = l.pop()
            if (str=="+"):
                l.append(b+a)
            if (str=="-"):
                l.append(b-a)
            if (str=="*"):
                l.append(b*a)
            if (str=="/"):
                l.append(int(b/(a*1.0)))
        else:
            l.append(int(str))
    return l[0]


print evalRPN("22+")     