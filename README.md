# Anonymize_Excel
 A Python script that anonymizes an Excel file and synthesizes new data in its place.

![Excel_Anonymized_Demo](https://github.com/Welding-Torch/Anonymize_Excel/assets/46340124/78b03e03-bad0-4cb0-9b84-46e3197e9344)
_Convert your sheets with sensitive data into anonymized data._

## What is Anonymize_Excel.py
Anonymize_Excel.py is a python script that helps to ensure sensitive data is properly managed and governed. It provides fast identification and anonymization for private entities in text such as credit card numbers, names, locations, phone numbers, email address, date/time, with more entities to come.  

## Use case
Data anonymization is crucial because it helps protect privacy and maintain confidentiality. If data is not anonymized, sensitive information such as names, addresses, contact numbers, or other identifiers linked to specific individuals could potentially be learned and misused. Hence, by obscuring or removing this personally identifiable information (PII), data can be used freely without compromising individuals’ privacy rights or breaching data protection laws and regulations.  

## Overview
Anonymization consists of two steps:  
1. Identification: Identify all data fields that contain personally identifiable information (PII).  
2. Replacement: Replace all PIIs with pseudo values that do not reveal any personal information about the individual but can be used for reference.  

Anonymize_Excel.py uses Microsoft Presidio together with Faker framework for anonymization purposes.

## Quickstart
1. Clone the repository
   ```
   git clone https://github.com/Welding-Torch/Anonymize_Excel.git
   ```

3. Install the requirements
   ```
   pip install presidio_analyzer
   pip install presidio_anonymizer
   python -m spacy download en_core_web_lg
   ```
4. Run the demo
   ```
   python Anonymize_Excel.py
   ```

That's it! 

## Usage
To use Anonymize_Excel.py with your Excel file, modify line 8 in the program.
```
df = pd.read_excel("your_excel_sheet_here.xlsx")
```

## Author
Siddharth Bhatia  
License: [MIT License](https://github.com/Welding-Torch/Anonymize_Excel/blob/main/LICENSE)
