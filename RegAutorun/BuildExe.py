import PyInstaller._main_
import shutil
import os

filename = "malicious.py"
exename = "benign.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd,"USB")

if os.path.isfile(exename):
  os.remove(exename)

#create executable from python script
PyInstaller._main_.run([
  "malicious.py",
  "--onefile",
  "--clean",
  "--log-level=ERROR",
  "--name="+exename,
  "--icon="+icon
])

#Clean up after Pyinstaller
shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("_pycache_")
os.remove(exename+".spec")
