---
name: reel-cutaway-storyboard
metadata:
  version: "0.1.0"
description: Turn an uploaded reel, video file, or playable link into a visual editing storyboard with timed B-roll cutaways. Use when the user asks where to cut away, what insert to show, or how to storyboard an existing short video. Not for a new story from a topic alone.
---

# Reel Cutaway Storyboard

Deliver one portable visual board an editor can use while scrubbing the original reel. Adapt the beat count, framing and visual style to the footage. Keep the original timeline and audio as the backbone.

## Read the reel

- Use the attached media or local file. For a link, open the actual media through an available player or retrieve a playable copy in a working directory. A direct video URL can be saved as media. For supported public watch pages, a local command such as `yt-dlp --no-playlist -o "work/reel.%(ext)s" -- URL` can resolve the video. Pass the URL as one literal argument. Verify playback or probe the video stream before analysis. If the link requires access or yields only a thumbnail, ask for an upload or playable share link.
- Watch through the ending, record duration and display orientation, and listen to the audio or read timed captions. For file-based review, use ffprobe for metadata and ffmpeg to extract representative frames at source timestamps. Sample more closely around quick cuts, reveals and gestures. If speech is inaccessible, use visible actions as cues and disclose the audio limitation. Quote only words verified against the recording or captions.
- Divide the whole reel into consecutive beats at changes in action, meaning, or emphasis. For each, record start and end times, a visible or audible cue, and a representative source frame. Identify B-roll already in the reel so an additional insert contributes something new.

## Design the cutaways

Keep the face on screen when expression carries the beat. Cut away when a detail, location, example or reaction would help the viewer understand what the reel is saying or doing. Match the proposed shot to an exact word, sound or visible action. Let the underlying voice or ambience continue unless the cut calls for a specific sound change.

For each insert, choose an in and out time within its beat, a concrete subject and action, shot size or angle, and a return cue. Specify where the editor can get the shot: a verified moment elsewhere in the reel with its source time, a pickup to film, or an asset to source. Label proposed imagery as a concept. Keep existing and proposed footage visually distinct. A hold on the original is a valid editorial decision.

## Make the visual board

Build a chronological HTML board with one card per beat. Pair an actual frame from the reel with an illustrated or photographic concept for each proposed cutaway. Preserve the reel's display aspect ratio in the frames. When image generation is unavailable, draw a simple blocking sketch showing the subject, framing and movement. A text-only shot list leaves the visual deliverable incomplete.

The bundled renderer produces a single HTML file with embedded images. Prepare its JSON input in scratch space. Use an object with a `title`, numeric `duration` in seconds, and a `beats` list. Each beat has numeric `start`, `end`, and strings `cue`, `source_image` and `audio`. Use a `hold` string giving the reason to stay on the source, or an `insert` object containing numeric `start` and `end`, and strings `image`, `shot`, `sourcing` and `return_cue`. Image paths resolve relative to the JSON. Use PNG, JPEG or WebP.

Run `python scripts/render_board.py plan.json storyboard.html` using the script in this skill folder. Inspect the board, check each suggested edit against the reel at its in and out points, and confirm that every image loads. Deliver the HTML and briefly identify pickups or assets the editor still needs.
