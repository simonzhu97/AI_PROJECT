import json
import magenta
import note_seq
from note_seq.protobuf import music_pb2 as mpb
import os
import os.path as osp

# convert maganeta files to txt

input_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/magenta_midi/'
# infile = osp.join(input_dir,'2020-10-28_224250_1.midi')
output_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/magenta_txt/'
# outfile = osp.join(output_dir,'2020-10-28_224250_1.txt')

def equal(note1,note2):
    if not note1.start_time:
        note1.start_time = 0.0
    dur1, dur2 = note1.end_time-note1.start_time, note2.end_time-note2.start_time
    return dur1 == dur2 and note1.pitch == note2.pitch

for mag_dir in os.listdir(input_dir):
    full_dir = osp.join(input_dir,mag_dir)
    for variation in osp.listdir(full_dir):
        midi_dir = osp.join(full_dir, variation)
        outfile = osp.join(output_dir, variation+'.txt')

        print('Parsing midi files...')
        seq = note_seq.midi_file_to_note_sequence(midi_dir)
        origin = [i for i in seq.notes if i.end_time <= 8.0]
        new = [i for i in seq.notes if i.start_time >= 8.0]


        print('Cleansing new...')
        for o in origin:
            for c in new:
                if equal(o,c):
                    new.remove(c)

        print('Writing output file...')
        with open(outfile,'w') as file:
            for n in origin:
                start, end, pitch = n.start_time, n.end_time, n.pitch
                line = ','.join([str(start),str(end),str(pitch)+'\n'])
                file.write(line)
            file.write('------------------------\n')
            for n in new:
                start, end, pitch = n.start_time, n.end_time, n.pitch
                line = ','.join([str(start),str(end),str(pitch)+'\n'])
                file.write(line)
        print('FINISHED')
