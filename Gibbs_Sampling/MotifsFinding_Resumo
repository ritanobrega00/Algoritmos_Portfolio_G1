Motifs são padrões recorrentes em sequências biológicas que na maioria dos casos têm uma função biológica (e.g locaisde ligação de proteínas regulatórias ao DNA, domínios conservados de uma proteína, locais de splicing).
Há algumas dificuldades relacionadas com a descoberta de motifs como o facto da sequência do motif e localização não serem conhecidas e de variarem ligeiramente de um gene para outro.

Há vários tipos de padrões: 
- Blocos ou motifs:sem espaçamentos, determínisticos (sub-sequências constantes) (Consensus)
- Patterns: com espaçamentos, determínisticos (representados por expressões regulares)
- Perfis: estocásticos (definem probabilidades por posição); podem ser representados por uma matriz (ex: PWM, onde as colunas representam as posições e as linhas os caractéres do alfabeto, sendo as posições da matriz a probabilidade de determinado caractér aparecer em determinada posição)

** Inferência de motifs a partir de conjuntos de sequências **
Como e sequências de DNA os motifs têm tamanho reduzido (~6 a 2 pb) constante e são frequentemente repetidos e conservados, mas as regiões intergénicas são muito longas e altamente variáveis tornando a descoberta de motifs díficil.
Descobrir os melhores motifs é um probelma de otimização que varia conforme o tipo de motif considerad (se determínistico ou probabilistico) e a função objetivo que define a "qualidade" dos motifs.

Problema:
- t = nº de sequências (seqs)
- n = comprimento das seqs
- L = comprimento do motif
- S=(s1, s2, ..., st) - vetor de posições iniciais do motif em cada seq

** Estratégia com Perfis e Consensos **
Aplica-se quando as posições iniciais dos motifs em cada sequência são conhecidas.
1. Alinhamento dos padrões pelas suas posições iniciais
2. Construir matriz de ocorrências (perfil) para termos a frequência de cada nucleótido nas várias posições da sequência
3. Definir a sequência Consenso através do nucleótido com maior socre em cada coluna

Função de avaliação (scoring): 
- é a soma do maior score em cada posição/coluna (que será o score do nucleótido mais frequente) 
- score mínimo: 0
- score máximo: t x L

** Problema da descoberta de motifs **
Descobrir o conjunto de motifs (subsequências) de comprimento L em cada sequência de DNA fornecida que maximiza uma dada função de avaliação (aquele motif que terá o maior score). Sendo que as posições iniciais destas subsequencias não são conhecidas.
Input: t sequências de DNA (de tamanho n); L (o comprimento das subsequências)
Output: vetor com t posições iniciais que maximixam a função score(s, DNA)

--> ** Algoritmos Exatos (descobrem a solução ótima) **
** Procura Exaustiva  **
ProcuraExaustivaMotifs(seqs, t, n, L)
    melhorScore = 0
    for s in range(0, n-L):
        if score(s) > melhorScore:
            melhorScore = socre(s)
            melhorMotif = s
    return melhorMotif

Soluções possíveis: (n - L + 1)^t 
Complexidade = L.(n - L + 1)^t = O.(L.n^t)
--> Mesmo para problemas de reduzida dimensão vão ser necessárias muitas operações

** Árvores de procura (Branch & Bound) **
Solução para tornar mais eficiente a procura: agrupar as soluções do vetor de posições pelos seus prefixos num árvora de procura. Nesta árvore os caminhos do nó inicial (a raiz) coincide com o nº de quências (t), enquanto as soluções estão nas folhas e o pai de um nó é o prefixo da sua solução.
Paa navegar esta árvore há 4 movimentos: 
- ir para a próxima folha;
- visitar todas as folhas; 
- ir para o próximo nó;
- bypass (saltar à frente dos ramos de um determinado nó para visitar o próximo nó de um dado nível)

ist ajuda porque podemos ignorar determinadas possíveis soluções se soubermos que não irão superar o melhor score obtido até a determinado momento, então usando o bypass continuamos a procurar a partir do próximo vértic no mesmo nível
Funções: ProximoVertice e ByPass

--> ** Algoritmos Heuristico (tipo Consensus) **

--> ** Algoritmos Estocásticos (métodos heurísticos em que se tomam algumas decisões aleatóriamente) **
- Gibbs sampling
- Algoritmo E-M (Expectativa - Maximização)
- Algoritmos evolucionários

Lógica: usar segmentos mais prováveis para ajustar as posições iniciais até atingir o melhor perfil
1. Selecionar posições em cada sequência de forma aleatória
2. Criar um perfil P a partir das posições anteriores
3. Descobrir o segmento a mais provável em cada sequência usando P. Mudar a posição inicial nessa sequência para a posição do segmento a
4. Calcular outra vez o P. Repetir os passos 3 e 4 enquanto for possível aumentar o score.

Problema: a probabilidade de acertarmos logo nas posições iniciais é reduzida logo o algoritmo vai ter de ser corrido muitas vezes com diferentes pontos iniciais para melhorar as hipóteses de se ter um bom resultado

Para resolver isto: substitui-se um segmento em cada iteração (Gibbs Sampling), mais lento, mas aumenta as possibilidade de se convergir para uma solução correta

Gibbs Sampling:
1. Selecionar posições em cada sequência de forma aleatória e formar segmentos respetivos
2. Escolher aleatóriamente uma sequência
3. Criar um perfil P  (com pseudo-contagens) a partir das posições anteriormente definidas
4. Para cada posição p na sequência escolhida, calcular a probabilidade do segmento iniciado em p com tamanho L ter sido gerado por P
5. Escolher a posição p de acordo com as probabilidades calculadas no passo 4 mas de forma estocastica (através de uma roulette wheel dado que a probabilidade de escolher uma certa posição é proporcional ao seu score)
6. Repetir os passos de 2 a 5 enquanto for possível melhorar ou atingir um determinado critéio de terminação (como o nº ficxo de iterações ou nº de iterações sem melhorias)
