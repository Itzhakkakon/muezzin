from time import sleep
from elasticsearch import Elasticsearch
import logging
import config.config as config
from  pprint import pprint

logger = logging.getLogger(__name__)

class ElasticSearchClient:
    def __init__(self):
        self.client = Elasticsearch(config.ES_URL)


    def is_connect(self):
        if self.client.ping():
            return True
        else:
            return False


    def get_info(self):
        return self.client.info


    def create_index(self):
        self.client.indices.delete(index=config.ES_INDEX_DATA, ignore_unavailable=True)
        logger.info('Index deleted')
        self.client.indices.exists(index=config.ES_INDEX_DATA)
        logger.info(f"Index {config.ES_INDEX_DATA} created successfully")


    def create_document(self, document, document_id=None):
        try:
            if document_id:
                response = self.client.index(index=config.ES_INDEX_DATA, document=document, id=document_id)
            else:
                response = self.client.index(index=config.ES_INDEX_DATA, document=document)
            logger.info(f"Document indexed with ID: {response['_id']}")
            sleep(5)
            return response
        except Exception as e:
            logger.error(f"Error indexing document: {e}")
            return None


    def get_document(self, document_id):
        try:
            response = self.client.get(index=config.ES_INDEX_DATA, id=document_id)
            return response['_source']
        except Exception as e:
            logger.error(f"Error retrieving document ID {document_id}: {e}")
            return None


    def update_document(self, document_id, update_data):
        try:
            response = self.client.update(index=config.ES_INDEX_DATA, id=document_id, doc={"doc": update_data})
            logger.info(f"Document ID {document_id} updated successfully")
            return response
        except Exception as e:
            logger.error(f"Error updating document ID {document_id}: {e}")
            return None



if __name__ == "__main__":
    es_client = ElasticSearchClient()
    pprint(es_client.get_info())