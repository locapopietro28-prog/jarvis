"""
Processore di comandi per Jarvis
Elabora e route i comandi verso le funzionalità appropriate
"""

from features.calculator import Calculator
from features.world_map import WorldMap
from config.settings import AVAILABLE_COMMANDS


class CommandProcessor:
    """Elabora e gestisce i comandi dell'utente"""
    
    def __init__(self):
        """Inizializza il processore di comandi"""
        self.calculator = Calculator()
        self.world_map = WorldMap()
    
    def process(self, user_input: str) -> str:
        """
        Elabora un comando dell'utente
        
        Args:
            user_input (str): Input dell'utente
            
        Returns:
            str: Risposta al comando
        """
        user_input = user_input.strip().lower()
        
        # Dividi il comando dalla parte rimanente
        parts = user_input.split(None, 1)
        command = parts[0] if parts else ""
        args = parts[1] if len(parts) > 1 else ""
        
        # Routing dei comandi
        if command == "calcola":
            return self.handle_calculate(args)
        elif command == "mostra":
            return self.handle_show_country(args)
        elif command == "mappa":
            return self.handle_world_map()
        elif command == "paesi":
            return self.handle_list_countries()
        elif command == "aiuto":
            return self.handle_help()
        else:
            return f"❌ Comando non riconosciuto: '{command}'. Scrivi 'aiuto' per vedere i comandi disponibili."
    
    def handle_calculate(self, expression: str) -> str:
        """Gestisce i calcoli matematici"""
        if not expression:
            return "❌ Per favore fornisci un'espressione matematica. Esempio: calcola 2 + 2"
        
        try:
            result = self.calculator.calculate(expression)
            return f"✅ Risultato: {expression} = {result}"
        except Exception as e:
            return f"❌ Errore nel calcolo: {str(e)}"
    
    def handle_show_country(self, country_name: str) -> str:
        """Gestisce la visualizzazione di informazioni su un paese"""
        if not country_name:
            return "❌ Per favore fornisci il nome di un paese. Esempio: mostra Italia"
        
        try:
            info = self.world_map.get_country_info(country_name)
            if info:
                return f"✅ {info}"
            else:
                return f"❌ Paese '{country_name}' non trovato."
        except Exception as e:
            return f"❌ Errore: {str(e)}"
    
    def handle_world_map(self) -> str:
        """Gestisce la visualizzazione della mappa del mondo"""
        try:
            self.world_map.display_map()
            return "✅ Mappa del mondo visualizzata!"
        except Exception as e:
            return f"❌ Errore nella visualizzazione della mappa: {str(e)}"
    
    def handle_list_countries(self) -> str:
        """Elenca i paesi disponibili"""
        try:
            countries = self.world_map.get_countries_list()
            return f"✅ Paesi disponibili: {', '.join(countries[:10])}... (e altri)"
        except Exception as e:
            return f"❌ Errore: {str(e)}"
    
    def handle_help(self) -> str:
        """Mostra l'aiuto sui comandi"""
        help_text = "📋 Comandi disponibili:\n\n"
        for command, description in AVAILABLE_COMMANDS.items():
            help_text += f"  • {command.upper()} - {description}\n"
        return help_text