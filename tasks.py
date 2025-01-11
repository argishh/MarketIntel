from crewai import Task
from agents import researcher_agent, analyzer_agent, validator_agent, resource_collector_agent, resource_solutions_proposer_agent


# ===================== Define Tasks =====================
research_task = Task(
    description="Conduct research to understand the industry, market, and operations of {company_name}.",
    agent=researcher_agent,
    expected_output="Comprehensive research on {company_name} in a format suitable for analysis.",
)

analysis_task = Task(
    description="Analyze the research data and identify AI or GenAI opportunities for {company_name}.",
    agent=analyzer_agent,
    expected_output="AI or GenAI use case proposals for {company_name}."
)

validation_task = Task(
    description="Propose AI or GenAI solutions based on the analysis and ensure alignment with {company_name}'s needs.",
    agent=validator_agent,
    expected_output="Detailed explanation of each AI or GenAI solutions proposed."
)

resource_collection_task = Task(
    description="Find datasets from platforms like Kaggle, HuggingFace, and GitHub that can be of use to integrate AI/GenAI solutions.",
    agent=resource_collector_agent,
    expected_output="A markdown list of datasets (with links) and propose GenAI solutions similar to document search, automated report generation, and AI-powered chat systems for internal or customer-facing purposes.",
    output_file="resources/resources.md"
)

resource_solutions_proposal_task = Task(
    description="Propose GenAI solutions based on the collected datasets.",
    agent=resource_solutions_proposer_agent,
    expected_output="GenAI solutions based on the collected datasets."
)
