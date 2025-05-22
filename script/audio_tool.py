import ffmpeg
import subprocess
import os


"""
1.基本命令（提取音频并保存为 MP3/WAV/FLAC 等格式）​

ffmpeg -i input_video.mp4 -vn -acodec copy output_audio.aac

    -i input_video.mp4：输入视频文件路径。
    -vn：禁用视频流（仅提取音频）。
    -acodec copy：直接复制音频流（无重新编码，速度最快，文件大小不变）。
    output_audio.aac：输出音频文件名（支持 .mp3、.wav、.flac 等格式）。

"""


def audio_extract(input_path, output_path):
    """
    解决中文路径ffmpeg无法运行的问题
    """
    # command = [
    #     'ffmpeg',
    #     '-y',            # 覆盖输出文件
    #     '-i', 'pipe:0',  # 从stdin读取输入
    #     '-vn',           # 仅提取音频
    #     '-acodec', 'copy',  # 直接复制音频流
    #     output_path     # 输出文件路径
    # ]

    # with open(input_path, 'rb') as f:
    #     subprocess.run(command, input=f.read())

    command = [
        'ffmpeg',
        '-y',            # 覆盖输出文件
        '-i', input_path,  # 从stdin读取输入
        '-vn',           # 仅提取音频
        '-acodec', 'copy',  # 直接复制音频流
        output_path     # 输出文件路径
    ]

    subprocess.run(command)
