# ChatIQ - WhatsApp Chat Analyzer 📱💬

ChatIQ is a Streamlit-based web application that analyzes WhatsApp chat data and provides insightful visualizations and statistics.

## Features

- Message count analysis 📝
- User activity statistics 👥
- Media and link sharing tracking 🔗
- Word cloud generation ☁️
- Emoji analysis 😊
- Monthly timeline visualization 📅
- Daily activity patterns ⏰
- Most common words analysis 📊

---

## 🚀 How to Use

1. Export your WhatsApp chat:
   - Open WhatsApp on mobile and navigate to the chat you want to extract 📱
   - Tap on the three dots in the top-right corner to open the menu ⚙️
   - Select "More" and then "Export chat" 📤
   - Choose "Without Media" 📄
   - Share the exported file to yourself 📨

2. Upload the chat file:
   - Use the file uploader in the sidebar 📂
   - Select the user for analysis (Overall or specific user) 👤
   - Click "Show Analysis" to view the results 📈

---

## 📊 Analysis Provided

- Total message count 💬
- Total word count 📝
- Media files shared 🖼️
- Links shared 🔗
- Most active users (for group chats) 👥
- Word cloud visualization ☁️
- Common words analysis 📊
- Emoji usage statistics 😊
- Monthly message timeline 📅
- Day-wise activity patterns 📊

---

## 🛠️ Technologies Used

- Python 🐍
- Streamlit 🌟
- Pandas 🐼
- Matplotlib 📈
- WordCloud ☁️
- URLExtract 🔗
- Emoji 😊

---

## 📁 Project Structure

- `main.py`: Main application file 🚀
- `preprocess.py`: Chat data preprocessing 🔄
- `stats.py`: Statistical analysis functions 📊

---

## 📌 Notes

- The analyzer supports both individual and group chat analysis 👥
- Handles different date-time formats ⏰
- Preserves user privacy (data is processed locally) 🔒
- Supports both English and Hinglish text analysis 🌐

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/chatiq.git
   cd chatiq
   ```

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**

   ```bash
   streamlit run app.py
   ```

Open [http://localhost:8501](http://localhost:8000) in your browser.

---

## Contributors
- [Naman Kukreti](https://github.com/kukretinaman)

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
