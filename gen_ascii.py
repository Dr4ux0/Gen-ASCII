#!/usr/bin/env python3

import pyfiglet
import os
import platform

# Constantes
SEPARATOR = "=" * 80
FONTS = pyfiglet.FigletFont.getFonts()

def clear():
    os.system("cls" if platform.system().lower() == "windows" else "clear")

def welcome():
    clear()
    print("""
\033[1;32m
         ██████╗ ███████╗███╗   ██╗     █████╗ ███████╗ ██████╗██╗██╗
        ██╔════╝ ██╔════╝████╗  ██║    ██╔══██╗██╔════╝██╔════╝██║██║
        ██║  ███╗█████╗  ██╔██╗ ██║    ███████║███████╗██║     ██║██║
        ██║   ██║██╔══╝  ██║╚██╗██║    ██╔══██║╚════██║██║     ██║██║
        ╚██████╔╝███████╗██║ ╚████║    ██║  ██║███████║╚██████╗██║██║
         ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝
                        \033[1;34mCreated By Dr4ux0\033[m \033[1;31mVersion 0.2\033[m
    """)

def generate_ascii(text, font):
    return pyfiglet.figlet_format(text, font=font)

def display_fonts():
    print("\nEscolha uma das fontes abaixo para gerar o ASCII Art:")
    for i, f in enumerate(FONTS, 1):
        print(f"{i}. {f}")
    print(f"\nTotal de fontes válidas: {len(FONTS)} fontes disponíveis.")
    print(f"Se preferir, pressione ENTER para gerar em todas as fontes.")

def save_to_file(text, font, filename="arts.txt"):
    with open(filename, "a") as file:
        file.write(f"\nFonte: {font}\n")
        file.write(generate_ascii(text, font))
        file.write("\n" + SEPARATOR + "\n")

def main():
    welcome()

    # Validação do texto
    while True:
        user_text = input("Digite o texto para converter em ASCII Art: ").strip()
        if user_text:
            break
        print("Por favor, insira um texto válido.")

    display_fonts()

    while True:
        font_choice = input("\nDigite o número da fonte desejada ou pressione ENTER para gerar em todas: ").strip()
        if not font_choice:
            chosen_font = None
            break
        elif font_choice.isdigit() and 1 <= int(font_choice) <= len(FONTS):
            chosen_font = FONTS[int(font_choice) - 1]
            break
        else:
            print("Opção inválida! Digite um número entre 1 e", len(FONTS))

    save_option = input("\nDeseja salvar o resultado em um arquivo? (s/n): ").strip().lower()
    save_to_file_flag = save_option == 's'

    if chosen_font:
        print(f"\nGerando ASCII Art usando a fonte: {chosen_font}")
        ascii_art = generate_ascii(user_text, chosen_font)
        print(ascii_art)
        if save_to_file_flag:
            save_to_file(user_text, chosen_font)
            print(f"Arte ASCII salva em 'arts.txt'.")
    else:
        print("\nGerando ASCII Art em todas as fontes disponíveis:\n")
        for font in FONTS:
            print(f"\nFonte: {font}")
            ascii_art = generate_ascii(user_text, font)
            print(ascii_art)
            print(SEPARATOR)
            if save_to_file_flag:
                save_to_file(user_text, font)
        if save_to_file_flag:
            print(f"\nTodas as artes ASCII foram salvas em 'arts.txt'.")

if __name__ == "__main__":
    main()
