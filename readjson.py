import json
tweets=[]
result = []
for line in open('file2.jsonl-00000-of-00192','r'):
    data = json.loads(line)
    for i in data['input_sequence']:
         result.append(i)

print(result[0])