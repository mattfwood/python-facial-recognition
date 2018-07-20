import face_recognition
from PIL import Image

image = face_recognition.load_image_file('group_photo2.jpg')
face_locations = face_recognition.face_locations(image)
print(face_locations[0])

for index, face_location in enumerate(face_locations):
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(
        top, left, bottom, right))

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    # pil_image.save('cropped{}.png'.format(index))
