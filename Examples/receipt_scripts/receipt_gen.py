# Receipts file generation and processing using 'random', 'json', 'os' & 'shutil'
# Creating files with random key/values in JSON format using random.functions

import random
import json
import os

count = int(os.getev("FILE_COUNT") or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)