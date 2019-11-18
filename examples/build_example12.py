def main(urd):

	# First, create a new dataset.
	# Second, iterate over this dataset and print return value

	print('\n# Run a method that creates a dataset')
	job = urd.build('example10')

	job = urd.build('example13', datasets=dict(source=job))
	print("# Job returns the sum:", job.load())
