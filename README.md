# 💬 WhatsApp Chat Analyzer

A powerful and interactive WhatsApp Chat Analyzer built using Python and Streamlit that provides detailed insights into your WhatsApp group or individual chats with visualizations and fun facts. 📊✨

---

## 🚀 Features

🔍 Chat Statistics
📏 Longest Message in Chat  
📆 Monthly & Daily Timelines  
📅 Most Busy Day & Month  
📊 Weekly Activity Heatmap  
👥 Most Active Users  
☁️ WordCloud Generation  
🔠 Most Common Words  
😄 Emoji Analysis  
🧠 Sentiment Analysis  
⏰ Active Time Analysis  
🔥 Most Engaging Conversations  
🎉 Fun Fact Generator  
🗑️ Deleted Messages Detection  
📈 Chat Streak Analysis  

---

## 🛠️ Tech Stack


| Tool/Library     | Purpose                        |
|------------------|--------------------------------|
| `Python`         | Core Programming Language      |
| `Streamlit`      | Web UI Framework               |
| `Pandas`         | Data Handling                  |
| `Matplotlib`     | Visualizations                 |
| `Seaborn`        | Advanced Plots                 |
| `WordCloud`      | Word cloud generation          |
| `Emoji`          | Emoji handling                 |
| `urlextract`     | Extract links from messages    |

---

## 📂 Folder Structure

📁 WhatsApp-Chat-Analyzer/
│
├── app.py                      # Main Streamlit app file
├── helper.py                   # Helper functions for data manipulation
├── preprocessor.py             # Preprocessing the WhatsApp chat data
├── requirements.txt            # Python dependencies
├── setup.sh                    # Shell script for setting up the environment
├── stop__hinglish.txt           # Custom stop words for Hinglish processing
├── .gitignore                  # Git ignore file for unnecessary files
└── README.md                   # Project documentation

___
💻 Installation:
To set up and run the WhatsApp Chat Analyzer, follow these steps:

Clone the repository:

git clone https://github.com/yourusername/WhatsApp-Chat-Analyzer.git
cd WhatsApp-Chat-Analyzer
___

Create a virtual environment:
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
___

Install dependencies:
pip install -r requirements.txt
___

Run the app:
streamlit run app.py

___

📑 How to Use
Upload Chat File:
Once the app opens in your browser, you'll be prompted to upload a WhatsApp chat file (e.g., .txt format).
Choose the file, and the app will start processing the chat data.

Explore Insights:
The app will provide you with a dashboard featuring various analytics such as:

>Sentiment analysis over time
>Word cloud of most common words
>Active user statistics
>Most engaging conversations
>Fun facts about your chat history

___

🚀 Features in Detail
📊 Chat Statistics
Displays key stats such as:

>Total messages
>Word count
>Media files sent
>Links shared

🗓️ Timeline (Monthly/Daily)
Analyzes the activity on a monthly or daily scale, showing how active the conversation was over time.

🔥 Weekly Heatmap
Visualizes the intensity of conversations across days of the week.

❤️ Sentiment Analysis
Shows the overall sentiment of the chat: Positive, Negative, or Neutral.

🔥 Deleted Messages Detection
Identifies messages that have been deleted from the chat.

___

🛠️ Development and Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that your code adheres to the style guide and passes existing tests.

To set up your local development environment, use the following shell script:

bash setup.sh
This will set up your environment with the necessary dependencies.





