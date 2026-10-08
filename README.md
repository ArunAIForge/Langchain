# LangChain LangSmith Tracing App

A simple Python application demonstrating how to use **LangChain with ChatOpenAI** and enable **LangSmith tracing through environment variables**.

The application sends multiple prompts to the OpenAI model in a single execution, prints each response, and automatically sends the LangChain runs to a named LangSmith project for monitoring and analysis.

## Features

* Uses **LangChain**
* Uses **ChatOpenAI**
* Sends 3 different prompts in a single run
* Prints each prompt and its response
* LangSmith tracing enabled through environment variables
* Uses a custom LangSmith project name
* View prompts, responses, latency, and token usage in LangSmith
* Uses `.env` for API keys and configuration
* Keeps application code simple with no tracing-specific code

## Project Structure

```text
TracingApp/
│
├── traced_app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

Make sure you have:

* Python 3.12+
* OpenAI API key
* LangSmith API key
* Internet connection

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd TracingApp
```

### 2. Create a Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet:

```powershell
pip install langchain langchain-openai langsmith python-dotenv
```

Then generate it:

```powershell
pip freeze > requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key

LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=TracingApp
```

### Environment Variables

| Variable            | Purpose                              |
| ------------------- | ------------------------------------ |
| `OPENAI_API_KEY`    | Authenticates requests to OpenAI     |
| `LANGSMITH_API_KEY` | Authenticates LangSmith tracing      |
| `LANGSMITH_TRACING` | Enables LangSmith tracing            |
| `LANGSMITH_PROJECT` | Specifies the LangSmith project name |

> **Important:** Never commit the `.env` file to GitHub. It contains sensitive API keys and should be included in `.gitignore`.

## Run the Application

Run:

```powershell
python traced_app.py
```

The application sends three different prompts and prints each response.

Example:

```text
--- Prompt 1 ---
Question: What is asynchronous processing?
Answer: ...

--- Prompt 2 ---
Question: Explain REST API in simple terms.
Answer: ...

--- Prompt 3 ---
Question: What are the SOLID principles in C#?
Answer: ...
```

## LangSmith Tracing

Tracing is enabled entirely through environment variables:

```env
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=TracingApp
```

There is **no LangSmith tracing code inside `traced_app.py`**.

After running the application, open LangSmith and navigate to the project:

```text
TracingApp
```

Each LangChain model invocation should appear as a separate run.

## What Can Be Viewed in LangSmith?

For each run, LangSmith provides information such as:

* Exact input/prompt
* Model response
* Latency
* Input token count
* Output token count
* Total token count
* Run details
* Model information
* Execution metadata

For example:

| Metric        | Example                          |
| ------------- | -------------------------------- |
| Prompt        | What is asynchronous processing? |
| Response      | Model-generated response         |
| Latency       | 1.23 seconds                     |
| Input Tokens  | 8                                |
| Output Tokens | 82                               |
| Total Tokens  | 90                               |

The actual values depend on the model response and API execution.

## Technologies Used

* **Python 3.12**
* **LangChain**
* **ChatOpenAI**
* **OpenAI**
* **LangSmith**
* **python-dotenv**

## Learning Objectives

This project demonstrates:

1. How to use `ChatOpenAI` through LangChain.
2. How to invoke an LLM from Python.
3. How to send multiple prompts in one execution.
4. How to configure LangSmith using environment variables.
5. How to organize runs under a custom LangSmith project.
6. How to inspect prompts, responses, latency, and token usage.
7. How to keep API credentials outside the source code.

## Security

Do not commit API keys to GitHub.

The `.env` file should remain local:

```text
.env
```

Make sure `.gitignore` contains:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

## Future Enhancements

Possible improvements include:

* Add a Streamlit user interface
* Accept prompts dynamically from the user
* Add conversation history
* Compare multiple OpenAI models
* Add structured output
* Add prompt templates
* Add LangChain chains
* Compare latency and token usage across models

## License

This project is intended for learning and demonstration purposes.
