import os
import shutil

trash_path = os.path.expanduser("~/.local/share/Trash/files")
file_to_delete = os.path.join(trash_path, "your_file.txt")

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("File deleted from Trash.")
else:
    print("File not found in Trash.")
