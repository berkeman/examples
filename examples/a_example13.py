datasets = ('source',)

def analysis(sliceno):
	c = 0
	for test in datasets.source.iterate(sliceno, 'test'):
		c += test
	return c

def synthesis(analysis_res):
	return analysis_res.merge_auto()
