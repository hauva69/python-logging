#!/usr/bin/python3

'''Simple logging examples.'''

import logging

def _very_simple():
    logging.warning('Watch out!')
    logging.info('I told you so.')

def _main():
    _very_simple()

if __name__ == '__main__':
    _main()
