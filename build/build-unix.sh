#!/bin/bash
dist="$(pwd)/fdm-gallery.fda"
cd "$(dirname "$0")"/../plugin/
rm -f "$dist"
zip -r "$dist" *