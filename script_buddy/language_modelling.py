import os
import torch

import transformers
from transformers import (GPT2Config, GPT2LMHeadModel, GPT2Tokenizer,
                          PreTrainedModel, PreTrainedTokenizer)

from torch.utils.data import (DataLoader, Dataset, RandomSampler,
                              SequentialSampler)

MODEL_CLASSES = {
    "gpt2": (GPT2Config, GPT2LMHeadModel, GPT2Tokenizer),
}

FILE_PATH = os.path.join("script_buddy","data","film_text.txt")

# Big thanks to the team at huggingface for providing their example
# on fine_tuning a dataset, this borrows heavily from that it.
# Please find a link to it below :-)
# https://github.com/huggingface/transformers/blob/master/examples/run_language_modeling.py
class ScriptData(Dataset):
    def __init__(self, tokenizer: PreTrainedTokenizer, file_path : str, block_size = 512 ):
        assert os.path.isfile(file_path)
        self.examples = []

        block_size = block_size - (tokenizer.max_len - tokenizer.max_len_single_sentence)
    

    def __len__(self):
        return len(self.examples)
    
    def __getitem__(self,item):
        return torch.tensor(self.examples[item],dtype= torch.long)

        


if __name__ == "__main__":
    sc = ScriptData(GPT2Tokenizer.from_pretrained("gpt2"),file_path= FILE_PATH)
