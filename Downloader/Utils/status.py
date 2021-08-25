from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def status_video(video, s_time, e_time, status_name):
    return ffmpeg_extract_subclip(video, s_time, e_time, targetname=status_name)

