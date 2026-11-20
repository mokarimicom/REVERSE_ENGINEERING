
from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips,
    vfx,
    afx
)
from PIL import Image, ImageOps
import numpy as np
from pathlib import Path

# VIDEO SETTINGS
WIDTH = 1920
HEIGHT = 1080
DURATION = 4
TRANSITION = 1
FPS = 30

# LOAD 10 PICTURES
folder = Path("pictures")

files = sorted(
    p for p in folder.iterdir()
    if p.suffix.lower() in [".jpg", ".jpeg", ".png"]
)

if len(files) != 10:
    raise ValueError(f"Expected 10 pictures, found {len(files)}")

clips = []

for i, file in enumerate(files):

    img = Image.open(file).convert("RGB")
    img = ImageOps.fit(img, (WIDTH, HEIGHT))

    clip = (
        ImageClip(np.array(img))
        .with_duration(DURATION)
        .with_mask()
    )

    # CROSS FADE TRANSITION
    if i > 0:
        clip = clip.with_effects([
            vfx.CrossFadeIn(TRANSITION)
        ])

    clips.append(clip)

# JOIN ALL PICTURES
final_video = concatenate_videoclips(
    clips,
    method="compose",
    padding=-TRANSITION
)

# LOAD BACKGROUND MUSIC
music = AudioFileClip("music.mp3")

# LOOP MUSIC AND SET VOLUME
music = music.with_effects([
    afx.AudioLoop(duration=final_video.duration),
    afx.MultiplyVolume(0.25),
    afx.AudioFadeOut(2)
])

# ADD MUSIC
final_video = final_video.with_audio(music)

# EXPORT FINAL VIDEO
final_video.write_videofile(
    "my_slideshow.mp4",
    fps=FPS,
    codec="libx264",
    audio_codec="aac",
    bitrate="8000k"
)

# CLOSE FILES
final_video.close()
music.close()

print("VIDEO CREATED SUCCESSFULLY!")

#pip install moviepy pillow numpy

#python make_video.py
# structure:
# MyVideo/
#   make_video.py
#   music.mp3
#   pictures/
#     01.jpg
#     02.jpg
#     03.jpg
#     ...
#     10.jpg