import json
import requests
import streamlit as st
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class SearchQuery(BaseModel):
    query: str = Field(..., description="The search query to look up")

class SearchTools(BaseTool):
    name: str = "Search the internet"
    description: str = "Useful to search the internet about a given topic and return relevant results"
    args_schema: type[BaseModel] = SearchQuery

    def _run(self, query: str) -> str:
        try:
            top_result_to_return = 4
            url = "https://google.serper.dev/search"
            payload = json.dumps({"q": query})
            headers = {
                'X-API-KEY': st.secrets['SERPER_API_KEY'],
                'content-type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            if response.status_code != 200:
                return f"Error: Search API request failed. Status code: {response.status_code}"
            
            data = response.json()
            if 'organic' not in data:
                return "No results found or API error occurred."
            
            results = data['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", 
                        f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", 
                        "\n-----------------"
                    ]))
                except KeyError:
                    continue
            return '\n'.join(string) if string else "No valid results found"
        except Exception as e:
            return f"Error during search: {str(e)}"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")
