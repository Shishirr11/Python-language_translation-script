# first step is to pip install the library
#!pip install googletrans==4.0.0-rc1
import os
from googletrans import Translator
# this is to check if the file's content is in telugu or not.
def is_telugu_text(file_path):
    '''Check if the content of a file is in telugu'''
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Detect the language of the text using Google Translate
    translator = Translator()
    result = translator.detect(str(text))

    if result.lang == 'te':
        return True
    else:
        return False

def translate_text(input_file, output_file):
    '''Translate the file contents'''
    with open(input_file, 'r', encoding='utf-8') as file:
        telugu_text = file.read()

    translator = Translator()
    translation = translator.translate(str(telugu_text), src='te', dest='hi')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translation.text)

    print(f'Translation completed for {input_file}. Output saved to {output_file}.')
# this function is to travese through the files in the directory given and generate the output files.
def translate_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_name in os.listdir(input_directory):
        input_file = os.path.join(input_directory, file_name)
        output_file = os.path.join(output_directory, file_name.replace('.txt', '_translated.txt'))

        if file_name.endswith('.txt') and is_telugu_text(input_file):
            translate_text(input_file, output_file)

#for actual path in your machine, use 
#curDir= r'D:\codes\python
input_directory = '/content/'
output_directory = '/content/'

translate_directory(input_directory, output_directory)
