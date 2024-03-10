import sys

from Xray.cloud_storage.s3_operation import S3Operation
from Xray.constants.training_pipeline import *
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging


class DataIngestion:

    def __init__(self, data_ingestion_congig:DataIngestionConfig) -> None:
        self.data_ingestion_config = DataIngestionConfig()
        self.s3 = S3Operation()

    def get_data_from_s3(self) -> None:
        try:
            logging.info("Started the get_data_from_s3 method from Data Ingestion class")
            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.s3_data_folder,
            )
            logging.info("Exited the get_data_from_s3 method from Data Ingestion class")
        except Exception as e:
            raise XRayException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            logging.info("Started the initiate_data_ingestion method from Data Ingestion class")
            self.get_data_from_s3()

            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path,
            )
            logging.info("Exited the initiate_data_ingestion method from Data Ingestion class")
            return data_ingestion_artifact
        except Exception as e:
            raise XRayException(e,sys)
        
        