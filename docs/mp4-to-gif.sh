#!/usr/bin/env bash

# mp4-to-gif file.mp4 duration
# where duration is formatted 00:00:10
# use ffprobe to determine duration of mp4

ffmpeg -y -i $1 -filter_complex "fps=4,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=32[p];[s1][p]paletteuse=dither=bayer" -ss 00:00:00 -t $2 `basename $1 .mp4`.gif
