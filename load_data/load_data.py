import os
from tinytag import TinyTag
from config import config
from pprint import pprint


class LoadData:
    def __init__(self):
        self.folder_path = config.DIRECTORY_PATH
        self.data = {}

    def load(self):
        if os.path.isdir(self.folder_path):
            entries = os.listdir(self.folder_path) #יוצר ליסט של כל הקבצים בתייקיה
            for entry in entries:
                full_path = os.path.join(self.folder_path, entry) #מחבר ושומר נתיב מלא לקובץ
                if os.path.isfile(full_path):
                    self.data['path'] = full_path #שומר ב-dict את הנתיב לקובץ
                    tag= TinyTag.get(full_path) #מחלץ מידע על הקובץ
                    metadata: dict = tag.as_dict() #שומר את המטה דאטה בקובץ
                    self.data['metadata'] = metadata #מוסיף את המטה דאטה במילון
                    yield self.data
                else:
                    print(f"Skipping directory: {full_path}")
        else:
            print(f"Error: The path '{self.folder_path}' is not a valid directory.")

if __name__ == "__main__":
    data = LoadData()
    for data in data.load():
        pprint(data)