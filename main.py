# 遍历目录、归并所有文件
# 2022-06-29 ， 涂晓帆
import os
import shutil

for dirpath, dirnames, filenames in os.walk('/Volumes/Seagate Basic/城市之眼资源'):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
        shutil.copy(os.path.join(dirpath, filename) , '/Volumes/Seagate Basic/城市之眼资源all/' + filename)
