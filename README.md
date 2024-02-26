# Excel Anonymizer
 A Python script that anonymizes an Excel file and synthesizes new data in its place.

![Excel_Anonymized_Demo](https://github.com/Welding-Torch/Anonymize_Excel/assets/46340124/78b03e03-bad0-4cb0-9b84-46e3197e9344)
_Convert your sheets with sensitive data into anonymized data._

## What is Excel Anonymizer
Excel Anonymizer is a python script that helps to ensure sensitive data is properly managed and governed. It provides fast identification and anonymization for private entities in text such as credit card numbers, names, locations, phone numbers, email address, date/time, with more entities to come.  

## Use case
Data anonymization is crucial because it helps protect privacy and maintain confidentiality. If data is not anonymized, sensitive information such as names, addresses, contact numbers, or other identifiers linked to specific individuals could potentially be learned and misused. Hence, by obscuring or removing this personally identifiable information (PII), data can be used freely without compromising individuals’ privacy rights or breaching data protection laws and regulations.  

## Overview
Anonymization consists of two steps:  
1. Identification: Identify all data fields that contain personally identifiable information (PII).  
2. Replacement: Replace all PIIs with pseudo values that do not reveal any personal information about the individual but can be used for reference.  

Excel Anonymizer uses Microsoft Presidio together with Faker framework for anonymization purposes.

## Quickstart
1. Install Excel Anonymizer
   ```
   pip install excel-anonymizer
   ```
> Note: Spacy will install a Natural Language Processing package on the first run (587.7MB).

2. Download personal_information.xlsx from this repository, and then type
   ```
   excel-anon personal_information.xlsx
   ```

That's it! 

## Usage
To use Excel Anonymizer with your Excel file, simply input the file.
```
excel-anon your_excel_file_here.xlsx
```

## Author
Siddharth Bhatia  
License: [MIT License](https://github.com/Welding-Torch/Anonymize_Excel/blob/main/LICENSE)
