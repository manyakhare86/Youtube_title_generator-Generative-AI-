# YouTube Video Title Generator

## Output

![Screenshot 2024-02-21 231817](https://github.com/manyakhare86/Youtube_title_generator-Generative-AI-/assets/74348408/d673729e-721f-4845-a69b-57344b7d905c)



The YouTube Video Title Generator is a tool designed to assist users in generating compelling titles for their YouTube videos. Leveraging OpenAI's powerful GPT-3 language model, this application suggests the top five titles based on the provided topic.

## Features

- **Topic Input**: Users can input the topic or subject for which they need video titles.
- **Title Generation**: Upon clicking the "Generate Title" button, the application utilizes OpenAI's GPT-3 model to generate the most relevant and engaging titles for the provided topic.
- **Real-time Feedback**: The application provides real-time feedback, updating users on the status of the title generation process.
- **Top 5 Titles**: Once the titles are generated, the top five suggestions are displayed, helping users choose the most suitable title for their video content.

## Data Source

The titles generated by this application are based on a dataset of YouTube video headings. The dataset was obtained from Kaggle and includes a wide range of video titles across various topics and genres.

## ChatGPT Assistant Integration

In addition to the title generation feature, this application integrates with ChatGPT, an AI-powered conversational agent developed by OpenAI. Users can interact with the ChatGPT assistant to receive additional information or assistance related to their video content.

## Installation

To run the YouTube Video Title Generator locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain an API key from OpenAI and replace `"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"` with your API key in the code.
4. Run the application using Streamlit by executing `streamlit run yotube_title_generator.py` in your terminal.

## Usage

1. Enter the topic or subject for which you need video titles in the provided text input field.
2. Click the "Generate Title" button to initiate the title generation process.
3. Wait for the application to generate the titles. You will receive real-time updates on the status of the process.
4. Once the titles are generated, the top five suggestions will be displayed in the text area.
5. Select the most suitable title for your video content from the provided options.

## Contributions

Contributions to the YouTube Video Title Generator project are welcome! Feel free to submit bug reports, feature requests, or pull requests through GitHub.
