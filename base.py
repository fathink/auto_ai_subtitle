import yaml

import subprocess
from script import translate_tool, audio_tool, whisper_tool

# 基础设置
whisper_model = "turbo"  # 可选:  base, small, medium, turbo

# 设置视频源语言和目标语言， en:英语，zh:中文，ja:日语，ko:韩语
language_from = "ja"  # 源语言
language_to = "zh"  # 目标语言
translate_threads = 10  # 翻译时开启多少线程


def single_run(base_dir, fname):

    video_fpath = f"{base_dir}/{fname}"
    audio_fpath = f"{base_dir}/{fname.split('.')[0]}.aac"
    srt_fpath = f"{base_dir}/{fname.split('.')[0]}.srt"
    srt_translate_fpath = f"{base_dir}/{fname.split('.')[0]}_translate.srt"
    out_video_fpath = f"{base_dir}/{fname.split('.')[0]}_{language_to}.mp4"

    # step1: 提取视频中的音频文件
    audio_tool.audio_extract(video_fpath,  audio_fpath)
    print("audio extract success")

    # step2: 采用whisper实现ASR，生成字幕格式文件
    whisper_tool.do_whisper(audio_fpath, srt_fpath, language_from, model=whisper_model)
    print("whisper success")

    # step3: 翻译字幕文件
    translate_tool.do_translate(srt_fpath, srt_translate_fpath, language_from, language_to, translate_threads)
    print("translate success")

    # step4: 字幕文件添加到视频中
    comand = [
        "ffmpeg",
        '-y',            # 覆盖输出文件
        "-i", video_fpath,
        "-i", srt_translate_fpath,
        "-c:v", "copy",  # 直接复制视频流（不重新编码）
        "-c:a", "copy",  # 直接复制音频流（不重新编码）
        "-c:s", "mov_text",  # 使用 MP4 支持的字幕格式（mov_text）
        out_video_fpath
    ]
    subprocess.run(comand)
    
    print("success")


if __name__ == '__main__':
    base_dir = "data"
    fname = "NHK_news_ja.mp4"

    single_run(base_dir, fname)
