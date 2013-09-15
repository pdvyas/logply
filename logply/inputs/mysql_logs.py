import time
import os

from mysql_log_parser.parser import SlowQueryLog

# this almost a copy of file input plugin

def do(kwargs):
	assert 'filename' in kwargs
	assert 'control_file' in kwargs

	filename = kwargs.get('filename')
	control_file = kwargs.get('control_file')

	with open(filename, 'r') as f:
		last_pos = get_seek_position(control_file) 
		cur_size = os.path.getsize(filename)

		if not last_pos > cur_size:
			f.seek(last_pos)

		set_seek_position(control_file, cur_size)
		log = SlowQueryLog(f)
		while f.tell() < cur_size:
			yield log.next()

def get_seek_position(control_file):
	try:
		with open(control_file, 'r') as cf:
			return int(cf.read())
	except:
		return 0

def set_seek_position(control_file, pos):
	with open(control_file, 'w') as cf:
		cf.write(str(pos))
