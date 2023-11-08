saveJson = True
modelIdx = 1

import whisper
import time
import json
viocePath = "../samples/1005智慧照護住民安全辨識輔助系統影片.wav"
modelTypes = ["base","medium","large"]
model = whisper.load_model(modelTypes[modelIdx])
result = model.transcribe(viocePath)

t1 = time.time()
result = model.transcribe(viocePath)
t2 = time.time()
print("Time cost : ",t2-t1," (sec)")
print(result["text"])
print("\n")
print(result.keys())

if saveJson:
    saveJsonName = f"../outputs/{viocePath.split('/')[-1]}_{modelTypes[modelIdx]}.json"
    with open(saveJsonName, 'w') as fp:
        json.dump(result, fp)
    print("Save Json successfully")
print("finished")
