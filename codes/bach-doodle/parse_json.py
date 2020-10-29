import json
import magenta
import note_seq
from note_seq.protobuf import music_pb2 as mpb
import os
import os.path as osp

res = []

raw_data_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/raw_data/'
out_file_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/outfile/'
if not os.path.isdir(out_file_dir):
    command = ['mkdir', out_file_dir]
    print(' '.join(command))
    run_result = os.system(' '.join(command))

raw_data = [file for file in os.listdir(raw_data_dir) if file != 'bach-doodle.jsonl.tar.gz']

for name in raw_data:
    file_path = osp.join(raw_data_dir,name)

    print('Reading raw data', name)
    with open(file_path,'r') as file:
        data = file.readlines()
        for line in data:
            info = json.loads(line)['input_sequence']#[0]['notes']
            res.append(info)

    print('\tgenerating 100 midi files...')
    #for single in res:
    for i in range(100):
        single = res[i]
        model = mpb.NoteSequence()
        notes = single[0]['notes']
        tempos = single[0]['tempos'][0]['qpm']
        total_time = single[0]['totalTime']
        for n in notes:
            if 'startTime' not in n.keys():
                start_time = 0.0
            else:
                start_time = n['startTime']
            pitch, end_time, velocity = n['pitch'], n['endTime'], n['velocity']
            model.notes.add(pitch=pitch, start_time=start_time, end_time=end_time, velocity=velocity)
        model.total_time = total_time
        model.tempos.add(qpm=tempos)

        num = name.split('.')[1].split('-')[1]
        out_dir = osp.join(out_file_dir,num)
        if not os.path.isdir(out_dir):
            command = ['mkdir', out_dir]
            print(' '.join(command))
            run_result = os.system(' '.join(command))
        out = osp.join(out_dir,str(i+1)+'.midi')

        note_seq.sequence_proto_to_midi_file(model, out)
    print('\tgenerating finished\n')
