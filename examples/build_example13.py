def main(urd):
	print('\n# This job creates three datasets')
	job = urd.build('example14')

	print('\n# Print dataset names, columns and types')
	for ds in job.datasets():
		print(ds, sum(ds.lines), list((val.name, val.type) for val in ds.columns.values()))

	print('\n#Try "bd dsinfo %s -l"' % (job,))
