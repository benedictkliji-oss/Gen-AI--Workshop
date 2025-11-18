# python "c:/Users/Lenovo/gen ai/emotionspeak.py"
import cv2
from deepface import DeepFace
import pyttsx3
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')       # getting details of current voice
engine.setProperty('voice', voices[0].id) 

# Load video from webcam
cap = cv2.VideoCapture(0)
last_emotion = None 
while True:
    key, img = cap.read()
    # Analyze emotion
    results = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)

    # Display emotion on frame
    emotion = results[0]['dominant_emotion']
   

    if emotion and emotion != last_emotion:
        engine.say('Hello Benedict')       # queue phrase
        engine.say(emotion)
        engine.runAndWait()      # speak (blocking while speaking)
        last_emotion = emotion   # update last spoken emotion



    cv2.putText(img, f'Emotion: {emotion}', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Emotion Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()