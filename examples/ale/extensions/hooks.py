from chainerrl.experiments.hooks import StepHook
import os
from .utils import data as dutils


class ExtendedStepHook(StepHook):
    def __init__(self):
        pass

    def raw_frame(self, raw_frame):
        pass


class SaveStateHook(ExtendedStepHook):
    def __init__(self, data_size=10 ** 6, outdir='states'):
        self.states = []
        self.data_size = data_size
        self.outdir = outdir
        self.last_raw_frame = None
        self.num_saved_frames = 0
        dutils.create_dir_if_not_exists(outdir)

    def __call__(self, monitor, agent, step):
        last_state = agent.last_state
        if self.raw_frame is not None:
            last_frame = self.last_raw_frame
        else:
            last_frame = last_state[3]
        last_action = agent.last_action

        data = dict(frame=last_frame, action=last_action)
        self.states.append(data)

        num_frames = len(self.states)
        if (num_frames % 1000) == 0:
            print('states appended so far: ' + str(len(self.states)))

        if (num_frames % self.data_size) == 0:
            self.num_saved_frames += num_frames
            dutils.pickle_data(os.path.join(self.outdir, '{}.pickle'.format(self.num_saved_frames)), self.states)
            self.states = []

    def raw_frame(self, raw_frame):
        self.last_raw_frame = raw_frame


class CheckStateHook(ExtendedStepHook):
    def __init__(self):
        pass

    def __call__(self, monitor, agent, step):
        last_state = agent.last_state
        last_action = agent.last_action
        last_frame = last_state[3]
        print('last state len: ', str(len(last_state)))
        print('last frame shape: ', str(last_frame.shape))
        print('last action: ', str(last_action))
