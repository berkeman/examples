def main(urd):
	print('\n# This job will execute a sujob')
	job = urd.build('example6')
	print('\n# Post data has information on subjobs')
	print(job.post().subjobs)

	for key, val in job.post().subjobs.items():
		print(key, type(key), val)
