from abc import ABC, abstractmethod

from saludo.domain.persona import Persona


class SaludarUseCase(ABC):
    @abstractmethod
    def saludar(self, persona: Persona) -> str:
        """Devuelve el mensaje de saludo"""