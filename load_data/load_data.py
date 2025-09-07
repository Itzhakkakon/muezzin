# from pathlib import Path
#
# path = Path("C:\podcasts\download (1).wav")
# meta_data = {
#     "name": path.name,
#     "without_extension": path.stem,
#     "extension":path.suffix,
#     "Parent_directory":path.stat()
# }
#
# print(meta_data)


# from tinytag import TinyTag
#
# tag: TinyTag = TinyTag.get('C:\podcasts\download (1).wav')
# metadata: dict = tag.as_dict()
# print(metadata)
import os
from tinytag import TinyTag
import config

DIRECTORY_PATH = config.DIRECTORY_PATH


def load_data(path):
    path_and_metadata = {}
    if os.path.isdir(path):
        entries = os.listdir(path)
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                # print(f"Processing file: {full_path}")
                tag= TinyTag.get(full_path)
                metadata: dict = tag.as_dict()
                path_and_metadata['path'] = full_path
                path_and_metadata['metadata'] = metadata
                # print(path_and_metadata)
                print(metadata)
            else:
                print(f"Skipping directory: {full_path}")
    else:
        print(f"Error: The path '{path}' is not a valid directory.")

load_data(DIRECTORY_PATH)



# class LoadData:
#     def __init__(self):
#         self.folder_path = DIRECTORY_PATH
#         self.data = {}
#
#     def load(self):
#         if os.path.isdir(self.folder_path):
#             entries = os.listdir(self.folder_path)
#             for entry in entries:
#                 full_path = os.path.join(self.folder_path, entry)
#                 if os.path.isfile(full_path):
#                     print(f"Processing file: {full_path}")
#                     self.data['path'] = full_path
#                     tag= TinyTag.get(full_path)
#                     metadata: dict = tag.as_dict()
#                     self.data[entry] = metadata
#                     print(self.data)
#                     return self.data
#                 else:
#                     print(f"Skipping directory: {full_path}")
#         else:
#             print(f"Error: The path '{self.folder_path}' is not a valid directory.")

