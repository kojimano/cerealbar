""" Main function for Cereal Bar experiments. """
from __future__ import absolute_import

import os
import logging
import multiprocessing

from agent.config import util
from agent.config import program_args
from agent.simulation import replay


def main():
    """ Main function for Cereal Bar experiments. """
    multiprocessing.set_start_method('spawn')
    args: program_args.ProgramArgs = util.get_args()

    run_type: program_args.RunType = args.get_run_type()

    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('matplotlib').setLevel(logging.WARNING)
    logging.getLogger('pyscreenshot').setLevel(logging.WARNING)
    logging.getLogger('slack').setLevel(logging.WARNING)

    logging.info(args)
    if run_type == program_args.RunType.TRAIN:
        logging.basicConfig(filename=os.path.join(args.get_training_args().get_save_directory(), 'train.log'),
                            level=logging.DEBUG)
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.info('Using device: %s', str(DEVICE))

        train(args)
    elif run_type == program_args.RunType.REPLAY:
        replay.replay(args.get_game_args(), args.get_replay_args())
    elif run_type == program_args.RunType.EVAL:
        logging.basicConfig(filename=os.path.join(args.get_training_args().get_save_directory(), 'eval.log'),
                            level=logging.DEBUG)
        logging.getLogger().addHandler(logging.StreamHandler())

        evaluate_games(args)


if __name__ == '__main__':
    main()