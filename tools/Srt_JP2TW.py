from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def translate_srt_file(input_file, output_file, source_lang, target_lang):
    with open(input_file, 'r', encoding='utf-8') as srt_file:
        lines = srt_file.readlines()

    translated_lines = []

    for line in lines:
        if line.strip().isdigit():
            translated_lines.append(line)  # 保留字幕序号
        elif line.strip() == '':
            translated_lines.append(line)  # 保留空行
        else:
            translated_text = translate_text(line, source_lang, target_lang)
            translated_lines.append(translated_text)

    with open(output_file, 'w', encoding='utf-8') as translated_srt_file:
        translated_srt_file.writelines(translated_lines)

# 输入的SRT文件和输出的翻译后SRT文件
input_srt_file = 'input.srt'
output_srt_file = 'translated.srt'

# 指定源语言和目标语言
source_language = 'en'  # 源语言，这里假设是英语
target_language = 'zh-TW'  # 目标语言，这里假设是繁体中文

# 进行SRT文件翻译
translate_srt_file(input_srt_file, output_srt_file, source_language, target_language)
