from transformers import pipeline

gpt_pipeline = pipeline("text-generation", model = "gpt2")

def ask_question(prompt):
    result = gpt_pipeline(prompt, max_length=100, num_return_sequences = 1)
    return result[0]["generated_)text"]
