import json
import magenta
import os
import os.path as osp

# input_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/json_midi/'
input_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/json_midi/00000/'
# infile = osp.join(input_dir,'2020-10-28_224250_1.midi')
output_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/magenta_midi/'
# outfile = osp.join(output_dir,'2020-10-28_224250_1.txt')
bundle_dir = '/u/ys4aj/YuchenSun/Course/CS4710/AI_PROJECT/codes/bach-doodle/to_polyphony/polyphony_rnn.mag'
run_dir = '/u/ys4aj/YuchenSun/Course/CS4710/magenta/magenta/models/polyphony_rnn/polyphony_rnn_generate.py'

# for json_dir in os.listdir(input_dir):
#     full_json_dir = osp.join(input_dir,json_dir)
#     for item in os.listdir(full_json_dir):
#         midi_dir = osp.join(full_json_dir,item)
#         poly_dir = osp.join(output_dir,json_dir+'_'+item)
#         command = [
#             'python',run_dir,'--bundle_file=',bundle_dir,'--output_dir=',poly_dir,'--num_output=1 --num_steps=68 --primer_midi=',midi_dir,'--condition_on_primer=false —-inject_primer_during_generation=true'
#         ]

#         print(' '.join(command))
#         run_result = os.system(' '.join(command))


for json_dir in os.listdir(input_dir):
        midi_dir = osp.join(input_dir,json_dir)
        poly_dir = osp.join(output_dir,json_dir)
        command = [
            'python',run_dir,'--bundle_file='+bundle_dir,'--output_dir='+poly_dir,'--num_output=1 --num_steps=68 --primer_midi='+midi_dir,'--condition_on_primer=false —-inject_primer_during_generation=true'
        ]

        print(' '.join(command))
        run_result = os.system(' '.join(command))
