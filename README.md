# Chatbot-Law-and-Rights

This project develops a chatbot using Python and the Gemini LLM to provide quick, accurate answers about laws and rights. The user-friendly interface, built with Streamlit, ensures that legal information is easily accessible, making complex legal knowledge understandable for everyone, anytime.

## Features

- **Instant Legal Assistance**: Get quick and accurate answers to questions related to laws and rights.
- **User-Friendly Interface**: Built with Streamlit, offering an intuitive and interactive user experience.
- **Powered by Gemini LLM**: Utilizes advanced natural language processing (NLP) capabilities for understanding and responding to legal queries.
- **24/7 Accessibility**: Access legal knowledge anytime, anywhere, through the chatbot interface.

## Technologies Used

- **Python**: Main programming language used for backend development.
- **Gemini LLM**: Large Language Model used to process and respond to user queries.
- **Streamlit**: Framework used for building the frontend interface, making the chatbot accessible and interactive.

## Installation

### Clone the repository:

```bash
git clone https://github.com/your-username/Chatbot-Law-and-Rights.git
cd Chatbot-Law-and-Rights
```
## Install the required dependencies:
``` bash
pip install -r requirements.txt
```
## Getting Your API Key

To interact with the Gemini LLM (or OpenAI if you are using GPT models), you'll need an API key. Here's how to get it:

1. Sign up for **Gemini LLM** or **OpenAI** and create an account.
2. Generate your API key from your account dashboard.
3. Store the key securely in your environment variables or a `.env` file.
4. In your code, access the key using the `os` module or `dotenv` package.

Remember, never expose your API key publicly for security reasons.

Once you have your API key, you can copy it in .env file

## Run the application:
```bash
streamlit run app.py
```
This will start the Streamlit app, and you can interact with the chatbot through your browser.
## Usage
Once the application is running, the chatbot will be available in your browser. You can ask questions related to laws and rights, and the chatbot will provide accurate, understandable answers based on the input received.

## Contributing
Feel free to fork the repository, open issues, and submit pull requests. Contributions are welcome to improve the functionality and accuracy of the chatbot.
