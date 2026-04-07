from datasets import load_dataset

dataset = load_dataset("wikitext", "wikitext-2-raw-v1")

train_data = dataset['train']
valid_data = dataset['validation']
test_data = dataset['test']

def save_dataset(split, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for line in split['text']:
            if line.strip():  # remove empty lines
                f.write(line + "\n")

save_dataset(train_data, "wiki.train.txt")
save_dataset(valid_data, "wiki.valid.txt")
save_dataset(test_data, "wiki.test.txt")

# dataset = load_dataset("openwebtext", split="train[:1%]")