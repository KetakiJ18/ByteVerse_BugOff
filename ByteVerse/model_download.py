from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "distilgpt2"

# Download the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model and tokenizer locally
model.save_pretrained("./distilgpt2")
tokenizer.save_pretrained("./distilgpt2")

print("Model and tokenizer have been downloaded and saved locally.")
