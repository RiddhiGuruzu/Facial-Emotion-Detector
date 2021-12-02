#librries to be installed
import PySimpleGUI as sg
import cv2
from deepface import DeepFace
import webbrowser

faceCascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
sg.theme('DarkBlue12')

layout = [
    [sg.Text('Welcome! Click open camera to begin.', font=("Helvetica", 25), text_color='white')],
    [sg.Text('Click s on your keyboard to play recommended songs.', font=("Helvetica", 20), text_color='white')],
    [sg.Text('Click m on your keyboard to play recommended movies.', font=("Helvetica", 20), text_color='white')],
    [sg.Button("Open Camera", font=("Times New Roman", 20))],]

window = sg.Window('Facial Emotion Detector', layout, size=(800,300))

vid = cv2.VideoCapture(0)
while True:
    event, values = window.read()
    if event == "Open Camera":
        while (True):
            ret, frame = vid.read()
            result = DeepFace.analyze(frame, actions=['emotion'])
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(gray, 1.1, 4)

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.putText(frame,
                        result['dominant_emotion'],
                        (50, 50),
                        font, 3,
                        (0, 0, 255),
                        2,
                        cv2.LINE_4)

            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                    if result['dominant_emotion']=='happy':
                        happys="https://www.audionetwork.com/browse/m/mood-emotion/mood-emotion/happy-sprightly-jolly/results"
                        webbrowser.open(happys)

                    elif result['dominant_emotion']=='sad':
                        sads= "https://www.audionetwork.com/browse/m/mood-emotion/mood-emotion/sad/results"
                        webbrowser.open(sads)

                    elif result['dominant_emotion'] == 'neutral':
                        neutrals = "https://www.audionetwork.com/browse/m/mood-emotion/mood-emotion/neutral/results"
                        webbrowser.open(neutrals)

                    elif result['dominant_emotion'] =='surprise':
                        supriseds = "https://www.audionetwork.com/browse/m/mood-emotion/mood-emotion/drama-general/results"
                        webbrowser.open(supriseds)

                    elif result['dominant_emotion'] == 'angry':
                         angrys = "https://www.audionetwork.com/browse/m/mood-emotion/mood-emotion/anger-aggression/results"
                         webbrowser.open(angrys)

                    elif result['dominant_emotion'] == 'fear':
                         fears = "https://www.audionetwork.com/browse/m/mood-emotion/mood-emotion/ghostly-eerie-spooky/results"
                         webbrowser.open(fears)

                    elif result['dominant_emotion'] == 'disgust':
                        disgusts = "https://www.audionetwork.com/browse/m/mood-emotion/mood-emotion/dream-heavenly-flight/results"
                        webbrowser.open(disgusts)

            elif cv2.waitKey(1) & 0xFF == ord('m'):
                    if result['dominant_emotion'] == 'happy':
                        happym = "https://www.imdb.com/search/title/?genres=musical&title_type=feature&sort=moviemeter"
                        webbrowser.open(happym)

                    elif result['dominant_emotion'] == 'sad':
                        sadm = "https://www.imdb.com/list/ls053456706/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"
                        webbrowser.open(sadm)

                    elif result['dominant_emotion'] == 'neutral':
                        neutralm = "https://www.imdb.com/search/title/?genres=sport&title_type=feature&sort=moviemeter"
                        webbrowser.open(neutralm)

                    elif result['dominant_emotion'] == 'surprise':
                        suprisedm = "https://www.imdb.com/search/title/?genres=drama&title_type=feature&sort=moviemeter"
                        webbrowser.open(suprisedm)

                    elif result['dominant_emotion'] == 'angry':
                        angrym = "https://www.imdb.com/list/ls053456706/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"
                        webbrowser.open(angrym)

                    elif result['dominant_emotion'] == 'fear':
                        fearm = "https://www.imdb.com/search/title/?genres=thriller&title_type=feature&sort=moviemeter"
                        webbrowser.open(fearm)

                    elif result['dominant_emotion'] == 'disgust':
                        disgustm = "https://www.imdb.com/search/title/?genres=comedy&title_type=feature&explore=genres"
                        webbrowser.open(disgustm)


vid.release()
window.close()
