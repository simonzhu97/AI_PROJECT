import json
import magenta
import note_seq
from note_seq.protobuf import music_pb2 as mpb

res = []
count = 0

print('initializing...')
with open('/u/ys4aj/YuchenSun/Course/CS4710/bach-doodle/json_ver/bach-doodle.jsonl-00000-of-00192','r') as file:
    data = file.readlines()
    for line in data:
        info = json.loads(line)['input_sequence']#[0]['notes']
        res.append(info)

print('\n\ngenerating files...')
#for single in res:
for i in range(100):
    single = res[i]
    count += 1
    model = mpb.NoteSequence()
    notes = single[0]['notes']
    tempos = single[0]['tempos'][0]['qpm']
    total_time = single[0]['totalTime']
    for n in notes:
        # print(n)
        if 'startTime' not in n.keys():
            start_time = 0.0
        else:
            start_time = n['startTime']
        pitch, end_time, velocity = n['pitch'], n['endTime'],n['velocity']
        model.notes.add(pitch=pitch, start_time=start_time, end_time=end_time, velocity=velocity)
    model.total_time = total_time
    model.tempos.add(qpm=tempos)

    name = '/u/ys4aj/YuchenSun/Course/CS4710/bach-doodle/json_ver/outfile/00000_'+str(count)+'.midi'

    note_seq.sequence_proto_to_midi_file(model, name)
    print('\tfile '+str(count)+' generated')

# print(res[0])
# print()
# print(res[1])



#midi_io.note_sequence_to_midi_file(res, '/u/ys4aj/YuchenSun/Course/CS4710/bach-doodle/json_ver/test_out.midi', drop_events_n_seconds_after_last_note=None)
