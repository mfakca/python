
import pyglet
from gtts import gTTS
def konus(x):

    tts = gTTS(text=x, lang='tr')
    tts.save("audio.mp3")
    merhaba=pyglet.resource.media('audio.mp3',streaming=False)
    merhaba.play()
    pyglet.app.run()

