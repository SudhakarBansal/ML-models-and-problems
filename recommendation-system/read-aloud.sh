#!/usr/bin/env bash
# Read a markdown file aloud using edge-tts (neural voice) + ffplay.
# Usage:
#   ./read-aloud.sh research-notes.md              # play immediately
#   ./read-aloud.sh research-notes.md --save       # also save mp3 next to the .md
#   ./read-aloud.sh research-notes.md --voice en-GB-RyanNeural
#   ./read-aloud.sh --list-voices                  # list all available voices

set -euo pipefail

EDGE_TTS="${EDGE_TTS:-$HOME/.local/bin/edge-tts}"
[ -x "$EDGE_TTS" ] || EDGE_TTS="$(command -v edge-tts || true)"
if [ -z "${EDGE_TTS:-}" ] || [ ! -x "$EDGE_TTS" ]; then
  echo "edge-tts not found. Install with: pip install --user --break-system-packages edge-tts" >&2
  exit 1
fi

if [ "${1:-}" = "--list-voices" ]; then
  "$EDGE_TTS" --list-voices | grep -E "en-(US|GB|IN|AU)" | head -30
  exit 0
fi

FILE="${1:?usage: $0 <markdown-file> [--save] [--voice <voice>]}"
shift || true

VOICE="en-US-AriaNeural"
SAVE=0
while [ $# -gt 0 ]; do
  case "$1" in
    --save) SAVE=1; shift ;;
    --voice) VOICE="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 1 ;;
  esac
done

[ -f "$FILE" ] || { echo "file not found: $FILE" >&2; exit 1; }

# Strip markdown to readable plain text.
CLEAN_TEXT="$(python3 - "$FILE" <<'PY'
import re, sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text()
# drop fenced code blocks
src = re.sub(r"```.*?```", " ", src, flags=re.S)
# drop inline code backticks (keep text)
src = re.sub(r"`([^`]*)`", r"\1", src)
# drop images
src = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", src)
# links: keep the link text only
src = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", src)
# tables: drop separator rows like |---|---|
src = re.sub(r"^\s*\|?\s*:?-{2,}.*$", "", src, flags=re.M)
# tables: replace pipes with commas for readability
src = re.sub(r"\s*\|\s*", ", ", src)
# headers: drop leading #'s, keep heading text + period
src = re.sub(r"^\s*#+\s*", "", src, flags=re.M)
# bold/italic markers
src = re.sub(r"\*\*([^*]+)\*\*", r"\1", src)
src = re.sub(r"\*([^*]+)\*", r"\1", src)
src = re.sub(r"__([^_]+)__", r"\1", src)
# blockquote markers
src = re.sub(r"^\s*>\s?", "", src, flags=re.M)
# list bullets
src = re.sub(r"^\s*[-*+]\s+", "", src, flags=re.M)
# horizontal rules
src = re.sub(r"^\s*-{3,}\s*$", "", src, flags=re.M)
# collapse blank lines
src = re.sub(r"\n{3,}", "\n\n", src)
print(src.strip())
PY
)"

OUT_MP3="$(mktemp --suffix=.mp3)"
trap '[ "$SAVE" = "1" ] || rm -f "$OUT_MP3"' EXIT

echo "Generating audio (voice: $VOICE)..." >&2
printf '%s' "$CLEAN_TEXT" | "$EDGE_TTS" --voice "$VOICE" --file /dev/stdin --write-media "$OUT_MP3" --write-subtitles /dev/null

if [ "$SAVE" = "1" ]; then
  KEEP="${FILE%.md}.mp3"
  cp "$OUT_MP3" "$KEEP"
  echo "Saved: $KEEP" >&2
fi

echo "Playing $OUT_MP3" >&2
if command -v mpv >/dev/null 2>&1; then
  # mpv terminal controls: space=pause, q=quit, arrows=seek, [/]=speed, 9/0=volume
  echo "Controls: space=pause, q=quit, ←/→=seek 5s, [/]=speed, 9/0=volume" >&2
  mpv --no-video --term-osd-bar "$OUT_MP3"
else
  # ffplay needs its window for keys to work. Open it (you can minimize it).
  echo "Controls: space=pause, q=quit, ←/→=seek (window must be focused)" >&2
  echo "Tip: install mpv for terminal-only controls -> sudo apt install mpv" >&2
  ffplay -autoexit -loglevel error -x 400 -y 100 "$OUT_MP3"
fi
