import random

while True:
  print("Pressione [1] para iniciar o jogo!")
  print("Pressione [2] para sair do jogo!")
  opcao = input("Escolha uma opção: ")

  if opcao == '2':
    print("GAME OVER!")
    break

  elif opcao == '1':
    hp_total = random.randint(200, 1000)

    jogador_hp = hp_total
    inimigo_hp = hp_total

    jogador_atq = random.randint(1, 50)
    jogador_def = random.randint(1, 50)

    inimigo_atq = random.randint(1, 50)
    inimigo_def = random.randint(1, 50)

    turno = 1

    while jogador_hp > 0 and inimigo_hp > 0:
      print("PLAYER")
      print(f"HP: {jogador_hp}")
      print(f"ATQ: {jogador_atq}")
      print(f"DEF: {jogador_def}")

      print("INIMIGO")
      print(f"HP: {inimigo_hp}")
      print(f"ATQ: {inimigo_atq}")
      print(f"DEF: {inimigo_def}")

      print(f"Turno: {turno}")
      print(f"HP PLAYER: {jogador_hp} | HP INIMIGO: {inimigo_hp}")

      acao = input("Sua vez: [1] Ataque | [2] Cura")

      if acao == '1':
        dano = jogador_atq - inimigo_def
        if dano < 0:
          dano =0
        inimigo_hp -= dano
        print(f"Você ataca! Inimigo perde {dano} HP")
      else:
        cura = random.randint(15, 30)
        jogador_hp += cura
        if jogador_hp > hp_total:
          jogador_hp = hp_total
        print(f"Você cura! Você recupera {cura} HP!")

        if inimigo_hp <= 0:
          print("Você vencer!")
          break

        escolha = random.choice(["Atacar","Curar"])

        if escolha == "Atacar":
          dano = inimigo_atq - jogador_def
          if dano < 0:
            dano = 0
          jogador_hp -= dano
          print(f"Inimigo ataca! Você {dano} HP")
        else:
          cura = random.randint(15, 30)
          inimigo_hp += cura
          if inimigo_hp > hp_total:
            inimigo_hp = hp_total
          print(f"Inimigo se cura em {cura} HP!")

        if jogador_hp <= 0:
          print("Você perdeu!")
          break

        turno += 1
        input("Pressione [ENTER] para continuar!")

    else:
      print("Opção inválida")