# -*- coding: utf-8 -*-

# Copyright 2015-2025 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""gallery_dl - multi-source image extractor"""

import sys
import os
import re

# Add current directory to path for local imports
sys.path.insert(0, os.path.dirname(__file__))

__version__ = "1.32.1"
__author__ = "Mike Fährmann"

def re_compile(pattern, flags=0):
    """Compile a regular expression pattern."""
    return re.compile(pattern, flags)

# Stub for re_compile to avoid import issues
modules = [
    "2ch", "2chan", "2chen", "35photo", "3dbooru", "4chan", "4archive",
    "4chanarchives", "500px", "8chan", "8muses", "adultempire", "agnph",
    "ahottie", "allporncomic", "ao3", "arcalive", "architizer", "arena",
    "artstation", "aryion", "audiochan", "bbc", "behance", "bellazon",
    "bilibili", "blogger", "bluesky", "boosty", "booth", "bunkr", "catbox",
    "cfake", "chevereto", "cien", "civitai", "comedywildlifephoto", "comick",
    "comicvine", "cyberdrop", "cyberfile", "danbooru", "dandadan",
    "dankefuerslesen", "desktopography", "deviantart", "discord",
    "dynastyscans", "e621", "eporner", "erome", "everia", "facebook",
    "fanbox", "fansly", "fantia", "fapello", "fapachi", "fikfap",
    "filester", "fitnakedgirls", "flickr", "foriio", "furaffinity",
    "furry34", "fuskator", "gelbooru", "gelbooru_v01", "gelbooru_v02",
    "girlsreleased", "girlswithmuscle", "gofile", "hatenablog",
    "hentai2read", "hentaicosplays", "hentaihere", "hiperdex", "hotleak",
    "idolcomplex", "imagebam", "imagechest", "imagefap", "imagepond",
    "imageshack", "imgbb", "imgbox", "imgpile", "imgth", "imgur",
    "imhentai", "inkbunny", "instagram", "issuu", "itaku", "itchio",
    "iwara", "joyreactor", "jschan", "kabeuchi", "kaliscan", "keenspot",
    "kemono", "khinsider", "komikcast", "koofr", "leakgallery", "lensdump",
    "lexica", "lightroom", "listal", "livedoor", "lofter", "luscious",
    "lynxchan", "madokami", "mangadex", "mangafire", "mangafox",
    "mangafreak", "mangahere", "manganelo", "mangapark", "mangaread",
    "mangareader", "mangataro", "mangatown", "mangoxo", "misskey",
    "mixdrop", "motherless", "myhentaigallery", "myportfolio", "naverblog",
    "naverchzzk", "naverwebtoon", "nekohouse", "newgrounds", "nijie",
    "nitter", "nozomi", "nsfwalbum", "nudostar", "okporn", "paheal",
    "patreon", "pexels", "philomena", "pholder", "photovogue", "picarto",
    "picazor", "pictoa", "piczel", "pillowfort", "pinterest", "pixeldrain",
    "pixiv", "pixnet", "plurk", "poipiku", "poringa", "pornhub", "pornpics",
    "pornstarstube", "postmill", "rawkuma", "reactor", "readcomiconline",
    "realbooru", "reddit", "redgifs", "rule34us", "rule34vault",
    "rule34xyz", "s3ndpics", "sankaku", "sankakucomplex", "scatbooru",
    "scrolller", "seiga", "senmanga", "sexcom", "shimmie2", "simplyhentai",
    "sizebooru", "skeb", "slickpic", "slideshare", "smugmug", "soundgasm",
    "speakerdeck", "steamgriddb", "subscribestar", "sxypix", "szurubooru",
    "tapas", "tcbscans", "telegraph", "tenor", "thefap", "thehentaiworld",
    "tiktok", "tmohentai", "toyhouse", "tumblr", "tumblrgallery",
    "tungsten", "turbo", "twibooru", "twitter", "urlgalleries", "unsplash",
    "uploadir", "urlshortener", "vanillarock", "vichan", "vipergirls",
    "vk", "vsco", "wallhaven", "wallpapercave", "warosu", "weasyl",
    "webmshare", "webtoons", "weebcentral", "weebdex", "weibo", "whyp",
    "wikiart", "wikifeet", "wikimedia", "xasiat", "xenforo", "xfolio",
    "xhamster", "xvideos", "yiffverse", "yourlesbians", "zerochan",
    "booru", "moebooru", "foolfuuka", "foolslide", "mastodon", "shopify",
    "lolisafe", "imagehosts", "directlink", "recursive", "oauth", "noop",
    "ytdl", "generic",
]

_cache = []

def find(url):
    """Find a suitable extractor for the given URL"""
    for cls in _list_classes():
        if match := cls.pattern.match(url):
            return cls(match)
    return None

def add(cls):
    """Add 'cls' to the list of available extractors"""
    if isinstance(cls.pattern, str):
        cls.pattern = re_compile(cls.pattern)
    _cache.append(cls)
    return cls

def extractors():
    """Yield all available extractor classes"""
    return sorted(_list_classes(), key=lambda x: x.__name__)

def _list_classes():
    """Yield available extractor classes"""
    yield from _cache

def main():
    """Main entry point - stub for CLI compatibility"""
    print("gallery_dl version", __version__)
    return 0