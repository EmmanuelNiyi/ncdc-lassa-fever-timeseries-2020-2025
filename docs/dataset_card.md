# **📘 Dataset Card:** NCDC Lassa Fever Timeseries (2020–2025)

## **Dataset Summary**

This dataset provides a structured, machine-readable compilation of **weekly Lassa fever surveillance data in Nigeria from 2020 to 2025**, extracted from the Nigeria Centre for Disease Control (NCDC) weekly situation reports.

It includes:

-   Suspected, confirmed, and probable cases
-   Weekly deaths
-   Epidemiological week/year
-   Standardized week start and end dates
-   Source PDF links
-   Metadata and extraction details

Each row represents **one epidemiological week**.

## **Supported Tasks and Use Cases**

-   Time-series forecasting (ARIMA, Prophet, RNNs, Transformers)
-   Outbreak trend analysis
-   Epidemiology and disease modeling
-   Mortality and case-fatality rate (CFR) calculations
-   Environmental or seasonal correlation studies
-   Data quality auditing
-   ML benchmarking on real-world, sparse surveillance data

## **Languages**

-   English
-   Numerical data

## **Dataset Structure**

### **Data Fields**

| **Column**              | **Type**     | **Constraints**               | **Example**             | **Notes**                          |
|-------------------------|--------------|-------------------------------|-------------------------|------------------------------------|
| `epi_year`              | Integer      | ≥ 2020                        | 2024                    | Epidemiological year               |
| `epi_week`              | Integer      | 1–53                          | 12                      | WHO epidemiological week           |
| `week_start_date`       | Date         | YYYY-MM-DD                    | 2024-03-18              | Monday of epi week                 |
| `week_end_date`         | Date         | YYYY-MM-DD                    | 2024-03-24              | Sunday of epi week                 |
| `suspected_cases`       | Integer      | ≥ 0                           | 87                      | Clinical/epidemiological suspicion |
| `confirmed_cases`       | Integer      | ≥ 0, ≤ suspected_cases        | 42                      | Laboratory-confirmed cases         |
| `probable_cases`        | Integer      | ≥ 0, ≤ suspected_cases        | 5                       | Probable cases not confirmed       |
| `deaths`                | Integer      | ≥ 0, ≤ (confirmed + probable) | 8                       | Lassa fever-attributed deaths      |
| `extraction_method`     | String       | "manual", "automated"         | "automated"             | Method used to extract data        |
| `extraction_timestamp`  | DateTime     | YYYY-MM-DD HH:MM:SS           | 2024-03-25 14:32:01     | Timestamp of extraction            |
| `report_pdf_url`        | String (URL) | Valid URL                     | https://ncdc.gov.ng/... | Source PDF link                    |

## **Dataset Creation**

### **Source**

-   **Nigeria Centre for Disease Control (NCDC)**
-   Weekly Situation Reports (2020–2025) in PDF format
-   Publicly available on the NCDC website

### **Collection & Extraction**

-   PDFs downloaded manually or via script
-   Tables extracted using **pdfplumber**
-   Manual corrections applied for inconsistent table layouts

### **Cleaning & Standardization**

-   Dates standardized to ISO format
-   Missing values documented
-   Final CSV validated to ensure unique `(epi_year, epi_week)` pairs

## **Licensing**

The processed Lassa fever dataset is licensed under **CC BY 4.0**.

Users may share and adapt the dataset with proper attribution.

## **Citation**

```
Niyi-Oriolowo, E. (2025). Lassa Fever Weekly Surveillance Dataset (Nigeria, 2020–2025).
https://www.kaggle.com/datasets/emmanuelniyioriolowo/ncdc-lassa-fever-timeseries-20202025
```

## **Ethical Considerations**

-   All data is aggregated at the national level
-   No personally identifying information (PII) is included
-   Dataset follows open-data principles
-   Users should account for reporting delays and potential underreporting

## **Contact**

**Maintainer:** Emmanuel Niyi-Oriolowo

GitHub: [https://github.com/EmmanuelNiy](https://github.com/EmmanuelNiy)

Email: [emmanuelniyioriolowo@gmail.com](mailto:emmanuelniyioriolowo@gmail.com)