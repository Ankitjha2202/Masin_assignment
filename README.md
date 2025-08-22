# Construction Claims Prompt Improver

A Python-based system that enhances raw, unstructured construction claim prompts into well-structured, legally-sound queries suitable for Large Language Models (LLMs).

## Features

- Transforms informal construction claim queries into professional, structured prompts
- Adds relevant legal and technical context
- Preserves original user intent while improving clarity
- Simple web interface built with Streamlit

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Masin_assignment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root (this file will be ignored by git):
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Or set it as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_api_key_here
     ```
   
   **IMPORTANT:** 
   - Never commit your actual API key to version control
   - The `.env` file is automatically ignored by git for security
   - Make sure to replace `your_api_key_here` with your actual OpenAI API key
   - Keep your API key secure and never share it publicly

## Usage

### Running the Web Interface

Start the Streamlit app:
```bash
streamlit run app.py
```

The web interface will open in your default browser.

### Using the Python Module

```python
from prompt_improver import ConstructionPromptImprover

improver = ConstructionPromptImprover()
improved_prompt = improver.improve_prompt("eot due to material delay. how to justify?")
print(improved_prompt)
```

## Approach and Limitations

The system uses OpenAI's GPT-4 model to improve construction claim prompts. The improvement process focuses on:
- Adding proper construction terminology
- Including relevant contractual context
- Specifying required documentation
- Emphasizing causation and impact analysis
- Maintaining legal and technical precision

Limitations:
- Requires OpenAI API key and internet connection
- Quality depends on the underlying LLM model
- May not capture highly specific or regional construction practices
- Cost considerations based on API usage

## Project Structure

```
.
├── README.md
├── requirements.txt
├── prompt_improver.py   # Core logic
├── app.py              # Streamlit web interface
└── .env               # API key (not included in repo)
```

## License

MIT