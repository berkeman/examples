def analysis(sliceno, job):
	job.save('this_is_the_data_analysis ' + str(sliceno), 'myfile1', sliceno=sliceno)

def synthesis(job):
	job.save('this_is_the_data_2', 'myfile2')
