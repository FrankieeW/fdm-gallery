# -*- coding: utf-8 -*-
"""Minimal job stub for gallery-dl submodule."""

class DownloadJob:
    def __init__(self, url):
        self.url = url
    def run(self):
        return 0

class UrlJob:
    maxdepth = 0
    def __init__(self, url):
        self.url = url
    def run(self):
        return 0
    def handle_url_fallback(self, url):
        pass

class DataJob:
    resolve = 0
    def __init__(self, url):
        self.url = url
    def run(self):
        return 0

class Job:
    ulog = None