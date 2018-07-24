import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

sean_image = face_recognition.load_image_file('project_managers/sean.jpg')
sean_face_encoding = face_recognition.face_encodings(sean_image)[0]

known_face_encodings = [
    sean_face_encoding
]

known_face_names = [
    "Sean"
]