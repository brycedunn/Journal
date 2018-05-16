# 8 May 2018
"""
This is a simple journal app for recording user-input texts.
"""
import journal


def main():
    """
    This method prints the header and runs the journal event loop.
    :return: header
    """
    print_header()
    run_event_loop()


def print_header():
    """
    This method prints the header on the screen.
    :return: header
    """
    print('-----------------------')
    print("    Bryce's Journal")
    print('-----------------------')


def run_event_loop():
    """
    This method asks the user for command.
    :return: string
    """
    cmd = 'EMPTY'
    # TODO: allow user to input the name of their journal
    journal_name = 'tests'
    journal_data = journal.load(journal_name)
    print('What would you like to do with your journal?')

    while cmd != 'x' and cmd:
        cmd = input("[L]ist entries. [A]dd entry. [X]Exit.")
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}' command".format(cmd))

    print('Done! Goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    """
    This method lists the journal entries
    :param data: from journal file
    :return: enumerated entries
    """
    #TODO: reverse the entry enumeration
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1 , entry))


def add_entry(data):
    """
    This method allows the user to type in a new journal entry.
    :param data: from journal file
    :return: none
    """
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()