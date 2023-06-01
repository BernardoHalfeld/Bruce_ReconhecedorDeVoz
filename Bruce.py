import speech_recognition as sr

rec = sr.Recognizer()

#print(sr.Microphone().list_microphone_names())
with sr.Microphone() as mic:
    print("Senhor, inicialização concluída, já pode começar a falar:")

    while True:
        #cancelar ruídos
        rec.adjust_for_ambient_noise(mic)
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
        if texto == "encerrar":
            print("Programa encerrado senhor, até a próxima")
            break
        

