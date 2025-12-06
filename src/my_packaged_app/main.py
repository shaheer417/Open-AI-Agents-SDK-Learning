#  0. Importing the necessary libraries
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

import os
from dotenv import load_dotenv, find_dotenv

def main() -> None:
    # 0.1. Loading the environment variables
    load_dotenv(find_dotenv())

    # 1. Which LLM Provider to use? -> OpenAI Chat Completions API Service
    external_client: AsyncOpenAI = AsyncOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # 2. Which LLM Model to use?
    llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
        model="gpt-3.5-turbo",
        openai_client=external_client
    )

    # 3. Creating the Agent
    agent: Agent = Agent(name="Assistant", model=llm_model)

    # 4. Running the Agent
    result = Runner.run_sync(starting_agent=agent, input="what is js")

    print("AGENT RESPONSE: " , result.final_output)

if __name__ == "__main__":
    main()