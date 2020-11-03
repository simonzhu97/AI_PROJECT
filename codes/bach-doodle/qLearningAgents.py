class qLearningAgent:
    def __init__(self, num_iter=100, alpha=0.5, gamma=1, epsilon=0.5):
        self.num_iter = num_iter
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = []

    def compute_actions_from_qvalue(self):
        return __

    def compute_qvalue(self):
        return __

    def get_action(self):
        #either return from compute_actions or random choice
        return __

    def update(self):
        #update both weights and self.actions
        return

    def get_legal_actions(self, state):
        return



class state:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_current_notes(self):
        return

    def get_previous_state(self):
        return


class layout:
    def __init__(self, note_seq_origin, note_seq_new):
        self.seq_origin = note_seq_origin
        self.seq_new = note_seq_new
        self.notes = {}
        self.update_notes()
        # self.notes_origin = [] # a list of notes
        # self.notes_new = []

    def update_notes(self):
        #update self.notes
        '''{(start_time, end_time):(origin_note, [new_notes])}'''
        pass




def get_major_notes(root):
    major_third = root + 4
    perfect_fifth = root + 7
    second_inversion = [root-8, root-5]
    consonance = [major_third, perfect_fifth, second_inversion[0], second_inversion[1]]
    return consonance

def get_dissonance(root):
    return [root+1, root+2, root-1, root-2, root-11, root-10, root+11, root+10]

#take in two pitch values; root is the original note and pitch is note being evaluated
# using major chords only
def get_major_reward(root, pitch):
    highest_reward = get_major_notes(root)
    dissonance = get_dissonance(root)
    octaves = [root+12, root-12]
    if pitch in highest_reward:
        return 50
    elif pitch in dissonance or pitch == root:
        return -50
    elif pitch in octaves:
        return 10
    elif abs(pitch-root) < 12:
        return 20
    # span more than one octave
    else:
        return -30


def get_comparison_reward(root, pitch, prev_root, prev_pitch):
    reward = 0
    pitch_dissonance = get_dissonance(pitch)
    if prev_root in pitch_dissonance or prev_pitch in pitch_dissonance:
        reward -= 40
    if abs(pitch-prev_root) > 12 or abs(pitch-prev_pitch) > 12:
        reward -= 30
    if root == prev_root and pitch == prev_pitch:
        reward -= 10
    consonance = get_major_notes(root)
    consonance.extend(root+12, root-12)
    sub = [ele for ele in consonance if ele in [root, pitch, prev_root, prev_root]]
    if len(sub) == 4:
        reward += 40
    if len(sub) == 3:
        reward += 30
    if (root < max(prev_root, prev_pitch) and root > min(prev_root, prev_pitch)) or (pitch < max(prev_root, prev_pitch) and pitch > min(prev_root, prev_pitch)):
        reward += 10

    return reward
        

def get_total_reward(root, pitch, prev_root, prev_pitch):
    return get_major_reward(root, pitch)+get_comparison_reward(root, pitch, prev_root, prev_pitch)
    


