def main(urd):

	# Connect two jobs, load and print return value

	print('\n# Run methods "example1" + "example2"')
	job1 = urd.build('example1')
	job2 = urd.build('example2', jobids=dict(first=job1))
	print('\n# Return value from "example1"')
	print(job1.load())
	print('\n# Return value from "example2"')
	print(job2.load())

	print('\n# Run method "example3" and print return value')
	job3 = urd.build('example3', jobids=dict(first=job1, second=job2))
	res3 = job3.load()
	print('"""' + res3 + '"""')

	print('\n# These files are stored by "method3"')
	for fn in job3.post().files:
		print('  ' + fn)

	print('\n# Load and print ex3file')
	ex3file = job3.load('ex3file')
	print(ex3file)

	print('\n# The job.filename()-function is used to get absolute paths to files in jobs.')
	print('# For example, here is the path to the last job (filename=\'\')')
	print(job3.filename(''))
