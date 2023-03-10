import cVetor

print("---- Testes -----")
vetor = cVetor.Vetor(5, 3, 3, 29, 43, 3)
print("[CRIAR][IMPRIMIR] Vetor:", vetor)
vetor.inserir(320)
print("[INSERIR] Vetor após adicionar um novo elemento:", vetor)
print("[BUSCAR] Posicao do elemento 29:", vetor.busca(29))
vetor.remover(29)
print("[REMOVER] Remover elemento 29:", vetor)
print("[TAMANHO] Tamanho do vetor:", vetor.tam())
print("[MINIMO] Mínimo:", vetor.minimo())
print("[MAXIMO] Máximo:", vetor.maximo())
print("[OCORRENCIAS] Qtd de elementos iguais a 3:", vetor.ocorrencias(3))
vetorb = cVetor.Vetor(5, 3, 3, 43, 3, 320)
print(f"[E_IDENTICO] Os vetores {vetor} e {vetorb} são iguais?", vetor == vetorb)
print("[INVERTER] Inverso:", vetor.inverter())
print("[GERAR ESTATISTICAS] Média:", vetor.estatisticas()[0])
print("[GERAR ESTATISTICAS] Desvio Padrão:", vetor.estatisticas()[1])
print("[GERAR ESTATISTICAS] Mediana:", vetor.estatisticas()[2])
print("[EXTRA - SOMATORIO] Somatório:", vetor.soma())
print("[EXTRA - ACESSAR ELEMENTO] Terceiro elemento:", vetor[2])
print("-----------------")
