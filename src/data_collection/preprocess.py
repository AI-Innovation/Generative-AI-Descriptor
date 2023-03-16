import json
import re
import os


def preprocess_data(data, output_file):
    """
    Preprocesses the input data and saves it to the specified output file.

    Args:
        data (list): A list of dictionaries containing the scraped data.
        output_file (str): The path to the output file where the preprocessed data will be saved.
    """

    # Initialize the preprocessed data container
    preprocessed_data = []

    # Loop through the data and preprocess each item
    for item in data:
        # Clean the description text
        cleaned_description = clean_text(item['description'])

        # Skip the item if the cleaned description is empty
        if not cleaned_description:
            continue

        # Add the preprocessed item to the list
        preprocessed_item = {
            'name': item['name'],
            'description': cleaned_description,
            'image_url': item['image_url'],
            'external_link': item['external_link'],
        }
        preprocessed_data.append(preprocessed_item)

    # Save the preprocessed data to the output file
    with open(output_file, 'w') as f:
        json.dump(preprocessed_data, f, ensure_ascii=False, indent=2)


def clean_text(text):
    """
    Cleans the input text by removing unnecessary characters and whitespace.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """

    # Remove HTML tags
    text = re.sub('<[^>]*>', ' ', text)

    # Remove URLs
    text = re.sub(r'http\S+', ' ', text)

    # Remove special characters and extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove leading and trailing whitespace
    text = text.strip()

    return text

# Main function or script execution


if __name__ == '__main__':
    # Load the scraped data from the input file
    input_file = 'path/to/your/scraped_data.json'
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Preprocess the data and save it to the output file
    output_file = 'path/to/your/preprocessed_data.json'
    preprocess_data(data, output_file)
