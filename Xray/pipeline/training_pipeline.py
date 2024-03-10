from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging
import sys

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Data Ingestion started for training pipeline")
        try:
            logging.info("getting the data from s3 bucket")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("GOt the train set and test set from s3")
            logging.info("Exiting the start_data_ingestion process of training pipeline")
            return data_ingestion_artifact
        
        except Exception as e:
            raise XRayException(e,sys)

