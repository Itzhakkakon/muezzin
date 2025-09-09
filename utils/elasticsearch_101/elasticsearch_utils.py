from elasticsearch import Elasticsearch
import logging
# from log.login import Logger
import config.config as config
from  pprint import pprint

# logger = Logger.get_logger()
logger = logging.getLogger(__name__)

class ElasticSearchClient:
    def __init__(self):
        self.clinet = config.ES_URL


    async def connect_elastic(self):
        Elasticsearch(self.clinet)
        try:
            if self.clinet.ping():
                logger.info("Connected to Elasticsearch successfully")
                return True
            else:
                logger.error("Could not connect to Elasticsearch")
                return False
        except Exception as e:
            logger.error(f"Error connecting to Elasticsearch: {e}")
            return False


    def get_clinet(self):
        if self.clinet is None:
            self.connect_elastic()
        return self.clinet


    async def create_index(self):
        await self.clinet.indices.delete(index=config.ES_INDEX_DATA, ignore=[400, 404])
        if not self.clinet.indices.exists(index=config.ES_INDEX_DATA):
            await self.clinet.indices.create(index=config.ES_INDEX_DATA, body=None)
            logger.info(f"Index {config.ES_INDEX_DATA} created successfully")
        else:
            logger.info(f"Index {config.ES_INDEX_DATA} already exists")


    async def create_document(self, document, document_id=None):
        try:
            await self.create_index()
            response = self.clinet.index(index=config.ES_INDEX_DATA, document=document, id=document_id)
            logger.info(f"Document indexed with ID: {response['_id']}")
            return response
        except Exception as e:
            logger.error(f"Error indexing document: {e}")
            return None


    def get_document(self, document_id):
        try:
            response = self.clinet.get(index=config.ES_INDEX_DATA, id=document_id)
            return response['_source']
        except Exception as e:
            logger.error(f"Error retrieving document ID {document_id}: {e}")
            return None


    def update_document(self, document_id, update_data):
        try:
            response = self.clinet.update(index=config.ES_INDEX_DATA, id=document_id, doc={"doc": update_data})
            logger.info(f"Document ID {document_id} updated successfully")
            return response
        except Exception as e:
            logger.error(f"Error updating document ID {document_id}: {e}")
            return None



if __name__ == "__main__":
    es_client = ElasticSearchClient()
    es = es_client.get_clinet()
    pprint(es.info())