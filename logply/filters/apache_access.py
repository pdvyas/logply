import re
from dateutil.parser import parse

reobj = re.compile(
	r'^(?P<client>\S+)\s+'
	r'(?P<auth>\S+\s+\S+)\s+'
	r'\[(?P<datetime>[^]]+)\]\s+'
	r'"(?:GET|POST|HEAD)'
	r' (?P<file>[^ ?"]+)\??(?P<parameters>[^ ?"]+)?'
	r' HTTP/[0-9.]+"\s+'
	r'(?P<status>[0-9]+)\s+(?P<size>[-0-9]+)\s+'
	r'"(?P<referrer>[^"]*)"\s+'
	r'"(?P<useragent>[^"]*)"$', re.MULTILINE)

def do(kwargs):
	line = kwargs.get('obj').rstrip()
	match = reobj.match(line)
	if match:
		ret = match.groupdict()
        ret['datetime'] = unicode(parse(ret['datetime'], fuzzy=True))
        return ret
	return None

