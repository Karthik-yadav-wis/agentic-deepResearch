from datetime import time

from agents import trace, Runner
from research_agents.query_agent import QueryPattern, query_agent
from research_agents.search_agent import search_agent
from research_agents.synthasis_agent import synthesis_agent
from research_agents.follow_up_agent import FollowUpDecisionResponse,follow_up_decision_agent
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from duckduckgo_search import DDGS
from pydantic import BaseModel

console=Console()

class SearchResult(BaseModel):
    title: str
    url: str
    summary: str 

class ResearchCoordinator:
    def __init__(self, query:str):
        self.query=query
    
    async def research(self)->str:
        with trace("deep research workflow"):
            query_response = await self.generate_quries()
            return "expected report"
            
    async def generate_quries(self)->QueryPattern:
        with console.status("[bold cyan]Analysing...[/bold cyan]"):

            result = await Runner.run(query_agent, input=self.query)

            console.print("[yellow]Thoughts:[/yellow]",result.final_output.thinking_process)
            console.print(Panel(f"[bold cyan]Analysis:[/bold cyan]"))
            console.print("[bold yellow]Generated search queries:[/bold yellow]")
            for i,query in enumerate(result.final_output.queries,1):
                console.print(f"{i}:{query}")

            return result.final_output
        
    def duckduckgo_search(self, query:str):
        try:
            result=DDGS().text(query, region="ind-en", safesearch="on", max_result="1")
            return result
        except Exception as ex:
            console.print("[bold red]error in fetching information [/bold red]")
            return []

    async def search_results(self, quries: list[str]):
        all_search_results={}
        for query in quries:
            search=self.duckduckgo_search(query)
            all_search_results[query]=search
            
    async def perform_research_for_queries(self, queries: list[str]) -> None:

        # get all of the search results for each query
        all_search_results = {}
        for query in queries:
            search_results = self.duckduckgo_search(query)
            all_search_results[query] = search_results

        for query in queries:
            console.print(f"\n[bold cyan]Searching for:[/bold cyan] {query}")

            for result in all_search_results[query]:
                console.print(f"  [green]Result:[/green] {result['title']}")
                console.print(f"  [dim]URL:[/dim] {result['href']}")
                console.print(f"  [cyan]Analyzing content...[/cyan]")

                start_analysis_time = time.time()
                search_input = f"Title: {result['title']}\nURL: {result['href']}"
                agent_result = await Runner.run(search_agent, input=search_input)
                analysis_time = time.time() - start_analysis_time

                search_result = SearchResult(
                    title=result['title'],
                    url=result['href'],
                    summary=agent_result.final_output
                )

                self.search_results.append(search_result)

                summary_preview = agent_result.final_output[:100] + ("..." if len(agent_result.final_output) > 100 else "")

                console.print(f"  [green]Summary:[/green] {summary_preview}")
                console.print(f"  [dim]Analysis completed in {analysis_time:.2f}s[/dim]\n")
        
        console.print(f"\n[bold green]✓ Research round complete![/bold green] Found {len(all_search_results)} sources across {len(queries)} queries.")

    async def synthesis_report(self) -> str:
         with console.status("[bold cyan]Synthesizing research findings...[/bold cyan]") as status:
            findings_text = f"Query: {self.query}\n\nSearch Results:\n"
            for i, result in enumerate(self.search_results, 1):
                findings_text += f"\n{i}. Title: {result.title}\n   URL: {result.url}\n   Summary: {result.summary}\n"

            result = await Runner.run(synthesis_agent, input=findings_text)

            return result.final_output
         
    async def generate_followup(self) -> FollowUpDecisionResponse:
        with console.status("[bold cyan]Evaluating if more research is needed...[/bold cyan]") as status:
            findings_text = f"Original Query: {self.query}\n\nCurrent Findings:\n"
            for i, result in enumerate(self.search_results, 1):
                findings_text += f"\n{i}. Title: {result.title}\n   URL: {result.url}\n   Summary: {result.summary}\n"

            result = await Runner.run(follow_up_decision_agent, input=findings_text)

            console.print(Panel(f"[bold cyan]Follow-up Decision[/bold cyan]"))
            console.print(f"[yellow]Decision:[/yellow] {'More research needed' if result.final_output.should_follow_up else 'Research complete'}")
            console.print(f"[yellow]Reasoning:[/yellow] {result.final_output.reasoning}")

            if result.final_output.should_follow_up:
                console.print("\n[yellow]Follow-up Queries:[/yellow]")
                for i, query in enumerate(result.final_output.queries, 1):
                    console.print(f"  {i}. {query}")

            return result.final_output
