import os
import face_recognition
import cv2

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

face_names = []
known_faces = []

print('Encoding Faces...')
# encode all faces in project_managers directory
for root, dirs, files in os.walk('./known_faces'):
    for filename in files:
        face_names.append(filename)
        path = 'known_faces/{}'.format(filename)
        image = face_recognition.load_image_file(path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(face_encoding)

print('Comparing with photo')
# load image to check
# unknown_image_path = 'mexico_group_photo.jpg'
unknown_image_path = 'group_photo_bright.jpg'
unknown_image = face_recognition.load_image_file(unknown_image_path)

# get location of each face in image
face_locations = face_recognition.face_locations(unknown_image)

# encode all faces
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# group_photo_encoding = face_recognition.face_encodings(group_photo)[0]


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    results = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.4)

    if True in results:
        first_match_index = results.index(True)
        name = face_names[first_match_index]
        print('Found: {}'.format(name))

# for index, name in enumerate(face_names):
#     if results[int(index)]:
#         print('Found Person: {}'.format(name))
