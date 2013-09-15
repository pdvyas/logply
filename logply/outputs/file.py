import json
from ..utils import json_handler

def do(kwargs):
	assert 'filename' in kwargs
	assert 'obj' in kwargs
	obj = kwargs.get('obj')

	with open(kwargs.get('filename'), 'a') as f:
		f.write(json.dumps(obj, default=json_handler))
		f.write('\n')
