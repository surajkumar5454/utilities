import face_recognition
import os
import shutil

# Load the jpg file into a numpy array
sample = face_recognition.load_image_file("images/img.jpg")
face_locations = face_recognition.face_locations(sample)
sample_encode = face_recognition.face_encodings(sample)[0]

path = 'images'
destination = 'destination'
filelist = os.listdir(path)
print(filelist)

for file in filelist:
    test = face_recognition.load_image_file(f"{path}/{file}")
    test_face_locations = face_recognition.face_locations(test)
    test_encode = face_recognition.face_encodings(test)[0]
    results = face_recognition.compare_faces([sample_encode], test_encode, 0.5)
    distance = face_recognition.face_distance([sample_encode], test_encode)
    print(results, distance)
    if results[0] == True:
        print("inside")
        shutil.copy(f"{path}/{file}", destination)
