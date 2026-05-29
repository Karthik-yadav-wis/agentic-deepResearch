from agents import trace, Runner
from project.research_agent.query_agent import QueryPattern, query_agent
from project.research_agentt import query_agent
from rich.console import Console
console=Console()

class ResearchCoordinator:
    def __init__(self, query:str):
        self.query=query
    
    async def research(self)->str:
        with trace("deep research workflow"):
            query_response=self.generate_quries()
            
    async def generate_quries(self)->QueryPattern:
        with console.status("[bold cyan]Analysing...[/bold cyan]"):

            result = await Runner.run(query_agent, input=self.query)

            console.print(panel("[bold cyan]Analysis:[/bold cyan]"))
            console.print("[yellow]Thoughts:[/yellow]",result.final_output.thinking_process)
            console.print("[bold yellow]Generated search queries:[/bold yellow]")
            for i,query in enumerate(result.final_output.queries,1):
                console.print(f"{i}:{query}")

            return result.final_output


