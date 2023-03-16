import openai
import json
import os

# Set your OpenAI API key
openai.api_key = "your_api_key_here"


def load_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def create_prompt(item):
    prompt = f"Create a description for the following media:\nTitle: {item['name']}\nOriginal Description: {item['description']}\n\nGenerated Description:"
    return prompt


def fine_tune(data):
    fine_tuned_data = []

    for item in data:
        prompt = create_prompt(item)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )

        fine_tuned_description = response.choices[0].text.strip()
        item["fine_tuned_description"] = fine_tuned_description
        fine_tuned_data.append(item)

    return fine_tuned_data


def save_data(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    # Load preprocessed data
    preprocessed_data_file = "path/to/your/preprocessed_data.json"
    preprocessed_data = load_data(preprocessed_data_file)

    # Fine-tune the GPT-3 model on the preprocessed data
    fine_tuned_data = fine_tune(preprocessed_data)

    # Save the fine-tuned data to a file
    fine_tuned_data_file = "path/to/your/fine_tuned_data.json"
    save_data(fine_tuned_data, fine_tuned_data_file)
