from pydantic import BaseModel,Field, computed_field
from typing import Annotated,Literal


class input(BaseModel):
    
    prompt:Annotated[str,Field(...,description='this is prompt')]
    url:Annotated[str,Field(...,description='the url of the video')]
   
    
    


