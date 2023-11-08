# VideoAddSubTitles_with_whisper
End to end add (translated) subtitles on video file with whisper which developed by OpenAI.

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

## Run the code to add translated subtitle only:
    python e2e_video_add_subtitles.py --source BBB.mp4 --modelType medium --langFrom ja --langTo zh-TW
