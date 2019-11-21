def main(urd):
	print('\n# This job writes sliced files in "myfile1", and a single file')
	print('# "myfile2"')
	job = urd.build('example4')

	print('\n# This job reads the sliced and the single file and prints its')
	print('# contents to stdout')
	job = urd.build('example5',
		options=dict(
			firstfile=job.withfile('myfile1', sliced=True),
			secondfile=job.withfile('myfile2'),
		)
	)

	print('\n# Read and print stored stdout for synthesis')
	print(job.output('synthesis'))
	print('\n# Read and print stored stdout for everything')
	print(job.output())
	print('\n# Read and print stored stdout for analysis process 2')
	print(job.output(2))

