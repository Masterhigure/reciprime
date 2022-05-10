import os

with open("reciprime.py") as f:
    lines = f.readlines()
    scenes = [line[6:-11] for line in lines if "(m.Scene):" in line]

print(os.stat("reciprime.py").st_mtime)
for scene in scenes:
    path = "media/videos/reciprime/480p15/" + scene + ".mp4"
    print(os.stat(path).st_mtime)

