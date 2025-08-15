from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import base64


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


class Base64DecodeToolInput(BaseModel):
    """Input schema for Base64DecodeTool."""
    encoded_content: str = Field(..., description="Base64 encoded string to decode.")

class Base64DecodeTool(BaseTool):
    name: str = "Base64 Decoder"
    description: str = (
        "Decodes base64 encoded content to readable text. Useful for processing "
        "base64 encoded email content and converting it to plain text for analysis."
    )
    args_schema: Type[BaseModel] = Base64DecodeToolInput

    def _run(self, encoded_content: str) -> str:
        """
        Decode base64 encoded content to readable text.
        
        Args:
            encoded_content: Base64 encoded string
            
        Returns:
            Decoded text content or error message
        """
        try:
            # Remove any whitespace and newlines that might be present
            cleaned_content = encoded_content.strip().replace('\n', '').replace('\r', '')
            
            # Decode base64 content
            decoded_bytes = base64.b64decode(cleaned_content)
            decoded_text = decoded_bytes.decode('utf-8')
            
            return decoded_text
            
        except Exception as e:
            return f"Error decoding base64 content: {str(e)}. Please ensure the input is valid base64 encoded text."
