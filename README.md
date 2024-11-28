# Solver-de-Torres-de-Hanoi-com-Recursao

Para resolver o problema, foi usado uma abordagem recursiva. O algoritmo criado consiste em:

  ● Mover os n - 1 discos superiores da torre de origem para a torre auxiliar, usando a torre de destino como auxiliar.
  
  ● Mover o disco maior (o n-ésimo disco) da torre de origem para a torre de destino.
  
  ● Mover os n - 1 discos da torre auxiliar para a torre de destino, usando a torre de origem como auxiliar.
  
Esse processo é repetido até que todos os discos tenham sido movidos para
a torre de destino. A cada etapa, os discos são transferidos de uma torre para outra,
seguindo as regras de não colocar um disco maior em cima de um disco menor.
