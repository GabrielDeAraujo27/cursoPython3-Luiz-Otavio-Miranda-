from logy import logy, logFileMixin, logPrintMixin
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


if __name__ == '__main__':
    #l = logy()
    #l.logy('Qualquer coisa')
    l = logFileMixin()
    l._logy('Qualquer coisa')
    l.log_error('Qualquer coisa')
    l.log_success('Qualquer coisa')
    l._logy('Qualquer coisa')

    print(LOG_FILE)