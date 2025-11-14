thonimport json
from analyzers.reddit_query_generator import generate_query
from analyzers.sentiment_filter import filter_sentiment
from analyzers.summarizer import summarize_discussion
from extractors.reddit_post_parser import parse_post
from extractors.reddit_comment_parser import parse_comment

def run_analysis(input_data):
    # Generate a query based on the input
    query = generate_query(input_data['query'])

    # Parse Reddit posts and comments
    posts = parse_post(query)
    comments = parse_comment(query)

    # Filter out low-quality posts and comments
    filtered_posts = filter_sentiment(posts)
    filtered_comments = filter_sentiment(comments)

    # Summarize the analysis
    summary = summarize_discussion(filtered_posts, filtered_comments)

    # Output the results in JSON format
    result = {
        'query': input_data['query'],
        'data': {
            'format': 'json',
            'heading': 'Output',
            'response': summary
        }
    }
    
    with open('output.json', 'w') as outfile:
        json.dump(result, outfile, indent=4)

if __name__ == "__main__":
    # Example input data
    input_data = {
        'query': 'What is the easiest musical instrument to learn?'
    }
    run_analysis(input_data)