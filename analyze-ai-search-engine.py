import requests
def analyze_ai_search_engine(engine_url, query):
    """
    Sends a query to an AI-based search engine to analyze its performance
    based on the response's relevance, context awareness, and sentiment.
    """
    # Send the query to the search engine
    response = requests.get(engine_url, params={'q': query})
    if response.status_code == 200:
        results = response.json()  # Expecting JSON response from the search engine.
        # Analysis criteria
        criteria = {
            "relevance_score": evaluate_relevance(results, query),
            "context_awareness": evaluate_context(results, query),
            "response_length": len(results.get("answer", "")),
            "sentiment_score": analyze_sentiment(results.get("answer", "")),
        }
        print(f"Results for '{query}' on {engine_url}")
        for criterion, score in criteria.items():
            print(f"{criterion}: {score}")
    else:
        print("Error: Could not reach the search engine.")
def evaluate_relevance(results, query):
    """
    Evaluates the relevance of the results based on keyword matches.
    """
    answer = results.get("answer", "").lower()
    query_words = query.lower().split()
    relevance = sum([1 for word in query_words if word in answer]) / len(query_words)
    return relevance
def evaluate_context(results, query):
    """
    Measures the ability of the answer to understand the context of the query.
    """
    answer = results.get("answer", "")
    # Basic context awareness check: Does a key part of the query appear in the answer?
    context_aware = query in answer
    return 1 if context_aware else 0
def analyze_sentiment(text):
    """
    Analyzes the sentiment of the response (positive, negative, or neutral).
    This example uses TextBlob.
    """
    from textblob import TextBlob
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns a value from -1 (negative) to 1 (positive)
# Example usage
engine_url = "https://your-ai-search-engine-api.com/search"  # URL for the search engine API
query = "best AI-based search engines"
analyze_ai_search_engine(engine_url, query)
