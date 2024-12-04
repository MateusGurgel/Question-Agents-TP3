from langchain_community.tools import GoogleSearchRun
from langchain_community.utilities import GoogleSearchAPIWrapper
from decouple import config
import os

os.environ["GOOGLE_API_KEY"] = config("GOOGLE_API_KEY")
os.environ["GOOGLE_CSE_ID"] = config("GOOGLE_CSE_ID")

google_search_tool = GoogleSearchRun(
    api_wrapper=GoogleSearchAPIWrapper(),
    name="Google Search Tool",
    description="This will result the search query on Google.",
)