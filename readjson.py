
import json

file = open('result.txt','w')


tweets=[]
result = []
count = 0
for line in open('file2.jsonl-00000-of-00192','r'):
    count +=1
    data = json.loads(line)
    result.append(data['input_sequence'])
    file.write(str(data['input_sequence'][0]))
    file.write('\n')
    # for i in data['input_sequence']:
    #      result.append(i)

# print(result[0])
# print("----------------------------------------------------------------")
# print(result[1])
# print(len(result))
# print(count)
file.close()

