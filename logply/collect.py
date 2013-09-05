import os
import json
from importlib import import_module

config_module = os.environ.setdefault('LOGPLY_CONFIG_MODULE', 'config')
config = import_module(config_module)

def assert_log_config(log_config):
	assert 'input' in log_config
	assert 'filter' in log_config
	assert 'output' in log_config

def get_stage(log_config, stage, **extra_args):
	method, args = get_stage_method_and_args(log_config, stage)
	args.update(extra_args)
	data  = method.get(args)
	return data

def get_stage_method_and_args(log_config, stage):
	config = log_config.get(stage)
	method = import_module(config.get('method'))
	args = config.get('args')
	return (method, args)

def collect():
	ret = []
	for log_name, log_config in config.logs.iteritems():
		assert_log_config(log_config)

		input_data = get_stage(log_config, 'input')
		filtered_data = get_stage(log_config, 'filter', obj=input_data)
		ret.append(json.dumps({log_name: filtered_data}))

	return ret

if __name__ == "__main__":
	for line in collect():
		print line
