"""
LangGraph Definition
Main workflow graph for the AI Security Intelligence Agent
"""
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from .state import AgentState
from .nodes import ingest_node, scrape_node, synthesize_node, report_node


def create_graph(use_checkpointer: bool = True) -> StateGraph:
    """
    Create the intelligence agent workflow graph

    Args:
        use_checkpointer: Whether to enable checkpointing for resume capability

    Returns:
        Compiled StateGraph
    """
    # Initialize graph with state schema
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("ingest", ingest_node)
    workflow.add_node("scrape", scrape_node)
    workflow.add_node("synthesize", synthesize_node)
    workflow.add_node("report", report_node)

    # Define edges (linear pipeline)
    workflow.set_entry_point("ingest")
    workflow.add_edge("ingest", "scrape")
    workflow.add_edge("scrape", "synthesize")
    workflow.add_edge("synthesize", "report")
    workflow.add_edge("report", END)

    # Compile with optional checkpointer
    if use_checkpointer:
        checkpointer = MemorySaver()
        return workflow.compile(checkpointer=checkpointer)

    return workflow.compile()


def run_agent(config: dict = None) -> str:
    """
    Run the intelligence agent and return the report

    Args:
        config: Configuration dictionary with:
            - credentials_path: Path to Gmail OAuth credentials
            - token_path: Path to store/load OAuth token
            - search_query: Gmail search query
            - max_emails: Maximum emails to process
            - scrape_delay: Delay between scraping domains
            - llm_provider: 'gemini' or 'anthropic'
            - llm_model: Model name to use
            - mark_as_read: Whether to mark processed emails as read

    Returns:
        Generated Markdown report
    """
    if config is None:
        config = {}

    # Initialize state
    initial_state: AgentState = {
        'emails': [],
        'articles': [],
        'themes': [],
        'report': '',
        'errors': [],
        'config': config
    }

    # Create and run graph
    graph = create_graph(use_checkpointer=False)
    result = graph.invoke(initial_state)

    return result.get('report', '')


# Export for use as module
__all__ = ['create_graph', 'run_agent']
