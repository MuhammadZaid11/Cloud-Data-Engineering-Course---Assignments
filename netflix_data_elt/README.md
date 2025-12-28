

## Project Overview
This workflow demonstrates an ELT architecture designed to process a Netflix dataset. Unlike traditional ETL (where transformation happens before loading), this project loads raw data directly into the database first, leveraging the database engine (SQL Server) to handle the transformations.

## Phase 1: Extraction and Loading (E & L)
The process begins with the ingestion of external data.

### Source: The source is the "Netflix Movies and TV Shows" dataset (likely a flat file like CSV).

### Tooling: Python is used as the orchestration tool to download the dataset.

### Action: Python scripts load the data exactly as-is into the SQL Server database, specifically into a designated Raw Data Layer. At this stage, no cleaning is performed; the focus is purely on ingesting the data into the system.

## Phase 2: Data Cleaning and Transformation (T)
Once the data is inside the SQL Server, the transformation phase begins. This involves moving data from the "Raw Data Layer" to the "Final Staging Layer."

The diagram highlights five specific cleaning and transformation operations performed via SQL:

Handling foreign characters: Ensuring non-standard characters (e.g., UTF-8) are correctly encoded.

### Removing duplicates: filtering out redundant records to ensure uniqueness.

### Data Type conversion: Casting columns to their correct formats (e.g., strings to dates, text to integers).

Identify and Populate missing values: Handling nulls through imputation or flagging.

New dimension table: Creating a separate table for countries to normalize the data schema.

## Phase 3: Data Analysis
The final phase utilizes the clean, structured data residing in the Final Staging Layer.

### Method: SQL queries are used to analyze the data.

### Objective: The specific goal listed is "Answering 5 SQL questions," likely business questions regarding trends in Netflix content.

Output: The insights are represented by the chart icon, indicating a reporting or visualization step.
<img width="945" height="418" alt="image" src="https://github.com/user-attachments/assets/25f28147-b0bb-4070-88cf-fa0ffb3218cf" />
