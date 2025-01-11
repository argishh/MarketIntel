# MarketIntel

MarketIntel is a tool designed to help users conduct comprehensive market research of a given company / industry to automatically analyze its data, and propose AI/GenAI solutions for companies or industries. At its core, it uses `CrewAI` as the mutli-agent framework. It can use `GPT` models through [OpenAI API](https://platform.openai.com/settings/organization/api-keys) as well as `local models` using [Ollama](https://ollama.com/models) to perform analysis and generate research reports. It uses [Serper API](seper.dev) to scrape search engine results and extract relevant information from the web. 

## Installation Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/argishh/MarketIntel.git
    cd MarketIntel
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file in the root directory.
    - Add your OpenAI API key:
        ```scala
        OPENAI_API_KEY = your_openai_api_key
        ```
    - Add your Serper API key:
        ```scala
        SERPER_API_KEY = your_serper_api_key
        ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open the application in your browser:
    ```
    http://localhost:8501
    ```

3. Configure the application:
    - Select the model provider (OpenAI or Local).
    - Enter the OpenAI API key if using OpenAI.
    - Enter the company or industry to be researched.
    - Click "Start Research" to begin the process.

### Using Local Ollama Models

In addition to OpenAI GPT models, you can also use local Ollama models. To use a local Ollama model:

1. Start the Ollama server:
    ```sh
    ollama start
    ```

2. Enter the model name in the sidebar.
3. Ensure the selected model is downloaded:
    ```sh
    ollama pull <model>
    ```

## More about the Crew

### Agents

- **Researcher Agent**: Conducts comprehensive research using tools like SerperDevTool and ScrapeWebsiteTool.
- **Analyzer Agent**: Analyzes the research data to identify AI/GenAI opportunities.
- **Validator Agent**: Validates and aligns AI/GenAI solutions with the company's needs.
- **Resource Collector Agent**: Collects relevant datasets from various platforms.
- **Resource Solutions Proposer Agent**: Proposes additional GenAI solutions based on the collected datasets.

### Tasks

- **Research Task**: Conducts research to understand the industry, market, and operations of the specified company.
- **Analysis Task**: Analyzes the research data to identify AI/GenAI opportunities.
- **Validation Task**: Proposes AI/GenAI solutions based on the analysis.
- **Resource Collection Task**: Finds datasets from platforms like Kaggle, HuggingFace, and GitHub.
- **Resource Solutions Proposal Task**: Proposes GenAI solutions based on the collected datasets.

### Tools
- **SerperDevTool**: A tool that uses the Serper API to scrape search engine results and extract relevant information.
- **ScrapeWebsiteTool**: A tool that scrapes websites to extract information for research purposes.


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Resources for CrewAI

- [CrewAI](https://docs.crewai.com/introduction)
- [DeepLearning.ai](https://learn.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai)
