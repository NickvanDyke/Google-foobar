def answer(l):
	c = []
	for i in range(0, len(l)):
		c.append(0)
	numTrips = 0
	for i in range(0, len(l)):
		for j in range(0, i):
			if (l[i] % l[j] == 0)
				c[i] += 1
				numTrips += c[j]
	return numTrips