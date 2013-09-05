import os
from importlib import import_module

config_module = os.environ.setdefault('LOGPLY_CONFIG', 'config')
config = import_module(config_module)

def assert_log_config(log_config):
	assert 'input' in log_config
	assert 'filter' in log_config
	assert 'output' in log_config

def collect():
	ret = {}
	for log_name, log_config in config.logs.iteritems():
		assert_log_config(log_config)

		input_config = log_config.get('input')
		input_method = import_module(input_config.get('method'))
		data = input_method.get(input_config.get('args'))
		ret[log_name] = data
	
	return ret

if __name__ == "__main__":
	print collect()
