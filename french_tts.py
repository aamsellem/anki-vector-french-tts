#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License isvi distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Permet de lire une phrase en francais sur vector
"""

import anki_vector
from gtts import gTTS
from pydub import AudioSegment

# Texte à convertir en audio
texte = "Cela fonctionne !"

# choix de la langue
langue = 'fr'
# on envoie les paramètres au moteur
tts = gTTS(text=texte, lang=langue, slow=False)

# on sauvegarde en mp3 pas le choix
tts.save('myfile.mp3')

#on convertit le mp3 en wav
sound = AudioSegment.from_mp3("myfile.mp3")
#si l'échantillonnage est trop haut cela ne fonctionne pas
sound = sound.set_frame_rate(16000)

sound.export("myfile.wav", format="wav")

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        #on demande au root de lire notre fichier converti en wav
        robot.audio.stream_wav_file("myfile.wav", 75)

if __name__ == "__main__":
    main()
