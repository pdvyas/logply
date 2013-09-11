from importlib import import_module

def assert_log_config(log_config):
	assert 'input' in log_config
	assert 'filters' in log_config
	assert 'output' in log_config

def get_stage(log_config, stage, **extra_args):
	method, args = get_stage_method_and_args(log_config, stage)
	args.update(extra_args)
	data  = method.do(args)
	return data

def get_stage_method_and_args(log_config, stage):
	config = log_config.get(stage)
	method = import_module(config.get('method'))
	args = config.get('args')
	return (method, args)

def get_filter_stage(log_config, obj):
	config = log_config.get('filters')
	ret = reduce(apply_filter, config, obj)
	return ret

def apply_filter(obj, config):
	method = import_module(config.get('method'))
	args = config.get('args')
	return method.do(obj, args)
