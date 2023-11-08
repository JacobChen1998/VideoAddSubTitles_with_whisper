import json
import os

JsonPath = '../outputs/1005智慧照護住民安全辨識輔助系統影片.wav_medium.json'
SaveSRTPath = JsonPath[:-4]+'srt'
f = open(JsonPath)
data = json.load(f)
segments = data['segments']
f.close()

def time_transfer(sec_form):
    hr = str(int(sec_form//3600)).zfill(2)
    min = str(int(sec_form//60)).zfill(2)
    sec = sec_form%60
    ms = sec-int(sec)
    sec = int(sec)
    ms = str(int(ms*1000)).zfill(3)
    return f"{hr}:{min}:{sec},{ms}"

srt_content = ""

for i,segment in enumerate(segments):
    idx = segment['id'] + 1
    start = segment['start']
    end = segment['end']
    text = segment['text']
    
    start = time_transfer(start)
    end = time_transfer(end)
    
    srt_content += f"{idx}\n"
    srt_content += f"{start} --> {end}\n"
    srt_content += f"{text}\n\n"

with open(SaveSRTPath, "w", encoding="utf-8") as srt_file:
    srt_file.write(srt_content)

print("Generate file : ",SaveSRTPath)