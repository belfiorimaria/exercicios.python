while true: # o loop infinito foi indicado
    comando = input( "digite 'sair' para desligar o motor: ")
   
    if comando.lower() == 'sair':
     print ("motor desligado.")
     break # a trava de segurança foi acionada!
    else:
     print(" o motor continua a rodar...")