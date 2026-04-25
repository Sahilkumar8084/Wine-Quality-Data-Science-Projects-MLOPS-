import os
from src.DATA_SCIENCE_Project import logger
from src.DATA_SCIENCE_Project.config.configuration import DataValidationConfig
import pandas as pd
from pathlib import Path

class DataValidationComponent:
    def __init__(self,config:DataValidationConfig):
        self.config = config
        
    def validate_all_data(self) -> bool:
        """
        Combined Validation: Checks both Column Names and Data Types
        """
        try:
            overall_status = True
            data = pd.read_csv(self.config.data_path, sep=";")
            all_cols = list(data.columns)
            all_schema = self.config.all_schema  # {col_name: dtype}

            # Sabse pehle report start karte hain
            report_lines = ["=== Data Validation Report ===\n"]

            # --- Validation Start ---
            for col, expected_dtype in all_schema.items():
                # 1. Check if column exists
                if col not in all_cols:
                    overall_status = False
                    report_lines.append(f"MISSING COLUMN: [{col}] ❌")
                    continue
                
                # 2. Check datatype
                actual_dtype = str(data[col].dtype)
                if actual_dtype != expected_dtype:
                    overall_status = False
                    report_lines.append(f"DTYPE MISMATCH: [{col}] Expected {expected_dtype}, got {actual_dtype} ❌")
                else:
                    report_lines.append(f"MATCHED: [{col}] ({actual_dtype}) ✅")

            # Final check: Kya CSV mein koi extra faltu column hai jo schema mein nahi hai?
            for col in all_cols:
                if col not in all_schema:
                    overall_status = False
                    report_lines.append(f"UNEXPECTED COLUMN: [{col}] found in CSV ❌")

            # --- Final Status Update ---
            report_lines.append(f"\nOVERALL VALIDATION STATUS: {overall_status}")

            # Ek hi baar file mein write karo (Efficient way)
            with open(self.config.STATUS_FILE, 'w', encoding='utf-8') as f:
                f.write("\n".join(report_lines))

            logger.info(f"Data Validation completed. Status: {overall_status}")
            return overall_status
        
        except Exception as e:
            logger.error("Error occurred during Data Validation Component! ⁉️")
            raise e
        
    # def validate_all_columns(self)-> bool:
    #     try:
    #         validation_status=None
    #         data = pd.read_csv(self.config.data_path,sep=";")
            
    #         all_cols = list(data.columns)
            
    #         all_schema = self.config.all_schema.keys()
            
            
    #         for col in all_cols:
    #             if col not in all_schema:
    #                 validation_status=False
    #                 with open(self.config.STATUS_FILE,'w', encoding='utf-8') as f:
    #                     f.write(f"Validation Status for {col} : {validation_status} ❌")
    #             else:
    #                 validation_status=True
    #                 with open(self.config.STATUS_FILE,'w', encoding='utf-8') as f:
    #                     f.write(f"Validation Status for {col} : {validation_status} ✅")
    #         return validation_status
        
    #     except Exception as e:
    #         logger.error("Something Went wrong...⁉️")
    #         raise e
    
    # def validate_all_datatypes(self) -> bool:
    #     try:
    #         validation_status = True  # Default True maante hain
    #         data = pd.read_csv(self.config.data_path,sep=";")
    #         all_schema = self.config.all_schema # Dictionary: {col_name: dtype_str}

    #         with open(self.config.STATUS_FILE, 'w', encoding='utf-8') as f:
    #             f.write("=== Data Type Validation Report ===\n")
                
    #             for column, expected_dtype in all_schema.items():
    #                 if column not in data.columns:
    #                     validation_status = False
    #                     f.write(f"Column Missing: {column} ❌\n")
    #                     continue
                    
    #                 actual_dtype = str(data[column].dtype)
                    
    #                 if actual_dtype != expected_dtype:
    #                     validation_status = False
    #                     f.write(f"Column {column}: Expected {expected_dtype}, got {actual_dtype} ❌\n")
    #                     print(f"Validation Failed for {column}: ❌")
    #                 else:
    #                     f.write(f"Column {column}: Match ({actual_dtype}) ✅\n")

    #         logger.info(f"Overall Data Type Validation: {validation_status}")
    #         return validation_status

    #     except Exception as e:
    #         logger.error("Something went wrong during datatype validation...⁉️")
    #         raise e
        
            
            
        
        
        
        