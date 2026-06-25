"""
Modulo per operazioni matematiche
Gestisce i calcoli e le operazioni matematiche
"""

import re
from typing import Union


class Calculator:
    """Calcolatrice per operazioni matematiche"""
    
    def __init__(self):
        """Inizializza la calcolatrice"""
        self.supported_operators = {'+', '-', '*', '/', '%', '**', '//'}
    
    def calculate(self, expression: str) -> Union[int, float]:
        """
        Calcola il risultato di un'espressione matematica
        
        Args:
            expression (str): Espressione matematica (es: "2 + 2")
            
        Returns:
            Union[int, float]: Risultato del calcolo
            
        Raises:
            ValueError: Se l'espressione è non valida
        """
        expression = expression.replace(" ", "")
        
        # Valida l'espressione
        if not self._is_valid_expression(expression):
            raise ValueError("Espressione matematica non valida")
        
        try:
            # Usa eval con un ambiente limitato per sicurezza
            result = eval(expression, {"__builtins__": {}}, {})
            return result
        except ZeroDivisionError:
            raise ValueError("Divisione per zero non consentita")
        except Exception as e:
            raise ValueError(f"Errore nel calcolo: {str(e)}")
    
    def _is_valid_expression(self, expression: str) -> bool:
        """
        Valida un'espressione matematica
        
        Args:
            expression (str): Espressione da validare
            
        Returns:
            bool: True se valida, False altrimenti
        """
        # Controlla che contenga solo numeri e operatori validi
        allowed_chars = re.compile(r'^[\d\.\+\-\*/%\(\)]+$')
        return bool(allowed_chars.match(expression))