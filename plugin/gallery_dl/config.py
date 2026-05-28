# -*- coding: utf-8 -*-
"""Minimal config stub for gallery-dl submodule."""

class Config:
    def get(self, path, key, default=None):
        return default
    def set(self, path, key, value):
        pass
    def interpolate(self, path, key, default=None):
        return default

config = Config()

def get(path, key, default=None):
    return default

def interpolate(path, key, default=None):
    return default

def set(path, key, value):
    pass