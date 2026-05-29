import os
from dotenv import load_dotenv
from project.coordinator import ResearchCoordinator

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found!!!")

from rich.console import Console
from rich.prompt import Prompt
import asyncio

console=Console()

async def main()->None:
    console.print("[bold cyan]Wissen E-Learn[/bold cyan]")
    console.print("this is a Learning platform powered by agentic workflows")

    query=Prompt.ask("[bold]please provide the topic you want to research about ")
    if not query.strip():
        console.print("[bold red]Please enter a valid topic[/bold red]")
        return
    
    research_codinate=ResearchCoordinator(query)
    report = await research_codinate.reserch()

if __name__=="__main__":
    asyncio.run(main())