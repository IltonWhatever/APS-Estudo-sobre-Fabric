class Config:
  _instance = None

  def __init__(self):
    self.tema = "Claro"
    self.idioma = "PT-Br"
    self.fonte = 13

  @classmethod
  def instance(cls):
    if cls._instance is None:
      cls._instance = cls()
    return cls._instance

config1 = Config.instance()
config2 = Config.instance()

if config1 == config2:
  print("Ambas configurações possuem a mesma instancia: \n", id(config1),"\n", id(config2))