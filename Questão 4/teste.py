from abc import ABC, abstractmethod
from typing import Any

# Interface para a fábrica abstrata
class RenderFactory(ABC):
    @abstractmethod
    def criar_renderizador_textura(self) -> Any:
        pass

    @abstractmethod
    def criar_renderizador_sombra(self) -> Any:
        pass

    @abstractmethod
    def criar_renderizador_modelo(self) -> Any:
        pass

# Implementação do Singleton
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Fábrica concreta para OpenGL
class OpenGLRenderFactory(RenderFactory, metaclass=Singleton):
    def criar_renderizador_textura(self) -> Any:
        return OpenGLRenderizadorTextura()

    def criar_renderizador_sombra(self) -> Any:
        return OpenGLRenderizadorSombra()

    def criar_renderizador_modelo(self) -> Any:
        return OpenGLRenderizadorModelo()

# Fábrica concreta para DirectX
class DirectXRenderFactory(RenderFactory, metaclass=Singleton):
    def criar_renderizador_textura(self) -> Any:
        return DirectXRenderizadorTextura()

    def criar_renderizador_sombra(self) -> Any:
        return DirectXRenderizadorSombra()

    def criar_renderizador_modelo(self) -> Any:
        return DirectXRenderizadorModelo()

# Produtos abstratos
class RenderizadorTextura(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class RenderizadorSombra(ABC):
    @abstractmethod
    def aplicar_sombra(self):
        pass

class RenderizadorModelo(ABC):
    @abstractmethod
    def renderizar_modelo(self):
        pass

# Produtos concretos para OpenGL
class OpenGLRenderizadorTextura(RenderizadorTextura):
    def renderizar(self):
        print("OpenGL: Renderizando textura")

class OpenGLRenderizadorSombra(RenderizadorSombra):
    def aplicar_sombra(self):
        print("OpenGL: Aplicando sombra")

class OpenGLRenderizadorModelo(RenderizadorModelo):
    def renderizar_modelo(self):
        print("OpenGL: Renderizando modelo")

# Produtos concretos para DirectX
class DirectXRenderizadorTextura(RenderizadorTextura):
    def renderizar(self):
        print("DirectX: Renderizando textura")

class DirectXRenderizadorSombra(RenderizadorSombra):
    def aplicar_sombra(self):
        print("DirectX: Aplicando sombra")

class DirectXRenderizadorModelo(RenderizadorModelo):
    def renderizar_modelo(self):
        print("DirectX: Renderizando modelo")

# Cliente
def main():
    # Escolher a fábrica desejada (OpenGL ou DirectX)
    opengl_factory = OpenGLRenderFactory()
    directx_factory = DirectXRenderFactory()

    # Criar renderizadores usando a fábrica escolhida
    opengl_renderizador_textura = opengl_factory.criar_renderizador_textura()
    opengl_renderizador_sombra = opengl_factory.criar_renderizador_sombra()
    opengl_renderizador_modelo = opengl_factory.criar_renderizador_modelo()

    directx_renderizador_textura = directx_factory.criar_renderizador_textura()
    directx_renderizador_sombra = directx_factory.criar_renderizador_sombra()
    directx_renderizador_modelo = directx_factory.criar_renderizador_modelo()

    # Utilizar os renderizadores
    opengl_renderizador_textura.renderizar()
    opengl_renderizador_sombra.aplicar_sombra()
    opengl_renderizador_modelo.renderizar_modelo()

    directx_renderizador_textura.renderizar()
    directx_renderizador_sombra.aplicar_sombra()
    directx_renderizador_modelo.renderizar_modelo()

if __name__ == "__main__":
    main()
