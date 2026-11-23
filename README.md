# Reel Cutaway Storyboard

Give your editing agent a short video or playable link. It maps the source timeline into beats and builds a portable HTML board pairing source frames with proposed B-roll. Each insert includes an in-point, out-point, shot description, sourcing note, audio treatment and return cue.

## Install

Run `npx skills add arm-pz/reel-cutaway-storyboard --skill reel-cutaway-storyboard` or extract the release ZIP into your agent's skills directory. For Codex, open a fresh chat and look for `$reel-cutaway-storyboard` in the skill picker.

## Try it

Attach a clip and ask, “Storyboard this reel. Show where to cut away, what to film, and when to come back.” For a linked video, paste the playable URL with the same instruction. For a talking-head edit, try “Find the lines that would benefit from a pickup shot and keep the speaker on screen for the payoff.”

## Requirements

Use an agent that can inspect the footage and prepare visual concepts. The HTML renderer uses Python 3.8 or later and its standard library. FFmpeg and ffprobe support local frame extraction. A watch-page link may require a compatible downloader or a playable upload. The board describes edits for an existing reel. For an illustrated sequence from a topic, use a topic-based storyboard skill.

## Release checks

See the [test record](CHECKS.md) and [changelog](CHANGELOG.md) for version 0.1.0.
