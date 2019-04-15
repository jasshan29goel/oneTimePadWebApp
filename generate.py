import itertools

res=["".join(seq) for seq in itertools.product("01", repeat=8)]
for x in res:
	print (x)
