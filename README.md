# 📊 LLM Performance Benchmarker

Architecting the future of AI Strategy requires more than just intuition; it requires hard data. This tool is a production-grade utility to benchmark **Large Language Models** (LLMs) across critical performance metrics: Latency, Throughput (Tokens/Sec), and Cost.

## 🚀 Strategic Value
When deploying AI at scale, choosing the right model is a balancing act between quality, speed, and cost. This benchmarker allows engineers and strategists to:
- **Optimize Latency**: Identify the fastest models for real-time agentic interactions.
- **Cost Management**: Compare "Token-for-Buck" value across GPT, Claude, and local Llama models.
- **Operational Clarity**: Provide stakeholders with verifiable performance reports before full-scale deployment.

## 🛠️ Key Metrics Tracked
- **TTFT (Time To First Token)**: Critical for user-facing applications.
- **TPS (Tokens Per Second)**: Measurement of raw inference throughput.
- **Total Latency**: End-to-end request time.
- **Cost Estimation**: Dynamic calculation based on current provider pricing models.

## 🏗️ Getting Started
1. Set up your `.env` with provider API keys.
2. Install requirements: `pip install -r requirements.txt`
3. Run a benchmark: `python benchmark_run.py --model gpt-4-turbo --prompt "Explain quantum physics"`

---
*Data-driven intelligence for agentic systems.*
