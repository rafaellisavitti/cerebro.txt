def ensinar():
    pergunta = input("Digite a pergunta:").strip().lower()
    resposta = input("Digite a resposta:").strip().lower()

    with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta} - {resposta}\n")


def conversar():
    fala = input("Você: ").strip().lower()
    encontrou = False

    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(" - ")
                if len(dados) == 2:
                    pergunta_salva, resposta_salva = dados[0], dados[1]
                    if fala == pergunta_salva:
                        print(f"Bot: {resposta_salva}")
                        encontrou = True
                        break

            if not encontrou:
                print("Bot: Desculpe, não sei a resposta. Use a opção 2 para me ensinar.")

    except FileNotFoundError:
        print("Bot: Meu cérebro está vazio! ME ensine algo primeiro .")


def listar_conhecimento():
    base_dados = []
    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(" - ")
                if len(dados) == 2:
                    # Cria tupla (pergunta, resposta) e adiciona na lista
                    base_dados.append((dados[0], dados[1]))

        # Ordena alfabeticamente pela primeira posição da tupla (pergunta)
        base_dados.sort()

        print("\n--- MEMÓRIA DO PYBOT (ORDENADA) ---")
        for item in base_dados:
            print(f"Pergunta: {item[0]} -> Resposta: {item[1]}")

    except FileNotFoundError:
        print("Nenhum dado cadastrado ainda.")


# Aula 75: Laço while principal
while True:
    print("\n=== MENU PYBOT ===")
    print("1 - Conversar")
    print("2 - Ensinar nova resposta")
    print("3 - Listar conhecimento (A-Z)")
    print("4 - Sair")

    escolha = input("Digite sua opção: ")

    if escolha == "1":
        conversar()
    elif escolha == "2":
        ensinar()
    elif escolha == "3":
        listar_conhecimento()
    elif escolha == "4":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")   

   

