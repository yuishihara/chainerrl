import os
import six.moves.cPickle as pickle


def create_dir_if_not_exists(outdir):
    if os.path.exists(outdir):
        if not os.path.isdir(outdir):
            raise RuntimeError(
                '{} is not a directory'.format(outdir))
        else:
            return
    os.makedirs(outdir)


def pickle_data(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
