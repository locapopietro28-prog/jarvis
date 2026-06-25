#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Jarvis - Assistente Intelligente
Punto di ingresso principale dell'applicazione
"""

from core.assistant import JarvisAssistant


def main():
    """Funzione principale di Jarvis"""
    print("🤖 Benvenuto in Jarvis!")
    print("Scrivi 'aiuto' per vedere i comandi disponibili")
    print("Scrivi 'esci' per uscire\n")
    
    jarvis = JarvisAssistant()
    
    while True:
        try:
            user_input = input("Tu: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() == 'esci':
                print("Jarvis: Arrivederci! 👋")
                break
            
            response = jarvis.process_command(user_input)
            print(f"Jarvis: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nJarvis: Arrivederci! 👋")
            break
        except Exception as e:
            print(f"Errore: {str(e)}")


if __name__ == "__main__":
    main()