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

