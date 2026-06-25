"""
Modulo utilità di Jarvis
Contiene funzionalità aggiuntive e conversioni
"""

import requests
from datetime import datetime
from typing import Optional


class Utilities:
    """Classe per funzionalità utili e conversioni"""
    
    def __init__(self):
        """Inizializza le utilità"""
        self.timeout = 5
    
    def get_current_datetime(self) -> str:
        """Restituisce data e ora attuali formattate"""
        now = datetime.now()
        formatted = f"📅 Data e Ora:\n"
        formatted += f"  📆 {now.strftime('%d/%m/%Y')}\n"
        formatted += f"  🕐 {now.strftime('%H:%M:%S')}\n"
        formatted += f"  📍 Giorno della settimana: {self._get_day_name(now.weekday())}"
        return formatted
    
    def _get_day_name(self, day_num: int) -> str:
        """Restituisce il nome del giorno della settimana"""
        days = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
        return days[day_num]
    
    def get_weather(self, city: str) -> str:
        """Ottiene informazioni meteo per una città"""
        try:
            api_url = f"https://api.weatherapi.com/v1/current.json"
            params = {"key": "demo", "q": city, "aqi": "no"}
            response = requests.get(api_url, params=params, timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json()
                current = data.get('current', {})
                location = data.get('location', {})
                weather_info = f"🌤️ Meteo - {location.get('name', city)}\n"
                weather_info += f"  🌡️ Temperatura: {current.get('temp_c', 'N/A')}°C\n"
                weather_info += f"  💧 Umidità: {current.get('humidity', 'N/A')}%\n"
                weather_info += f"  💨 Vento: {current.get('wind_kph', 'N/A')} km/h\n"
                weather_info += f"  📝 Condizioni: {current.get('condition', {}).get('text', 'N/A')}"
                return weather_info
            else:
                return f"❌ Città '{city}' non trovata"
        except Exception as e:
            return f"⚠️ Servizio meteo temporaneamente non disponibile"
    
    def get_news(self) -> str:
        """Ottiene le ultime notizie"""
        try:
            news_data = [
                "📰 Ultime notizie italiane disponibili su: corriere.it, ansa.it, repubblica.it",
                "🌍 Notizie internazionali disponibili su: bbc.com, reuters.com, ap.org",
                "💻 Tech news disponibili su: techcrunch.com, theverge.com, arstechnica.com"
            ]
            return "\n".join(news_data)
        except Exception as e:
            return f"❌ Errore nel recupero delle notizie"
    
    def calculate_calories(self, args: str) -> str:
        """Calcola il fabbisogno calorico giornaliero (Harris-Benedict)"""
        try:
            parts = args.split()
            if len(parts) < 3:
                return "❌ Formato: calorie eta peso sesso (M/F)"
            
            age = int(parts[0])
            weight = float(parts[1])
            sex = parts[2].upper()
            height = float(parts[3]) if len(parts) > 3 else (175 if sex == 'M' else 165)
            
            if sex == 'M':
                bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)
            elif sex == 'F':
                bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
            else:
                return "❌ Sesso non valido. Usa 'M' o 'F'"
            
            tdee = bmr * 1.55
            result = f"🔥 Calorie giornaliere:\n"
            result += f"  BMR: {bmr:.0f} kcal\n"
            result += f"  TDEE: {tdee:.0f} kcal"
            return result
        except ValueError:
            return "❌ Inserisci numeri validi"
        except Exception as e:
            return f"❌ Errore: {str(e)}"
    
    def convert_units(self, args: str) -> str:
        """Converte unità di misura"""
        try:
            if " to " not in args:
                return "❌ Formato: conversioni 100 km to miles"
            
            parts = args.split(" to ")
            from_part = parts[0].strip().split()
            to_unit = parts[1].strip().lower()
            
            value = float(from_part[0])
            from_unit = from_part[1].lower()
            
            conversions = {
                ("km", "miles"): value * 0.621371,
                ("miles", "km"): value * 1.60934,
                ("m", "ft"): value * 3.28084,
                ("ft", "m"): value * 0.3048,
                ("cm", "inches"): value * 0.393701,
                ("inches", "cm"): value * 2.54,
                ("kg", "lbs"): value * 2.20462,
                ("lbs", "kg"): value * 0.453592,
                ("g", "oz"): value * 0.035274,
                ("oz", "g"): value * 28.3495,
                ("celsius", "fahrenheit"): (value * 9/5) + 32,
                ("fahrenheit", "celsius"): (value - 32) * 5/9,
            }
            
            key = (from_unit, to_unit)
            if key in conversions:
                result = conversions[key]
                return f"✅ {value} {from_unit} = {result:.2f} {to_unit}"
            else:
                return f"❌ Conversione non supportata"
        except ValueError:
            return "❌ Numero non valido"
        except Exception as e:
            return f"❌ Errore: {str(e)}"
