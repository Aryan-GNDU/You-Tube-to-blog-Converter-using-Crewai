# 🎥 YouTube to Blog Converter

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)
![YouTube](https://img.shields.io/badge/YouTube-API-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-Embeddings-orange.svg)

**Transform YouTube videos into engaging blog content using AI-powered agents**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 🚀 Overview

This project leverages the power of **CrewAI** to automatically convert YouTube video content into well-structured blog posts. Using intelligent AI agents, it extracts information from YouTube videos and transforms them into engaging, readable blog content.

### 🤖 How It Works

The system uses two specialized AI agents working in sequence:

1. **📚 Research Agent**: Analyzes YouTube videos and extracts key information
2. **✍️ Writer Agent**: Transforms the extracted content into compelling blog posts

---

## ⚠️ **IMPORTANT: API Key Requirement**

<div align="center">

### 🔑 **OpenAI API Key Required**

This project **requires an OpenAI API key** for embeddings functionality. While the LLM can use Ollama, the embeddings are powered by OpenAI's embedding models.

**Why OpenAI Embeddings?**
- Superior semantic understanding
- Better content analysis
- Enhanced search capabilities
- Industry-standard performance

**Setup Required:**
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

</div>

---

## ✨ Features

- 🎯 **Targeted Content Extraction**: Focus on specific YouTube channels
- 🤖 **AI-Powered Analysis**: Intelligent content understanding and summarization
- 📝 **Blog Post Generation**: Automatic creation of structured blog content
- 🔄 **Sequential Processing**: Organized workflow with research and writing phases
- 💾 **Memory & Caching**: Efficient processing with built-in memory management
- 📁 **Output Customization**: Configurable output formats and file naming

---

## 🛠️ Installation

### Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Ollama (for local LLM processing)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd youtube-to-blog
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key**
   ```bash
   # On Windows
   set OPENAI_API_KEY=your-openai-api-key-here
   
   # On macOS/Linux
   export OPENAI_API_KEY=your-openai-api-key-here
   ```

4. **Install and start Ollama** (for local LLM)
   ```bash
   # Download from https://ollama.ai
   # Start Ollama service
   ollama serve
   
   # Pull the required model
   ollama pull granite3-dense:latest
   ```

---

## 🚀 Usage

### Basic Usage

```python
from crew import crew

# Start the conversion process
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})
print(result)
```

### Custom Configuration

You can modify the target YouTube channel in `tools.py`:

```python
# Change the channel handle to your target channel
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@your-channel-handle')
```

### Output

The system generates:
- **Research Report**: Detailed analysis of video content
- **Blog Post**: Final formatted blog content (saved as `new-blog-post.md`)

---

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   YouTube       │    │   Research      │    │   Writer        │
│   Video Input   │───▶│   Agent         │───▶│   Agent         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │                        │
                              ▼                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   Research      │    │   Blog Post     │
                       │   Report        │    │   Output        │
                       └─────────────────┘    └─────────────────┘
```

### Components

- **`agents.py`**: Defines AI agents (Researcher & Writer)
- **`task.py`**: Defines processing tasks and workflows
- **`tools.py`**: YouTube integration tools
- **`crew.py`**: Main orchestration and execution
- **`requirements.txt`**: Project dependencies

---

## 🔧 Configuration

### Agent Settings

Both agents are configured with:
- **Memory**: Enabled for context retention
- **Verbose Mode**: Detailed execution logging
- **Delegation**: Flexible task assignment
- **LLM**: Ollama with granite3-dense model

### Process Configuration

- **Sequential Execution**: Tasks run in order
- **Memory & Caching**: Optimized performance
- **Rate Limiting**: 100 RPM maximum
- **Crew Sharing**: Enabled for collaboration

---

## 📋 Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| `crewai` | Latest | AI agent framework |
| `crewai_tools` | Latest | YouTube integration tools |
| `ollama` | Latest | Local LLM processing |

---

## 🚨 Troubleshooting

### Common Issues

1. **OpenAI API Key Error**
   ```
   Solution: Ensure OPENAI_API_KEY is set correctly
   ```

2. **Ollama Connection Error**
   ```
   Solution: Verify Ollama is running on localhost:11434
   ```

3. **YouTube Channel Access**
   ```
   Solution: Check channel handle in tools.py
   ```

### Performance Tips

- Use high-quality OpenAI API key for better embeddings
- Ensure stable internet connection for YouTube API calls
- Monitor Ollama resource usage for large videos

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **CrewAI** team for the amazing agent framework
- **OpenAI** for powerful embedding models
- **Ollama** for local LLM capabilities
- **YouTube** for content access

---

<div align="center">

**Made with ❤️ for content creators**

[Report Bug](https://github.com/your-username/youtube-to-blog/issues) • [Request Feature](https://github.com/your-username/youtube-to-blog/issues)

</div>
