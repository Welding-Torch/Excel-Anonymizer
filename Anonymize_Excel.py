'''
Filename: Anonymize_Excel.py
Author: Siddharth Bhatia
'''

import pandas as pd

df = pd.read_excel("personal_information.xlsx")
print(df)

# Column values to list, which I will use at the end
columns_ordered_list = df.columns.values.tolist()
print(columns_ordered_list)

# Initialize an empty dictionary to store cell locations and values
cell_data = {}

# Iterate over every cell
for index, row in df.iterrows():
    for column in df.columns:
        cell_value = row[column]
        cell_location = (index, column)
        cell_data[cell_location] = cell_value

# Print the list of cell values
print(cell_data)
print("###")

# Presidio code begins here
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Faker code begins here
from faker import Faker

fake = Faker()
from presidio_anonymizer.entities.engine import OperatorConfig

# Faker Custom Operators
fake_operators = {
    "PERSON": OperatorConfig("custom", {"lambda": lambda x: fake.name()}),
    "PHONE_NUMBER": OperatorConfig("custom", {"lambda": lambda x: fake.phone_number()}),
    "LOCATION": OperatorConfig("custom", {"lambda": lambda x: str(fake.country())}),
    "EMAIL_ADDRESS": OperatorConfig("custom", {"lambda": lambda x: fake.email()}),
    "DATE_TIME": OperatorConfig("custom", {"lambda": lambda x: str(fake.date_time())}),
    "CREDIT_CARD": OperatorConfig("custom", {"lambda": lambda x: fake.credit_card_number()}),
    "US_BANK_NUMBER": OperatorConfig("custom", {"lambda": lambda x: fake.credit_card_number()}),
    #"DEFAULT": OperatorConfig(operator_name="mask", 
    #                          params={'chars_to_mask': 10, 
    #                                  'masking_char': '*',
    #                                  'from_end': False}),
}

fake = Faker(locale="en_IN")

for cell in cell_data:
    # Print every cell with it's location
    # print(cell, cell_data[cell])
    print(cell_data[cell])

    # Analyze + anonymize it
    analyzer_results = analyzer.analyze(text=str(cell_data[cell]), language="en")
    print(analyzer_results)

    anonymized_results = anonymizer.anonymize(
        text=str(cell_data[cell]),
        analyzer_results=analyzer_results,
        operators=fake_operators,
    )

    print(f"text: {anonymized_results.text}")
    print()
    # then return it to the dictionary
    cell_data[cell] = anonymized_results.text
print("---")

# print (cell_data)
# OUTPUT: {(0, 'Name'): '<PERSON>', (0, 'Phone Number'): '<PHONE_NUMBER>',
#         (1, 'Name'): '<PERSON>', (1, 'Phone Number'): '<PHONE_NUMBER>'}

data = {}
columns = list(set(column for _, column in cell_data))
for (index, column), value in cell_data.items():
    data.setdefault(index, [None] * len(columns))
    data[index][columns_ordered_list.index(column)] = value
anonymized_df = pd.DataFrame.from_dict(data, columns=columns_ordered_list, orient="index")
print(anonymized_df)

anonymized_df.to_excel(
    "anonymized_personal_information.xlsx",
    # Don't save the auto-generated numeric index
    index=False
)