import json
import magenta
import note_seq
from note_seq.protobuf import music_pb2 as mpb
import os
import os.path as osp

res = []

selected_file = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/qlearn_midi/all_selected.txt'
original_file = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/magenta_txt/'
out_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/final_midi/'
if not os.path.isdir(out_dir):
    command = ['mkdir', out_dir]
    print(' '.join(command))
    run_result = os.system(' '.join(command))

info = {}

print('\tLoading data...')
with open(selected_file,'r') as file:
    data = file.readlines()
    for line in data:
        content = line.strip().split(',')
        info[content[0]] = content[1:]
print(info)
print('\tLoading finished')

print('\tTransfering txt to result midi...')
for i in info.keys():
    origin_path = osp.join(original_file,i)
    new_pitchs = info[i]
    origin_info = []
    with open(origin_path,'r') as file:
        lines = [file.readline() for i in range(12)]
        origin_info = [l.strip().split(',') for l in lines]
    
    model = mpb.NoteSequence()
    for i in range(12):
        start, end, origin = origin_info[i]
        new = new_pitchs[i]
        model.notes.add(pitch=origin,start_time=start,end_time=end,velocity=80)
        model.notes.add(pitch=new,start_time=start,end_time=end,velocity=80)
    model.total_time=8
    model.tempos.add(qpm=60)

    name = i.strip().split('.')[0]+'_result.midi'
    out = osp.join(out_dir,name)

    note_seq.sequence_proto_to_midi_file(model, out)
print('Finished')