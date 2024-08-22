import time
import logging
from datetime import datetime
from crewai import Task
from pydantic import BaseModel, Field

# Pydantic model for tool invocation validation
class ToolInvocationArgs(BaseModel):
    tool_name: str = Field(..., description="Name of the tool to be called")
    arguments: dict = Field(..., description="Arguments required by the tool")

class AINewsLetterTasks():
    
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch top AI news stories from the past 24 hours. The current time is {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""A list of top AI news story titles, URLs, and a brief summary for each story from the past 24 hours. 
                Example Output: 
                [
                    {  'title': 'AI takes spotlight in Super Bowl commercials', 
                    'url': 'https://example.com/story1', 
                    'summary': 'AI made a splash in this year\'s Super Bowl commercials...'
                    }, 
                    {{...}}
                ]
            """
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description='Analyze each news story and ensure there are at least 5 well-formatted articles',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A markdown-formatted analysis for each news story, including a rundown, detailed bullet points, 
                and a "Why it matters" section. There should be at least 5 articles, each following the proper format.
                Example Output: 
                '## AI takes spotlight in Super Bowl commercials\n\n
                **The Rundown:
                ** AI made a splash in this year\'s Super Bowl commercials...\n\n
                **The details:**\n\n
                - Microsoft\'s Copilot spot showcased its AI assistant...\n\n
                **Why it matters:** While AI-related ads have been rampant over the last year, its Super Bowl presence is a big mainstream moment.\n\n'
            """
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the analyzed news stories into a complete markdown-formatted newsletter. Use the analysis provided for each story and create a cohesive newsletter.',
            agent=agent,
            context=context,
            expected_output="""A complete newsletter in markdown format, with a consistent style and layout.
                Example Output: 
                '# Top stories in AI today:\\n\\n
                - AI takes spotlight in Super Bowl commercials\\n
                - Altman seeks TRILLIONS for global AI chip initiative\\n\\n

                ## AI takes spotlight in Super Bowl commercials\\n\\n
                **The Rundown:** AI made a splash in this year\'s Super Bowl commercials...\\n\\n
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
                ## Altman seeks TRILLIONS for global AI chip initiative\\n\\n
                **The Rundown:** OpenAI CEO Sam Altman is reportedly angling to raise TRILLIONS of dollars...\\n\\n'
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
            """,
            callback=callback_function
        )
def execute_task_with_delay(self, task, delay_seconds=30):
    try:
        # Ensure that the agent has at least one tool and it's callable
        if not task.agent.tools or not callable(task.agent.tools[0]):
            raise ValueError("Agent does not have a valid tool for execution.")
        
        # Extract the tool (first one from the list of tools)
        tool_function = task.agent.tools[0]
        
        # Prepare the tool invocation argument structure
        tool_invocation = ToolInvocationArgs(
        tool_name=tool_function.__name__, 
        arguments={  # Provide necessary arguments
        "coworker": "NewsletterCompiler",
        "task": "Compile the newsletter",
        "context": "I have provided a markdown-formatted analysis for each news story..."
    }
)
        
        # Execute the task using the validated tool invocation arguments
        result = tool_function(**tool_invocation.arguments)  # Call the tool function with arguments
        
        # Wait for the specified delay before allowing the next API call
        logging.info(f"Waiting for {delay_seconds} seconds before making the next API request...")
        time.sleep(delay_seconds)
        
        # Return the result of the task
        return result
    
    except Exception as e:  # Corrected indentation for except block
        logging.error(f"Error during task execution: {e}")
        return None
