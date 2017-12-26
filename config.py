# -*- coding: utf-8 -*-

import json

def load_conf():
    with open('config.json', 'r') as f:
        s = json.loads(f.read())
    return s
