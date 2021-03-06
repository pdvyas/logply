import psutil
from datetime import datetime

def do(kwargs):
	params = ['total', 'used', 'free', 'percent']
	ret = obj_to_dict(psutil.phymem_usage(), params, prefix='physical_memory_')
	ret.update(obj_to_dict(psutil.virtmem_usage(), params, prefix='virtual_memory_'))
	ret.update({'timestamp': unicode(datetime.utcnow())})
	yield ret

def obj_to_dict(obj, attrs, prefix=''):
	return {prefix+attr: getattr(obj, attr) for attr in attrs}
