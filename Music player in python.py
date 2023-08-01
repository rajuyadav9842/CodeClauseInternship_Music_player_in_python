from playsound import playsound

print("NO. of available songs on music playlist\n1.flute\n2.Elevated\n3.chequesong")


order = input('Enter the music which you want to play:-')

if "flute" in order:

    playsound('C:\\Users\\User\\Desktop\\musicplayer\\flute.mp3')

elif "Elevated" in order:

    playsound('C:\\Users\\User\\Desktop\\musicplayer\\Elevated.mp3')

elif "chequesong" in order:

    playsound('C:\\Users\\User\\Desktop\\musicplayer\\chequesong.mp3')

