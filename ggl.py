import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Language codes and names
LANGUAGES = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian',
    'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian',
    'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish',
    'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish',
    'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek',
    'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'he': 'Hebrew', 'hi': 'Hindi',
    'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish',
    'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer',
    'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian',
    'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay',
    'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)',
    'ne': 'Nepali', 'no': 'Norwegian', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese',
    'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian',
    'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali',
    'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'te': 'Telugu',
    'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh',
    'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'
}

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src_language = src_lang_combobox.get()
    dest_language = dest_lang_combobox.get()

    if text and src_language and dest_language:
        translator = Translator()
        translation = translator.translate(text, src=src_language, dest=dest_language)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translation.text)

# Create main window
root = tk.Tk()
root.title("Language Translation Tool")

# Input text
tk.Label(root, text="Input Text:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
input_text = tk.Text(root, height=10, width=50)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Source language selection
tk.Label(root, text="Source Language:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
src_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
src_lang_combobox.grid(row=2, column=1, padx=10, pady=10)
src_lang_combobox.current(21)  # Default to English

# Destination language selection
tk.Label(root, text="Destination Language:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
dest_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
dest_lang_combobox.grid(row=3, column=1, padx=10, pady=10)
dest_lang_combobox.current(50)  # Default to Spanish

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Output text
tk.Label(root, text="Translated Text:").grid(row=5, column=0, padx=10, pady=10, sticky='w')
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
