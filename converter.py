from os import listdir, getcwd, chdir,mkdir
from os.path import isfile, join, exists
import subprocess
try:
	subprocess.run(['ffmpeg', '-veriosn'])
except Exception as ex:
	print("ffmpeg is not install\n Installing ffmpeg please Input your password")
	subprocess.call(['sudo', 'apt-get', 'install', 'ffmpeg'], shell=True)
converted = join(getcwd(), "converted")
if not exists(converted):
	mkdir(converted)
def convert_mp4_to_mp3(filename):
	subprocess.call(['ffmpeg', '-i', filename, join(converted, f"{filename.split('.')[0]}.mp3")])

files = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
for file in files:
	convert_mp4_to_mp3(file)