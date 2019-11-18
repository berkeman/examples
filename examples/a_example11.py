
datasets = ('parent',)

def prepare(job):
	dw = job.datasetwriter(parent=datasets.parent)
	dw.add('strtest', 'unicode')
	return dw

def analysis(sliceno, prepare_res):
	dw = prepare_res
	for test in datasets.parent.iterate(sliceno, 'test'):
		dw.write(str(test))
