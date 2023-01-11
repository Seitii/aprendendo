pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', "CDG"),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destino = 'FCO'


voos = {}
for linha in open('flights.txt'):
  #print(linha)
  #print(linha.split(', '))
  origem, destino, saida, chegada, preco = linha.split(',')
  voos.setdefault((origem, destino), []) #ADICONA DENTRO DO DICIONARIO, CASO NAO EXISTIR A ORIGEM DESTINO
  voos[(origem, destino)].append((saida, chegada, int(preco)))

voos

