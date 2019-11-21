def main(urd):
	print('\n# This job writes sliced files in "myfile1", and a single file')
	print('# "myfile2"')
	job1 = urd.build('example4')

	print('\n# This job reads the sliced and the single file and prints its')
	print('# contents to stdout')
	job2 = urd.build('example5',
		options=dict(
			firstfile=job1.withfile('myfile1', sliced=True),
			secondfile=job1.withfile('myfile2'),
		)
	)

	print('\n# Read and print stored stdout for synthesis')
	print(job2.output('synthesis'))
	print('\n# Read and print stored stdout for everything')
	print(job2.output())
	print('\n# Read and print stored stdout for analysis process 2')
	print(job2.output(2))

	import pickle
	with job1.open('myfile2', 'rb') as fh:
		print('x', pickle.load(fh), 'x')

	print()
	print(job1.open('setup.json').read())
