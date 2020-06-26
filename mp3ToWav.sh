for f in *.mp3
do 
  ffmpeg -i "$f" "$(basename -s .mp3 $f).wav"
done