import os

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class EmailMessageSchema(BaseModel):
    subject: str
    contents: str
    invalid_request: bool | None = Field(default=False)




OPENAI_BASE_URL = os.environ.get('OPENAI_BASE_URL') or None
OPENAI_MODEL_NAME = os.environ.get('OPENAI_MODEL_NAME') or 'gpt-4o-mini'
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise NotImplementedError("`OPENAI_API_KEY` is required")

# def get_openai_llm():
openai_params = {
    "model": OPENAI_MODEL_NAME,
    "api_key": OPENAI_API_KEY
}
if OPENAI_BASE_URL:
    openai_params['base_url'] = OPENAI_BASE_URL

llm_base = ChatOpenAI(**openai_params)
llm = llm_base.with_structured_output(EmailMessageSchema)

messages = [
    {
        "system",
        "You are a helpful assistant that generates email messages based on the provided subject and contents."
    },
    {
        "human": "Generate an email message with the subject 'Meeting Reminder' and contents 'Don't forget our meeting tomorrow at 10 AM.'"
    }
]


reponse = llm.invoke(llm)
print(reponse)