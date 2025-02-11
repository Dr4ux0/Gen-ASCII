#!/usr/bin/env python3

import pyfiglet
import os
import platform

def clear():
    system_name = platform.system().lower()
    if system_name == "windows":
        os.system("cls")
    else:
        os.system("clear")

def welcome():
    clear()
    print("""
\033[1;32m
     ██████╗ ███████╗███╗   ██╗     █████╗ ███████╗ ██████╗██╗██╗
    ██╔════╝ ██╔════╝████╗  ██║    ██╔══██╗██╔════╝██╔════╝██║██║
    ██║  ███╗█████╗  ██╔██╗ ██║    ███████║███████╗██║     ██║██║
    ██║   ██║██╔══╝  ██║╚██╗██║    ██╔══██║╚════██║██║     ██║██║
    ╚██████╔╝███████╗██║ ╚████║    ██║  ██║███████║╚██████╗██║██║
    ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝\033[m   
                    \033[1;34mCreated By Dr4ux0\033[m \033[1;31mVersion 0.1\033[m                                                  
    """)

def get_valid_fonts():
    valid_fonts = []
    for font in pyfiglet.Figlet().getFonts():
        try:
            pyfiglet.figlet_format("test", font=font)
            valid_fonts.append(font)
        except pyfiglet.FontNotFound:
            pass
    return valid_fonts

FONTS = get_valid_fonts()

def generate_ascii(text, font):
    return pyfiglet.figlet_format(text, font=font)

def display_fonts():
    print("\nEscolha uma das fontes abaixo para gerar o ASCII Art:")
    for i, f in enumerate(FONTS, 1):
        print(f"{i}. {f}")

    print(f"\nTotal de fontes válidas: {len(FONTS)} fontes disponíveis.")
    print(f"Se preferir, pressione ENTER para gerar em todas as fontes.")

def main():
    welcome()
    user_text = input("Digite o texto para converter em ASCII Art: ")

    display_fonts()

    font_choice = input("\nDigite o número da fonte desejada ou pressione ENTER para gerar em todas: ").strip()

    if font_choice.isdigit() and 1 <= int(font_choice) <= len(FONTS):
        chosen_font = FONTS[int(font_choice) - 1]
        print(f"\nGerando ASCII Art usando a fonte: {chosen_font}")
        print(generate_ascii(user_text, chosen_font))
    else:
        print("\nGerando ASCII Art em todas as fontes disponíveis:\n")
        for font in FONTS:
            print(f"\nFonte: {font}")
            print(generate_ascii(user_text, font))
            print("=" * 80)

if __name__ == "__main__":
    main()
