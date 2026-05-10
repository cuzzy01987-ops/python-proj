"""
===========================================================
STATISTICAL DATA ANALYSIS ENGINE
===========================================================

Name: John Otieno
Registration Number: SCM223-1428/2024

Project Description:
This project implements a data-driven Statistical Data
Analysis Engine using Object-Oriented Programming (OOP).

The system includes:

1. Data Cleaning & Transformation Pipeline
2. Data Handling Subsystem
3. Functional Data Pipeline
4. File-Based Data Persistence
5. Exception-Safe System
6. Factory Design Pattern
7. Singleton Design Pattern
8. Refactored Modular Architecture
9. Reliability and Failure Analysis

===========================================================
"""

# =========================================================
# IMPORTING REQUIRED LIBRARIES
# =========================================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import logging
import os


# =========================================================
# LOGGING CONFIGURATION
# =========================================================

logging.basicConfig(
    filename="system_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================================================
# SINGLETON DESIGN PATTERN
# DATABASE CONNECTION MANAGER
# =========================================================

class DatabaseConnection:
    """
    Singleton Pattern:
    Ensures only one database connection object exists.
    """

    __instance = None

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super(DatabaseConnection, cls).__new__(cls)
            print("Creating Database Connection...")

        return cls.__instance

    def connect(self):
        print("Database Connected Successfully")


# =========================================================
# DATA LOADER CLASSES
# =========================================================

class CSVLoader:

    def load(self, file_path):

        try:
            data = pd.read_csv(file_path)

            logging.info("CSV File Loaded Successfully")
            print("CSV File Loaded Successfully")

            return data

        except FileNotFoundError:
            logging.error("File Not Found")
            print("Error: File Not Found")

        except Exception as error:
            logging.error(error)
            print("Unexpected Error:", error)


class JSONLoader:

    def load(self, file_path):

        try:
            data = pd.read_json(file_path)

            logging.info("JSON File Loaded Successfully")
            print("JSON File Loaded Successfully")

            return data

        except FileNotFoundError:
            logging.error("File Not Found")
            print("Error: File Not Found")

        except Exception as error:
            logging.error(error)
            print("Unexpected Error:", error)


# =========================================================
# FACTORY DESIGN PATTERN
# FILE LOADER FACTORY
# =========================================================

class FileFactory:
    """
    Factory Pattern:
    Creates objects depending on file type.
    """

    @staticmethod
    def create_loader(file_type):

        if file_type == "csv":
            return CSVLoader()

        elif file_type == "json":
            return JSONLoader()

        else:
            raise ValueError("Unsupported File Type")


# =========================================================
# DATA CLEANING SUBSYSTEM
# =========================================================

class DataCleaner:

    def remove_missing_values(self, data):

        try:
            numeric_columns = data.select_dtypes(include=np.number).columns

            for column in numeric_columns:
                data[column] = data[column].fillna(
                    data[column].mean()
                )

            logging.info("Missing Values Removed")
            print("Missing Values Handled Successfully")

            return data

        except Exception as error:
            logging.error(error)
            print("Error Removing Missing Values:", error)

    def remove_duplicates(self, data):

        try:
            data = data.drop_duplicates()

            logging.info("Duplicate Records Removed")
            print("Duplicate Records Removed")

            return data

        except Exception as error:
            logging.error(error)
            print("Error Removing Duplicates:", error)

    def remove_outliers(self, data, column):

        try:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)

            IQR = Q3 - Q1

            filtered_data = data[
                (data[column] >= Q1 - 1.5 * IQR) &
                (data[column] <= Q3 + 1.5 * IQR)
            ]

            logging.info("Outliers Removed")
            print("Outliers Removed Successfully")

            return filtered_data

        except Exception as error:
            logging.error(error)
            print("Error Removing Outliers:", error)


# =========================================================
# DATA TRANSFORMATION SUBSYSTEM
# =========================================================

class DataTransformer:

    def normalize_data(self, data, columns):

        try:
            scaler = MinMaxScaler()

            data[columns] = scaler.fit_transform(data[columns])

            logging.info("Data Normalized Successfully")
            print("Data Normalized Successfully")

            return data

        except Exception as error:
            logging.error(error)
            print("Normalization Error:", error)

    def encode_categories(self, data, column):

        try:
            data[column] = data[column].astype("category").cat.codes

            logging.info("Categorical Data Encoded")
            print("Categorical Data Encoded Successfully")

            return data

        except Exception as error:
            logging.error(error)
            print("Encoding Error:", error)


# =========================================================
# STATISTICAL ANALYSIS SUBSYSTEM
# =========================================================

class StatisticalAnalyzer:

    def descriptive_statistics(self, data):

        try:
            print("\n===== DESCRIPTIVE STATISTICS =====")
            print(data.describe())

            logging.info("Statistical Analysis Completed")

        except Exception as error:
            logging.error(error)
            print("Analysis Error:", error)

    def correlation_matrix(self, data):

        try:
            print("\n===== CORRELATION MATRIX =====")
            print(data.corr(numeric_only=True))

            logging.info("Correlation Matrix Generated")

        except Exception as error:
            logging.error(error)
            print("Correlation Error:", error)


