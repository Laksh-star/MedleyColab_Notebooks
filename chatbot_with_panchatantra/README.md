# 🦁 Leadership Wisdom Chatbot

A modern chatbot that provides leadership advice through the timeless wisdom of Panchatantra stories. Built with Streamlit and powered by a curated database of ancient Indian tales, this application helps leaders find relevant guidance for their modern challenges.

## ✨ Features

### 💡 Smart Leadership Advice
- Context-aware responses based on your questions
- Multi-concept tagging system
- Relevant Panchatantra story matching
- Six leadership categories: Decision Making, Teamwork, Trust, Strategy, Communication, and Conflict Resolution

### 🎨 Modern UI/UX
- Clean, intuitive chat interface
- Organized history view with concept tags
- Example questions for guidance
- Beautiful story and advice presentation
- Mobile-responsive design

### 💾 Data Management
- Persistent chat history using SQLite
- CSV export functionality
- Concept-tagged responses for easy reference

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/leadership-wisdom-chatbot.git
cd leadership-wisdom-chatbot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📱 Usage

1. **Ask Questions**: Type your leadership-related question in the chat interface
2. **Get Wisdom**: Receive contextual advice and a relevant Panchatantra story
3. **Track Progress**: View your leadership journey in the history tab
4. **Export Data**: Download your chat history as a CSV file

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Database**: SQLite
- **Data Processing**: Pandas
- **Language**: Python

## 📂 Project Structure

```
leadership-wisdom-chatbot/
├── app.py              # Main application file
├── db.py              # Database operations
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## 🏗️ Architecture

### Development Process
![Development Process](development_process.svg)

Our iterative development process involved close collaboration between user requirements and AI implementation, progressing through five main phases from initial setup to final documentation.

### Code Architecture
![Code Architecture](code_architecture.svg)

The application follows a clean architecture with:
- Core application logic in app.py
- Database operations isolated in db.py
- Modern UI components using Streamlit
- SQLite persistence for chat history
- Panchatantra stories database with concept tagging

## 📊 Sample Questions

- "How do I make better decisions as a leader?"
- "What's the importance of teamwork?"
- "How should I build trust in my team?"
- "What's the best strategy to solve problems?"
- "How can I improve my communication skills?"
- "How do I resolve conflicts effectively?"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by the ancient Indian text Panchatantra
- Built with Streamlit's amazing framework
- Special thanks to all contributors

## 📧 Contact

For any queries or suggestions, please open an issue in the repository.
