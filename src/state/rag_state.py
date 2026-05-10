from typing import List
from pydantic import BaseModel
from langchain_core.documents import Document

class RAGstate(BaseModel):
    '''
    State object for RG workflow
    
    '''

    question :str
    retrieved_docs:List[Document] = []
    answer:str = ""

    