import os, os.path
from PIL import Image


DIR = r"C:\Users\admin\PycharmProjects\Maciek_Kamil"
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

previous_root = ""
for root, dirs, files in os.walk(DIR, topdown=True):
    # print("prev root", previous_root)
    depth = root.replace(DIR, "").count("\\")
    print(root.replace(DIR, ""))
    for file in files:
        if file.endswith(".png"):
            os.rename(file, file[:file.rfind(".")] + ".jpg")

        print('\t'*depth, file)
    previous_root = root[:root.rfind("\\")]
