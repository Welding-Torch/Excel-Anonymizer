'''
Filename: excel_anonymizer.py
Author: Siddharth Bhatia
'''

import argparse
import logging
import logging.config

import pandas as pd
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities.engine import OperatorConfig
from faker import Faker

def main():
    """Just a main function needed to publish this to PyPI"""

    # Disable loggers from all imported modules
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': True,
    })

    # Initialize parser
    parser = argparse.ArgumentParser(
                        prog='excel_anonymizer.py',
                        description='Anonymizes an Excel file and \
                            synthesizes new data in its place.',
                        epilog='Made by Siddharth Bhatia')

    # Take file as input
    parser.add_argument('filename', help="your excel file here")
    parser.add_argument('-v', '--verbose',
                        action='store_true')

    # Read arguments from command line
    args = parser.parse_args()

    filename = args.filename

    if args.verbose is True:
        logging.basicConfig(format="%(message)s", level=logging.INFO)
        logging.info("Verbose output.")

    def log(string):
        """Make function for logging."""
        if args.verbose is True:
            logging.info(string)

    df = pd.read_excel(f"{filename}")
    log(df)
    log("")

    # Column values to list, which I will use at the end
    columns_ordered_list = df.columns.values.tolist()
    log(f"Columns: {columns_ordered_list}")
    log("")

    # Initialize an empty dictionary to store cell locations and values
    cell_data = {}

    # Iterate over every cell
    for index, row in df.iterrows():
        for column in df.columns:
            cell_value = row[column]
            cell_location = (index, column)
            cell_data[cell_location] = cell_value

    # log the list of cell values
    log(f"Cell Data: {cell_data}")
    log("")
    log("###")

    # Presidio code begins here
    analyzer = AnalyzerEngine()
    anonymizer = AnonymizerEngine()

    # Faker code begins here
    fake = Faker()

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

    for location, entity in cell_data.items():
        # log every cell with it's location
        # log(cell, cell_data[cell])
        log(entity)

        # Analyze + anonymize it
        analyzer_results = analyzer.analyze(text=str(entity), language="en")
        log(analyzer_results)

        anonymized_results = anonymizer.anonymize(
            text=str(entity),
            analyzer_results=analyzer_results,
            operators=fake_operators,
        )

        log(f"text: {anonymized_results.text}")
        log("")
        # then return it to the dictionary
        cell_data[location] = anonymized_results.text
    log("---")

    # log(cell_data)
    # OUTPUT: {(0, 'Name'): '<PERSON>', (0, 'Phone Number'): '<PHONE_NUMBER>',
    #         (1, 'Name'): '<PERSON>', (1, 'Phone Number'): '<PHONE_NUMBER>'}

    data = {}
    columns = list(set(column for _, column in cell_data))
    for (index, column), value in cell_data.items():
        data.setdefault(index, [None] * len(columns))
        data[index][columns_ordered_list.index(column)] = value
    anonymized_df = pd.DataFrame.from_dict(data, columns=columns_ordered_list, orient="index")
    log(anonymized_df)

    filename = filename.rstrip(".xlsx")
    anonymized_df.to_excel(
        f"{filename}-anonymized.xlsx",
        # Don't save the auto-generated numeric index
        index=False
    )

    print(f"Output generated: {filename}-anonymized.xlsx")

if __name__ == "__main__":
    main()
