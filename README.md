# Generative AI Descriptor for Accessible Media

Generative AI Descriptor is a Software as a Service (SaaS) solution that utilizes generative AI technology to create accessible descriptions of visually driven media such as movies, TV shows, graphic novels, and more. The project aims to assist blind users by providing them with an interpretation of the media content in a creative and engaging way.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- AI-generated descriptions for various media types.
- User customization of media types and preferences.
- Fine-tuned AI model based on OpenAI's GPT-3 or GPT-4 architecture.
- Accessible API or standalone application for easy consumption.

## Installation

To set up the project, follow the instructions in the [installation guide](docs/installation.md).

## Usage

For instructions on how to use the software, please refer to the [usage guide](docs/usage.md).

## Customization

To learn more about customizing your experience with the various media types, check out the [customization guide](docs/customization.md).

## Contributing

We welcome contributions to the project! To get started, please follow the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE). Please see the [LICENSE](LICENSE) file for more information.

```
AI-Innovators/
│
└── Generative-AI-Descriptor/
    ├── .gitignore
    ├── README.md
    ├── LICENSE
    ├── requirements.txt
    ├── setup.py
    ├── src/
    │   ├── data_collection/
    │   │   ├── scraper.py          # Web scraping scripts for IMDb, Rotten Tomatoes, and Goodreads
    │   │   └── preprocess.py       # Data preprocessing and standardization
    │   ├── model/
    │   │   ├── fine_tune.py        # Fine-tuning the pre-trained AI model on the dataset
    │   │   └── generate_descriptions.py    # Generates descriptions based on user preferences
    │   └── user_interface/
    │       ├── user_profile.py     # Handles user preferences and profile storage
    │       └── app.py              # User interface for media type selection and customization
    ├── aws/
    │   ├── amplify/
    │   │   ├── backend/
    │   │   │   ├── api/
    │   │   │   │   └── generativeaidesc/
    │   │   │   │       ├── schema.graphql   # GraphQL schema for API
    │   │   │   │       └── resolvers/       # GraphQL resolvers for API operations
    │   │   │   │           └── ...
    │   │   │   └── auth/          # Authentication and authorization configuration
    │   │   │       └── ...
    │   │   ├── frontend/          # Frontend UI code for web application
    │   │   │   └── ...
    │   │   └── amplify.yml        # AWS Amplify configuration file
    │   ├── cloudformation/
    │   │   ├── generative_ai_descriptor_stack.yml   # AWS CloudFormation stack template
    │   │   └── parameters.json    # AWS CloudFormation parameters
    │   └── terraform/
    │       ├── main.tf            # Terraform main configuration file
    │       ├── outputs.tf         # Terraform output variables
    │       └── variables.tf       # Terraform input variables
    ├── tests/
    │   ├── test_data_collection.py   # Tests for data collection and preprocessing
    │   ├── test_model.py             # Tests for the AI model and description generation
    │   └── test_user_interface.py    # Tests for user interface and profile management
    └── docs/
        ├── installation.md          # Installation instructions
        ├── usage.md                 # Usage instructions
        └── customization.md         # Customization guide for users
```
