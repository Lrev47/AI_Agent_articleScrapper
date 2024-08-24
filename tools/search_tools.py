from langchain_community.tools import tool

class SearchTools:

    @tool("Search the internet")
    def search_internet(self, input_data: dict):
        """Search the internet about a given topic and return relevant results."""
        query = input_data.get("query")
        if not query:
            return "Error: 'query' field is required."

        print(f"Searching the internet for: {query}")
        
        # Mocked search logic - replace with actual search implementation
        results = [
            {"url": "https://example.com/article1", "content": f"Search results for {query}: Content of article 1."},
            {"url": "https://example.com/article2", "content": f"Search results for {query}: Content of article 2."}
        ]

        result_strings = [
            f"URL: {result['url']}\nContent: {result['content']}\n"
            for result in results
        ]
        return "\n".join(result_strings)
