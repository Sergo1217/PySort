import os

#comfig
dirname = 'D:\pysort'
config_dirs = ['Archives','Torrents','Videos','Pictures','Documents']

config_archives = ['.rar','.7z','.zip']
config_torrents = ['.torrent']
config_videos = ['.mp4','.mkv','avi']
config_pictures = ['.jpeg','.jpg','.png']
config_Documents = ['.doc','.docx','.txt']
config_formats = [config_archives, config_torrents, config_videos, config_pictures, config_Documents]

#starts
dirfiles = os.listdir(dirname)

for dir in config_dirs:
    if not os.path.isdir(os.path.join(dirname, dir)):
        os.mkdir(os.path.join(dirname, dir))


dirs = []
files = []

for file in dirfiles:
    if os.path.isdir(os.path.join(dirname, file)): dirs.append(file)
    if os.path.isfile(os.path.join(dirname, file)): files.append(file)

for j in config_formats:
    folder = config_dirs[config_formats.index(j)]
    for k in j:
        for i in files:
            rez = i.find(k)
            if k == os.path.splitext(i)[1]:
                print(os.path.join(dirname, folder, i))
                print(os.path.splitext(i)[1])
                #os.replace(os.path.join(dirname, i), os.path.join(dirname, folder, i))
