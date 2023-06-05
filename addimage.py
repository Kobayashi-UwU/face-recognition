import cv2
import face_recognition
import os, sys
import face_recognition
import numpy as np
import shutil
import datetime

id_of_image = input("Enter your ID: ")
name_of_image = input("Enter your Name: ")

file_path_image = "encodedimage.npy"
file_path_name = "encodedname.npy"
file_path_id = "encodedid.npy"

if name_of_image != None:
    cap = cv2.VideoCapture(0)
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow("Camera", frame)

        # Check if 't' key is pressed
        if cv2.waitKey(1) & 0xFF == ord(" "):
            # Save the captured image
            cv2.imwrite(f"./add_to_database/{name_of_image}.jpg", frame)
            print("Image captured.")
            break
    cap.release()
    cv2.destroyAllWindows()
    face_image = face_recognition.load_image_file(
        f"./add_to_database/{name_of_image}.jpg"
    )
    face_encodings = face_recognition.face_encodings(face_image)
    if len(face_encodings) > 0:
        folder_path = "./add_to_database"
        if len(os.listdir(folder_path)) == 0:
            print("There is no image to add to Database")
        else:
            if os.path.getsize(file_path_image) == 0:
                known_face_encodings = np.empty((0, 128))
                face_names = []
                for image in os.listdir("add_to_database"):
                    face_image = face_recognition.load_image_file(
                        f"add_to_database/{image}"
                    )
                    face_encodings = face_recognition.face_encodings(face_image)

                    if len(face_encodings) > 0:
                        face_encoding = face_encodings[0]
                        known_face_encodings = np.concatenate(
                            (known_face_encodings, [face_encoding]), axis=0
                        )
                        face_names.append(image)
                        print(f"added {image}")
                        source_file = f"./add_to_database/{image}"
                        destination_folder = "./already_add_to_database/"
                        shutil.move(source_file, destination_folder)
                face_names = np.array(face_names)
                face_id = []
                face_id.append(id_of_image)
                print(f"{face_id} {face_names}")
                np.save(file_path_image, known_face_encodings)
                np.save(file_path_name, face_names)
                np.save(file_path_id, face_id)

            else:
                known_face_encodings = np.load(file_path_image)
                face_names = np.load(file_path_name)

                for image in os.listdir("add_to_database"):
                    face_image = face_recognition.load_image_file(
                        f"add_to_database/{image}"
                    )
                    face_encodings = face_recognition.face_encodings(face_image)

                    if len(face_encodings) > 0:
                        face_encoding = face_encodings[0]
                        known_face_encodings = np.concatenate(
                            (known_face_encodings, [face_encoding]), axis=0
                        )
                        face_names = np.concatenate((face_names, [image]))
                        print(f"added {image}")
                        source_file = f"./add_to_database/{image}"
                        destination_folder = "./already_add_to_database/"
                        shutil.move(source_file, destination_folder)
                face_id = np.array(id_of_image)
                know_face_id = []
                know_face_id = np.load(file_path_id)
                know_face_id = np.append(know_face_id, face_id)
                print(f"{know_face_id} {face_names}")
                np.save(file_path_image, known_face_encodings)
                np.save(file_path_name, face_names)
                np.save(file_path_id, know_face_id)

    else:
        print("No face found.")
        os.remove(f"./add_to_database/{name_of_image}.jpg")
else:
    print("Need name of picture")
