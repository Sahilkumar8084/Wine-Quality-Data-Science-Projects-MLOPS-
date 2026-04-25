import os
import yaml
from src.DATA_SCIENCE_Project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
import urllib.request as request

# Iska use isliye kiya hai taaki agar function mein galat data type pass ho, toh ye turant error de de (Runtime Validation).
@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} Loaded Sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml File is Empty")
    except Exception as e:
        raise e
            
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        
        if verbose:
            logger.info(f"Created Directory of path : {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    try:
        
        with open(path,'w') as f:
            json.dump(data,f,indent=4)
        logger.info(f"Json File Saved to the path: {path}")      

    except Exception as e:
        logger.error(f"unable to Save the Json File of path: {path}")
        raise e
        

@ensure_annotations
def laod_json(path:Path)->ConfigBox:
    try:
        
        with open(path) as f:
            content = json.load(f)
            
        logger.info(f"JSON Loaded Sucessfully ✅ Path: {path}")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"unable to LOAD the Json File ❌ of path: {path}")
        raise e
    
@ensure_annotations
def save_model(data:Any,path:Path):
    try:
        
        joblib.dump(value=data,filename=path)
        logger.info(f"Model Saved Sucessfully ✅ Path: {path}")
        
    except Exception as e:
        logger.error(f"unable to SAVE the MODEL❌ path: {path}")
        raise e
    
@ensure_annotations
def Load_model(path:Path)->Any:
    try:
        
        data  = joblib.load(path)
        logger.info("Binary Model File Loaded From: {path} Sucessfully ✅")
        return data
    except Exception as e:
        logger.error(f"unable to Load the MODEL❌ path: {path}")
        raise e
    
    
