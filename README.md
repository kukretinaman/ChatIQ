# ChatIQ - WhatsApp Chat Analytics

ChatIQ is a powerful tool for extracting and analyzing various information from WhatsApp chats between two individuals or within a WhatsApp group. This repository provides all the necessary tools and instructions to perform detailed analyses on your WhatsApp conversations.

## Features

- **Message Frequency Analysis**: Determine how often messages are sent and received.
- **Word Cloud Generation**: Visualize the most frequently used words in the chat.
- **Emoji Analysis**: Analyze the sentiment of the messages to understand the overall tone of the conversation.
- **Participant Activity**: Track the activity levels of different participants in a group chat.


## Extracting a WhatsApp Chat

To extract a WhatsApp chat from any group chat or individual chat, follow these steps:

1. Open WhatsApp on your mobile device and navigate to the chat you want to extract.
2. Tap on the three dots in the top-right corner to open the menu.
3. Select "More" and then "Export chat".
4. Choose not to include media files.
5. Select the method of sharing (e.g., email, Google Drive, etc.) and send the chat to yourself.
6. Once received, download the chat file to your computer.
7. Upload the chat file to ChatIQ for analysis.

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kukretinaman/ChatIQ.git
   cd ChatIQ
   ```

2. **Run the Analysis**

   Execute the main analysis script to start processing your chat file:

   ```bash
   streamlit run main.py
   ```
3. **Upload Your WhatsApp Chat File**

   Browse your WhatsApp chat file (usually named `WhatsApp Chat with XYZ.txt`) and click 'Upload'.

4. **View the Results**

   After the analysis is complete, the results will be available in the right hand side panel. You can view the generated stats and visualizations.
   
## Contributors

- [Naman Kukreti](https://github.com/kukretinaman)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
