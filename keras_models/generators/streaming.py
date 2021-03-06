from keras.layers import Dense, Input
from keras.models import Model
from pathlib import Path
import spacy
from itertools import product, chain
from keras.utils import Sequence
from collections import Counter
import numpy as np
from time import time
from keras import backend as K
import random


class StreamingFromDirGenerator(Sequence):

    def __init__(self, datadir, batch_size, random_seed=None, shuffle=True):

        self.datadir = Path(datadir)
        self.instances = [f for f in self.datadir.iterdir() if f.is_file() and f.name.endswith('npz')]
        assert self.datadir.exists() and self.datadir.is_dir(), f'path:{datadir} is not a folder or does not exist.'

        self.shuffle = shuffle
        self.batch_size = batch_size
        self.steps_each_epoch = len(self.instances) // self.batch_size + 1

        np.random.seed(random_seed or int(time()))
        self.on_epoch_end()

    def __len__(self):
        return len(self.instances)

    def __getitem__(self, index):

        istart = index * self.batch_size % len(self.instances)
        instances = self.instances[istart: istart + self.batch_size]

        X, Y = [], []

        for i, ins in enumerate(instances):
            with np.load(ins.absolute().as_posix()) as data:
                X.append(data['x'])
                Y.append(data['y'])

        X = np.array(X)
        Y = np.array(Y)

        return X, Y

    def on_epoch_end(self):
        if self.shuffle:
            random.shuffle(self.instances)
        return super().on_epoch_end()

    def summary(self, stdout=True):
        msg = f'''>>> Streaming Data Generator Summary:
        | Name             |                       Value                        |
        |------------------+----------------------------------------------------|
        | data_dir         | {self.datadir.absolute().as_posix():^50s} |
        | batch_size       | {self.batch_size:^50d} |
        | instances count  | {len(self.instances):^50d} |
        | steps_each_epoch | {len(self.instances) // self.batch_size + 1:^50d} |
        \n'''

        if stdout:
            print(msg)
        return msg
