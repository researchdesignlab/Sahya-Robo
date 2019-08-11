import face_recognition
import cv2
import os
import speak as spk 
known_face_encodings = []
kfe=[]
nameL=[]#this list is used to store the name of recognised faces


#function to encode the images in dataset
def faceencoding(): 
    
    for path,subdir,fname in os.walk(directory):
        for f in fname:
            img_path=os.path.join(path,f)
            img = face_recognition.load_image_file(img_path)
            face_encoding = face_recognition.face_encodings(img)[0]
            known_face_encodings.append(face_encoding)
        return  known_face_encodings

#names of each person
known_face_names = [
  "Monisha",
  "Vasu",
  "Reona",
  "Riya",
  "Dushyanth",
  "Raghav"
]

directory="C:/Users/asus/Desktop/face_recognition_examples-master/img/new" #path of dataset
kfe=faceencoding()

#live video capture
cam=cv2.VideoCapture(0)#to open the camera
while True:
    rect,test_image=cam.read()#to capture a frame
    face_locations = face_recognition.face_locations(test_image)#x,y,w,h location points of face
    face_encodings = face_recognition.face_encodings(test_image, face_locations)#encoding the captured face
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):  #loop if more than one face exist in captured frame
        matches = face_recognition.compare_faces(kfe, face_encoding)#comparing the images and storeing the result (TRUE or FALSE)

        name = "Unknown Person"
        if True in matches: #if true content of name will be replaced 
            first_match_index = matches.index(True)#selecting the index value of matched face
            name = known_face_names[first_match_index]
            
        if name=="Unknown Person":
            spk.tts("sorry I do not recognize you" )#function call of texttospeech converter
        else:
            if name not in nameL:   
                spk.tts("hello  "+name)#function call of texttospeech converter
                nameL.append(name)

cam.release()#to close the camera

