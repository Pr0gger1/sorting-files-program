import os
import sys
import shutil

import stat
import traceback

from tkinter import messagebox
import tkinter as tk

extensions_category = {
    'Фотографии': ['png', 'jpg', 'jpeg', 'svg', 'tiff', 'tif', 'bmp', 'gif', 'webp'],
    'Видео': ['mp4', 'avi', 'mkv', 'mpeg', 'mpg', 'mov', '3g2', '3gp', 'webm'],
    'Документы': ['pdf', 'txt', 'rtf', 'epub', 'doc', 'docx', 'docm'],
    'Архивы': ['zip', 'rar', '7z', 'tar', 'arj', 'iso'],
    'Аудио': ['mp3', 'ogg', 'wav', 'flac', 'aac'],
    'Скрипты': ['py', 'js', 'jar', 'php'],
    'Иконки': ['ico'],
    'Шрифты': ['otf', 'ttf', 'fon', 'fnt'],
    'Исполняемые файлы': ['exe', 'msi', 'bat'],
    'Презентации': ['pptx', 'ppt'],
    'Excel-таблицы': ['xlsx', 'xls'],
    'Торренты': ['torrent'],
    'Веб-страницы': ['html', 'htm']
}

class FileSorter():
  def __init__(self, file_categoryDict: dict, current_rootPath: str):
    self.root = tk.Tk()
    self.root.withdraw()
    
    self.file_categoryDict: dict = file_categoryDict
    self.current_rootPath: str = current_rootPath
    
    
  def __get_extension(self, file: str) -> str:
    return file.split(".")[0]
  
# getting folders from current directory
  def __get_subfolder_paths(self) -> list:
    return [f.path for f in os.scandir(self.current_rootPath) if f.is_dir()]

# creating folders for category files
  def create_folders_with_categories(self) -> None:
    for folder in self.file_categoryDict:
      if not os.path.exists(f'{self.current_rootPath}\\{folder}'):
        os.mkdir(folder)


# getting the absolute path to files in a directory
  def __get_file_paths(self) -> list:
    return [file for file in os.listdir(self.current_rootPath) if os.path.isfile(file)]

# sorting files algorihtm
  def sort_files(self) -> None:
    files: list = self.__get_file_paths()

    try:
      for file in files:
        file_path: str = os.path.join(self.current_rootPath, file)
        file_extension: str = self.__get_extension(file)

        # skip executable program
        if file_path.lower() == sys.argv[0].lower():
          continue

        for type_data, ext in self.file_categoryDict.items():
          if file_extension in ext:
            shutil.move(file, f"{self.current_rootPath}\\{type_data}\\{file}")

    except Exception:
      messagebox.showerror("Ошибка!", f"Не удалось сортировать некоторые файлы\n{traceback.format_exc()}")
          
  def del_empty_dir(self):
    subfolder_path: list = self.__get_subfolder_paths()

    for dir in subfolder_path:
      if not os.listdir(dir):
        os.chmod(dir, stat.S_IWRITE)
        os.rmdir(dir)

if __name__ == '__main__':
  # getting path to current directory
  current_dir: str = os.getcwd()

  sorter = FileSorter(
    file_categoryDict = extensions_category, 
    current_rootPath = current_dir
    )
  sorter.create_folders_with_categories()
  sorter.sort_files()
  sorter.del_empty_dir()