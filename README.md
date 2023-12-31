# VideoAddSubTitles_with_whisper
End to end adding (translated) subtitles on video file with whisper which developed by OpenAI.
For translation, we supported two piplelines, version 2 (v2) has better result. The work-flow as shown in figure
## Follow instructure to use this tool:
    conda create --name whisperTorch python=3.9
    conda activate whisperTorch
    pip install -U openai-whisper
    pip install git+https://github.com/openai/whisper.git 
    pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
    pip install googletrans==4.0.0rc1
    pip install moviepy

## Prepare your video, put it in ./samples/ folder is recommanded.

## Run the code to add subtitle only:
    python e2e_video_add_subtitles.py --source AAA.mp4 --modelType medium
    python e2e_video_add_subtitles_v2.py --source AAA.mp4 --modelType medium

## Run the code to add translated subtitle only:
    python e2e_video_add_subtitles.py --source BBB.mp4 --modelType medium --langFrom ja --langTo zh-TW
    python e2e_video_add_subtitles_v2.py --source BBB.mp4 --modelType medium --langFrom ja --langTo zh-TW

## Work-Flow of transcription:
![pic1](https://github.com/JacobChen1998/VideoAddSubTitles_with_whisper/blob/main/trancribe_constructure.png)

## Work-Flow of tranlation:
![pic2](https://github.com/JacobChen1998/VideoAddSubTitles_with_whisper/blob/main/translate_constructure.png)

