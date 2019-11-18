jobids=('first', 'second',)

def synthesis(job):
	res1 = jobids.first.load()
	res2 = jobids.second.load()
	s = 'Hello from \"%s\"' % (job.method,)
	s += '\n  second job is \"%s\"' % (jobids.second.method,)
	s += '\n  first job took %f seconds' % (jobids.first.post().profile.total,)
	s += '\n  now I store something in \"ex3file\"'
	job.save(dict(a=3, b='foo'), 'ex3file')
	return s
