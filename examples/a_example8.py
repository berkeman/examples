
def prepare():
	return 'this is prepare'

def analysis(sliceno, prepare_res):
	return 'this is analysis' + str(sliceno) + prepare_res

def synthesis(analysis_res, prepare_res):
	x = '\n'.join(analysis_res)
	print(x)
	print(prepare_res)
	return prepare_res + x
