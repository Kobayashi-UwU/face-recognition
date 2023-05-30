import face_recognition
import os
import numpy as np
import shutil

folder_path = "./add_to_database"
if len(os.listdir(folder_path)) == 0:
    print("There is no image to add to Database")
else:
    file_path_image = "encodedimage.npy"
    file_path_name = "encodedname.npy"

    if os.path.getsize(file_path_image) == 0:
        print("File is empty")
        known_face_encodings = np.empty((0, 128))
        face_names = []

        for image in os.listdir("add_to_database"):
            face_image = face_recognition.load_image_file(f"add_to_database/{image}")
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
        print(face_names)
        np.save(file_path_image, known_face_encodings)
        np.save(file_path_name, face_names)

    else:
        known_face_encodings = np.load(file_path_image)
        face_names = np.load(file_path_name)

        for image in os.listdir("add_to_database"):
            face_image = face_recognition.load_image_file(f"add_to_database/{image}")
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

        np.save(file_path_image, known_face_encodings)
        np.save(file_path_name, face_names)
