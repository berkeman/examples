def prepare(job):
	print(dir(job))
	dw = job.datasetwriter()
	dw.add('test', 'number')
	return dw

def analysis(sliceno, prepare_res):
	dw = prepare_res
	dw.write(sliceno)