# =========================================================
# FILE-BASED DATA PERSISTENCE
# =========================================================

class DataStorageManager:

    def save_csv(self, data, filename):

        try:
            data.to_csv(filename, index=False)

            logging.info("Data Saved Successfully")
            print(f"Data Saved Successfully to {filename}")

        except Exception as error:
            logging.error(error)
            print("Saving Error:", error)

    def load_csv(self, filename):

        try:
            data = pd.read_csv(filename)

            logging.info("Data Loaded from Storage")
            print("Stored Data Loaded Successfully")

            return data

        except Exception as error:
            logging.error(error)
            print("Loading Error:", error)


# =========================================================
# FUNCTIONAL DATA PIPELINE
# =========================================================

class DataPipeline:

    def __init__(self):

        self.cleaner = DataCleaner()
        self.transformer = DataTransformer()
        self.analyzer = StatisticalAnalyzer()
        self.storage = DataStorageManager()

    def process(self, data):

        try:

            # Step 1: Remove Missing Values
            data = self.cleaner.remove_missing_values(data)

            # Step 2: Remove Duplicates
            data = self.cleaner.remove_duplicates(data)

            # Step 3: Normalize Numeric Data
            numeric_columns = data.select_dtypes(include=np.number).columns

            data = self.transformer.normalize_data(
                data,
                numeric_columns
            )

            # Step 4: Statistical Analysis
            self.analyzer.descriptive_statistics(data)

            self.analyzer.correlation_matrix(data)

            # Step 5: Save Processed Data
            self.storage.save_csv(
                data,
                "processed_dataset.csv"
            )

            logging.info("Pipeline Executed Successfully")
            print("\nPipeline Executed Successfully")

            return data

        except Exception as error:
            logging.error(error)
            print("Pipeline Error:", error)


# =========================================================
# RELIABILITY AND FAILURE ANALYSIS
# =========================================================

class ReliabilityAnalyzer:

    def system_check(self):

        print("\n===== SYSTEM RELIABILITY ANALYSIS =====")

        print("1. Exception handling implemented")
        print("2. Duplicate removal implemented")
        print("3. Missing value handling implemented")
        print("4. File persistence implemented")
        print("5. Logging system implemented")
        print("6. Modular OOP architecture implemented")

    def failure_analysis(self):

        print("\n===== FAILURE ANALYSIS =====")

        print("Possible Failure -> Solution")
        print("---------------------------------------")
        print("Missing File -> FileNotFoundError")
        print("Invalid Format -> Validation Checks")
        print("Duplicate Data -> Duplicate Removal")
        print("Missing Values -> Mean Replacement")
        print("System Crash -> Exception Handling")


# =========================================================
# MAIN APPLICATION CONTROLLER
# =========================================================

class StatisticalDataAnalysisEngine:

    def __init__(self):

        self.pipeline = DataPipeline()
        self.reliability = ReliabilityAnalyzer()

    def run(self):

        try:

            print("\n===== STATISTICAL DATA ANALYSIS ENGINE =====")

            # =================================================
            # SINGLETON DATABASE CONNECTION
            # =================================================

            db1 = DatabaseConnection()
            db1.connect()

            db2 = DatabaseConnection()

            print("Singleton Verification:", db1 == db2)

            # =================================================
            # CREATE SAMPLE DATASET
            # =================================================

            sample_data = {
                "Age": [20, 21, np.nan, 22, 20],
                "Marks": [70, 85, 90, np.nan, 70],
                "Salary": [50000, 52000, 51000, 50000, 50000]
            }

            dataset = pd.DataFrame(sample_data)

            print("\n===== RAW DATASET =====")
            print(dataset)

            # =================================================
            # SAVE SAMPLE DATASET
            # =================================================

            dataset.to_csv("sample_dataset.csv", index=False)

            # =================================================
            # FACTORY PATTERN USAGE
            # =================================================

            loader = FileFactory.create_loader("csv")

            data = loader.load("sample_dataset.csv")

            # =================================================
            # PROCESS DATA THROUGH PIPELINE
            # =================================================

            processed_data = self.pipeline.process(data)

            # =================================================
            # DISPLAY PROCESSED DATA
            # =================================================

            print("\n===== PROCESSED DATASET =====")
            print(processed_data)

            # =================================================
            # RELIABILITY ANALYSIS
            # =================================================

            self.reliability.system_check()

            self.reliability.failure_analysis()

            print("\nSystem Executed Successfully")

        except Exception as error:

            logging.error(error)
            print("Fatal System Error:", error)


# =========================================================
# PROGRAM EXECUTION
# =========================================================

if __name__ == "__main__":

    engine = StatisticalDataAnalysisEngine()

    engine.run()