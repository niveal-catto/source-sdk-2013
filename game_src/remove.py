import os
import subprocess
from os import walk

CWD = r"u:\main\source-sdk-2013"

# print("_\nmisc")

def delf(path, file: str):
    if file == "Release" or file == "_vpc_":
        os.system(f"del {CWD}\\{path}\\{file} /q /s")
        os.system(f"rmdir {CWD}\\{path}\\{file} /q /s")
    else:
        try:
            os.system(f"del {CWD}\\{path}\\{file}")
            print(f"Deleted file - {CWD}\\{path}\\{file}")
        except Exception as e:
            # print(e)
            print(f"Unable to delete file - {CWD}\\{path}\\{file}")
    

def has_flag(file: str):
    flags = [
        ".vcxproj",
        ".vpc_cache",
        "Release",
        "_vpc_"
    ]
    for flag in flags:
        if flag in file:
            return True
    return False

try:
    # what = input("Remove: ")


    for file in os.listdir(CWD + "\\game\\tf\\bin\\x64"):
        if file.endswith(".pdb"):
            delf("game\\tf\\bin\\x64", file)
    for file in os.listdir(CWD + "\\src\\vgui2\\vgui_controls"):
        if has_flag(file):
            delf("src\\vgui2\\vgui_controls", file)
    for file in os.listdir(CWD + "\\src\\vgui2\\matsys_controls"):
        if has_flag(file):
            delf("src\\vgui2\\matsys_controls", file)
    for file in os.listdir(CWD + "\\src\\utils\\vvis_launcher"):
        if has_flag(file):
            delf("src\\utils\\vvis_launcher", file)
    for file in os.listdir(CWD + "\\src\\utils\\vvis"):
        if has_flag(file):
            delf("src\\utils\\vvis", file)
    for file in os.listdir(CWD + "\\src\\utils\\vtfdiff"):
        if has_flag(file):
            delf("src\\utils\\vtfdiff", file)
    for file in os.listdir(CWD + "\\src\\utils\\vtf2tga"):
        if has_flag(file):
            delf("src\\utils\\vtf2tga", file)
    for file in os.listdir(CWD + "\\src\\utils\\vrad_launcher"):
        if has_flag(file):
            delf("src\\utils\\vrad_launcher", file)
    for file in os.listdir(CWD + "\\src\\utils\\vrad"):
        if has_flag(file):
            delf("src\\utils\\vrad", file)
    for file in os.listdir(CWD + "\\src\\utils\\vice"):
        if has_flag(file):
            delf("src\\utils\\vice", file)
    for file in os.listdir(CWD + "\\src\\utils\\vbsp"):
        if has_flag(file):
            delf("src\\utils\\vbsp", file)
    for file in os.listdir(CWD + "\\src\\utils\\tgadiff"):
        if has_flag(file):
            delf("src\\utils\\tgadiff", file)
    for file in os.listdir(CWD + "\\src\\utils\\serverplugin_sample"):
        if has_flag(file):
            delf("src\\utils\\serverplugin_sample", file)
    for file in os.listdir(CWD + "\\src\\utils\\qc_eyes"):
        if has_flag(file):
            delf("src\\utils\\qc_eyes", file)
    for file in os.listdir(CWD + "\\src\\utils\\motionmapper"):
        if has_flag(file):
            delf("src\\utils\\motionmapper", file)
    for file in os.listdir(CWD + "\\src\\utils\\height2normal"):
        if has_flag(file):
            delf("src\\utils\\height2normal", file)
    for file in os.listdir(CWD + "\\src\\utils\\glview"):
        if has_flag(file):
            delf("src\\utils\\glview", file)
    for file in os.listdir(CWD + "\\src\\utils\\captioncompiler"):
        if has_flag(file):
            delf("src\\utils\\captioncompiler", file)
    for file in os.listdir(CWD + "\\src\\tier1"):
        if has_flag(file):
            delf("src\\tier1", file)
    for file in os.listdir(CWD + "\\src\\raytrace"):
        if has_flag(file):
            delf("src\\raytrace", file)
    for file in os.listdir(CWD + "\\src\\mathlib"):
        if has_flag(file):
            delf("src\\mathlib", file)
    for file in os.listdir(CWD + "\\src\\materialsystem\\stdshaders"):
        if has_flag(file):
            delf("src\\materialsystem\\stdshaders", file)


    for file in os.listdir(CWD + "\\src\\game\\server"):
        if has_flag(file):
            delf("src\\game\\server", file)
    for file in os.listdir(CWD + "\\src\\game\\client"):
        if has_flag(file):
            delf("src\\game\\client", file)
            
        
                
except KeyboardInterrupt:
    exit()