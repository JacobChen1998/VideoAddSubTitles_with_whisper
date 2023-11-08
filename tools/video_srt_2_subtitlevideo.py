

video_file = "/home/k100/develop/whisperTorch/samples/1005智慧照護住民安全辨識輔助系統影片.mp4"
srt_file = "/home/k100/develop/whisperTorch/outputs/1005智慧照護住民安全辨識輔助系統影片.wav_medium.srt"
output_video_file = video_file.replace("samples","outputs")
output_video_file = output_video_file[:-4]+"_addSubtitle"+output_video_file[-4:]

import subprocess
 
cmdLine = f'ffmpeg -i {video_file} -vf subtitles={srt_file} {output_video_file}'
subprocess.call(cmdLine, shell=True)
print("Generate : ", output_video_file)