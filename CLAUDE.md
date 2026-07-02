# CLAUDE.md — Gemini Chat Apps

Three iterations of a Gemini-powered chat interface at different complexity levels.

## Repos

- **Gemini-V1** — simple CLI loop, no chat history, textwrap output
- **Gemini-V2** — CLI loop with conversation history via `model.start_chat()`, Markdown formatting
- **Gemini-V1-Ui** — Streamlit web UI for Gemini text generation

## Common setup

```bash
pip install google-generativeai
```

Set your API key: `genai.configure(api_key='...')`

## Running

```bash
# CLI with history
python GeminiV2.py

# CLI without history
python GeminiV1.py

# Streamlit UI
streamlit run GeminiV1-UI.py
```

All accept `END GEMINI` as the exit keyword.
