from moviepy.editor import VideoFileClip

video_file = "../samples/1005智慧照護住民安全辨識輔助系統影片.mp4"
output_audio_file = "../samples/1005智慧照護住民安全辨識輔助系統影片.wav"
video_clip = VideoFileClip(video_file)
video_clip.audio.write_audiofile(output_audio_file, codec='pcm_s16le')
