Este código define uma classe chamada RedeMetabolica que trabalha com reações metabólicas representadas como um grafo direcionado.
- Esta classe herda o 'AnalisadorGrafo' presente no script 'Grafos' deste mesmo reportório;
- Possui um método construtor que inicializa um novo objeto RedeMetabolica e chama o construtor da classe AnalisadorGrafo através do uso do 'super().init()'.

-> A função 'adicionar_reacao' recebe o nome da reação, os substratos e os produtos. Se a reação for reversível, as arestas também serão adicionadas no sentido contrário.

-> A função 'adicionar_grafo' adiciona uma reação ao grafo, juntamente com os nós (ou seja, os metabolitos) que estão envolvidos antes e depois da reação.

-> A função 'parse_reaction_string' analisa uma string contendo reações, divide-a em reações individuais e adiciona-as ao grafo. Esta função também desenha o grafo recorrendo à biblioteca graphviz. São utilizadas expressões regulares para fazer a divisão da string de reação em partes (nome da reação, substratos, tipo de reação, produtos), e em seguida, a função 'adicionar_grafo' adiciona a reação ao grafo.

A linha 'display(G.render('output', format='png'))' será responsável por criar uma representação visual do grafo, através do formato png.
Posteriormente, a imagem do grafo aparecerá diretamente no ambiente de execução (compatibilidade com notebook Jupyter ou IPython).
Os metabolitos são representados por bolas com cor verde e as reações aparecem em quadrados, a amarelo.
