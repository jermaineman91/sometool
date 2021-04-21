def calc(amount, arr, i, n, rs, pmin):
	if pmin < 0:
		print('out of')
		return 200000000000;
	if i == n:
		return 200000000000;
	a = amount//arr[i]
	b = amount%arr[i]
	if b == 0:
		rs.append((arr[i], a))
		return a
	rs.append((arr[i], a))
	return a + calc(b, arr, i + 1, n, rs, pmin - a);


types = [200, 500, 3, 1]
types.sort(reverse=True)
print(types)

amount = 800

n = len(types)
nmin = 200000000000
nrs = None
for i in range(n):
	rs = []
	b = calc(amount, types, i, n, rs, nmin)
	if b < nmin:
		nrs = rs
		nmin = b
	print(rs, b)

print(nmin)
print(nrs)
