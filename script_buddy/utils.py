import transformers
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import random

def load_model(model_dir=None):
    if model_dir is None:
        model_dir = 'models/'

    device = 'cpu'
    if torch.cuda.is_available():
        device = 'cuda'

    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
    model = GPT2LMHeadModel.from_pretrained(model_dir)
    return model, tokenizer


def generate(model, tokenizer, input_text=None, num_samples=1, max_length=1000):
    model.eval()

    if input_text:
        input_ids = tokenizer.encode(input_text, return_tensors='pt')
        output = model.generate(
            input_ids= input_ids,
            do_sample=True,   
            top_k=50, 
            max_length = max_length,
            top_p=0.95, 
            num_return_sequences= num_samples
        )
    else:
        output = model.generate(
            bos_token_id=random.randint(1,30000),
            do_sample=True,   
            top_k=50, 
            max_length = max_length,
            top_p=0.95, 
            num_return_sequences=num_samples

        )


    decoded_output = []
    for sample in output:
        decoded_output.append(tokenizer.decode(
            sample, skip_special_tokens=True))

    print(decoded_output[0])



model, tokenizer = load_model()
generate(model, tokenizer,max_length=500)
