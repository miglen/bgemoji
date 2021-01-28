#!/usr/bin/env python3
"""Translate Bulgarian text file into English and Emojis."""
from google_trans_new import google_translator
import urllib.parse
import requests
import sys
import time
from os import path
#
# Превод на Под Игото (Ynder the Yoke) в Emojis
# Workflow: Bulgarian > English > EmojiTranslate API > Chars to Emoji Map > Output
# Под Игото в текстов файл: https://chitanka.info/text/3753-pod-igoto
#

def bgemoji(text=None):
    """Translate Bulgarian text file into English and Emojis."""
    # Translate Bulgarian to English
    translator = google_translator()
    text = translator.translate(text,lang_src='bg',lang_tgt='en')
    # Emojitranslate API - words to emoji symbols
    api_url = "https://api.emojitranslate.com/?f=en&t=emoji&o=ft00-&k=jlgivjjmp&d="
    time.sleep(0.1) # API wait time to avoid throttling
    text = requests.get(api_url + urllib.parse.quote_plus(text)).text
    # Letters to emojis
    alphabet_emojis = {
        "a": "🅰️",
        "b": "🅱️",
        "c": "©️",
        "d": "↩️",
        "e": "📧",
        "f": "🎏",
        "g": "⛽️",
        "h": "♓️",
        "i": "ℹ️",
        "j": "🗾",
        "k": "🎋",
        "l": "👢",
        "m": "♏️",
        "n": "♑️",
        "o": "�️",
        "p": "🅿️",
        "q": "🕠",
        "r": "®️",
        "s": "💲",
        "t": "✝️",
        "u": "⛎",
        "v": "♈️",
        "w": "〰️",
        "x": "❎",
        "y": "💹",
        "z": "⚡️",
        "\"": "",
        ",": "",
        ".": "⚫",
        "-": "➖",
        " ": ""}
    emoji_text = ""
    for i in str(text):
        if i.lower() in alphabet_emojis:
            emoji_text = emoji_text + alphabet_emojis[i.lower()]
        else:
            emoji_text = emoji_text + i
    return emoji_text


if __name__ == "__main__":
    if len(sys.argv) > 0:
        if path.isfile(sys.argv[1]):
            outfile = open(sys.argv[1] + "-emoji.txt", "w")
            with open(sys.argv[1]) as file:
                for line in file.read().splitlines():
                    line = line.strip()
                    if line == "":
                        continue
                    else:
                        emojiline = bgemoji(line.strip())
                        print(emojiline, line)
                        outfile.write(emojiline)
            outfile.close()
        else:
            print(bgemoji(sys.argv[1]))
    else:
        print("Give me something?")
