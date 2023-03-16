# Generative AI Descriptor

Generative AI Descriptor is a Software as a Service (SaaS) that uses the GPT-NeoXT-Chat-Base-20B model to create accessible and creative descriptions for visually-driven media, including movies, TV shows, graphic novels, NFTs, and more. The service is designed to assist blind users in interpreting these media by generating descriptions in a conversational manner.

## Features

- Data collection from various media sources like IMDb, Rotten Tomatoes, Goodreads, and NFT platforms
- Preprocessing and standardization of media data
- Fine-tuning of GPT-NeoXT-Chat-Base-20B for generating accessible descriptions
- Customizable user profiles to tailor generated content
- Chatbot-style user interface for easy interaction
- API and standalone deployment options

## Installation

For detailed installation instructions, please refer to the [installation.md](docs/installation.md) file.

## Usage

For information on how to use Generative AI Descriptor, please see the [usage.md](docs/usage.md) file.

## Customization

To learn more about customizing the user experience and media types, read the [customization.md](docs/customization.md) file.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to this project. Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute.

## Support and Feedback

If you encounter any issues or have feedback, please open an issue on our GitHub repository or contact us at support@ai-innovators.com.


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
