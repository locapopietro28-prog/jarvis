"""
Modulo per la gestione della mappa interattiva del mondo
Visualizza e gestisce informazioni geografiche
"""

import json
from typing import List, Dict, Optional
from pathlib import Path


class WorldMap:
    """Gestione della mappa del mondo e informazioni geografiche"""
    
    def __init__(self):
        """Inizializza la mappa del mondo"""
        self.data_dir = Path(__file__).parent.parent / "data"
        self.countries_data = self._load_countries_data()
    
    def _load_countries_data(self) -> Dict:
        """
        Carica i dati dei paesi dal file JSON
        
        Returns:
            Dict: Dati dei paesi
        """
        try:
            countries_file = self.data_dir / "countries.json"
            if countries_file.exists():
                with open(countries_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Errore nel caricamento dei dati: {str(e)}")
        
        # Dati di fallback
        return self._get_default_countries()
    
    def _get_default_countries(self) -> Dict:
        """
        Restituisce dati di fallback per i paesi
        
        Returns:
            Dict: Dati predefiniti dei paesi
        """
        return {
            "italia": {
                "capitale": "Roma",
                "continente": "Europa",
                "popolazione": "59.1 milioni",
                "coordinate": [41.8719, 12.5674]
            },
            "germania": {
                "capitale": "Berlino",
                "continente": "Europa",
                "popolazione": "83.4 milioni",
                "coordinate": [51.1657, 10.4515]
            },
            "francia": {
                "capitale": "Parigi",
                "continente": "Europa",
                "popolazione": "67.7 milioni",
                "coordinate": [46.2276, 2.2137]
            },
            "spagna": {
                "capitale": "Madrid",
                "continente": "Europa",
                "popolazione": "47.4 milioni",
                "coordinate": [40.4637, -3.7492]
            },
            "inghilterra": {
                "capitale": "Londra",
                "continente": "Europa",
                "popolazione": "56.5 milioni",
                "coordinate": [55.3781, -3.4360]
            },
        }
    
    def get_country_info(self, country_name: str) -> Optional[str]:
        """
        Ottiene informazioni su un paese
        
        Args:
            country_name (str): Nome del paese
            
        Returns:
            Optional[str]: Informazioni formattate sul paese
        """
        country_key = country_name.lower()
        
        if country_key in self.countries_data:
            country_data = self.countries_data[country_key]
            info = f"🌍 {country_name.title()}\n"
            info += f"  📍 Capitale: {country_data.get('capitale', 'N/A')}\n"
            info += f"  🌎 Continente: {country_data.get('continente', 'N/A')}\n"
            info += f"  👥 Popolazione: {country_data.get('popolazione', 'N/A')}"
            return info
        
        return None
    
    def get_countries_list(self) -> List[str]:
        """
        Ottiene la lista di tutti i paesi disponibili
        
        Returns:
            List[str]: Lista dei paesi
        """
        return list(self.countries_data.keys())
    
    def display_map(self) -> None:
        """
        Visualizza la mappa interattiva del mondo
        """
        try:
            import matplotlib.pyplot as plt
            import geopandas as gpd
            from config.settings import MAP_CONFIG
            
            # Carica i dati geografici
            world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
            
            # Crea la figura
            fig, ax = plt.subplots(figsize=MAP_CONFIG['figsize'], dpi=MAP_CONFIG['dpi'])
            
            # Disegna la mappa
            world.plot(ax=ax, alpha=0.5, edgecolor=MAP_CONFIG['edgecolor'], cmap=MAP_CONFIG['cmap'])
            
            # Aggiungi titolo e label
            ax.set_title('🗺️ Mappa Interattiva del Mondo', fontsize=16, fontweight='bold')
            ax.set_xlabel('Longitudine')
            ax.set_ylabel('Latitudine')
            
            # Mostra la mappa
            plt.tight_layout()
            plt.show()
            
        except ImportError:
            print("⚠️ Librerie geografiche non installate. Installa con: pip install geopandas matplotlib")
        except Exception as e:
            raise Exception(f"Errore nella visualizzazione della mappa: {str(e)}")