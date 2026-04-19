import os
from abc import ABC, abstractmethod
from typing import Tuple, Dict

class BaseProvider(ABC):
    @abstractmethod
    def generate(self, model_id: str, prompt: str) -> Tuple[str, Dict[str, int]]:
        pass

class OpenAIProvider(BaseProvider):
    def generate(self, model_id: str, prompt: str) -> Tuple[str, Dict[str, int]]:
        # Mocking for demonstration to avoid API key requirements in repo
        return "Simulated OpenAI Response", {"total_tokens": len(prompt.split()) + 50}

class AnthropicProvider(BaseProvider):
    def generate(self, model_id: str, prompt: str) -> Tuple[str, Dict[str, int]]:
        # Mocking for demonstration
        return "Simulated Anthropic Response", {"total_tokens": len(prompt.split()) + 45}
