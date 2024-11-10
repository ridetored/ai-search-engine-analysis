# AI Search Engine Analysis Script

This Python script evaluates AI-based search engine responses by analyzing their relevance, context awareness, and sentiment. By sending queries to a specified AI search engine and scoring the responses, this tool can help assess the quality of different search engine outputs.

## Features

- Sends a query to a specified AI-based search engine.
- Analyzes response based on:
  - **Relevance**: Checks keyword matches between query and answer.
  - **Context Awareness**: Measures if the response understands the query context.
  - **Response Length**: Captures the length of the response text.
  - **Sentiment**: Uses sentiment analysis to score the response.
- Provides detailed feedback for each analysis criterion.

## Requirements

- Python 3.6+
- Libraries:
  - `requests`
  - `textblob`

Install these packages using:

```bash
pip install requests textblob
