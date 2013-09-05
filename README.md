### Logply

Logply is a log processor inspired from logstash

Logply needs to be configured using a python module. You can tell Logply to use
your configuration by setting an environment variable, `LOGPLY_CONFIG_MODULE`
and it should be in python path systax and the module should be in python import
path.

example config.py,

```
logs = {
	'memory': {
		'input': {
			'method': 'logply.inputs.memory',
			'args': {}
		},
		'filter': {
			'method': 'logply.filters.dummy',
			'args': {}
		},
		'output': {
			'method': 'logply.outputs.file',
			'args': {
				'filename': 'test.txt'
			}
		}
	},

	'apache': {
		'input': {
			'method': 'logply.inputs.file',
			'args': {
				'filename': '/tmp/access_log',
				'control_file': '/tmp/inputfilecontrol'
			}
		},
		'filter': {
			'method': 'logply.filters.apache_access',
			'args': {}
		},
		'output': {
			'method': 'logply.outputs.file',
			'args': {
				'filename': 'test.txt'
			}
		}
	}
}
```

The above config defines two logging jobs. 
* The first one takes memory info as an input, does no filtering (dummy) and
  puts it in a text file. 

* The second job takes an input file (followed for changes using a controlfile),
  filters it as per apache log regex and puts it in a text file.
