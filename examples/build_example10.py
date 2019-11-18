def main(urd):

	print('\n# Run a method that creates a dataset')
	job = urd.build('example10')
	print('# (Now, test "bd dsinfo %s" to inspect the dataset!)' % (job,))

	print('\n# Run a method that appends a column to the dataset')
	job = urd.build('example11', datasets=dict(parent=job))
	print('# (Now, test "bd dsinfo %s" to inspect the dataset!)' % (job,))
