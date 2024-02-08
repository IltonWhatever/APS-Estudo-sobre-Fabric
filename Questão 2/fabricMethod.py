from abc import ABC, abstractmethod

class Log(ABC):
    
    @abstractmethod
    def registrar(self, msg: str):
        pass

class LogArquivo(Log):
    def registrar(self, msg: str):
        print(f"Mensagem registrada do tipo LogArquivo: {msg}")

class LogConsole(Log):
    def registrar(self, msg: str):
        print(f"Mensagem registrada do tipo LogConsole: {msg}")

class LogBancoDeDados(Log):
    def registrar(self, msg: str):
        print(f"Mensagem registrada do tipo LogBancoDeDados: {msg}")

class LogFactory:
    @staticmethod
    def criar_log(tipo: str) -> Log:
        if tipo.lower() == 'arquivo':
            return LogArquivo()
        elif tipo.lower() == 'console':
            return LogConsole()
        elif tipo.lower() == 'banco':
            return LogBancoDeDados()
        else:
            raise ValueError('Tipo de log desconhecido')

if __name__ == "__main__":
    tipo = input("Digite o tipo de log a ser usado [Arquivo, console, banco]: ")
    msg = input("Digite a mensagem a ser armazenada em Log: ")

    log = LogFactory.criar_log(tipo)
    log.registrar(msg)