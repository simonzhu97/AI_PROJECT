import json
import magenta
import note_seq
from note_seq.protobuf import music_pb2 as mpb
import os
import os.path as osp

res = []

selected_file = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/qlearn_midi/demo.txt'
original_file = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/magenta_txt/'
out_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/final_midi/'

#original_file = 'C:/Users/lin_x/Desktop/UVA/2.3/CS 4710/final_project/AI_PROJECT/codes/bach-doodle/magenta_txt/'
#selected_file = 'C:/Users/lin_x/Desktop/UVA/2.3/CS 4710/final_project/AI_PROJECT/codes/bach-doodle/qlearn_midi/all_selected_try.txt'
#out_dir = 'C:/Users/lin_x/Desktop/UVA/2.3/CS 4710/final_project/AI_PROJECT/codes/bach-doodle/final_midi/'



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
print('\tLoading finished')

print('\tTransfering txt to result midi...')
for i in info.keys():
    origin_path = osp.join(original_file,i)
    new_pitchs = info[i]
    origin_info = []
    with open(origin_path,'r') as file:
        lines = [file.readline() for i in range(12)]
        origin_info = [l.strip().split(',') for l in lines]
    
    if len(origin_info) == 3:
        model = mpb.NoteSequence()
        for j in range(12):
            start, end, origin = origin_info[j]
            new = new_pitchs[j]
            model.notes.add(pitch=int(origin),start_time=float(start),end_time=float(end),velocity=80)
            model.notes.add(pitch=int(new),start_time=float(start),end_time=float(end),velocity=80)
        model.total_time=8
        model.tempos.add(qpm=60)

        name = i.strip().split('.')[0]+'_result.midi'
        out = osp.join(out_dir,name)

        note_seq.sequence_proto_to_midi_file(model, out)
    print('Finished')
