__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import os
from pathlib import Path

import streamlit as st
from crewai import LLM, Crew, Process
from dotenv import load_dotenv
from agents import *
from tasks import *

load_dotenv()

try:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
except:
    OPENAI_API_KEY = None

try:
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
except:
    try:
        SERPER_API_KEY = st.secrets["SERPER_API_KEY"]
    except:
        st.error("Please enter your SerpAPI API key in the environment variables.")

# ===================== Main Function =====================
def main():
    
    st.set_page_config(
        page_title="Market Analysis Tool",
        page_icon="🔍",
        layout="wide"
    )
    
    st.title("Market Research Assistant")
    st.sidebar.title("Configuration")

    # Model provider selection
    model_provider = st.sidebar.radio(
        "Select Model Provider",
        ["OpenAI", "Local (Ollama)"]
    )
    
    if model_provider == "OpenAI":
        # API Key input
        api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        
        # OpenAI model list
        model_options = {
            "o1": "o1",
            "o1 mini": "o1-mini",
            "o1 Preview": "o1-preview",
            "GPT 4o": "chatgpt-4o-latest",
            "GPT 4o mini": "gpt-4o-mini",
            "GPT 4 Turbo": "gpt-4-turbo",
            "GPT 4": "gpt-4",
            "GPT 3.5 Turbo": "gpt-3.5-turbo",
        }
        model_name = st.sidebar.selectbox(
            "Select GPT Model",
            list(model_options.keys()),
            index=7
        )
        os.environ['OPENAI_MODEL_NAME'] = model_options[model_name]
        llm = LLM(model=f"openai/{os.getenv('OPENAI_MODEL_NAME')}", )

    else:
        # Ollama model selection
        local_model = st.sidebar.text_input("Enter Ollama Model Name", value="llama3.2")
        llm = LLM(model=f"ollama/{local_model}", base_url="http://localhost:11434")

    # Company to be researched
    company_name = st.text_input("Enter Company / Industry:")

    # Select the OpenAI model to use
    os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

    if st.button("Start Research"):
        if not company_name:
            st.error("Please enter a company / industry")
            return

        if model_provider == "OpenAI" and OPENAI_API_KEY is None:
            st.error("Please enter your OpenAI API key in the sidebar.")
            return

        # Input Data
        inputs = {
            "company_name": company_name
        }

        # ===================== Crew Setup =====================
        researchCrew = Crew(
            agents=[researcher_agent, analyzer_agent, validator_agent],
            tasks=[research_task, analysis_task, validation_task],
            manager_llm=llm,
            process=Process.sequential,
            verbose=True,
        )
        
        resourceSolutionsCrew = Crew(
            agents=[resource_collector_agent, resource_solutions_proposer_agent],
            tasks=[resource_collection_task, resource_solutions_proposal_task],
            process=Process.sequential,
            verbose=True,
        )
        
        # ===================== Kickoff Crews =====================
        with st.spinner("Generating insights and proposal..."):
            results = researchCrew.kickoff(inputs=inputs)

        # Display results
        st.markdown(results.raw, unsafe_allow_html=True)

        # inputs for resourceSolutionsCrew
        inputs2 = {
            "company_name": company_name,
            "solutions_by_research_crew": results.raw
        }
        # Generate solutions based on responses
        with st.spinner("Finding resources for GenAI solutions..."):
            response = resourceSolutionsCrew.kickoff(inputs=inputs2)
        
        # Display resources
        resources = Path("./resources/resources.md").read_text(encoding="utf-8")
        st.markdown('### Resources')
        st.markdown(resources, unsafe_allow_html=True)
        
        st.markdown('### GenAI Based Solutions')
        # Display response
        st.markdown(response.raw, unsafe_allow_html=True)            
        
    # ===================== How to use =====================
    with st.sidebar.expander("How to use", expanded=False):
        
        if model_provider == "OpenAI":
            # How to use OpenAI models
            st.markdown("""
            1. Enter your OpenAI API key
            2. Select the GPT model
            3. Enter a company/industry
            4. Click 'Start Research'""")
            
            # Add API setup help
            st.markdown("""
            **To get OpenAI API Key**:
            1. Visit [OpenAI API](https://platform.openai.com/api-keys)
            2. Create new API key""")
            
        else:
            # How to use Ollama models
            st.markdown("""
            1. Start Ollama
            2. Enter the model name above⬆️ 
            3. Ensure the selected model is downloaded
                ```sh
                ollama pull <model>
                ```
            4. Enter a company/industry
            5. Click 'Start Research'""")

if __name__ == "__main__":
    main()
