# How to build program for Windows
____
1. Install `pyinstaller` python-package
```
pip install pyinstaller
```
2. Build executable program with command:
```
pyinstaller --onefile FileSorter.py
```
bash
If you need you may also add an icon to the program
```
pyinstaller --onefile -i "icon_path" FileSorter.py
```
