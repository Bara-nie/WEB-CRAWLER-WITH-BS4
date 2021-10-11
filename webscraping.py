from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd


tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

tokens = tokenizer.encode('you are worse than me', return_tensors='pt')

result = model(tokens)
result.logits
print(result)

int(torch.argmax(result.logits))+1

r = requests.get('')
soup = BeautifulSoup(r.text, 'html.parser')
regex = re.compile('.*script.*')
results = soup.find_all('p', {'class':type})
class= [result.text for result in results]

print(biden)