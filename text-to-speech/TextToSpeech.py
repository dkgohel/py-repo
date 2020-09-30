from gtts import gTTS

text=input("Enter text to convert into Speech : ")
language="en"
voice=gTTS(text=text,lang=language,slow=False)
voice.save("convert.mp3")