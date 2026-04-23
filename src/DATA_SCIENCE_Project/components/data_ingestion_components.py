import urllib.request as request
import zipfile
from src.DATA_SCIENCE_Project import logger
from src.DATA_SCIENCE_Project.entity.config_entity import DataIngestionConfig
import os
#Componenet of the Data Ingestion

class DataingestionComponent:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        #Here we ar Downlaoding the Data
        
    def download_data(self):
        try:
            # Sudhaar 1: Folder check aur create karna
            os.makedirs(os.path.dirname(self.config.local_data_files), exist_ok=True)

            if not os.path.exists(self.config.local_data_files):
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_files
                )
                logger.info(f"{filename} download! with following info: \n{headers}")
            else:
                # File size check karna bhi achhi practice hai
                file_size = os.path.getsize(self.config.local_data_files)
                logger.info(f"File already exists with size: {file_size} bytes")
                
        except Exception as e:
            logger.error(f"Error downloading the file from {self.config.source_URL}")
            raise e        
        
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_files,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
            