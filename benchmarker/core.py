import time
import tiktoken
from typing import Dict, Any, List
from benchmarker.providers import OpenAIProvider, AnthropicProvider

class BenchmarkingSuite:
    def __init__(self):
        self.providers = {
            "openai": OpenAIProvider(),
            "anthropic": AnthropicProvider()
        }

    def run_benchmark(self, provider_name: str, model_id: str, prompt: str) -> Dict[str, Any]:
        provider = self.providers.get(provider_name)
        if not provider:
            raise ValueError(f"Provider {provider_name} not supported.")

        start_time = time.perf_counter()
        
        # Simulated or actual call
        response_text, token_usage = provider.generate(model_id, prompt)
        
        end_time = time.perf_counter()
        total_time = end_time - start_time
        
        # Calculate Metrics
        tokens_count = token_usage.get("total_tokens", 0)
        tokens_per_sec = tokens_count / total_time if total_time > 0 else 0
        
        return {
            "model": model_id,
            "latency_sec": round(total_time, 3),
            "total_tokens": tokens_count,
            "tokens_per_sec": round(tokens_per_sec, 2),
            "response_preview": response_text[:100] + "..."
        }
