import psutil
import time
import os

def do(kwargs):
	assert 'filename' in kwargs
	assert 'control_file' in kwargs

	filename = kwargs.get('filename')
	control_file = kwargs.get('control_file')

	with open(filename) as f:
		f.seek(get_seek_position(control_file))
		cur_size = os.path.getsize(filename)
		while f.tell() < cur_size:
			yield f.readline()
		set_seek_position(control_file, cur_size)


def get_seek_position(control_file):
	try:
		with open(control_file, 'r') as cf:
			return int(cf.read())
	except:
		return 0

def set_seek_position(control_file, pos):
	with open(control_file, 'w') as cf:
		cf.write(str(pos))
