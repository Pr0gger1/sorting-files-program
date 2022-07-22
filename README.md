# How to build program for Windows
____
1. Install `pyinstaller` python-package
```bash
pip install pyinstaller
```
2. Build executable program with command:
```bash
pyinstaller --onefile FileSorter.py
```
If you need you may also add an icon to the program
```
pyinstaller --onefile -i "icon_path" FileSorter.py
```
