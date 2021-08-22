from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def status_video(video, s_time, e_time, status_name):
    return ffmpeg_extract_subclip(video, s_time, e_time, targetname=status_name)


status_video("test.mp4", 0, 30, "status1.mp4")
status_video("test.mp4", 31, 60, "status2.mp4")
status_video("test.mp4", 61, 90, "status3.mp4")
status_video("test.mp4", 91, 120, "status4.mp4")
status_video("test.mp4", 121, 150, "status5.mp4")
