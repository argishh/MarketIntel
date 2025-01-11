from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# ========================= Tools =========================
serper_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


# ===================== Define Agents =====================
researcher_agent = Agent(
    role="Researcher",
    goal="Conduct comprehensive research to understand the industry and segment {company_name} is operating in, including key offerings, strategic focus areas, and vision.",
    backstory="""You are a professional researcher tasked with researching all aspects of {company_name}, including industry, market, finance, marketing, sales,
    operations, human resources, R&D, legal, and customer service. Use the tools [serper_tool, scrape_tool] to search websites and gather information.
    Summarize insights about the industry segment, key offerings, and strategic focus areas.
    Provide actionable data to the analyzer for further analysis.""",
    tools=[serper_tool, scrape_tool],
    allow_delegation=True,
    verbose=True
)

analyzer_agent =  Agent(
    role="Analyzer",
    goal="Analyze the research context received from the researcher and identify potential areas where AI or GenAI can improve workflows and processes at {company_name}.",
    backstory="""You are a professional analyzer. You have to analyze the background of {company_name} and its industry, and think about identifying opportunities to leverage AI/ML and GenAI technologies. 
    Use [serper_tool] to assess industry trends and propose relevant use cases to enhance processes, customer satisfaction, and operational efficiency. 
    Your output should be concise and actionable for validation.""",
    tools=[],
    allow_delegation=True,
    verbose=True
)

validator_agent =  Agent(
    role="Validator",
    goal="Write detailed integrating AI/GenAI solutions for {company_name}, ensuring accuracy, relevance, and alignment with {company_name}'s objectives.",
    backstory="""You are a professional editor-in-chief and a validator. You are the final agent who has to compile information from analyzer.
    You have to review the analysis received from the analyzer and check for factual accuracy and alignment with {company_name}'s needs.
    Identify gaps, irrelevant information or areas for improvement and fix them. Finally, write a very detailed explanation for integrating AI or GenAI solutions.""",
    tools=[],
    allow_delegation=False,
    verbose=True
)

resource_collector_agent =  Agent(
    role="Resource Collector",
    goal="Collect datasets relevant to the validated use cases and propose GenAI solutions for {company_name}.",
    backstory="""From the validated use cases, locate and gather datasets from platforms like Kaggle, HuggingFace, and GitHub.
    Use [serper_tool, scrape_tool] to search for relevant resources. Save the resource links in a markdown file for future reference.
    Ensure all datasets are suitable for implementing the proposed GenAI solutions.""",
    tools=[serper_tool, scrape_tool],
    allow_delegation=False,
    verbose=True
)

resource_solutions_proposer_agent = Agent(
    role="GenAI Solutions Proposer",
    goal="Propose more GenAI solutions based on the collected datasets, that are different from the suggested solutions.",
    backstory="""You are a professional Generative AI developer. You have to propose GenAI solutions based on the datasets collected and propose solutions other that the solutions proposed below -
    {solutions_by_research_crew}
    Use the collected datasets to propose GenAI solutions like document search, automated report generation, and AI-powered chat systems for internal or customer-facing purposes.
    Ensure the proposed solutions are relevant and feasible for implementation.""",
    tools=[],
    allow_delegation=False,
    verbose=True   
)
