"""
This is the journal module. Describes methods for loading and saving the journal.
"""
import os


def get_full_pathname(name):
    """
    This method find the pathname for a journal file
    :param name: name of journal
    :return: pathname
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This is the base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method allows the user to save their journal entries to a journal file
    :param name: name of journal
    :param journal_data: entries
    :return: writes to file
    """
    filename = get_full_pathname(name)
    print('.....saving to : {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def add_entry(text, journal_data):
    """
    This method allows the user to add an entry
    :param text: entry
    :param journal_data: existing journal entries
    :return: appends to file
    """
    journal_data.append(text)
