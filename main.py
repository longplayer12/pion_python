import pyttsx3
from gtts import gTTS
import time
import threading
# # mp3ファイル再生関数。引数はファイルパス（なるべく絶対パス）。
from playsound import playsound

def main():
    '''
    playsound('sample.mp3')
    auto_speech('おはようございます。本日は晴天です。')
    '''
    thread_1 = threading.Thread(target=playsound('sample.mp3'))
    thread_2 = threading.Thread(target=auto_speech('おはようございます。本日は晴天です。'))

    thread_2.start()
    thread_1.start()

# テキスト読み上げ関数。引数はstr型文字列。
def auto_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
