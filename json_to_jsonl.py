
import json

file_path = '생활법령.json'

# Define the input JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    input_json = json.load(f)

# Convert the input JSON data to the desired JSONL format
output_jsonl = []
for item in input_json:
    messages = []
    messages.append({"role": "system", "content": "너는 법률 상담을 해주는 AI야."})
    messages.append({"role": "user", "content": item["instruction"]})
    messages.append({"role": "assistant", "content": item["output"]})
    output_jsonl.append({"messages": messages})

# Save the output as a JSONL file
output_file_path = '생활법령.jsonl'
with open(output_file_path, 'w') as file:
    for entry in output_jsonl:
        json.dump(entry, file, ensure_ascii=False)
        file.write('\n')

output_file_path

