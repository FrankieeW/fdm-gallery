# -*- coding: utf-8 -*-
"""Minimal text utilities stub for gallery-dl submodule."""

import re

def re_compile(pattern, flags=0):
    """Compile a regular expression pattern."""
    return re.compile(pattern, flags)

def extr(text, start, end):
    """Extract text between start and end markers."""
    s = text.find(start)
    if s == -1:
        return ""
    s += len(start)
    e = text.find(end, s)
    if e == -1:
        return ""
    return text[s:e]

def unescape(text):
    """Unescape HTML entities."""
    import html
    return html.unescape(text)

def ensure_http_scheme(url, scheme='https://'):
    """Ensure URL has an HTTP scheme."""
    if url and not url.startswith(('http://', 'https://')):
        return scheme + url
    return url

def nameext_from_url(url, data):
    """Extract filename and extension from URL."""
    import os
    path = url.split('?')[0].split('#')[0]
    name = os.path.basename(path)
    if '.' in name:
        data['filename'], data['extension'] = name.rsplit('.', 1)
    else:
        data['filename'] = name
        data['extension'] = ''

def _re(pattern, flags=0):
    """Compile and return a regex pattern."""
    return re.compile(pattern, flags)