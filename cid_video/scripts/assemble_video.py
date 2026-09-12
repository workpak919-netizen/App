"""Join six 10-second CID clips into one vertical 60-second MP4.

Requires ffmpeg installed and available on PATH.
Run from the repository root:
    python cid_video/scripts/assemble_video.py
"""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CLIPS = ROOT / "output" / "clips"
OUTPUT = ROOT / "output" / "CID_Murghi_Murder_60s.mp4"
LIST = ROOT / "output" / "concat.txt"

files = [CLIPS / f"scene_{i:02d}.mp4" for i in range(1, 7)]
missing = [str(p) for p in files if not p.exists()]
if missing:
    raise SystemExit("Missing clips:\n" + "\n".join(missing))

LIST.parent.mkdir(parents=True, exist_ok=True)
LIST.write_text("".join(f"file '{p.as_posix()}'\n" for p in files), encoding="utf-8")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", str(LIST),
    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
    str(OUTPUT),
]
subprocess.run(cmd, check=True)
print(f"Created: {OUTPUT}")
