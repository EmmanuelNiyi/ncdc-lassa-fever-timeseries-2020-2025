# **📘 Data Dictionary —** NCDC Lassa Fever Timeseries (2020–2025)

This data dictionary defines each variable in the dataset, its type, allowed values, and interpretation. Each row corresponds to **one epidemiological week** of reporting.

## **1\. Core Epidemiological Fields**

### **`epi_year`**

-   **Type:** Integer
-   **Description:** Epidemiological year following the WHO standard.
-   **Notes:** Used to align weeks with epidemiological reporting; may differ slightly from calendar year for overlapping weeks.

### **`epi_week`**

-   **Type:** Integer
-   **Range:** 1–53
-   **Description:** WHO epidemiological week number for the reporting period.
-   **Notes:** Unique when combined with `epi_year`. Some years include week 53.

### **`week_start_date`**

-   **Type:** Date (YYYY-MM-DD)
-   **Description:** Start date of the epidemiological week.
-   **Notes:** Standardized for consistency across years.

### **`week_end_date`**

-   **Type:** Date (YYYY-MM-DD)
-   **Description:** End date of the epidemiological week.

## **2\. Weekly Case Counts**

### **`suspected_cases`**

-   **Type:** Integer
-   **Description:** Number of suspected Lassa fever cases reported during the week.
-   **Definition (NCDC):** Any individual presenting with one or more of the following: malaise, fever, headache, sore throat, cough, nausea, vomiting, diarrhoea, myalgia, chest pain, hearing loss and either:
    -   a. History of contact with excreta or urine of rodents
    -   b. History of contact with a probable or confirmed Lassa fever case within 21 days of onset of symptoms
    -   OR any person with inexplicable bleeding/hemorrhage
-   **Notes:** May be zero; includes both confirmed and probable cases plus those awaiting laboratory results.

### **`confirmed_cases`**

-   **Type:** Integer
-   **Description:** Lab-confirmed Lassa fever cases for the week.
-   **Definition (NCDC):** Any suspected case with laboratory confirmation (positive IgM antibody, PCR, or virus isolation).
-   **Notes:** Primary variable for forecasting; subset of suspected cases.

### **`probable_cases`**

-   **Type:** Integer
-   **Description:** Probable Lassa fever cases for the week.
-   **Definition (NCDC):** Any suspected case who died or absconded without collection of specimen for laboratory testing.
-   **Notes:** Epidemiologically linked cases where laboratory confirmation was not possible.

### **`deaths`**

-   **Type:** Integer
-   **Description:** Deaths attributed to Lassa fever during the week.
-   **Notes:** Includes deaths among both confirmed and probable cases.

## **3\. Metadata and Provenance**

### **`extraction_method`**

-   **Type:** String
-   **Allowed values:**
    -   `"manual"`
    -   `"automated"` `i.e. table_extraction + regex`
-   **Description:** Method used to extract case numbers from the report.

### **`extraction_timestamp`**

-   **Type:** DateTime (YYYY-MM-DD HH:MM:SS)
-   **Description:** Timestamp when data was extracted from the report.
-   **Notes:** Useful for tracking updates or re-extractions.

### **`report_pdf_url`**

-   **Type:** String (URL)
-   **Description:** Direct link to the NCDC weekly report PDF.
-   **Notes:** Ensures transparency and reproducibility.

## **4\. Dataset Indexing**

-   **Primary Key:** `epi_year + epi_week`
-   **Uniqueness:** Each row corresponds to exactly one epidemiological week.

## **5\. Missing Data Standards**

All missing data has been manually filled. The dataset contains:

-   **Zero cases** → encoded as `0`
-   **No missing weeks** → all epidemiological weeks from 2020 to 2025 are included
-   **Complete case counts** → all four case count fields (`suspected_cases`, `confirmed_cases`, `probable_cases`, `deaths`) are populated for every week

## **6\. Data Types Summary**

| Column                  | Type         | Constraints                   | Example                 | Notes                             |
|-------------------------|--------------|-------------------------------|-------------------------|-----------------------------------|
| `epi_year`              | Integer      | ≥ 2020                        | 2024                    | Epidemiological year              |
| `epi_week`              | Integer      | 1 ≤ week ≤ 53                 | 12                      | WHO epi week                      |
| `week_start_date`       | Date         | YYYY-MM-DD format             | 2024-03-18              | Monday of epi week                |
| `week_end_date`         | Date         | YYYY-MM-DD format             | 2024-03-24              | Sunday of epi week                |
| `suspected_cases`       | Integer      | ≥ 0                           | 87                      | Clinical/epidemiological criteria |
| `confirmed_cases`       | Integer      | ≥ 0, ≤ suspected_cases        | 42                      | Laboratory-confirmed              |
| `probable_cases`        | Integer      | ≥ 0, ≤ suspected_cases        | 5                       | Died/absconded without testing    |
| `deaths`                | Integer      | ≥ 0, ≤ (confirmed + probable) | 8                       | Lassa fever-attributed deaths     |
| `extraction_method`     | String       | "manual" or "automated"       | "automated"             | Extraction method used            |
| `extraction_timestamp`  | DateTime     | YYYY-MM-DD HH:MM:SS           | 2024-03-25 14:32:01     | When extraction occurred          |
| `report_pdf_url`        | String (URL) | Valid URL format              | https://ncdc.gov.ng/... | Source PDF link                   |

## **7\. Additional Notes**

-   **Seasonality:** Lassa fever exhibits seasonal patterns in Nigeria, with peak transmission typically occurring during the dry season (January–April).
-   **Reporting lag:** `report_week_published` may be 1–2 weeks after `week_end_date` due to data compilation time.
-   **Data completeness:** All weeks from 2020 onwards are included with manually verified case counts.