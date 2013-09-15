import os
from datetime import datetime

def do(kwargs):
    assert 'mount_points' in kwargs

    ret = {
        'timestamp': unicode(datetime.utcnow()),
        'mount_points': []
    }

    for mount_point in kwargs['mount_points']:
        s = os.statvfs(mount_point)
        total = (s.f_blocks * s.f_frsize) / 1024
        free = (s.f_bfree * s.f_frsize) / 1024
        used = total - free
        ret['mount_points'].append({
            'mount_point': mount_point,
            'total': total,
            'available': free,
            'used': used
        })

    yield ret
