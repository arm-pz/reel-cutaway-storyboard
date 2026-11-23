"""Render a reel edit plan as a portable, self-contained HTML board."""
import argparse
import base64
import json
import math
from html import escape
from pathlib import Path


def stamp(seconds):
    tenths = round(seconds * 10)
    return f"{tenths // 600:02}:{tenths % 600 / 10:04.1f}"


def span(start, end):
    return f"{stamp(start)} – {stamp(end)}"


def picture(folder, filename, label):
    path = folder / filename
    mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
            ".webp": "image/webp"}[path.suffix.lower()]
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return (f'<figure><figcaption>{label}</figcaption>'
            f'<img alt="{label}" src="data:{mime};base64,{encoded}"></figure>')


def render(plan, folder):
    duration = plan["duration"]
    cursor = 0
    cards = []
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("Duration must be positive and finite")
    for beat in plan["beats"]:
        start, end = beat["start"], beat["end"]
        if abs(start - cursor) > 0.001 or not 0 <= start < end <= duration:
            raise ValueError("Beats must cover the reel in order, without gaps or overlaps")
        cursor = end
        pictures = picture(folder, beat["source_image"], "Source frame")
        if bool(beat.get("insert")) == bool(beat.get("hold")):
            raise ValueError("Each beat needs one insert or one hold")
        if insert := beat.get("insert"):
            if not start <= insert["start"] < insert["end"] <= end:
                raise ValueError("Cutaway falls outside its beat")
            pictures += picture(folder, insert["image"], "Proposed cutaway")
            edit = (f'<p><b>Insert {span(insert["start"], insert["end"])}</b> '
                    f'{escape(insert["shot"])}</p><p><b>Source</b> {escape(insert["sourcing"])}</p>'
                    f'<p><b>Return</b> {escape(insert["return_cue"])}</p>')
        else:
            edit = f'<p><b>Hold on source</b> {escape(beat["hold"])}</p>'
        cards.append(f'<article><h2>{span(start, end)}</h2><p>{escape(beat["cue"])}</p>'
                     f'<section>{pictures}</section>{edit}<p><b>Audio</b> '
                     f'{escape(beat["audio"])}</p></article>')
    if not cards or abs(duration - cursor) > 0.001:
        raise ValueError("Timeline must reach the end of the reel")
    title = escape(plan["title"])
    return f"""<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<style>*{{box-sizing:border-box}}body{{max-width:960px;margin:auto;padding:24px;font:17px/1.5 system-ui;color:#203230}}
h1,h2{{line-height:1.2}}article{{border-top:2px solid #466b66;padding:12px 0 24px;break-inside:avoid}}
section{{display:flex;gap:16px;flex-wrap:wrap}}figure{{margin:0;flex:1 1 200px;min-width:0}}
figcaption{{font-weight:bold}}img{{width:100%;height:clamp(180px,40vh,400px);object-fit:contain;background:#eef1ef}}
b{{margin-right:.4em}}</style><main><h1>{title}</h1>{''.join(cards)}</main></html>"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.plan.read_text(encoding="utf-8-sig"))
    args.output.write_text(render(data, args.plan.parent), encoding="utf-8")
