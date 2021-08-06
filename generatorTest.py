def gn(x:int):
	i=0
	while i<=x:
		print("i %d" %i)
		 # next the runing code is paused at this point,and return the value of i
		c = yield i
		print("c:",c)
		i+=1
		print("i after %d" %i)
	print("end")
	return "yanjc"

g=gn(6)
# def cc(g):
for y in g:
	print("for %d" %y)
	print()

def main():
	# for g in gn(6):
	# 	yield g
	
	f=yield from gn(6) #等同上
	print(f)
	
st=list(main())
print(st)

