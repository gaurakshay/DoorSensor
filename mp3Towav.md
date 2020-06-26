## For a single file:

    ffmpeg -i input.mp3 output.wav

## For all the files in a folder

    for f in *.mp3
    do 
      ffmpeg -i "$f" "$(basename $f).wav"
    done