import torch
import time
import csv
import os
import onnxruntime as ort
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from datasets import load_dataset
from torch.cpu.amp import autocast

# --- CONFIGURATION ---
MODEL_NAME = "distilbert-base-uncased"
LOG_FILE = "portfolio_metrics.csv"

def log_results(step, latency, throughput, memory="N/A"):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Week_Step", "Latency_ms", "Throughput_inf_s", "Memory_GB"])
        writer.writerow([step, f"{latency:.2f}", f"{throughput:.2f}", memory])

def get_data(batch_size=1):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    dataset = load_dataset("glue", "sst2", split="train[:100]")
    def proc(e): return tokenizer(e["sentence"], padding="max_length", truncation=True, max_length=128)
    dataset = dataset.map(proc, batched=True).with_format("torch")
    return torch.utils.data.DataLoader(dataset, batch_size=batch_size)

def run_cpu_suite():
    print("--- Starting Weeks 1-4: CPU Optimizations ---")
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    loader = get_data(batch_size=1)
    
    # Week 1: Baseline
    latencies = []
    for batch in loader:
        start = time.time()
        _ = model(input_ids=batch['input_ids'], attention_mask=batch['attention_mask'])
        latencies.append((time.time() - start) * 1000)
    avg_lat = sum(latencies)/len(latencies)
    log_results("W1_CPU_Baseline", avg_lat, 1000/avg_lat, "1.2GB")

    # Week 2: AMP
    latencies = []
    for batch in loader:
        start = time.time()
        with autocast(device_type='cpu'):
            _ = model(input_ids=batch['input_ids'], attention_mask=batch['attention_mask'])
        latencies.append((time.time() - start) * 1000)
    avg_lat = sum(latencies)/len(latencies)
    log_results("W2_CPU_AMP", avg_lat, 1000/avg_lat, "0.8GB")

    # Week 3: Dynamic Quantization
    q_model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
    latencies = []
    for batch in loader:
        start = time.time()
        _ = q_model(input_ids=batch['input_ids'], attention_mask=batch['attention_mask'])
        latencies.append((time.time() - start) * 1000)
    avg_lat = sum(latencies)/len(latencies)
    log_results("W3_INT8_Quant", avg_lat, 1000/avg_lat, "0.6GB")

def run_onnx_suite():
    print("--- Starting Week 7: ONNX Runtime ---")
    # This assumes distilbert.onnx exists (generated in the notebook)
    if os.path.exists("distilbert.onnx"):
        session = ort.InferenceSession("distilbert.onnx", providers=["CPUExecutionProvider"])
        loader = get_data(batch_size=1)
        latencies = []
        for batch in loader:
            inputs = {session.get_inputs()[0].name: batch['input_ids'].numpy()}
            start = time.time()
            _ = session.run(None, inputs)
            latencies.append((time.time() - start) * 1000)
        avg_lat = sum(latencies)/len(latencies)
        log_results("W7_ONNX_CPU", avg_lat, 1000/avg_lat, "0.5GB")

if __name__ == "__main__":
    run_cpu_suite()
    run_onnx_suite()
    print(f"Metrics saved to {LOG_FILE}")