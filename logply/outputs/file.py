def put(obj, params):
	assert 'filename' in params
	f = open(params.get('filename'), 'a')
	f.write(obj)
