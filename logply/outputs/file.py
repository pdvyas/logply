import json

def do(kwargs):
	assert 'filename' in kwargs
	assert 'obj' in kwargs
	obj = kwargs.get('obj')

	with open(kwargs.get('filename'), 'a') as f:
		f.write(json.dumps(obj))
		f.write('\n')
