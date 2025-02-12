# ASCII Art Generator

Este é um script Python que permite gerar arte ASCII a partir de um texto fornecido pelo usuário. O script utiliza a biblioteca `pyfiglet` para criar diferentes estilos de arte ASCII com uma variedade de fontes disponíveis.

## Requisitos

- Python 3.x
- Biblioteca `pyfiglet`

## Instalação

1. **Instale o Python 3.x**:
   - Certifique-se de que o Python 3.x está instalado no seu sistema. Você pode verificar isso executando o comando:
     ```bash
     python3 --version
     ```
   - Se o Python 3.x não estiver instalado, você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. **Instale a biblioteca `pyfiglet`**:
   - Você pode instalar a biblioteca `pyfiglet` usando o `pip`, que é o gerenciador de pacotes do Python. Execute o seguinte comando no terminal:
     ```bash
     pip install pyfiglet
     ```

3. **Erro no pip install**:
   - Caso apareça o seguinte erro ao tentar instalar o `pyfiglet`:
     ```
     error: externally-managed-environment

     × This environment is externally managed
     ╰─> To install Python packages system-wide, try apt install
         python3-xyz, where xyz is the package you are trying to
         install.

        If you wish to install a non-Debian-packaged Python package,
        create a virtual environment using python3 -m venv path/to/venv.
        Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
        sure you have python3-full installed.

        If you wish to install a non-Debian packaged Python application,
        it may be easiest to use pipx install xyz, which will manage a
        virtual environment for you. Make sure you have pipx installed.

        See /usr/share/doc/python3.11/README.venv for more information.

     note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
     hint: See PEP 668 for the detailed specification.
     ```

4. **Solução**:
   - A maneira recomendada é usar um ambiente virtual para evitar conflitos com o sistema:

     ```bash
     python3 -m venv meu_ambiente
     source meu_ambiente/bin/activate  # Linux/macOS
     meu_ambiente\Scripts\activate     # Windows (CMD)
     meu_ambiente\Scripts\Activate.ps1 # Windows (PowerShell)

     pip install pyfiglet
     ```

## Como Usar

1. **Execute o script**:
   - Navegue até o diretório onde o script está localizado e execute o seguinte comando:
     ```bash
     python3 gen-ascii.py
     ```

2. **Digite o texto**:
   - O script exibirá uma mensagem e solicitará que você insira o texto que deseja converter em arte ASCII.

3. **Escolha a fonte**:
   - Uma lista de fontes será mostrada. Você pode escolher uma fonte específica digitando o número correspondente ou pressionar `ENTER` para gerar arte ASCII em todas as fontes disponíveis.

4. **Visualize a arte ASCII**:
   - O script gerará a arte ASCII com base na sua escolha e a exibirá no terminal.

## Exemplo de Uso

```bash
$ python3 gen-ascii.py

     ██████╗ ███████╗███╗   ██╗     █████╗ ███████╗ ██████╗██╗██╗
    ██╔════╝ ██╔════╝████╗  ██║    ██╔══██╗██╔════╝██╔════╝██║██║
    ██║  ███╗█████╗  ██╔██╗ ██║    ███████║███████╗██║     ██║██║
    ██║   ██║██╔══╝  ██║╚██╗██║    ██╔══██║╚════██║██║     ██║██║
    ╚██████╔╝███████╗██║ ╚████║    ██║  ██║███████║╚██████╗██║██║
     ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝
                    Created By Dr4ux0 Version 0.1

Digite o texto para converter em ASCII Art: Hello World

Escolha uma das fontes abaixo para gerar o ASCII Art:
1. 3-d
2. 3x5
3. 5lineoblique
...
Total de fontes válidas: mais de 500 fontes disponíveis.
Se preferir, pressione ENTER para gerar em todas as fontes.

Digite o número da fonte desejada ou pressione ENTER para gerar em todas: 1

Gerando ASCII Art usando a fonte: 3-d
  ___ ___   ___   ___   ___   ___   ___   ___ 
 / __| __| / _ \ / _ \ / _ \ / _ \ / _ \ / _ \
| (__| _| | (_) | (_) | (_) | (_) | (_) | (_) |
 \___|___| \___/ \___/ \___/ \___/ \___/ \___/
