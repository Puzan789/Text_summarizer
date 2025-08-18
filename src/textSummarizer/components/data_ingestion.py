## components 
import os 
import urllib.request as request 
import zipfile
from textSummarizer.logging import logger 
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path

# class DataIngestion:
#     def __init__(self,config:DataIngestionConfig):
#         self.config=config
    
#     def download_file(self):
#         if not os.path.exists(self.config.local_data_file):
#             file_name,headers=request.urlretrieve(
#                 url=self.config.source_URL,
#                 filename=self.config.local_data_file,
#             )
#             logger.info(f"{file_name} download! with following info :\n {headers}")
#         else:
#             logger.info(f"File already exists of size : {get_size(self.config.local_data_file)}")
    

#     def extract_zip_file(self):
#         unzip_path = self.config.unzip_dir
#         os.makedirs(unzip_path, exist_ok=True)
#         logger.info(f"Extracting zip file to {unzip_path}")

#         try:
#             with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
#                 zip_ref.extractall(unzip_path)
#             logger.info(f"Extraction completed successfully.")
#         except zipfile.BadZipFile:
#             logger.error(f"Bad zip file: {self.config.local_data_file}")
#             raise
#         except zipfile.LargeZipFile:
#             logger.error(f"Zip file is too large: {self.config.local_data_file}")
#             raise
#         except Exception as e:
#             logger.error(f"An unexpected error occurred during extraction: {e}")
#             logger.error(f"Error details: {str(e)}")  # Capture and print the error details
#             raise

#         # unzip_path=self.config.unzip_dir
#         # os.makedirs(unzip_path,exist_ok=True)
#         # with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
#         #             zip_ref.extractall(unzip_path)
    
    
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not self.config.local_data_file.exists() or os.path.getsize(self.config.local_data_file) == 0:
            try:
                file_name, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file,
                )
                logger.info(f"{file_name} downloaded! with following info:\n{headers}")
                
                # Verify the file is not empty
                if os.path.getsize(self.config.local_data_file) == 0:
                    logger.error("Downloaded file is empty. The download might have failed.")
                    raise Exception("Downloaded file is empty.")
                
            except Exception as e:
                logger.error(f"An error occurred while downloading the file: {e}")
                raise
        else:
            logger.info(f"File already exists with size: {get_size(self.config.local_data_file)}")

    def extract_zip_file(self):
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            logger.info(f"Extracting zip file to {unzip_path}")

            try:
                with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                    zip_ref.extractall(unzip_path)
                logger.info(f"Extraction completed successfully.")
            except zipfile.BadZipFile:
                logger.error(f"Bad zip file: {self.config.local_data_file}")
                raise
            except zipfile.LargeZipFile:
                logger.error(f"Zip file is too large: {self.config.local_data_file}")
                raise
            except Exception as e:
                logger.error(f"An unexpected error occurred during extraction: {e}")
                logger.error(f"Error type: {type(e).__name__}")  # Capture the type of the error
                logger.error(f"Error details: {str(e)}")  # Capture and print the error details
                raise

