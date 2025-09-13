#!/usr/bin/env bash
set -euo pipefail

SRC_DIR="POLICIES"
DST_DIR="docs/policies"

rm -rf "$DST_DIR"
mkdir -p "$DST_DIR"

# Mirror policies into docs, preserving subdirs
rsync -a --delete "$SRC_DIR"/ "$DST_DIR"/

echo "Synced $SRC_DIR -> $DST_DIR"
