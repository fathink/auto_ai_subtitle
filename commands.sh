








# 对视频文件添加字幕

ffmpeg -i input_video.mp4 -i subtitle.srt -c:v copy -c:a copy -c:s mov_text output_video.mp4




ffmpeg -i xgplayer-demo-360p.mp4 -vf f"subtitles=xgplayer-demo-360p_translate.srt", xgplayer-demo-360p_translate.srt -c:v copy -c:a copy -c:s mov_text output_video.mp4