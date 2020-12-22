from gtts import gTTS

if __name__ == "__main__":    
    texto = input("Introduce el texto a convertir: ")
    voz = gTTS(texto, lang='es-us')
    voz.save("audio.mp3")
    
