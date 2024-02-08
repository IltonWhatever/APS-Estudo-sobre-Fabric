from abc import ABC, abstractmethod

class Botao(ABC):
    @abstractmethod
    def click(self):
        pass

class Janela(ABC):
    @abstractmethod
    def abrir(self):
        pass

class Cursor(ABC):
    @abstractmethod
    def mover(self):
        pass

class Select(ABC):
    @abstractmethod
    def selecionar(self):
        pass

class Input(ABC):
    @abstractmethod
    def receber_entrada(self):
        pass

class UIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

    @abstractmethod
    def criar_cursor(self) -> Cursor:
        pass

    @abstractmethod
    def criar_select(self) -> Select:
        pass

    @abstractmethod
    def criar_input(self) -> Input:
        pass

class WindowsUIFactory(UIFactory):
    def criar_botao(self) -> Botao:
        return WindowsBotao()

    def criar_janela(self) -> Janela:
        return WindowsJanela()

    def criar_cursor(self) -> Cursor:
        return WindowsCursor()

    def criar_select(self) -> Select:
        return WindowsSelect()

    def criar_input(self) -> Input:
        return WindowsInput()

class LinuxUIFactory(UIFactory):
    def criar_botao(self) -> Botao:
        return LinuxBotao()

    def criar_janela(self) -> Janela:
        return LinuxJanela()

    def criar_cursor(self) -> Cursor:
        return LinuxCursor()

    def criar_select(self) -> Select:
        return LinuxSelect()

    def criar_input(self) -> Input:
        return LinuxInput()

class WindowsBotao(Botao):
    def click(self):
        print("Botão do Windows clicado")

class WindowsJanela(Janela):
    def abrir(self):
        print("Janela do Windows aberta")

class WindowsCursor(Cursor):
    def mover(self):
        print("Cursor do Windows movido")

class WindowsSelect(Select):
    def selecionar(self):
        print("Seleção no Windows")

class WindowsInput(Input):
    def receber_entrada(self):
        print("Entrada de dados no Windows")

class LinuxBotao(Botao):
    def click(self):
        print("Botão do Linux clicado")

class LinuxJanela(Janela):
    def abrir(self):
        print("Janela do Linux aberta")

class LinuxCursor(Cursor):
    def mover(self):
        print("Cursor do Linux movido")

class LinuxSelect(Select):
    def selecionar(self):
        print("Seleção no Linux")

class LinuxInput(Input):
    def receber_entrada(self):
        print("Entrada de dados no Linux")

def main():
    sistema_operacional = "Windows"
    if sistema_operacional == "Windows":
        fabrica = WindowsUIFactory()
    elif sistema_operacional == "Linux":
        fabrica = LinuxUIFactory()
    else:
        raise ValueError("Sistema operacional não suportado")

    botao = fabrica.criar_botao()
    janela = fabrica.criar_janela()
    cursor = fabrica.criar_cursor()
    select = fabrica.criar_select()
    entrada = fabrica.criar_input()

    botao.click()
    janela.abrir()
    cursor.mover()
    select.selecionar()
    entrada.receber_entrada()

if __name__ == "__main__":
    main()
