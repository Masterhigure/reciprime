import os

filenames = [filename for filename in os.listdir()
        if ".py" in filename and filename != "run.py"]

for filename in filenames:
    movie_path = f"media/videos/{filename[:-3]}/480p15/{filename[:-3].capitalize()}.mp4"
    script_mtime = os.path.getmtime(filename)
    movie_mtime = 0
    if os.path.exists(movie_path):
        movie_mtime = os.path.getmtime(movie_path)
        if movie_mtime > script_mtime:
            print(f"Scene {filename[:-3].capitalize()} up to date")
            continue
    print(f"Scene {filename[:-3].capitalize()} up to date")
    os.system(f"manim -ql {filename} {filename[:-3].capitalize()}")


