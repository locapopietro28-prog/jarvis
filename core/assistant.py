"""
Classe principale dell'assistente Jarvis
Gestisce i comandi e coordina le varie funzionalità
"""

from core.command_processor import CommandProcessor
from config.settings import AVAILABLE_COMMANDS


class JarvisAssistant:
    """Assistente principale Jarvis"""
    
    def __init__(self):
        """Inizializza l'assistente"""
        self.command_processor = CommandProcessor()
        self.running = True
    
    def process_command(self, user_input: str) -> str:
        """
        Elabora un comando dell'utente
        
        Args:
            user_input (str): Input dell'utente
            
        Returns:
            str: Risposta di Jarvis
        """
        return self.command_processor.process(user_input)
    
    def get_help(self) -> str:
        """
        Restituisce l'aiuto sui comandi disponibili
        
        Returns:
            str: Lista dei comandi disponibili
        """
        help_text = "📋 Comandi disponibili:\n\n"
        for command, description in AVAILABLE_COMMANDS.items():
            help_text += f"  • {command.upper()} - {description}\n"
        return help_text