## pip install -r requirements.txt
## python --version (Python 3.11.x)

import os

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM


# ============================================================
# 1. LOAD .env
# ============================================================

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
model = os.getenv("ANTHROPIC_MODEL")
api_version = os.getenv("ANTHROPIC_VERSION", "2023-06-01")


# ============================================================
# 2. CHECK SETTINGS
# ============================================================

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY is missing in .env")

if not model:
    raise ValueError("ANTHROPIC_MODEL is missing in .env")


# ============================================================
# 3. CREATE ANTHROPIC LLM
# ============================================================

llm = LLM(
    model=f"anthropic/{model}",
    api_key=api_key,
    client_params={
        "default_headers": {"anthropic-version": api_version},
    },
)


# ============================================================
# 4. RESEARCHER AGENT
# ============================================================

researcher = Agent(
    role="AI Researcher",

    goal="Find and explain important AI trends",

    backstory=(
        "You are a simple and helpful AI researcher. "
        "You find important information and explain it clearly."
    ),

    llm=llm,

    verbose=True
)


# ============================================================
# 5. WRITER AGENT
# ============================================================

writer = Agent(
    role="AI Writer",

    goal="Create a simple article using the researcher's information",

    backstory=(
        "You are a technology writer. "
        "You explain technical topics in simple language."
    ),

    llm=llm,

    verbose=True
)


# ============================================================
# 6. RESEARCH TASK
# ============================================================

research_task = Task(
    description="""
    Research the topic:

        Artificial Intelligence

        Find 3 important AI trends.

        Explain each trend in simple language.
        """,

        expected_output="""
        A simple list of 3 AI trends.
        Each trend should have a short explanation.
        """,

        agent=researcher
    )


# ============================================================
# 7. WRITING TASK
# ============================================================

writing_task = Task(
        description="""
        Use the researcher's result.

        Write a short and simple article about
        the 3 AI trends.

        The article should be easy for students to understand.
        """,

        expected_output="""
        A simple 3-paragraph article about AI trends.
        """,

        agent=writer
    )


# ============================================================
# 8. CREATE CREW
# ============================================================

crew = Crew(
        agents=[researcher, writer],

        tasks=[research_task, writing_task],

        verbose=True
    )


    # ============================================================
    # 9. START CREW
    # ============================================================

if __name__ == "__main__":

    print()
    print("=" * 50)
    print("          AI RESEARCH AGENTS")
    print("=" * 50)
    print()

    print("AI Agents are working together...")
    print()

    result = crew.kickoff()

    print()
    print("=" * 50)
    print("             FINAL RESULT")
    print("=" * 50)
    print()

    print(result)