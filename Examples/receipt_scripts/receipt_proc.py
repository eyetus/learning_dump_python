# Create new directory with 'os'
# get filenames with glob and add to 'receipts'
# Iterate through 'receipts' adding 'content' dict values to subtotal
# using shutil to move files to new directory and print total

import random
import json
import os
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists")

subtotal = 0.0

for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print(f"Receipt subtotal: ${round(subtotal, 2)}")