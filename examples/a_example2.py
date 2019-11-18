jobids=('first',)

def synthesis():
	res = jobids.first.load()
	return res + res
