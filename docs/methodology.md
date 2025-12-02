# Methodology

## 1\. Overview

This methodology outlines the structured process used to collect, extract, clean, validate, and prepare weekly Lassa fever surveillance data from Nigeria Centre for Disease Control (NCDC) reports for time‑series analysis. The goal was to convert unstructured PDF situation reports into a standardized, machine‑readable dataset suitable for epidemiological modeling, forecasting, and descriptive analytics.

## **2\. Data Sources**

The primary data source was the **NCDC Lassa Fever Situation Report PDFs (SitRep)** covering 2020–2025. These reports provided weekly counts of suspected, probable, confirmed cases, and deaths.

To address missing or inconsistent information in some SitRep documents, the **Weekly Epidemiological Reports (WER)** were also used as a secondary source. These were incorporated later in the pipeline to augment or validate specific weeks, which is detailed in later sections of the methodology.

Data characteristics:

-   **Format:** PDF files (predominantly text-based, some containing embedded tables) and webpages.
-   **Location:** Publicly accessible URLs from NCDC archives.
-   **Structure Variability:** Table formats and layouts varied across years, requiring a flexible extraction workflow.

## 3\. Data Extraction Workflow

Data extraction was split into **automated extraction** and **manual extraction**, depending on the quality and consistency of each PDF.

### **3.1 Automated Extraction**

Automated extraction was used for PDFs containing clean, machine-readable tables.

**Tools & Libraries**

-   `pdfplumber` for text and table parsing
-   Python scripts for looping through URLs, downloading files, and extracting tables
-   `BeautifulSoup` for parsing HTML tables when direct automated scraping was not feasible

**Steps**

1.  Fetched each PDF via script and saved it locally.
2.  Renamed files systematically to maintain consistent version control.
3.  Opened each file with `pdfplumber`.
4.  Attempted table extraction page-by-page.
5.  Parsed extracted rows into a structured list of dictionaries.
6.  Standardized column names, formats, and datatypes.
7.  Extracted additional fields such as **epidemiological week**, **year**, and **report date** to support later formatting.
8.  Appended all extracted data to a cumulative dataframe.

**Note on HTML Extraction**

Because setting up Selenium presented reliability challenges within the kaggle working environment, the **single HTML table containing all PDF download links** on the NCDC website was copied manually and parsed using `BeautifulSoup`. While not a fully automated or scalable approach, this workaround reliably provided the complete list of report URLs needed for bulk PDF retrieval.

### **3.2 Manual Extraction**

Manual extraction was used in cases where automated parsing failed or produced incomplete output. These situations typically occurred when:

-   Table structures were split across pages
-   Data was embedded inside images
-   PDF layouts were inconsistent or text was not machine-readable

**Process**

1.  Identified missing, incomplete, or incorrectly parsed values from the automated output.
2.  Visually cross-checked the affected weeks using the original PDF files.
3.  Entered corrected values into a supplemental CSV file.
4.  Merged the supplemental CSV with the automated extraction output to produce a complete dataset.

**Handling Missing or Broken PDFs**

For **11 weeks**, the SitRep PDF links were missing or broken.

In these cases, the corresponding data was obtained from the **Weekly Epidemiological Reports (WER)**, which provided the same weekly counts needed to fill these gaps.

## 4\. Data Cleaning and Preprocessing

The extracted data underwent several cleaning steps to ensure usability:

-   **Column Standardization:** Normalized naming conventions (e.g., `Confirmed cases` → `confirmed`).
-   **Type Conversion:** Converted numeric fields to integers; ensured week/year were properly formatted.
-   **Missing Data Handling:** Filled missing entries with `0` or `NaN` where appropriate, and derived values from cumulative reports when necessary.
-   **Date Engineering:** Converted epidemiological week + year into actual start/end dates.
-   **Duplication Removal:** Ensured no overlap across intermediate extractions.

## 5\. File Processing

The data processing pipeline saved outputs at multiple stages to enhance reproducibility and traceability.

### PDF Parsing

All PDFs were downloaded and stored locally. Parsing was logged to track extraction issues and facilitate troubleshooting.

### Intermediate CSV

An intermediate CSV was created directly from the automated and manual extractions. This dataset contained raw rows and potential inconsistencies, serving as a checkpoint prior to validation.

### Processed CSV

The final processed CSV represented the cleaned and validated dataset. It included:

-   Standardized column names
-   Completed epidemiological week and year values
-   Engineered start/end date fields
-   Verified counts of confirmed, suspected, probable cases, and deaths

This multi-stage workflow ensured both transparency in data handling and a reproducible record of transformations.

## 6\. Data Validation

To ensure accuracy and reliability, the dataset underwent multiple validation steps:

-   **Cross‑Reference Validation:** Compared extracted values against the original PDFs for each week.
-   **Range Checks:** Verified that numeric fields (e.g., case counts) fell within plausible ranges.
-   **Consistency Checks:** Ensured cumulative weekly trends followed logical epidemiological patterns.
-   **Duplicate Detection:** Checked for repeated entries for the same epidemiological week.

## 7\. Storage and Outputs

### Final Outputs

1.  **Full CSV (`lassa_fever_timeseries_full.csv`):** Contains the complete cleaned dataset along with metadata and auxiliary fields.
2.  **Minimal CSV (`lassa_fever_timeseries_minimal.csv`):** Contains the cleaned dataset stripped of metadata and extraneous columns, ready for analysis.
3.  **Dataset Card:** Documents the data origin, structure, and known limitations.
4.  **Data Dictionary:** Defines all variables and their formats.
5.  **Methodology:** Describes the extraction, cleaning, validation, and processing workflow.

## 8\. Versioning and Reproducibility

To ensure transparency and reproducibility, all code and data transformations were tracked using Git version control, with scripts, notebooks, and data processing steps versioned to allow tracing of changes and reproducibility of the entire pipeline.

## 9\. Limitations

The methodology has several constraints:

-   PDF inconsistencies: Layouts varied across years, complicating full automation.
-   Missing or incomplete reports: Some weeks were absent, and cumulative statistics occasionally contained inconsistencies.
-   Manual verification: Required for accuracy but labor-intensive.
-   Large file sizes: PDF collections are sizable, which may limit storage on platforms such as GitHub. To mitigate this, a zip archive containing all PDFs was uploaded to Google Drive for access.

## 10\. Summary

This methodology outlines a structured and transparent process for transforming unstructured NCDC reports into a clean, validated, analysis-ready Lassa fever timeseries dataset. It integrates automated extraction with targeted manual correction to balance efficiency with accuracy, providing a reproducible workflow suitable for epidemiological research and further analysis.