# -*- coding: utf-8 -*-
"""Minimal output stub for gallery-dl submodule."""

class Output:
    ANSI = False
    COLORS = False

def initialize_logging(level):
    import logging
    return logging.getLogger()

def configure_logging(level):
    pass

def configure_standard_streams():
    pass

def setup_logging_handler(name, fmt="{message}", mode="w", defer=False):
    return None

def stderr_write(s):
    import sys
    sys.stderr.write(s)