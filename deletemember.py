import os
import cv2
import numpy as np
import math

file_path_image = "encodedimage.npy"
file_path_name = "encodedname.npy"
known_face_encodings = np.load(file_path_image)
known_face_encodings = np.array(known_face_encodings, dtype=np.float64)
known_face_names = np.load(file_path_name)
known_face_names = np.array(known_face_names)

remove_name = input("input: ")
remove_name = remove_name + ".jpg"
folder_path = "./already_add_to_database"
file_path = os.path.join(folder_path, remove_name)
for i in range(len(known_face_names) - 1, -1, -1):
    if remove_name == known_face_names[i]:
        print(f"deleting {remove_name}")
        known_face_encodings = np.delete(known_face_encodings, i, axis=0)
        known_face_names = np.delete(known_face_names, i, axis=0)
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            print(f"The file '{remove_name}' does not exist in the folder.")


np.save(file_path_image, known_face_encodings)
np.save(file_path_name, known_face_names)
