'''
Only Add SubTitle
python e2e_video_add_subtitles.py --source AAA.mp4 --modelType medium

Add SubTitle with translate
python e2e_video_add_subtitles.py --source BBB.mp4 --modelType medium --langFrom ja --langTo zh-TW

'''

from moviepy.editor import VideoFileClip
from googletrans import Translator

import subprocess
import argparse

import whisper
import time
import json

'''
modelType : base,medium,large
lang : 0,
        英语：'en'
        中文（简体）：'zh-CN'
        中文（繁体）：'zh-TW'
        日语：'ja'
        西班牙语：'es'
        法语：'fr'
        德语：'de'
        俄语：'ru'
        阿拉伯语：'ar'
        葡萄牙语：'pt'
        意大利语：'it'
        韩语：'ko'
'''
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--source", help="9527", required=True)
parser.add_argument("--output", help="9487", default=0, required=False)
parser.add_argument("--modelType", help="9487", default="medium", required=False)
parser.add_argument("--langTo", help="9487", default=0, required=False)
parser.add_argument("--langFrom", help="9487", default=0, required=False)

args = parser.parse_args()


t1_total = time.time()
output_video_file = None
if args.output is 0:
    idx = args.source.rindex(".")
    output_video_file = args.source[:idx]+"_addSubtitle"+args.source[idx:]
else:
    output_video_file = args.output

def time_transfer(sec_form):
    hr = str(int(sec_form//3600)).zfill(2)
    min = str(int(sec_form//60)).zfill(2)
    sec = sec_form%60
    ms = sec-int(sec)
    sec = int(sec)
    ms = str(int(ms*1000)).zfill(3)
    return f"{hr}:{min}:{sec},{ms}"

def translate(translator,text,source_lang='ja',target_lang='zh-TW'):
    
    translation = translator.translate(text=text, src=source_lang, dest=target_lang)

    return translation.text


### video2voice ###
audio_file = args.source.split("/")[-1]
output_audio_file = "./tmp/" + audio_file[:audio_file.rindex(".")] + ".wav"
video_clip = VideoFileClip(args.source)
video_clip.audio.write_audiofile(output_audio_file, codec='pcm_s16le')

### voice2SubTitles ###
# viocePath = "../samples/1005智慧照護住民安全辨識輔助系統影片.wav"
# modelTypes = ["base","medium","large"]
model = whisper.load_model(args.modelType)
result = model.transcribe(output_audio_file)

print("\n\nStart inference use model : ", args.modelType)
t1 = time.time()
result = model.transcribe(output_audio_file)
t2 = time.time()
print("Inference time cost : ",t2-t1," (sec)")
print(result["text"])
print("\n")
segments = result['segments']


srt_content = ""
translator = None
if args.langTo is not 0:
    translator = Translator()
for i,segment in enumerate(segments):
    idx = segment['id'] + 1
    start = segment['start']
    end = segment['end']
    text = segment['text']
    
    if args.langTo is not 0:
        langTo = args.langTo
        langFrom = args.langFrom

        text = translate(translator,text,source_lang=langFrom,target_lang=langTo)

    start = time_transfer(start)
    end = time_transfer(end)
    
    srt_content += f"{idx}\n"
    srt_content += f"{start} --> {end}\n"
    srt_content += f"{text}\n\n"

SaveSRTPath = output_audio_file.replace(".wav",".srt")
with open(SaveSRTPath, "w", encoding="utf-8") as srt_file:
    srt_file.write(srt_content)
print("Generate file : ",SaveSRTPath)

cmdLine = f'ffmpeg -i {args.source} -vf subtitles={SaveSRTPath} {output_video_file}'
subprocess.call(cmdLine, shell=True)

t2_total = time.time()

print(f"Generate : {output_video_file} => Cost time :  {t2_total -t1_total} (sec)")

