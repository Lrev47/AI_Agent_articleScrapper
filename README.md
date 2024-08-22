# AI Newsletter Project

This project is an AI-driven application that automates the process of fetching, analyzing, and compiling top AI news stories into a newsletter format. The application uses multiple agents that interact with each other to handle different tasks. The current implementation is focused on creating a newsletter, but the goal is to extend it into a full-stack AI agent web application using Flask for the backend and a frontend interface.

## Technologies Used

- **Python**: The main programming language used for building the agents and tasks.
- **LangChain**: A framework that simplifies the creation of applications powered by language models, such as GPT-3.5-turbo.
- **OpenAI GPT-3.5-turbo**: The AI model used for text generation and decision-making in the agents.
- **CrewAI**: A task and agent management library that enables structured workflows involving multiple agents.
- **Pydantic**: A data validation library used to ensure proper structure of inputs and outputs in agent tool invocations.
- **Flask (future plan)**: The backend web framework planned for building a REST API to manage the AI agents and tasks.
- **React.js (future plan)**: The frontend framework to create an interactive user interface for the application.

## Project Structure

### Files Overview

- **agents.py**: Defines the different agents responsible for performing specific tasks within the application.
- **tasks.py**: Contains the task definitions that outline what each agent should do and includes logic for executing tasks with delays.
- **main.py**: The entry point for the application. It initializes the agents and tasks, forms the crew, and kicks off the execution process.
- **file_io.py**: Handles saving the generated newsletter to a markdown file.
- **search_tools.py**: Implements the search tool that allows agents to fetch relevant AI news articles from the internet.
- **.env**: Stores environment variables, including the API keys for the search tool.

### Agent Structure and Interaction

The application is built around the concept of agents, each with a specific role. These agents interact with each other by delegating tasks and processing outputs from other agents. Here’s a breakdown of each agent:

1. **Editor Agent**:

   - **Role**: Oversee the creation of the AI Newsletter.
   - **Goal**: Ensure the newsletter not only informs but also engages and inspires the readers.
   - **Interaction**: The Editor Agent is responsible for managing the overall flow, ensuring that tasks are delegated properly to the other agents.

2. **News Fetcher Agent**:

   - **Role**: Fetch the top AI news stories for the day.
   - **Goal**: Act as a digital sleuth, scouring the internet for the latest and most impactful AI news.
   - **Interaction**: The News Fetcher Agent interacts with the search tool to fetch relevant articles and passes the results to the News Analyzer Agent for further processing.

3. **News Analyzer Agent**:

   - **Role**: Analyze each news story and generate a detailed markdown summary.
   - **Goal**: Provide insightful analyses of AI news stories, making them accessible and engaging for the audience.
   - **Interaction**: The News Analyzer Agent processes the output from the News Fetcher Agent and formats it into a markdown-style summary, which is then passed to the Newsletter Compiler Agent.

4. **Newsletter Compiler Agent**:
   - **Role**: Compile the analyzed news stories into a final newsletter format.
   - **Goal**: Act as the final architect of the newsletter, ensuring consistency and proper formatting.
   - **Interaction**: The Newsletter Compiler Agent receives the formatted news stories from the News Analyzer Agent and compiles them into a cohesive newsletter. It saves the newsletter as a markdown file using the file_io module.

### Task Execution

Tasks in this application are defined in the `tasks.py` file. Each task corresponds to a specific responsibility of an agent, such as fetching news, analyzing it, or compiling the newsletter. The tasks are executed in a hierarchical process, where each agent’s output serves as the input for the next agent.

To avoid hitting API rate limits, the `execute_task_with_delay` method is used to introduce a delay between task executions, ensuring that each API call is spaced out by a specified interval (e.g., 30 seconds).

### Future Plans: Full-Stack AI Agent Web Application

The goal is to extend this project into a full-stack AI agent web application by integrating a backend and frontend interface.

#### Backend: Flask

- **Flask** will be used to create a RESTful API that will manage the agents and tasks. The Flask backend will serve as the controller for the AI agents, handling task delegation and storing data.
- The backend will also manage user authentication and session management, allowing users to customize their newsletter preferences.

#### Frontend: React.js

- A **React.js** frontend will be built to provide an interactive interface for users. The frontend will allow users to trigger agent tasks, view generated newsletters, and customize the content they want to receive in their newsletters.
- The frontend will communicate with the Flask backend via API calls, providing a seamless user experience.

#### Database Integration

- The backend will use a database (e.g., PostgreSQL or SQLite) to store user preferences, task history, and generated content.
- The agents’ outputs will be saved in the database, allowing users to retrieve previous newsletters or review past tasks.

### Future Enhancements

- **Custom Agent Creation**: Users will be able to create their own agents with specific goals and tasks, tailored to their needs.
- **Task Scheduling**: Implement a scheduling system where users can set recurring tasks, such as daily or weekly newsletter generation.
- **Advanced AI Models**: As AI technology evolves, integrate more advanced models for better news analysis and content generation.

## Conclusion

This project serves as a foundation for a powerful AI-driven newsletter generator, with the potential to be expanded into a full-stack AI agent web application. By integrating a Flask backend and React.js frontend, the application will provide an interactive and customizable experience for users looking to stay informed about the latest developments in AI.
