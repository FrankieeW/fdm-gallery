# -*- coding: utf-8 -*-
"""Message types for extractor."""

class Message:
    class Directory:
        pass
    class Url:
        pass
    class Queue:
        pass

Directory = Message.Directory
Url = Message.Url
Queue = Message.Queue