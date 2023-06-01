import cv2
import face_recognition
import os

name_of_image = input("Enter your Name: ")

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
    try:
        face_encodings = face_recognition.face_encodings(
            f"./add_to_database/{name_of_image}.jpg"
        )
    except Exception as e:
        print("Error: not found humen face")
        os.remove(f"./add_to_database/{name_of_image}.jpg")

#
else:
    print("Need name of picture")
