# AI Research Crew

A small [CrewAI](https://www.crewai.com/) demo that uses two AI agents and Anthropic's Claude model to research artificial intelligence trends and write a short article in language suitable for students.

## What It Does

1. An **AI Researcher** identifies three important AI trends.
2. A **Writer** turns the research into a simple, three-paragraph article.
3. The crew prints its progress and the final result in the terminal.

Both agents use the configured Anthropic Claude model.

## Requirements

- Python 3.11
- An Anthropic API key
- Access to the Claude model specified in `ANTHROPIC_MODEL`

## Setup

Create and activate a virtual environment, then install the project dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root with your Azure OpenAI settings:

```env
ANTHROPIC_API_KEY=your-anthropic-api-key
ANTHROPIC_VERSION=2023-06-01
ANTHROPIC_MODEL=claude-sonnet-4-6
```

`ANTHROPIC_API_KEY` and `ANTHROPIC_MODEL` are required. `ANTHROPIC_VERSION` defaults to `2023-06-01` if omitted.

Keep `.env` private and do not commit real credentials to source control.

## Run

From the project root, run:

```powershell
python ai_research_crew.py
```

The agents' activity and the generated article are displayed in the terminal. The generated article is not automatically saved to a file.

## Project Files

- `ai_research_crew.py` - configures the Azure OpenAI model, agents, tasks, and crew.
- `requirements.txt` - pinned Python dependencies.
- `new_post.md` - an example article about AI trends.
