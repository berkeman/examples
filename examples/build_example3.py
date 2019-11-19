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

	print('\n# Read and print stored stdout for some of the processes')
	from glob import glob
	for fn in glob(job.filename('OUTPUT/*'))[:5]:
		print(fn)
		with open(fn, 'rt') as fh:
			print(fh.read())