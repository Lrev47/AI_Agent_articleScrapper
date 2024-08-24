from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import logging
import traceback

# Load environment variables from .env file
load_dotenv()

# Initialize agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Initialize OpenAI GPT-3.5-turbo model
OpenAIGPT4 = ChatOpenAI(model="gpt-3.5-turbo")

# Instantiate agents
editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

# Create tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
compile_newsletter_task = tasks.compile_newsletter_task(newsletter_compiler, [analyze_news_task], save_markdown)

# Form the crew with the hierarchical process and verbose logging
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4,
    verbose=2
)

try:
    # Kick off the crew's work and get results
    results = crew.kickoff()
    
    if results:
        logging.info(f"Crew Work Results: {results}")
        print("Crew Work Results:")
        print(results)  # Optionally format this if it's complex data
    else:
        logging.error("No results were returned from the crew's work.")
        print("No results were returned.")
        
except Exception as e:
    # Log the error and the full stack trace for better debugging
    logging.error(f"An error occurred during the crew's work: {e}")
    logging.error(traceback.format_exc())
