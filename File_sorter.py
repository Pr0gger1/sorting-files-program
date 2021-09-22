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
    'Скрипты': ['py', 'js', 'jar'],
    'Иконки': ['ico'],
    'Шрифты': ['otf', 'ttf', 'fon', 'fnt'],
    'Исполняемые файлы': ['exe', 'msi', 'bat'],
    'Системные файлы': ['sys', 'reg'],
    'Презентации': ['pptx, ppt'],
    'Excel-таблицы': ['xlsx', 'xls'],
    'Торренты': ['torrent'],
    'Веб-страницы': ['html', 'htm']
}

class FileSorter():

  def __init__(self, file_categoryDict: dict, current_rootPath: str):
    self.root = tk.Tk()
    self.root.withdraw()
    
    self.file_categoryDict = file_categoryDict
    self.current_rootPath = current_rootPath
  
  def get_subfolder_paths(self) -> list:                # <-- получение папок из текущего каталога
    return [f.path for f in os.scandir(self.current_rootPath) if f.is_dir()]

  def create_folders_with_categories(self):             # <-- создание папок под категории файлов
    for folder in self.file_categoryDict:
      if not os.path.exists(f'{self.current_rootPath}\\{folder}'):
        os.mkdir(folder)

  def get_file_paths(self) -> list:                     # <-- получение полного пути файлов, лежащих в каталоге
    return [file for file in os.listdir(self.current_rootPath) if os.path.isfile(file)]

  def sort_files(self):       # <-- алгоритм сортировки файлов
    file_paths = self.get_file_paths()

    try:
      for file in file_paths:
        file_path = os.path.join(self.current_rootPath, file)
        file_extension = file.split('.')[-1]

        #пропуск программы-сортировщика
        if file_path.lower() == sys.argv[0]:
          continue

        for type_data, ext in self.file_categoryDict.items():
          if (file_extension in ext):
            shutil.move(file, f'{self.current_rootPath}\\{type_data}\\{file}')

    except:
      messagebox.showerror("Ошибка!", f"Не удалось сортировать некоторые файлы\n{traceback.format_exc()}")
          
  def del_empty_dir(self):
    subfolder_path = self.get_subfolder_paths()

    for dir in subfolder_path:
      if not os.listdir(dir):
        os.chmod(dir, stat.S_IWRITE)
        os.rmdir(dir)

if __name__ == '__main__':
  #Получение каталога, с которого был запущен скрипт
  current_dir = os.getcwd()

  sorter = FileSorter(file_categoryDict = extensions_category, current_rootPath = current_dir)
  sorter.create_folders_with_categories()
  sorter.sort_files()
  sorter.del_empty_dir()