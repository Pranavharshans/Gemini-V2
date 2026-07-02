# Gemini-V2

Interactive command-line chat application using Google Gemini Pro with conversation history. Supports multi-turn dialogue with Markdown-formatted responses.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranavharshans/Gemini-V2.git
   cd Gemini-V2
   ```

2. Install dependencies:
   ```bash
   pip install google-generativeai
   ```

3. Add your Gemini API key in `GeminiV2.py`:
   ```python
   genai.configure(api_key='YOUR_API_KEY')
   ```

## Usage

```bash
python GeminiV2.py
```

Type messages to chat with Gemini. The model maintains conversation history across turns. Type `END GEMINI` to exit.

### Example

```
You: What are the three laws of robotics?
Gemini: 1. A robot may not injure a human being...
You: Who created them?
Gemini: Isaac Asimov introduced them in his 1942 short story...
You: END GEMINI
```

## How It Differs from Gemini-V1

- Maintains full conversation history via `model.start_chat()`
- Responses formatted as Markdown with bullet conversion
- Multi-turn context awareness

## Project Structure

```
Gemini-V2/
└── GeminiV2.py    # Main chat application
```

## Dependencies

- `google-generativeai`
