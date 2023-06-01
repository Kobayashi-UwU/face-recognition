import subprocess


key_wait = input("input: ")


if key_wait == "take":
    subprocess.run(["python", "./addimage.py"])
elif key_wait == "recog":
    subprocess.run(["python", "./recognition.py"])
elif key_wait == "delete":
    subprocess.run(["python", "./deletemember.py"])
