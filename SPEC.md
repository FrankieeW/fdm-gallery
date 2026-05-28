# FDM Gallery Plugin Design Specification

**Date:** 2026-05-28
**Project:** gallery-dl FDM Plugin (codename: `fdm-gallery`)
**Status:** Draft

## Overview

Create an FDM (Free Download Manager) 6 browser extension add-on that wraps the [gallery-dl](https://github.com/mikf/gallery-dl) Python library. This allows FDM to download images/galleries from various image hosting sites using gallery-dl's extractor infrastructure.

**Architecture Reference:** Based on [Elephant](https://github.com/meowcateatrat/elephant) FDM plugin.

## Core Concept

- Wrap gallery-dl's Python codebase as an FDM plugin
- FDM JS parsers call Python scripts via `launchPythonScript`
- gallery-dl outputs JSON metadata via `--dump-json` flag
- JS parsers parse JSON and return FDM-compatible format

## Project Structure

```
fdm-gallery/
├── docs/
│   └── specs/
│       └── 2026-05-28-gallery-plugin-design.md  # This file
├── plugin/
│   ├── manifest.json          # Plugin manifest
│   ├── icon.svg               # Plugin icon
│   ├── tools.js               # Shared utilities (cookies, logging)
│   ├── msgalleryparser.js    # Main single-item gallery parser
│   ├── msbatchparser.js      # Batch/playlist parser
│   ├── gallery-dl/          # Python library (selective files)
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── version.py
│   │   ├── extractor/
│   │   │   ├── __init__.py
│   │   │   ├── common.py
│   │   │   ├── generic.py
│   │   │   └── [select extractors]
│   │   ├── job.py
│   │   ├── config.py
│   │   ├── option.py
│   │   ├── output.py
│   │   └── [other core modules]
│   └── pyproject.toml        # For dependency reference
├── build/
│   ├── build-unix.sh
│   └── build-windows.bat
└── README.md
```

## Plugin Manifest (`manifest.json`)

```json
{
  "uuid": "fdm-gallery",
  "name": "Gallery Downloader",
  "description": "Download image galleries from various sites using gallery-dl",
  "version": "1.0.0",
  "icon": "icon.svg",
  "mediaParser": true,
  "mediaListParser": true,
  "minApiVersion": 6,
  "minFeaturesLevel": 3,
  "targetApiVersion": 6,
  "dependencies": {
    "Python": {"minVersion": "3.8"}
  },
  "permissions": ["launchPython"],
  "scripts": [
    "tools.js",
    "msgalleryparser.js",
    "msbatchparser.js"
  ],
  "updateUrl": "https://example.com/fdm-gallery-update.json"
}
```

## JavaScript Parser Interface

### `msgalleryparser.js` (Single Gallery Parser)

```javascript
var msParser = (function() {
    function MsParser() {}
    MsParser.prototype = {
        parse: function(obj) {
            // 1. Prepare gallery-dl arguments
            // 2. Call: launchPythonScript(requestId, interactive, "gallery_dl/__main__.py", args)
            // 3. Parse JSON output
            // 4. Return FDM-compatible format
        },
        isSupportedSource: function(url) {
            // Delegate to gallery-dl's extractor matching
            return true; // gallery-dl handles URL validation
        },
        supportedSourceCheckPriority: function() { return 0; },
        isPossiblySupportedSource: function(obj) {
            // Check content type / URL format
        },
        overrideUrlPolicy: function(url) { return true; },
        minIntevalBetweenQueryInfoDownloads: function() { return 300; }
    };
    return new MsParser();
}());
```

### `msbatchparser.js` (Playlist/Batch Parser)

For galleries with multiple images, gallery-dl handles batch download internally. This parser may be a pass-through or minimal wrapper.

## gallery-dl Integration

### Argument Mapping

| gallery-dl arg | Purpose |
|----------------|---------|
| `--dump-json` | Output structured JSON instead of downloading |
| `-G` | Process gallery as playlist |
| `--cookies` | Browser cookie authentication |
| `--user-agent` | Spoof user agent if needed |
| `--proxy` | Use FDM proxy settings |

### JSON Output Format (gallery-dl `--dump-json`)

gallery-dl outputs one JSON object per line for each image:

```json
{
  "url": "https://i.pximg.net/img-original/img/2024/01/15/00/00/123456789_p0.jpg",
  "extension": "jpg",
  "filename": "123456789_p0.jpg",
  "num": 0,
  "author": {"id": 123456, "name": "artist_name"},
  "gallery_title": "Gallery Name",
  "gallery_id": "abc123",
  "title": "Image Title",
  "date": "2024-01-15T00:00:00",
  "width": 1920,
  "height": 1080
}
```

### Output Transformation

JS parser transforms gallery-dl JSON to FDM format:

```javascript
{
    id: "gallery_id",
    title: "Gallery Title",
    webpage_url: "https://source.site/gallery/123",
    upload_date: "2024-01-15",
    formats: [{
        url: "https://i.pximg.net/img-original/img/...",
        ext: "jpg",
        protocol: "https"
    }]
}
```

## Cookie/Authentication Handling

Same approach as Elephant:

1. Check `App.pluginsAllowWbCookies`
2. If browser cookies available, write to Netscape format temp file
3. Pass `--cookies <path>` to gallery-dl
4. Fallback: try Firefox as default browser

## Build Process

```bash
# Unix
cd build && ./build-unix.sh

# Windows
build\build-windows.bat
```

Build script:
1. Clean previous dist
2. Copy required Python files from gallery-dl
3. `zip -r fdm-gallery.fda plugin/`

## Extractor Selection

**Full list:** https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md

**Priority extractors to include:**
- Pixiv (artwork, novels)
- Twitter/X
-微博
-小红书
- Danbooru/ Gelbooru (anime art)
- Reddit
- Tumblr
- Instagram
- Unsplash
- Lofter
- EHentai/ NHentai

**Rationale:** These are most commonly requested and well-maintained.

## Open Questions

1. **Extractor auto-detection** - gallery-dl auto-detects site from URL. Should plugin also filter by known supported sites for performance?
2. **Pixiv OAuth** - Pixiv requires OAuth for full access. Elephant doesn't handle auth. Consider: optional login prompt?
3. **Error handling** - gallery-dl returns non-zero exit codes for various errors. Map to FDM error format.

## Implementation Notes

- Use `launchPythonScript(requestId, interactive, "gallery_dl/__main__.py", args)`
- gallery-dl's `__main__.main()` returns exit code, not JSON
- JSON is written to stdout
- Need to capture stdout separately from process output

## Next Steps

1. Create project scaffold
2. Copy and prune gallery-dl Python codebase
3. Implement `msgalleryparser.js`
4. Test with one site (Pixiv recommended)
5. Add more extractors
6. Build and release