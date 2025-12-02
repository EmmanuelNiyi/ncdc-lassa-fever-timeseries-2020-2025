# NCDC Lassa Fever Weekly Timeseries Dataset (Nigeria, 2020–2025)

**Version:** 1.0

**Maintainer:** Emmanuel Niyi-Oriolowo

**License:** CC BY 4.0

**Last Updated:** 01-12-2025

---

## **1. Overview**

This repository provides a consolidated and standardized dataset of weekly Lassa fever surveillance data in Nigeria from 2020 to 2025. The dataset is derived from the Nigeria Centre for Disease Control (NCDC) Weekly Epidemiological Reports, which are published as PDF documents.

The primary objective of this dataset is to offer a clean, machine-readable time series suitable for epidemiological analysis, infectious disease modeling, trend assessment, and public-health forecasting.

The dataset includes:

- Weekly suspected, confirmed, probable, and fatal cases
- Epidemiological year and week numbers
- Standardized ISO week start and end dates
- Report identifiers and direct links to source documents
- Documentation of data inconsistencies and extraction anomalies

---

## **2. Files Included**

This repository contains raw extracted outputs, intermediate processed files, finalized datasets, documentation, and reproducible scripts. The structure and purpose of each file are described below.

---

### **2.1 Data Files**

### **Raw Extraction Outputs**

These files represent the initial outputs obtained directly from automated PDF extraction tools. They retain missing values and noise from the source reports.

1. **`lassa_fever_timeseries_data_extracted_with_null.csv`**
    
    Raw extracted data containing missing values as obtained from PDF parsing.
    
2. **`lassa_fever_timeseries_data_extracted_null_filled.csv`**
    
    Same as above, but with missing values filled or inferred during early preprocessing.
    

### **Intermediate Cleaning Outputs**

These files represent partially processed datasets used during the cleaning and validation pipeline.

1. **`lassa_fever_timeseries_intermediate.csv`**
    
    Intermediate dataset produced after structural cleaning, week alignment, and normalization steps.
    

### **Final Datasets**

These files represent the complete and fully validated datasets intended for analysis and publication.

1. **`lassa_fever_timeseries_full.csv`**
    
    Comprehensive dataset containing all variables, including cumulative counts, metadata fields, extraction notes, and source references.
    
2. **`lassa_fever_timeseries_minimal.csv`**
    
    Reduced dataset containing only essential epidemiological variables (e.g., week, year, confirmed cases, deaths) for lightweight modeling and rapid prototyping.
    

---

### **2.2 Documentation**

### **`docs/` Directory**

Contains human-readable documentation describing the dataset, methodology, and metadata.

- **`data_dictionary.md`**
    
    Detailed descriptions of all variables, including definitions, units, formatting conventions, and expected value ranges.
    
- **`methodology.md`**
    
    A comprehensive description of the data extraction, cleaning, validation, and quality assurance procedures used to construct the final dataset.
    
- **`dataset_card.json`**
    
    Machine-readable metadata containing schema definitions, field types, and high-level dataset descriptors consistent with modern dataset documentation standards.
    

---

### **2.3 Scripts**

All scripts used in the data ingestion and cleaning pipeline are provided to ensure reproducibility.

- **`data_ingestion_extended.ipynb`**
    
    Notebook detailing PDF download, report identification, and extraction routines (including OCR and table parsing).
    
- **`data_cleaning.ipynb`**
    
    Notebook implementing cleaning procedures, standardization of epidemiological weeks, cumulative variable generation, and anomaly detection.
    

All scripts are located in the **`scripts/`** directory.

---

## **3. Dataset Structure**

---

