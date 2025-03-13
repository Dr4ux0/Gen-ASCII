#!/usr/bin/env python3

import pyfiglet
import os
import platform
import argparse
import sys
import time

# Constantes
SEPARATOR = "=" * 80
FONTS = pyfiglet.FigletFont.getFonts()
DEFAULT_FONT = "slant"

# Cores ANSI
RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
RESET = "\033[m"


def clear():
    """Limpa o terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    """Exibe uma mensagem de boas-vindas"""
    clear()
    print(f"""
{GREEN}
         ██████╗ ███████╗███╗   ██╗     █████╗ ███████╗ ██████╗██╗██╗
        ██╔════╝ ██╔════╝████╗  ██║    ██╔══██╗██╔════╝██╔════╝██║██║
        ██║  ███╗█████╗  ██╔██╗ ██║    ███████║███████╗██║     ██║██║
        ██║   ██║██╔══╝  ██║╚██╗██║    ██╔══██║╚════██║██║     ██║██║
        ╚██████╔╝███████╗██║ ╚████║    ██║  ██║███████║╚██████╗██║██║
         ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝
{BLUE}                        Created By Dr4ux0 {RED}Version 0.4{RESET}
    """)


def generate_ascii(text, font):
    """Gera arte ASCII para um texto usando uma fonte específica"""
    return pyfiglet.figlet_format(text, font=font)


def display_fonts():
    """Exibe a lista de fontes disponíveis"""
    print("\nEscolha uma das fontes abaixo para gerar o ASCII Art:")
    for i, f in enumerate(FONTS, 1):
        print(f"{i}. {f}")
    print(f"\nTotal de fontes disponíveis: {len(FONTS)}")
    print(f"Pressione ENTER para gerar em todas as fontes.")


def save_to_file(text, font, filename="arts.txt"):
    """Salva a arte ASCII gerada em um arquivo"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"\nFonte: {font}\n")
        file.write(generate_ascii(text, font))
        file.write("\n" + SEPARATOR + "\n")


def progress_bar(total, duration=3):
    """Exibe uma barra de progresso de 0% a 100%"""
    steps = 30
    interval = duration / steps

    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = "█" * i + "-" * (steps - i)
        sys.stdout.write(f"\r{GREEN}[{bar}] {percent}%{RESET}")
        sys.stdout.flush()
        time.sleep(interval)

    sys.stdout.write("\n")


def generate_and_display(text, font=None, save=False):
    """Gera e exibe ASCII Art apenas se uma única fonte for escolhida"""

    if font:
        
        print(f"\nGerando ASCII Art usando a fonte: {font}")
        progress_bar(100, 2)
        ascii_art = generate_ascii(text, font)
        print(ascii_art)
        if save:
            save_to_file(text, font)
            print(f"Arte ASCII salva em 'arts.txt'.")
    else:
        
        print("\nGerando ASCII Art em todas as fontes disponíveis... (salvando no arquivo)")
        progress_bar(100, len(FONTS) * 0.02)  # Ajusta tempo baseado no número de fontes
        for f in FONTS:
            save_to_file(text, f)
        if save:
            print(f"\n{GREEN}Todas as artes ASCII foram salvas em 'arts.txt'.{RESET}")
        else:
            print(f"\n{RED}A geração foi concluída, mas nenhuma arte foi exibida na tela.{RESET}")


def main():
    welcome()

    parser = argparse.ArgumentParser(description="Gerador de ASCII Art")
    parser.add_argument("-t", "--text", type=str, help="Texto a ser convertido em ASCII Art")
    parser.add_argument("-f", "--font", type=str, choices=FONTS, help="Fonte a ser utilizada")
    parser.add_argument("-s", "--save", action="store_true", help="Salvar saída em um arquivo")

    args = parser.parse_args()

    user_text = args.text
    while not user_text:
        user_text = input("Digite o texto para converter em ASCII Art: ").strip()
        if not user_text:
            print(f"{RED}Por favor, insira um texto válido.{RESET}")


    chosen_font = args.font
    if not chosen_font:
        display_fonts()
        while True:
            font_choice = input("\nDigite o número da fonte desejada ou pressione ENTER para todas: ").strip()
            if not font_choice:
                break
            elif font_choice.isdigit() and 1 <= int(font_choice) <= len(FONTS):
                chosen_font = FONTS[int(font_choice) - 1]
                break
            else:
                print(f"{RED}Opção inválida! Escolha entre 1 e {len(FONTS)}.{RESET}")

    generate_and_display(user_text, chosen_font, args.save or input("\nDeseja salvar? (s/n): ").strip().lower() == 's')


if __name__ == "__main__":
    main()
