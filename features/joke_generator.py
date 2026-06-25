"""
Modulo per la generazione casuale di barzellette
Utilizza un'API esterna per ottenere barzellette
"""

import requests
from typing import Optional, Dict


class JokeGenerator:
    """Generatore di barzellette da API esterne"""
    
    # API disponibili per le barzellette
    JOKE_APIS = {
        "official": "https://official-joke-api.appspot.com/random_joke",
        "geek": "https://v2.jokeapi.dev/joke/Programming",
        "general": "https://v2.jokeapi.dev/joke/Any",
    }
    
    def __init__(self):
        """Inizializza il generatore di barzellette"""
        self.timeout = 5
    
    def get_random_joke(self, api_type: str = "general") -> Optional[str]:
        """
        Ottiene una barzelletta casuale da un'API esterna
        
        Args:
            api_type (str): Tipo di API da utilizzare ('official', 'geek', 'general')
            
        Returns:
            Optional[str]: La barzelletta formattata o None se c'è un errore
        """
        try:
            api_url = self.JOKE_APIS.get(api_type, self.JOKE_APIS["general"])
            response = requests.get(api_url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            
            # Formatta la risposta in base al tipo di API
            if api_type == "official":
                return self._format_official_joke(data)
            else:
                return self._format_jokeapi_joke(data)
                
        except requests.exceptions.Timeout:
            return "❌ Timeout: Connessione troppo lenta con l'API"
        except requests.exceptions.ConnectionError:
            return "❌ Errore di connessione: Impossibile connettersi al servizio"
        except Exception as e:
            return f"❌ Errore nel recupero della barzelletta: {str(e)}"
    
    def _format_official_joke(self, data: Dict) -> str:
        """
        Formatta una barzelletta dall'API official-joke-api
        
        Args:
            data (Dict): Dati della barzelletta
            
        Returns:
            str: Barzelletta formattata
        """
        setup = data.get("setup", "")
        punchline = data.get("punchline", "")
        joke_type = data.get("type", "general")
        
        formatted = f"😂 Barzelletta ({joke_type.upper()}):\n"
        formatted += f"📝 {setup}\n"
        formatted += f"😄 {punchline}"
        return formatted
    
    def _format_jokeapi_joke(self, data: Dict) -> str:
        """
        Formatta una barzelletta dall'API jokeapi.dev
        
        Args:
            data (Dict): Dati della barzelletta
            
        Returns:
            str: Barzelletta formattata
        """
        joke_type = data.get("type", "single")
        category = data.get("category", "General")
        
        if joke_type == "single":
            joke = data.get("joke", "")
            formatted = f"😂 Barzelletta ({category}):\n"
            formatted += f"📝 {joke}"
        else:
            setup = data.get("setup", "")
            delivery = data.get("delivery", "")
            formatted = f"😂 Barzelletta ({category}):\n"
            formatted += f"📝 {setup}\n"
            formatted += f"😄 {delivery}"
        
        return formatted
    
    def get_multiple_jokes(self, count: int = 3, api_type: str = "general") -> str:
        """
        Ottiene multiple barzellette
        
        Args:
            count (int): Numero di barzellette da ottenere
            api_type (str): Tipo di API da utilizzare
            
        Returns:
            str: Multiple barzellette formattate
        """
        jokes = []
        for i in range(count):
            joke = self.get_random_joke(api_type)
            if joke and not joke.startswith("❌"):
                jokes.append(f"\n🎭 Barzelletta {i+1}:\n{joke}")
        
        if jokes:
            return "".join(jokes)
        else:
            return "❌ Impossibile recuperare le barzellette"
