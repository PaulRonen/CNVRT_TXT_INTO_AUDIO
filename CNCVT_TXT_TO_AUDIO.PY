from typing import Text
from gtts import gTTS                        # IMPORTED THIS SO THAT WE CAN PLAY CONVERTED AUDIO
import os

txt='Hi welcome to my GITHUB repository'     # MSG

language = 'en'                              #LANGUAHE


obj=gTTS(text=txt,lang=language ,slow=False) #

obj.save('1st Audio.mp3')                    # SAVING AUDIO

os.system('mpg321 1st Audio.mp3')            #PLAY CONVERTED FILE