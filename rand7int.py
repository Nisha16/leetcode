from random import randint
import random
def rand2():
	x = random.randint(0,5)
	if x == 4:
		return rand2() # restart
	else:
		return x % 2
def rand7():
	x = rand2() * 4 + rand2() * 2 + rand2()
	if (x == 7):
		return rand7() #restart
	else:
		return x

print "number is: ", rand7()

cnt = [0 for x in range(7)]
def simulate(depth,tot):
    if(depth==0):
        cnt[tot%7] += 1
    else:
        for i in range(5):
            simulate(depth-1,tot+i)
simulate(7,0)
tot = sum(cnt)
print "temp: ", [float(x)/tot for x in cnt]			
