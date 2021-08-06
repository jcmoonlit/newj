def main(fn):
	def f(x,y):
		print("start")
		max=fn(x,y)
		print("max",max)
		print("totail",x+y)
	return f


@main
def max(x,y):
	if x >= y:
		return x
	else:
		return y

max(1,2)



# def new_fn(f):
# 	print("strat!")
# 	s=f
# 	print("end!")
# 	return s

# @new_fn
# def fn():
# 	print("yang")
# 	return "yanjc"

# print(fn())
