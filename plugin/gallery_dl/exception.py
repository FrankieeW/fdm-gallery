# -*- coding: utf-8 -*-
"""Minimal exception stub for gallery-dl submodule."""

class GalleryException(Exception):
    code = 1

class NotFoundError(GalleryException):
    code = 2

class HttpError(GalleryException):
    code = 3

class ChallengeError(GalleryException):
    code = 4

class InputFileError(GalleryException):
    code = 128

class NoExtractorError(GalleryException):
    code = 64

class AbortExtraction(GalleryException):
    pass

class ControlException(GalleryException):
    pass

class RestartExtraction(GalleryException):
    pass