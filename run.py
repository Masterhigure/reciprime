import os

scene_names = []

with open("scene_names.txt") as fs:
    scene_names = [s.strip("\n") for s in fs.readlines()]

for scene_name in scene_names:
    movie_path = f"media/videos/{scene_name}/1080p60/{scene_name.capitalize()}.mp4"
    script_mtime = os.path.getmtime("scripts/" + scene_name + ".py")
    movie_mtime = 0
    if os.path.exists(movie_path):
        movie_mtime = os.path.getmtime(movie_path)
        if movie_mtime > script_mtime:
            print(f"Scene {scene_name.capitalize()} up to date")
            continue
    print(f"Scene {scene_name.capitalize()} not up to date")
    os.system(f"manim -qh {'scripts/' + scene_name}.py {scene_name.capitalize()}")

with open("media/videos/tmp.txt", mode="w") as fs:
     fs.writelines([f"file '{scene_name}/1080p60/{scene_name.capitalize()}.mp4'\n" for scene_name in scene_names])

os.system("ffmpeg -f concat -i media/videos/tmp.txt -c copy -y output.mp4")