| **Column**             | **Type**     | **Constraints**               | **Example**                                     | **Notes**                         |
|------------------------|--------------|-------------------------------|-------------------------------------------------|-----------------------------------|
| `epi_year`             | Integer      | ≥ 2020                        | 2024                                            | Epidemiological year              |
| `epi_week`             | Integer      | 1 ≤ week ≤ 53                 | 12                                              | WHO epi week                      |
| `week_start_date`      | Date         | YYYY-MM-DD format             | 2024-03-18                                      | Monday of epi week                |
| `week_end_date`        | Date         | YYYY-MM-DD format             | 2024-03-24                                      | Sunday of epi week                |
| `suspected_cases`      | Integer      | ≥ 0                           | 87                                              | Clinical/epidemiological criteria |
| `confirmed_cases`      | Integer      | ≥ 0, ≤ suspected_cases        | 42                                              | Laboratory-confirmed              |
| `probable_cases`       | Integer      | ≥ 0, ≤ suspected_cases        | 5                                               | Died/absconded without testing    |
| `deaths`               | Integer      | ≥ 0, ≤ (confirmed + probable) | 8                                               | Lassa fever-attributed deaths     |
| `extraction_method`    | String       | "manual" or "automated"       | "automated"                                     | Extraction method used            |
| `extraction_timestamp` | DateTime     | YYYY-MM-DD HH:MM:SS           | 2024-03-25 14:32:01                             | When extraction occurred          |
| `report_pdf_url`       | String (URL) | Valid URL format              | [https://ncdc.gov.ng/](https://ncdc.gov.ng/)... | Source PDF link                   |

## **4. Data Source**

All observations originate from the **Nigeria Centre for Disease Control (NCDC)** Weekly Epidemiological Reports (2020–2025). These reports constitute the authoritative national source for Lassa fever surveillance in Nigeria.

Each observation in the dataset is directly traceable to a specific PDF document using its `report_pdf_url`.

---

## **5. Methodology**

### **5.1 Data Acquisition**

PDFs were downloaded from the NCDC’s publicly accessible archive. Report identifiers were recorded to establish an audit trail and ensure reproducibility.

### **5.2 Data Extraction**

Data were extracted using a combination of automated and manual techniques:

- `pdfplumber` for structured tables and well-formatted reports
- Manual correction for reports with irregular formatting, inconsistent layouts, or non-tabular data presentation

### **5.3 Data Cleaning and Standardization**

Several steps were undertaken to harmonize the dataset:

- Conversion of all reporting weeks to ISO-standard start and end dates
- Normalization of variable names and data types
- Handling of missing, duplicated, or irregular weeks
- Reconciliation of discrepancies with NCDC annual summaries when available

### **5.4 Quality Assurance**

Quality checks included:

- Verification of week-to-week temporal continuity
- Detection of duplicate or misaligned week numbers
- Annotation of anomalies

---

## **6. Potential Applications**

This dataset is suitable for a wide range of analytical and modeling tasks, including:

- Time-series forecasting of infectious disease incidence
- Seasonal and cyclical pattern analysis
- Case fatality ratio estimation
- Outbreak detection and anomaly identification
- Public-health policy evaluation
- Machine learning model development and benchmarking
- Comparative epidemiology across years or regions

---

## **7. Example Usage (Python)**

```python
import pandas as pd

df = pd.read_csv("lassa_fever_weekly_nigeria_2020_2025.csv")

df['week_start_date'] = pd.to_datetime(df['week_start_date'])

# Example: simple weekly confirmed case time series
confirmed_ts = df.set_index('week_start_date')['confirmed_cases']
confirmed_ts.plot(figsize=(12, 4))
```

---

## **8. Limitations**

- Considerable variation in PDF formatting, especially for reports from 2021–2022, required manual intervention.
- Some epidemiological weeks are missing in the official reports and are documented accordingly.
- Probable cases are inconsistently reported across years.
- Cumulative counts reset at the start of each epidemiological year.

These limitations should be taken into account when performing temporal or cross-year comparisons.

---

## **9. Licensing**

This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

Under this license, users are permitted to:

- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, including commercial use

Provided that appropriate credit is given to the dataset creator.

For full licensing terms, refer to the `LICENSE` file or the official license documentation.

---

## **10. Citation**

Users of this dataset should cite it as follows:

```
Niyi-Oriolowo, E. (2025). NCDC Lassa Fever Weekly Timeseries Dataset (Nigeria, 2020–2025).
[https://www.kaggle.com/datasets/emmanuelniyioriolowo/ncdc-lassa-fever-timeseries-20202025](https://www.kaggle.com/datasets/emmanuelniyioriolowo/ncdc-lassa-fever-timeseries-20202025)
```

---

## **11. Contact**

For questions, corrections, or contributions:

**Emmanuel Niyi-Oriolowo**

GitHub: [https://github.com/EmmanuelNiyi](https://github.com/YOUR_USERNAME)

Email: emmanuelniyioriolowo@gmail.com