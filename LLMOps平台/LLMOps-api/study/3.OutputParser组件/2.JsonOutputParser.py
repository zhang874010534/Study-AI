import dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

dotenv.load_dotenv()

class Joke(BaseModel):
    joke: str = Field(description="一个笑话")
    punchline: str = Field(description="笑话的 punchline")

parser = JsonOutputParser(pydantic_object=Joke)

print(parser.get_format_instructions())
