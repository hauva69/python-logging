#!/usr/bin/python3

'''Simple logging examples.'''

import logging

import mylib

def _very_simple():
    logging.warning('Watch out!')
    logging.info('I told you so.')

def _log2file():
    _clear_log_config()
    _fn = 'example.log'
    # encoding was introduced in Python 3.9.
    logging.basicConfig(filename=_fn, filemode='w', encoding='utf-8', level=logging.DEBUG)
    logging.debug('this message goes to the log file %s', _fn)
    logging.info('this is info')
    logging.warning('this is a warning')
    logging.error('and some non ASCII characters: äöÅü蟻')

def _formatted_log():
    _clear_log_config()
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
    logging.warning('is when the event was logged')

def _clear_log_config():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

def _main():
    _very_simple()
    _log2file()
    mylib.hello()
    _formatted_log()

if __name__ == '__main__':
    _main()
