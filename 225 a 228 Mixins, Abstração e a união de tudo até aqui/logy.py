#abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class logy:
    def _logy(self, msg):
        raise NotImplementedError('Implemente o método log')
    def log_error(self, msg):
        return self._logy(f"Error: {msg}")
    def log_success(self, msg):
        return self._logy(f'Success: {msg}')

class logFileMixin(logy):
    def _logy(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class logPrintMixin(logy):
    def _logy(self, msg):
        print(f'{msg} ({self.__class__.__name__})')




