# first step is to pip install the library
#!pip install googletrans==4.0.0-rc1
from googletrans import Translator

def translate_text(input_file, output_file):
    # Read the Telugu text file
    with open(input_file, 'r', encoding='utf-8') as file:
        telugu_text = file.read()
    print(telugu_text)
    # Translate Telugu text to Hindi
    translator = Translator()
    translation = translator.translate(telugu_text, src='te', dest='hi')

    # Save the translated text into a separate file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translation.text)

    print('Translation completed.')


curDir = "/content"

input_file = '/content/telugu.txt'
output_file = '/content/hindi.txt'

translate_text(input_file, output_file)
