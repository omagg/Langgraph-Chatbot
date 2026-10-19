# LangGraph Chatbot 💬

A powerful, stateful conversational AI chatbot built with **LangGraph**, **LangChain**, and **Streamlit**. This project demonstrates advanced agentic AI workflows with persistent memory, tool integration, and real-time streaming responses.

## ✨ Features

- **Stateful Conversation Memory**: Leverages LangGraph's graph-based architecture for maintaining conversation state across multiple turns
- **Multi-turn Reasoning**: Support for complex, multi-step conversations with context retention
- **Streaming Responses**: Real-time streaming of AI responses for a fluid user experience
- **Tool Integration**: Built-in support for external tools and APIs
- **Web Interface**: Clean, interactive Streamlit frontend for seamless user interaction
- **Extensible Architecture**: Modular design allows easy addition of new tools and capabilities

## 🏗️ Architecture

### Backend (`langgraph_backend.py`)
- Implements the core LangGraph workflow
- Manages conversation state and message history
- Handles tool invocations and routing
- Maintains checkpoints for conversation recovery

### Frontend (`streamlit_frontend.py`)
- Interactive web UI built with Streamlit
- Real-time message streaming
- User-friendly chat interface
- Session management

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip or conda
- Groq API key (get it from [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/omagg/Langgraph-Chatbot.git
cd Langgraph-Chatbot
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Running the Application

```bash
streamlit run streamlit_frontend.py
```

The chatbot will be accessible at `http://localhost:8501`

## 📁 Project Structure

```
Langgraph-Chatbot/
├── langgraph_backend.py      # Core LangGraph implementation
├── streamlit_frontend.py      # Streamlit UI
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore               # Git ignore file
└── README.md                # This file
```

## 🔧 Usage

1. **Start a conversation**: Type your message in the chat input box
2. **View responses**: The chatbot will respond in real-time with streaming output
3. **Multi-turn interaction**: Continue the conversation; the chatbot maintains full context
4. **Tool usage**: The chatbot can invoke tools when needed to answer complex queries

### Example Interactions

**Simple Query:**
```
User: What's the capital of France?
Assistant: The capital of France is Paris...
```

**Complex Multi-turn:**
```
User: Tell me about the history of AI
Assistant: [Provides detailed historical overview]

User: Can you focus on the recent developments?
Assistant: [Provides context-aware response about recent developments]
```

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Graph Framework** | LangGraph |
| **LLM Integration** | LangChain |
| **Language Model** | Groq API |
| **Frontend** | Streamlit |
| **Language** | Python 3.9+ |

## 📚 Key Concepts

### LangGraph
- **State Management**: Maintains conversation state as a graph
- **Message History**: Automatically tracks all messages in conversation
- **Checkpointing**: Enables conversation replay and recovery

### LangChain
- **Tool Integration**: Built-in support for various APIs and tools
- **Prompt Management**: Flexible prompt templating
- **Memory Management**: Efficient handling of conversation history

## 🎯 Future Enhancements

- [ ] Add support for additional tools (web search, calculator, etc.)
- [ ] Implement conversation saving and loading
- [ ] Add user authentication
- [ ] Support for multiple conversation threads
- [ ] Enhanced error handling and logging
- [ ] Performance optimization for longer conversations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 🙋 Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

## 🔗 Resources

- [LangGraph Documentation](https://langgraph.dev/)
- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Documentation](https://console.groq.com/docs/overview)

---

**Built with** ❤️ **for AI-powered conversations**
