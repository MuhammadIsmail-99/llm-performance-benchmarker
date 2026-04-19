import argparse
from benchmarker.core import BenchmarkingSuite
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser(description="LLM Performance Benchmarker")
    parser.add_argument("--provider", default="openai", help="Provider to test")
    parser.add_argument("--model", default="gpt-4-turbo", help="Model ID to test")
    parser.add_argument("--prompt", default="Calculate the future of AI", help="Prompt to send")
    
    args = parser.parse_args()
    
    suite = BenchmarkingSuite()
    print(f"\n--- Running Benchmark for {args.model} ---")
    
    results = suite.run_benchmark(args.provider, args.model, args.prompt)
    
    # Format table
    table_data = [
        ["Metric", "Value"],
        ["Model", results["model"]],
        ["Latency (s)", results["latency_sec"]],
        ["Tokens", results["total_tokens"]],
        ["Tokens/Sec", results["tokens_per_sec"]]
    ]
    
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
    print(f"\nResponse Preview: {results['response_preview']}")

if __name__ == "__main__":
    main()
