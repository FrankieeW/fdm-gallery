# -*- coding: utf-8 -*-
"""Minimal util stub for gallery-dl submodule."""

import os
import re

USERAGENT_FIREFOX = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
USERAGENT_CHROME = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
USERAGENT_GALLERYDL = "gallery-dl/1.0"

WINDOWS = os.name == 'nt'
EXECUTABLE = False

def noop(*args, **kwargs):
    pass

def identity(x):
    return x

def false(*args, **kwargs):
    return False

def re_compile(pattern, flags=0):
    return re.compile(pattern, flags)

def expand_path(path):
    return os.path.expanduser(path)

def json_loads(s):
    import json
    return json.loads(s)

def json_dumps(obj):
    import json
    return json.dumps(obj)

def build_proxy_map(proxy, log):
    return None

def build_duration_func(duration, minimum=0):
    return None

def build_duration_func_ex(duration):
    return identity

SENTINEL = object()

class LazyPrompt:
    def __str__(self):
        return ""

class NullResponse:
    def __init__(self, url, msg):
        self.url = url
        self.text = ""