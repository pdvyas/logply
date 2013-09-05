import os
import json

from importlib import import_module
from .utils import assert_log_config, get_stage

config_module = os.environ.setdefault('LOGPLY_CONFIG_MODULE', 'logply.config')
config = import_module(config_module)

def do():
	for log_name, log_config in config.logs.iteritems():
		assert_log_config(log_config)

		for input_data in get_stage(log_config, 'input'):
			filtered_data = get_stage(log_config, 'filter', obj=input_data)
			dispatched_data = get_stage(log_config, 'output', obj=filtered_data)

if __name__ == "__main__":
	do()
