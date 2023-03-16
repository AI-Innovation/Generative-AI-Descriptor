import openai
import json

# Set your OpenAI API key
openai.api_key = "your_api_key_here"


def generate_description(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    generated_description = response.choices[0].text.strip()
    return generated_description


def create_prompt(item):
    prompt = f"Create a description for the following media:\nTitle: {item['name']}\nOriginal Description: {item['description']}\n\nGenerated Description:"
    return prompt


if __name__ == '__main__':
    # Example media item for which you want to generate a description
    media_item = {
        'name': 'Example Movie',
        'description': 'An example movie about AI and the future of technology.'
    }

    # Create a prompt for the GPT-3 model
    prompt = create_prompt(media_item)

    # Generate the description using the fine-tuned GPT-3 model
    generated_description = generate_description(prompt)

    # Print the generated description
    print(generated_description)
