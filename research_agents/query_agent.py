from agents import Agent
from pydantic import BaseModel


class QueryPattern(BaseModel):
    thinking_process: str
    queries: list[str]

Query_Agent_prompt="""
you are an helpfull assitant, your job is generate search queries for research based on the topic provided
for each topic follow the following steps:

1. Think through and explain:
    - breakdown the key aspects which are needed to be researched and addresed 
    - comeup with the potential challenges and how you'll address them
    - explain your strategy for finding comprehensive information

2. Then generate 3 search queries 
    - these are specific and focused on retriving high quality information
    - cover different aspect of topics 
    - will help find relevent and diverse information

always provide both your thinking process and the generated 3 queries
"""

query_agent = Agent(
    name="query generator agent",
    instructions=Query_Agent_prompt,
    output_type=QueryPattern,
)
