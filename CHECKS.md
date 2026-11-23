# Release checks

## Structure

The Skillsmith and Codex validators checked the release copy. The ZIP was extracted into a separate directory and the bundled renderer was run there.

## Renderer cases

- A three-second portrait fixture with two beats, one insert and one hold produced a self-contained HTML board. The embedded images were compared byte-for-byte with the input PNGs.
- An insert extending beyond its beat was rejected.
- The development smoke test also retrieved the synthetic video from a local HTTP server. Instagram and TikTok watch-page retrieval and real-world editorial quality remain unverified.

## Discovery

Manual description review only. Automatic selection in a fresh agent session remains untested.

| Prompt | Expected routing |
| --- | --- |
| Storyboard this uploaded reel with timed cutaways. | Select |
| Where should I insert B-roll in the clip at this link? | Select |
| Pair frames from my interview with pickup shots and return cues. | Select |
| Give my cooking reel an edit board showing when to show the hands. | Select |
| Paint an original six-panel story from this topic. | Use a topic-based storyboard skill |
| Transcribe this video. | Use transcription |
| Render the final cut from my completed edit list. | Use video editing |
| Download this clip and tell me its duration. | Use media retrieval and inspection |
