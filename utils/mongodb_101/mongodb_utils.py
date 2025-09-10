from pymongo import MongoClient
import gridfs
from gridfs import GridFS
import config.config as config
import logging
from bson.objectid import ObjectId

logger = logging.getLogger(__name__)

class MongoDBClient:
    def __init__(self, url=None, mongodb=None, mongo_collection=None):
        self.client = MongoClient(url)
        self.db = self.client[mongodb]
        self.collection = self.db[mongo_collection]
        self.fs = gridfs.GridFS(self.db)

    def is_connect(self):
        if self.client.admin.command('ping'):
            return True
        else:
            return False

    def get_info(self):
        return self.client.info

    def add_file_gridfs(self,file_path,predefined_id):
        try:
            logger.info("Starting gridfs...")
            fs = GridFS(self.db, collection=config.MONGO_COLLECTION)
            logger.info("Adding file gridfs")
            with open(file_path, "rb") as audio_file:
                file_id = fs.put(audio_file, filename=file_path.split('/')[-1], _id=ObjectId(predefined_id))
            logger.info(f"Audio file uploaded successfully with ID: {file_id}")

        except FileNotFoundError:
            logger.info(f"Error: File not found at {file_path}")
        except Exception as e:
            logger.info(f"An error occurred: {e}")

    def get_file(self, file_id, destination_path):
        try:
            output_file = self.fs.get(file_id)
            with open(destination_path, "wb") as f:
                f.write(output_file.read())
            logger.info(f"File {file_id} written to {destination_path}")
        except Exception as e:
            logger.error(f"Error retrieving file {file_id}: {e}")

if __name__ == "__main__":
    md_client = MongoDBClient()
    print(md_client.get_info())

