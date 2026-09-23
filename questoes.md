# Banco de Questões: CRSC04, Arquitetura de Computadores II

**Prova 01: 29/09/2026.** Nível ISA, O Sistema Operacional e Aritmética de ponto fixo e ponto flutuante (Aulas 01 a 13, mais os exemplos em C do zip).

São **611 questões de alternativas** em **ordem aleatória**: os assuntos estão misturados e as alternativas também foram embaralhadas, como numa prova. As de verdadeiro/falso aparecem no formato "analise as afirmativas", sempre com alternativas.

**Legenda:** [F] fácil · [M] médio · [D] difícil · ★ = assunto provavelmente comentado em aula, além do texto dos slides (Tanenbaum/Stallings ou conhecimento clássico ligado ao slide).

O gabarito fica no final: primeiro uma lista rápida, depois a tabela comentada com o assunto de cada questão.

---

### Questão 1 [F]

Qual a faixa de um inteiro com sinal de 5 bits em complemento de dois?

a) -16 a 15  
b) 0 a 31  
c) -32 a 31  
d) -15 a 15

### Questão 2 [D] ★

Em float (binary32), o inteiro 16.777.217 (2^24 + 1):

a) É representável exatamente  
b) Vira infinito  
c) Não é representável exatamente e vira 16.777.216  
d) Vira NaN

### Questão 3 [M]

Qual a grande vantagem do DMA sobre a E/S por interrupção caractere a caractere?

a) A CPU fica em espera ocupada  
b) Apenas uma interrupção por bloco inteiro  
c) Não usa o barramento  
d) Elimina a necessidade de memória

### Questão 4 [M]

O gabarito (template) de um pacote IA-64 informa:

a) Quais unidades funcionais o pacote precisa e onde fica a fronteira de um grupo de instruções  
b) O endereço de retorno  
c) O tamanho da página  
d) A prioridade da interrupção

### Questão 5 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 3, 6, 1, 3, 4, 3, 5, 1, 5, 3, quantas faltas de página ocorrem com LRU?

a) 8  
b) 5  
c) 7  
d) 6

### Questão 6 [M]

O endereçamento de pilha é o limite da redução porque:

a) Só funciona com ponto flutuante  
b) Usa endereços de 64 bits  
c) Exige três endereços  
d) As instruções não têm nenhum campo de endereço (apenas opcode)

### Questão 7 [M]

Em base 16, deslocar o significando 1 dígito corresponde a:

a) 4 bits  
b) 1 bit  
c) 8 bits  
d) 16 bits

### Questão 8 [M]

Qual a representação de −124 em complemento de dois com 8 bits?

a) 1000 0100  
b) 1000 0011  
c) 1111 1100  
d) 0111 1100

### Questão 9 [M]

Em 4 bits (C2), calcule M − S com M = 1100 (-4) e S = 0000 (0), somando M ao complemento de dois de S:

a) 1100 (overflow)  
b) 1101  
c) 1100  
d) 1010

### Questão 10 [M]

Na representação geométrica (círculo) dos inteiros em complemento de dois, ocorre overflow quando:

a) A operação atravessa a junção entre o maior positivo e o menor negativo  
b) Se anda no sentido horário  
c) O resultado cai no zero  
d) O resultado é ímpar

### Questão 11 [M]

No esquema FAT, um arquivo ocupa as unidades 4 → 52 → 19 → EOF. O que contém a linha 52 da tabela?

a) EOF  
b) 4  
c) 52  
d) 19

### Questão 12 [M]

Com unidades de alocação de 32.768 bytes, um arquivo de 100 bytes desperdiça quantos bytes na última unidade?

a) 32.668  
b) 16.384  
c) 100  
d) 65.436

### Questão 13 [M]

Aplicando deslocamento aritmético de 2 bit(s) à direita ao byte 0111 0001, obtém-se:

a) 0001 1100  
b) 1100 0100  
c) 1100 0101  
d) 0101 1100

### Questão 14 [M]

Um programa de 58.268 bytes usa páginas de 8.192 bytes. Quantas páginas ocupa e quanto é desperdiçado por fragmentação interna?

a) 7 páginas, 924 bytes  
b) 8 páginas, 924 bytes  
c) 8 páginas, 7.268 bytes  
d) 8 páginas, 0 bytes

### Questão 15 [M]

Qual a forma RPN da expressão infixa 3 + 7 + (9 − 1)?

a) `3 7 + 9 1 − +`  
b) `+ 7 1 + 9 3 −`  
c) `3 7 9 1 + − +`  
d) `+ − 1 9 + 7 3`

### Questão 16 [M]

Na E/S por interrupção, o sinal de interrupção é gerado por:

a) AND entre INTERRUPT ENABLE e READY  
b) A própria CPU, periodicamente  
c) OR entre INTERRUPT ENABLE e READY  
d) XOR entre os bits de erro

### Questão 17 [M]

A tradução virtual → físico é feita por:

a) Uma MMU (Memory Management Unit), usando a tabela de páginas  
b) O disco  
c) O controlador de DMA  
d) O compilador

### Questão 18 [F]

O padrão IEEE 754 de precisão simples (float) tem quantos bits e cerca de quantos dígitos decimais de precisão?

a) 16 bits, ~3 dígitos  
b) 32 bits, ~15 dígitos  
c) 64 bits, ~15 dígitos  
d) 32 bits, ~7 dígitos

### Questão 19 [F]

Na instrução indexada `MOV R4, A(R2)`, com A = 136188 e R2 = 8, qual endereço é lido?

a) 136220  
b) 136188  
c) 8  
d) 136196

### Questão 20 [M]

Por que o complemento de dois tem um número negativo a mais que positivos?

a) Por causa do bit de paridade  
b) Não tem: são simétricos  
c) Porque o hardware reserva um padrão  
d) Porque o zero tem uma única representação e ocupa uma das combinações 'não negativas'

### Questão 21 [F]

Quase todos os registradores do ATmega168 têm:

a) 32 bits  
b) 64 bits  
c) 16 bits  
d) 8 bits

### Questão 22 [M]

Por causa das condições de disputa, a Sun:

a) Removeu suspend() e resume() da classe Thread do Java  
b) Proibiu buffers circulares  
c) Criou os semáforos  
d) Removeu threads do Java

### Questão 23 [M]

No exemplo de predicação, CMPEQ R1, R2, P4 faz:

a) R1 = R2  
b) Zera R1 e R2  
c) Desvia se R1 == R2  
d) P4 = 1 se R1 == R2, e o predicado complementar P5 = 0 automaticamente

### Questão 24 [M]

Qual o valor da expressão em RPN `4 6 4 + 3 5 + + −`, avaliada com uma pilha?

a) 14  
b) -13  
c) -28  
d) -14

### Questão 25 [M]

Conceitualmente, memória virtual e cache são:

a) Técnicas opostas  
b) A mesma ideia aplicada em níveis diferentes da hierarquia  
c) Gerenciadas pelo compilador  
d) Exclusivas do Core i7

### Questão 26 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 3?

a) 0x40400000  
b) 0xC0400000  
c) 0x40C00000  
d) 0x00C00000

### Questão 27 [F]

Em C, uma cadeia de caracteres é normalmente delimitada por:

a) Um campo de comprimento no início  
b) Um ponteiro para o próximo caractere  
c) Um bit de paridade  
d) Um caractere especial \0 no final

### Questão 28 [M]

Em 8 bits, negar −128 (1000 0000) resulta em:

a) 0  
b) −127  
c) −128 (1000 0000): uma anomalia, pois +128 não é representável  
d) +128

### Questão 29 [M]

No IEEE 754, expoente 0 e fração diferente de 0 representa:

a) Infinito  
b) Número subnormal (desnormalizado): bit implícito 0 e expoente verdadeiro −126 (em 32 bits)  
c) NaN  
d) Zero

### Questão 30 [M]

No buffer circular, os ponteiros in e out indicam:

a) in: próxima posição livre onde o produtor coloca; out: próximo número a ser retirado pelo consumidor  
b) in: número a retirar; out: posição livre  
c) Ambos apontam o topo  
d) O tamanho do buffer

### Questão 31 [M]

Qual a representação de −18 em complemento de dois com 8 bits?

a) 1001 0010  
b) 0001 0010  
c) 1110 1101  
d) 1110 1110

### Questão 32 [M] ★

O algoritmo ótimo de substituição (o 'oráculo') remove:

a) A página que será usada mais tarde no futuro  
b) A mais antiga  
c) Uma aleatória  
d) A menos usada no passado

### Questão 33 [M]

O flag V (overflow) é ligado quando:

a) O resultado é zero  
b) Há vai-um saindo do bit mais à esquerda  
c) Uma operação aritmética com sinal dá resultado que não cabe na representação  
d) O resultado tem paridade par

### Questão 34 [D]

Um semáforo começa em 2. Processos distintos executam, nesta ordem: down, down, down, up. Qual o estado final?

a) Semáforo = 2, 0 processo(s) bloqueado(s)  
b) Semáforo = 0, 1 processo(s) bloqueado(s)  
c) Semáforo = 0, 0 processo(s) bloqueado(s)  
d) Semáforo = 1, 0 processo(s) bloqueado(s)

### Questão 35 [F]

A instrução CLR:

a) Limpa o flag de carry apenas  
b) Limpa a cache  
c) Remove o processo  
d) Zera um registrador ou posição de memória

### Questão 36 [M]

Qual o valor da expressão em RPN `6 2 × 2 × 4 3 × 9 6 × − +`, avaliada com uma pilha?

a) -36  
b) -17  
c) -18  
d) 18

### Questão 37 [F]

Numa máquina que exige alinhamento, um dado de 4 bytes pode começar em qual endereço?

a) 16  
b) 15  
c) 18  
d) 17

### Questão 38 [M]

Se o tamanho da página é n bytes, o desperdício médio por fragmentação interna na última página é:

a) n bytes  
b) Zero  
c) n/2 bytes  
d) n/4 bytes

### Questão 39 [M]

Por que o POSIX foi criado?

a) Para padronizar o hardware  
b) Para criar o Windows  
c) Porque as vertentes BSD e System V eram incompatíveis, o que atrapalhava a portabilidade de software  
d) Para substituir o C

### Questão 40 [F]

Como o número decimal 34 é codificado em BCD empacotado (1 byte)?

a) 0011 0100  
b) 0010 1000  
c) 0010 0010  
d) 0100 0011

### Questão 41 [M]

Some, em complemento de dois com 4 bits, 0001 (1) + 1011 (-5). Resultado (descartando o vai-um) e situação:

a) 0110, sem overflow  
b) 1100, sem overflow  
c) 1101, sem overflow  
d) 1100, com overflow

### Questão 42 [M]

Na normalização do resultado (ex.: 0,00101 × 2^5):

a) Desloca-se à direita: 1,01 × 2^8  
b) Desloca-se à esquerda até o MSB ser 1, decrementando o expoente: 1,01 × 2^2  
c) Nada é feito  
d) Arredonda-se para zero

### Questão 43 [M]

Segundo o comparativo de formatos, qual arquitetura usa byte de prefixo para modificar a ação da instrução?

a) ARM OMAP4430  
b) ATmega168  
c) Nenhuma delas  
d) Core i7

### Questão 44 [M]

No ARM do OMAP4430:

a) Não existe registrador de ligação  
b) Todas as instruções alteram as flags  
c) R13 é o PC  
d) As flags só são alteradas com o sufixo S (ex.: ADDS); R15 = PC e R14 = LR

### Questão 45 [M]

No endereçamento de base indexado, com R5 = 2000 (base), R2 = 12 (índice) e deslocamento 4, o endereço efetivo é:

a) 2012  
b) 2004  
c) 2048  
d) 2016

### Questão 46 [M]

Uma entrada típica de diretório (Figura 6.23) NÃO contém:

a) O conteúdo completo do arquivo  
b) Nome e comprimento  
c) Localização dos blocos  
d) Datas de criação e acesso

### Questão 47 [D]

Quantas operações de soma/subtração o algoritmo de Booth faz com o multiplicador 0110 0110 (8 bits, Q−1 inicial = 0)?

a) 5  
b) 3  
c) 6  
d) 4

### Questão 48 [M]

Uma máquina com endereços de 32 bits endereçada por palavra de 32 bits (não por byte) consegue endereçar:

a) 8 GB  
b) 16 GB  
c) 4 GB  
d) 32 GB

### Questão 49 [M]

EMT-64 (x86-64) em relação à IA-32 é:

a) Uma versão mais larga do Pentium, com registradores e endereços de 64 bits  
b) Uma ISA de 16 bits  
c) O mesmo que IA-64  
d) Uma ISA totalmente nova e incompatível

### Questão 50 [F]

Como o número decimal 22 é codificado em BCD empacotado (1 byte)?

a) 0001 0111  
b) 0001 0110  
c) 0010 0010  
d) 0001 1100

### Questão 51 [F]

Numa máquina que exige alinhamento, um dado de 2 bytes pode começar em qual endereço?

a) 9  
b) 7  
c) 6  
d) 5

### Questão 52 [M]

Um programa de 4.653 bytes usa páginas de 1.024 bytes. Quantas páginas ocupa e quanto é desperdiçado por fragmentação interna?

a) 4 páginas, 557 bytes  
b) 5 páginas, 557 bytes  
c) 5 páginas, 467 bytes  
d) 5 páginas, 0 bytes

### Questão 53 [M]

O bit A (vai-um auxiliar) da PSW existe principalmente para:

a) Indicar paridade par do resultado  
b) Dar suporte às correções de aritmética BCD (vai-um do bit 3)  
c) Sinalizar overflow em complemento de dois  
d) Habilitar interrupções mascaráveis

### Questão 54 [D]

O padrão IEEE 754 de 32 bits 0x40C00000 representa o valor:

a) -6  
b) 12  
c) 6  
d) 3

### Questão 55 [M]

Um disco tem 1.048.576 unidades de alocação. Quanto espaço ocupa o mapa de bits de espaço livre?

a) 131.072 bytes  
b) 1.048.576 bytes  
c) 16.384 bytes  
d) 4.194.304 bytes

### Questão 56 [D]

Pelo algoritmo de Booth com 4 bits, M = 0011 (3) e Q = 1011 (-5). Qual o conteúdo final de A:Q?

a) 1111 0010 (-14)  
b) 0000 1111 (15)  
c) 1111 0001 (-15)  
d) 0010 0001 (33)

### Questão 57 [F]

Uma instrução de um endereço normalmente usa como segundo operando:

a) A pilha  
b) Um acumulador implícito  
c) O contador de programa  
d) Um valor imediato obrigatório

### Questão 58 [M]

Por que o tamanho e a rapidez do prólogo e epílogo importam?

a) Porque definem o tamanho da página  
b) Porque o compilador não os gera  
c) Porque afetam só a E/S  
d) Se forem longos e lentos, chamadas de procedimento ficam caras

### Questão 59 [M]

Qual o valor da expressão em RPN `1 8 + 8 4 − + 5 4 − 2 9 − × −`, avaliada com uma pilha?

a) 20  
b) 21  
c) 40  
d) -20

### Questão 60 [M]

Some, em complemento de dois com 4 bits, 0111 (7) + 0010 (2). Resultado (descartando o vai-um) e situação:

a) 0101, sem overflow  
b) 1010, com overflow  
c) 1001, sem overflow  
d) 1001, com overflow

### Questão 61 [M]

Qual modo de endereçamento para desvios é o mais usado em desvios curtos e gera código relocalizável?

a) Direto  
b) Relativo ao PC  
c) Imediato  
d) Indireto de registrador

### Questão 62 [M]

Segundo a aula, se os acessos à memória são rápidos um projeto baseado em pilha (IJVM) é bom; se são lentos, o melhor é:

a) Usar BCD  
b) Eliminar o PC  
c) Ter instruções de 15 bytes  
d) Ter muitos registradores (como o ARM do OMAP4430)

### Questão 63 [M]

Um sistema de arquivos com arquivos de 1.200, 700, 2.000 e 900 setores alocados consecutivamente a partir do setor 0 coloca o terceiro arquivo começando no setor:

a) 2.000  
b) 1.200  
c) 3.900  
d) 1.900

### Questão 64 [M]

Aplicando rotação de 2 bit(s) à direita ao byte 1011 0010, obtém-se:

a) 1100 1010  
b) 0010 1100  
c) 1100 1000  
d) 1010 1100

### Questão 65 [M]

7 ÷ (−3), pela regra de sinais do slide, resulta em:

a) Quociente −2 e resto −1  
b) Quociente +2 e resto +1  
c) Quociente −2 e resto +1  
d) Quociente −3 e resto −2

### Questão 66 [D]

Na rotina de serviço do exemplo (impressão), as variáveis globais ptr e count servem para:

a) Apontar o próximo caractere e contar quantos faltam; se count > 0, copia-se o próximo para o buffer de saída  
b) Guardar a prioridade da CPU  
c) Guardar o PC e a PSW  
d) Guardar o vetor de interrupção

### Questão 67 [M]

A fragmentação externa ('tabuleiro de xadrez') é:

a) Espaço perdido dentro da última página  
b) Excesso de entradas na TLB  
c) Lacunas entre segmentos na memória, cada uma pequena demais para ser útil  
d) Perda de dados no disco

### Questão 68 [M]

Em 4 bits (C2), calcule M − S com M = 1111 (-1) e S = 0110 (6), somando M ao complemento de dois de S:

a) 1001  
b) 1010  
c) 1001 (overflow)  
d) 0101

### Questão 69 [M]

Os dois subsistemas centrais do núcleo UNIX, segundo a aula, são:

a) Compilador e editor  
b) Sistema de arquivos e gerenciamento de processos  
c) Shell e X Windows  
d) Rede e gráficos

### Questão 70 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 5, 5, 2, 2, 1, 3, 4, 1, 6, 1, quantas faltas de página ocorrem com LRU?

a) 8  
b) 7  
c) 5  
d) 6

### Questão 71 [M]

Some, em complemento de dois com 4 bits, 0110 (6) + 1000 (-8). Resultado (descartando o vai-um) e situação:

a) 1110, sem overflow  
b) 1110, com overflow  
c) 0000, sem overflow  
d) 1111, sem overflow

### Questão 72 [M]

O que é EPIC?

a) Explicitly Parallel Instruction Computing: o compilador torna o paralelismo explícito  
b) Um modo de endereçamento do ARM  
c) Um tipo de cache  
d) Um controlador de interrupção

### Questão 73 [M]

Qual ação é feita pelo SOFTWARE (rotina de serviço) e não pelo hardware na interrupção?

a) Empilhar o PC e a PSW  
b) Salvar todos os registradores que a rotina vai usar  
c) Ativar o sinal de reconhecimento de interrupção  
d) Ler o vetor de interrupção do barramento

### Questão 74 [M]

No Core i7, por que os parâmetros de printf são empilhados em ordem inversa?

a) Porque o ARM exige  
b) printf tem número variável de parâmetros; em ordem inversa, o ponteiro da cadeia de formato fica no topo, em posição conhecida  
c) Porque a pilha cresce para cima  
d) Por economia de memória

### Questão 75 [F]

O componente de software que cria e gerencia máquinas virtuais é o:

a) Controlador DMA  
b) Hipervisor  
c) Compilador  
d) Escalonador de disco

### Questão 76 [M]

Em IEEE 754 de 32 bits, qual o campo de expoente (polarizado) de 0,03125?

a) 123 (01111011)  
b) 122 (01111010)  
c) 121 (01111001)  
d) -5 (11111011)

### Questão 77 [M]

O nível OSM, em relação ao ISA:

a) É idêntico ao ISA  
b) Reaproveita a maior parte das instruções ISA, adiciona instruções novas e remove as potencialmente perigosas  
c) Remove todas as instruções ISA  
d) Só adiciona instruções de PF

### Questão 78 [D]

Quantas operações de soma/subtração o algoritmo de Booth faz com o multiplicador 0000 1000 (8 bits, Q−1 inicial = 0)?

a) 3  
b) 2  
c) 4  
d) 1

### Questão 79 [M]

O princípio da localidade diz que:

a) Páginas vizinhas nunca são usadas juntas  
b) A memória é local à CPU  
c) As referências de um programa tendem a se concentrar em um número pequeno de páginas  
d) Todas as páginas são acessadas uniformemente

### Questão 80 [M]

Em relação a processos, o Windows usa ___ e o UNIX usa ___:

a) fork; CreateProcess  
b) CreateThread; exec  
c) spawn; wait  
d) CreateProcess; fork + exec

### Questão 81 [M]

Qual o valor da expressão em RPN `9 9 − 6 + 3 1 × 5 3 × + ×`, avaliada com uma pilha?

a) 109  
b) 216  
c) -108  
d) 108

### Questão 82 [D] ★

Por que 0,1 + 0,2 == 0,3 costuma dar falso em C/Python/Java?

a) Porque a soma em PF é inteira  
b) Porque 0,3 é NaN  
c) 0,1 e 0,2 não têm representação binária exata (são dízimas em base 2), e os erros de arredondamento se acumulam  
d) Por bug do compilador

### Questão 83 [D]

Mesmo com extensão de sinal, deslocar à direita um número negativo:

a) Gera exceção  
b) Arredonda para zero  
c) Sempre dá o resultado exato da divisão  
d) Arredonda em direção ao inteiro mais negativo (ex.: −5 >> 1 = −3), o que difere da divisão inteira truncada

### Questão 84 [M]

Um disco tem 32.768 unidades de alocação. Quanto espaço ocupa o mapa de bits de espaço livre?

a) 4.096 bytes  
b) 131.072 bytes  
c) 32.768 bytes  
d) 512 bytes

### Questão 85 [M]

Qual o valor da expressão em RPN `4 8 + 6 − 7 4 × 3 − ×`, avaliada com uma pilha?

a) 150  
b) 151  
c) 300  
d) -150

### Questão 86 [M]

Um laço que percorre 9 páginas numa memória de 8 quadros, com LRU:

a) Causa faltas só na primeira volta  
b) Causa falta de página em toda nova referência: o LRU faz a pior escolha sempre  
c) Não causa faltas  
d) Causa uma única falta

### Questão 87 [M]

Por que usar exceções (traps) em vez de testar manualmente um bit de overflow após cada instrução?

a) Porque exceções são assíncronas  
b) Testar após cada instrução é lento e desperdiça espaço  
c) Porque o bit não existe  
d) Porque o compilador proíbe

### Questão 88 [F]

Em uma máquina que exige que palavras de 8 bytes estejam alinhadas, em qual endereço uma palavra pode começar?

a) 30  
b) 20  
c) 24  
d) 12

### Questão 89 [M]

Na analogia do vôlei (10 jogos, 7 bolas no cesto), quantos jogos ficam esperando no início?

a) 3  
b) 7  
c) 0  
d) 10

### Questão 90 [M]

No paralelismo simulado (uma CPU):

a) Cada processo tem sua CPU física  
b) Só um processo existe  
c) Não há problemas de sincronização  
d) A CPU comuta entre processos em fatias de tempo, e os problemas de comunicação são os mesmos do paralelismo real

### Questão 91 [M]

Após `CALL _printf` com 3 parâmetros de 4 bytes, `ADD ESP, 12`:

a) Descarta os parâmetros da pilha (sem apagá-los da memória)  
b) Salva 12 registradores  
c) Chama printf 12 vezes  
d) Aloca 12 variáveis locais

### Questão 92 [M]

No esquema FAT, onde fica a tabela de encadeamento durante o uso?

a) Em cada bloco de dados  
b) Na TLB  
c) Na memória principal  
d) No registrador de segmento

### Questão 93 [M]

Para trocar os 8 bits da direita de uma palavra por um novo caractere C:

a) (A AND máscara com zeros nos 8 bits da direita) OR C  
b) (A OR máscara) AND C  
c) NOT A AND C  
d) A XOR C

### Questão 94 [M]

VMX no Core i7 significa:

a) Um modo de 16 bits  
b) Virtual Machine Extensions: extensões de instrução, memória e interrupção para virtualização  
c) Uma instrução de vetor  
d) Um barramento de E/S

### Questão 95 [F]

Quantos movimentos a solução recursiva das Torres de Hanói faz com 10 discos?

a) 1.023  
b) 100  
c) 512  
d) 1.024

### Questão 96 [F]

Sem desvios nem chamadas, o PC, observado ao longo do tempo, é aproximadamente:

a) Uma função aleatória  
b) Decrescente  
c) Constante  
d) Uma função linear crescente do tempo

### Questão 97 [M]

Banda da cache de instruções de 96 Gbit/s e tamanho médio de instrução de 24 bits. Qual o limite de instruções por segundo (t/r)?

a) 12 bilhões  
b) 2 bilhões  
c) 4 bilhões  
d) 2304 bilhões

### Questão 98 [M]

Banda da cache de instruções de 48 Gbit/s e tamanho médio de instrução de 12 bits. Qual o limite de instruções por segundo (t/r)?

a) 576 bilhões  
b) 2 bilhões  
c) 4 bilhões  
d) 6 bilhões

### Questão 99 [D] ★

Por que o Core i7 (x86) venceu no mercado mesmo com uma ISA irregular?

a) Porque não usa pipeline  
b) Porque o Itanium executava x86 mais rápido  
c) Pela base enorme de software já compilado, que a compatibilidade preserva  
d) Porque a ISA x86 é mais regular que a ARM

### Questão 100 [M]

Em complemento de dois, qual a relação entre NEG e NOT?

a) NEG(x) = NOT(x) − 1  
b) NEG(x) = x XOR 1  
c) NEG(x) = NOT(x)  
d) NEG(x) = NOT(x) + 1

### Questão 101 [M]

Os três tipos de formato definidos pelo IEEE 754-2008 são:

a) Normal, subnormal e NaN  
b) Curto, longo e estendido  
c) Inteiro, real e complexo  
d) Aritmético, básico e de intercâmbio

### Questão 102 [M]

O valor de 32 bits 0x11223344 é gravado a partir do endereço 200 numa máquina little-endian. Qual byte fica no endereço 200?

a) 0x11  
b) 0x22  
c) 0x33  
d) 0x44

### Questão 103 [D] ★

Por que o Linux e o Windows em x86 praticamente não usam a segmentação do x86?

a) Porque segmentação é mais rápida  
b) Porque o x86 não tem segmentação  
c) Usam um modelo 'plano' (base 0 e limite máximo em todos os segmentos) e fazem a proteção por paginação  
d) Porque o x86-64 obriga segmentação pura

### Questão 104 [F]

Qual a faixa de um inteiro com sinal de 10 bits em complemento de dois?

a) -512 a 511  
b) -1.024 a 1.023  
c) 0 a 1.023  
d) -511 a 511

### Questão 105 [M]

Expoente 0 e fração 0 no IEEE 754 representa:

a) O menor normalizado  
b) NaN  
c) Somente +0  
d) +0 ou −0, conforme o bit de sinal

### Questão 106 [M]

Como calcular 18 × n só com deslocamentos e soma?

a) (n << 4) + (n << 1)  
b) (n << 4) + n  
c) (n << 5) − n  
d) (n << 3) + (n << 1)

### Questão 107 [M]

Sobre a MFT do NTFS:

a) Não guarda atributos  
b) É uma lista encadeada como a FAT  
c) Cada arquivo é uma entrada, e arquivos pequenos (< 1 KB) cabem inteiros na MFT  
d) Guarda apenas diretórios

### Questão 108 [F]

Qual a faixa de um inteiro com sinal de 16 bits em complemento de dois?

a) 0 a 65.535  
b) −65.536 a +65.535  
c) −32.767 a +32.767  
d) −32.768 a +32.767

### Questão 109 [M]

Qual a forma RPN da expressão infixa (6 − 1) × 4?

a) `× 4 − 1 6`  
b) `6 1 − 4 ×`  
c) `6 1 4 × −`  
d) `6 1 4 − ×`

### Questão 110 [M]

Se o vetor de interrupção n aponta para a entrada no endereço 4·n, onde fica a entrada do vetor 32?

a) 256  
b) 128  
c) 64  
d) 32

### Questão 111 [M]

A memória virtual é transparente ao programador porque:

a) Ele escreve como se houvesse memória para todo o espaço virtual, sem nem saber que ela existe  
b) Ele precisa chamar o SO a cada acesso  
c) Ele gerencia a tabela de páginas  
d) Ele define os overlays

### Questão 112 [M]

Qual a representação de −117 em complemento de dois com 8 bits?

a) 1000 1010  
b) 1111 0101  
c) 0111 0101  
d) 1000 1011

### Questão 113 [M]

No produtor-consumidor com semáforos (buffer de 100 posições), os valores iniciais são:

a) available = 100 e filled = 0  
b) available = 0 e filled = 100  
c) ambos 1  
d) ambos 0

### Questão 114 [F]

No ATmega168, o ponteiro de 16 bits Y é formado pelo par:

a) R25:R24  
b) R27:R26  
c) R31:R30  
d) R29:R28

### Questão 115 [M]

No modelo de controle total entre pai e filho, o pai pode:

a) Nada após a criação  
b) Interromper, reiniciar, examinar e encerrar o filho à força  
c) Apenas criar o filho  
d) Apenas ler a saída do filho

### Questão 116 [M]

Em 4 bits (C2), calcule M − S com M = 1011 (-5) e S = 0011 (3), somando M ao complemento de dois de S:

a) 1000  
b) 1110  
c) 1000 (overflow)  
d) 1001

### Questão 117 [M]

Analise, sobre o Core i7:

I. As instruções têm de 1 a 15 bytes.  
II. Existe instrução que soma memória + memória.  
III. Os operandos precisam estar alinhados.  
IV. A irregularidade vem de escolhas antigas mantidas por compatibilidade.

Está correto:

a) I, II, III e IV  
b) Apenas I e IV  
c) Apenas II e III  
d) Apenas I e II

### Questão 118 [M]

Por que muitos processadores têm registradores separados para inteiros e ponto flutuante?

a) Porque PF não pode ser guardado em memória  
b) Porque inteiros usam IEEE 754  
c) Para evitar conflito entre os operandos e permitir execução em paralelo  
d) Para economizar transistores

### Questão 119 [M]

Uma condição de disputa (race condition) ocorre quando:

a) Dois processos usam CPUs diferentes  
b) O processo é muito rápido  
c) O resultado depende de quem vence a corrida no acesso a dados compartilhados  
d) Não há dados compartilhados

### Questão 120 [M]

O algoritmo LRU remove:

a) A página carregada há mais tempo, independentemente do uso  
b) A página usada há mais tempo  
c) Uma página aleatória  
d) A página mais usada

### Questão 121 [M]

Multiplicar dois significandos de 24 bits gera um produto de até:

a) 24 bits  
b) 96 bits  
c) 12 bits  
d) 48 bits, que é depois arredondado/truncado para 24

### Questão 122 [M]

A memória do Itanium 2 pode ser acessada em unidades de 1, 2, 4, 8, 16 e 10 bytes. O tamanho de 10 bytes serve para:

a) Instruções  
b) Ponto flutuante de 80 bits (IEEE 754 estendido)  
c) BCD  
d) Endereços

### Questão 123 [M]

Na divisão sem sinal de 4 bits por restauração, dividendo 1100 (12) e divisor 0100 (4). Ao final:

a) Q = 0000, R = 0011  
b) Q = 0100, R = 0000  
c) Q = 0011, R = 0100  
d) Q = 0011, R = 0000

### Questão 124 [M]

Uma rotina de interrupção ser 'transparente' significa:

a) Executa sem usar a pilha  
b) Não pode ser interrompida  
c) Ela é invisível ao SO  
d) Ao terminar, o computador volta ao estado idêntico ao de antes da interrupção

### Questão 125 [M]

Qual a forma RPN da expressão infixa 3 + 5 − 6 × 3?

a) `3 5 6 3 + × −`  
b) `− × 3 6 + 5 3`  
c) `3 5 6 3 − × +`  
d) `3 5 + 6 3 × −`

### Questão 126 [M]

Nas instruções LODS, STOS, MOVS, CMPS e SCAS do Core i7, o grupo é o de:

a) Operações BCD  
b) Controle de laço  
c) Cadeias de caracteres  
d) Ponto flutuante

### Questão 127 [M]

Uma desvantagem do endereçamento por palavra (em vez de por byte) é:

a) Impede o uso de ponto flutuante  
b) Comparar ou manipular caracteres individuais exige extraí-los da palavra  
c) Os endereços ficam mais longos  
d) A memória endereçável diminui

### Questão 128 [M]

No algoritmo de Booth, o deslocamento de A, Q, Q−1 à direita é:

a) À esquerda  
b) Aritmético: o bit de sinal de A é preservado (replicado)  
c) Uma rotação  
d) Lógico: entra 0 pela esquerda

### Questão 129 [M]

Qual a representação de −31 em complemento de dois com 8 bits?

a) 1110 0001  
b) 0001 1111  
c) 1110 0000  
d) 1001 1111

### Questão 130 [M]

O padrão de 8 bits 1110 0101, interpretado em complemento de dois, vale:

a) 229  
b) -26  
c) -101  
d) -27

### Questão 131 [M]

A diferença entre deslocamento e rotação é que:

a) Não há diferença  
b) A rotação preenche com zeros  
c) O deslocamento preserva todos os bits  
d) Na rotação os bits que saem por um lado reaparecem no outro; no deslocamento eles se perdem

### Questão 132 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 20?

a) 0x41A00000  
b) 0x02200000  
c) 0xC1A00000  
d) 0x42200000

### Questão 133 [D]

O padrão IEEE 754 de 32 bits 0xC2200000 representa o valor:

a) -20  
b) -80  
c) -40  
d) 40

### Questão 134 [D]

O AVR ATmega168 é descrito com 'manipulação de bits poderosa' e 'poucos transistores'. O principal fator de projeto dele é:

a) Suporte a memória virtual  
b) Estado da arte em desempenho  
c) Compatibilidade com o 8086  
d) Baixo custo por CPU

### Questão 135 [M]

Com R1 = 3, R2 = 0x1000, M[0x1000] = 7 e M[0x1004] = 9, qual o valor de R1 após `ADD R1, (R2)`?

a) 7  
b) 10  
c) 0x1003  
d) 12

### Questão 136 [M]

Um disco tem 131.072 unidades de alocação. Quanto espaço ocupa o mapa de bits de espaço livre?

a) 131.072 bytes  
b) 524.288 bytes  
c) 2.048 bytes  
d) 16.384 bytes

### Questão 137 [M]

Sobre as instruções Thumb do ARM:

a) São instruções CISC de tamanho variável  
b) São versões de 16 bits, com dois operandos e acesso apenas aos 8 primeiros registradores  
c) São instruções de 64 bits para ponto flutuante  
d) Só podem ser usadas pelo SO

### Questão 138 [D]

Quantas operações de soma/subtração o algoritmo de Booth faz com o multiplicador 0111 0110 (8 bits, Q−1 inicial = 0)?

a) 4  
b) 6  
c) 3  
d) 5

### Questão 139 [M]

Aplicando rotação de 2 bit(s) à direita ao byte 1000 0011, obtém-se:

a) 0010 0000  
b) 0000 1110  
c) 0000 1100  
d) 1110 0000

### Questão 140 [M]

Overflow de expoente em PF acontece quando:

a) O expoente fica maior que o máximo representável (magnitude grande demais)  
b) O número é negativo  
c) O significando é pequeno demais  
d) Há vai-um no significando

### Questão 141 [M]

A operação UP num semáforo com valor 0 e um processo dormindo nele:

a) Acorda esse processo, e o semáforo continua 0  
b) Bloqueia quem chamou  
c) Passa o semáforo para 1 e não acorda ninguém  
d) Passa para 2

### Questão 142 [F]

O nível de máquina de sistema operacional (OSM) é o:

a) Nível 0  
b) Nível 1, abaixo da microarquitetura  
c) Nível 3, acima do nível ISA  
d) Nível 2, igual ao ISA

### Questão 143 [M]

Se a memória está a 30 cm da CPU, o tempo mínimo de ida e volta de um sinal é:

a) 2 ns  
b) 0,5 ns  
c) 30 ns  
d) 1 ns

### Questão 144 [M]

Qual NÃO é um registrador típico do controlador de DMA?

a) Quantidade de bytes a transferir  
b) Número do dispositivo e direção  
c) Endereço de memória  
d) O contador de programa do processo

### Questão 145 [D]

No exemplo da matriz 10.000 × 10.000 armazenada por coluna (8 bytes por elemento), percorrer uma linha numa memória de 32 MB:

a) Funciona igual com qualquer tamanho de página  
b) Páginas de 8 KB são melhores  
c) Com páginas de 8 KB exige 80 MB e causa thrashing; com páginas de 1 KB exige só 10 MB  
d) Não há diferença porque é memória virtual

### Questão 146 [D]

Na tabela MOD × R/M do Core i7 (32 bits), MOD = 00 e R/M = 101 significa:

a) M[EBP]  
b) Endereçamento direto (endereço de 32 bits na instrução)  
c) Presença de byte SIB  
d) O registrador EBP

### Questão 147 [M]

Na divisão sem sinal de 4 bits por restauração, dividendo 1111 (15) e divisor 0110 (6). Ao final:

a) Q = 0011, R = 0011  
b) Q = 0011, R = 0010  
c) Q = 0010, R = 0011  
d) Q = 0010, R = 0110

### Questão 148 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 100?

a) 0x42C80000  
b) 0x43480000  
c) 0xC2C80000  
d) 0x03480000

### Questão 149 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de -2,25?

a) 0xC0100000  
b) 0xC0900000  
c) 0x80900000  
d) 0x40100000

### Questão 150 [F]

Na instrução indexada `MOV R4, A(R2)`, com A = 171576 e R2 = 20, qual endereço é lido?

a) 171596  
b) 20  
c) 171656  
d) 171576

### Questão 151 [M]

Um mapa de bits (bitmap) para monitorar 4096 blocos livres em disco ocupa:

a) 64 bytes  
b) 4096 bytes  
c) 512 bytes  
d) 4 KB por bloco

### Questão 152 [F]

Quando o conteúdo do endereço 2000 é 'movido' para um registrador:

a) A posição 2000 é zerada  
b) Cria-se uma cópia no registrador e o original continua intacto na memória  
c) O valor é apagado da memória  
d) O registrador passa a apontar para 2000

### Questão 153 [M]

O equivalente Win32 de lseek é:

a) CreateFile  
b) CloseHandle  
c) ReadFile  
d) SetFilePointer

### Questão 154 [D]

Na paginação de dois níveis do Core i7 (32 bits, páginas de 4 KB), o endereço linear se divide em:

a) DIR (8), PAGE (8), OFF (16)  
b) DIR (12), PAGE (12), OFF (8)  
c) DIR (16), OFF (16)  
d) DIR (10 bits), PAGE (10 bits) e OFF (12 bits)

### Questão 155 [M]

Segundo o comparativo (Figura 5.28), qual afirmação é correta?

a) Nenhuma delas tem modo imediato  
b) O ARM do OMAP4430 não tem endereçamento direto  
c) O Core i7 é o único com base indexado  
d) O AVR tem endereçamento indexado

### Questão 156 [D]

O padrão IEEE 754 de 32 bits 0x3FE00000 representa o valor:

a) -1,75  
b) 1,75  
c) 0,875  
d) 3,5

### Questão 157 [M]

O valor de 32 bits 0x0A0B0C0D é gravado a partir do endereço 200 numa máquina big-endian. Qual byte fica no endereço 200?

a) 0x0A  
b) 0x0C  
c) 0x0B  
d) 0x0D

### Questão 158 [M]

Na adição em complemento de dois, o vai-um além do bit mais significativo:

a) Gera exceção  
b) É ignorado  
c) Indica sempre overflow  
d) É somado ao resultado (end-around carry)

### Questão 159 [F]

A carta 'Go To Statement Considered Harmful' (1968), que deu origem à programação estruturada, é de:

a) Donald Knuth  
b) Alan Turing  
c) Dennis Ritchie  
d) Edsger Dijkstra

### Questão 160 [M]

Por que a comparação não é simplesmente uma subtração?

a) Porque mesmo que a subtração transborde, a CMP deve retornar a resposta correta  
b) Porque CMP só existe em RISC  
c) Porque a subtração não afeta as flags  
d) Porque subtração não existe em hardware

### Questão 161 [M]

Um ponteiro, como tipo de dado, é:

a) Apenas um endereço de máquina  
b) Um inteiro com sinal obrigatório  
c) Um tipo de ponto flutuante  
d) Um tipo exclusivo de linguagens de alto nível

### Questão 162 [M]

No ARM do OMAP4430, o campo de 4 bits presente em todas as instruções de 32 bits:

a) Fica nos bits 0–3 e indica o registrador destino  
b) Indica o tamanho da instrução  
c) Fica nos bits 28–31 e é o campo de condição, que torna a instrução predicada  
d) É o bit S, que habilita as flags

### Questão 163 [M]

No programa que soma 1024 elementos (`ADD R1,(R2)`, `ADD R2,#4`, `CMP R2,R3`, `BLT LOOP`), qual modo NÃO aparece no corpo do laço?

a) Indireto de registrador  
b) Imediato  
c) Indexado  
d) Registrador

### Questão 164 [M]

No copy.c (Figura 6.36), o laço termina quando:

a) close é chamado  
b) read retorna 0 (fim de arquivo)  
c) O buffer enche  
d) write retorna 0

### Questão 165 [M]

Qual é o grupo de instruções com MAIS variedade entre máquinas, segundo a aula?

a) Movimento de dados  
b) Entrada/Saída  
c) Aritméticas  
d) Comparações

### Questão 166 [M]

Se os expoentes diferem muito na adição em PF:

a) Ocorre sempre overflow  
b) O resultado é zero  
c) O maior é descartado  
d) O número menor pode ser totalmente perdido, e o resultado é o número maior

### Questão 167 [F]

A luz no vácuo percorre aproximadamente:

a) 30 cm por nanossegundo  
b) 300 m por nanossegundo  
c) 3 cm por nanossegundo  
d) 30 km por nanossegundo

### Questão 168 [M]

Sobre diretórios:

a) Diretórios não guardam atributos  
b) Cada diretório é, em si, um arquivo, e diretórios podem conter outros diretórios, formando uma árvore  
c) Um sistema só pode ter um diretório  
d) Diretórios ficam só na RAM

### Questão 169 [M]

Um pacote (bundle) da IA-64 tem 128 bits, compostos por:

a) 2 instruções de 64 bits  
b) 3 instruções de 40 bits + 8 bits de prefixo  
c) 3 instruções de 41 bits + 1 gabarito de 5 bits  
d) 4 instruções de 32 bits

### Questão 170 [M]

Qual lição histórica sobre ISAs foi destacada em aula?

a) A ISA mais elegante sempre vence no mercado  
b) Uma ISA feia e barata pode vencer uma elegante e cara  
c) ISAs duram no máximo 5 anos  
d) Compatibilidade nunca importa

### Questão 171 [M]

No Windows 7, a função VirtualProtect:

a) Consulta o estado das páginas  
b) Altera a proteção de páginas de uma região  
c) Libera uma região  
d) Reserva páginas

### Questão 172 [M]

No ARM do OMAP4430, a instrução LDRSB mostra que:

a) LDRSB é uma instrução de cadeia  
b) O ARM só carrega palavras de 32 bits  
c) Nas cargas o programa especifica tamanho e sinal do dado (load signed byte)  
d) O ARM trata BCD em hardware

### Questão 173 [M]

Cada par de ponteiros X, Y ou Z do AVR endereça até:

a) 64 KB  
b) 1 MB  
c) 4 GB  
d) 256 bytes

### Questão 174 [M]

A chamada que substitui a imagem do processo por um novo programa é:

a) exit()  
b) wait()  
c) execve()  
d) fork()

### Questão 175 [M]

No FIFO com contadores (todos começam em 0), após cada falta tratada:

a) Os contadores são zerados  
b) Sai a de menor contador  
c) O contador de cada página na memória aumenta em 1, a recém-trazida recebe 0, e sai a de maior contador  
d) Só a página nova é incrementada

### Questão 176 [M]

O que faz `LEAVE` no x86?

a) Salva todos os registradores  
b) Retorna ao chamador  
c) Restaura ESP a partir de EBP e desempilha o EBP antigo (desfaz o quadro)  
d) Encerra o programa

### Questão 177 [M]

Programa de 26.000 bytes com páginas de 4.096 bytes. Quantos bytes são desperdiçados na última página?

a) 2.672  
b) 4.096  
c) 1.424  
d) 0

### Questão 178 [M]

A taxa máxima de instruções é limitada por t/r (t = banda da cache em bit/s, r = tamanho médio da instrução em bits). Com t = 64 Gbit/s e r = 16 bits, o limite é:

a) 2 bilhões  
b) 1 bilhão  
c) 4 bilhões de instruções/s  
d) 8 bilhões

### Questão 179 [M]

Um quadro de página é:

a) Uma parte da memória física do mesmo tamanho de uma página  
b) Um setor do disco  
c) Uma entrada da TLB  
d) Uma parte do espaço virtual

### Questão 180 [M]

Analise:

I. O ARM do OMAP4430 exige que todos os operandos estejam alinhados.  
II. O ATmega168 tem ponto flutuante em hardware.  
III. O Core i7 suporta BCD em hardware (8 bits).  
IV. O ARM do OMAP4430 tem instruções de hardware para cadeias de caracteres.

Está correto:

a) Apenas I e II  
b) Apenas I e III  
c) Apenas III e IV  
d) Apenas II e IV

### Questão 181 [M]

Underflow em ponto flutuante acontece quando:

a) A mantissa tem zeros  
b) A magnitude do resultado é pequena demais para ser representada  
c) O resultado é grande demais  
d) O resultado é negativo

### Questão 182 [M]

Qual a forma RPN da expressão infixa 3 × 2 − 7?

a) `− 7 × 2 3`  
b) `3 2 7 × −`  
c) `3 2 × 7 −`  
d) `3 2 7 − ×`

### Questão 183 [F]

Quando surge uma máquina nova, perguntas de compatibilidade devem ser respondidas. Qual NÃO está entre as citadas em aula?

a) Ela é compatível com a antecessora?  
b) Ela executará meus programas existentes sem modificações?  
c) Ela consome menos energia que a antecessora?  
d) Ela pode executar meu sistema operacional antigo?

### Questão 184 [M]

Uma página limpa, ao ser removida:

a) Precisa ser reescrita  
b) Não precisa ser reescrita no disco, pois já existe cópia exata  
c) É apagada do disco  
d) Vira página suja

### Questão 185 [M]

A polarização (bias) do expoente de 8 bits é:

a) 128  
b) 255  
c) 1023  
d) 127

### Questão 186 [M]

O equivalente Windows de pthread_create é:

a) CreateProcess  
b) CreateThread  
c) WaitForSingleObject  
d) CreateFile

### Questão 187 [M]

O Windows NT foi:

a) Uma extensão do MS-DOS  
b) Um derivado do UNIX  
c) Um SO de 32 bits escrito do zero pela Microsoft, inicialmente para Intel, MIPS e PowerPC  
d) Um SO de 16 bits

### Questão 188 [M]

Em `MOV R4, A(R2)` (Figura 5.19), com A = 124300:

a) R2 é o deslocamento e A é o registrador base  
b) A é o deslocamento na instrução e R2 é o índice  
c) A é um imediato somado a R4  
d) R4 é o registrador índice

### Questão 189 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 2, 3, 4, 4, 4, 2, 4, 6, 2, 2, quantas faltas de página ocorrem com LRU?

a) 3  
b) 4  
c) 5  
d) 6

### Questão 190 [D]

No programa processo.c do professor, o pai cria 3 filhos com fork() em if/else aninhados, e todos seguem até o printf("Programa encerrado!\n") final. Quantas vezes essa mensagem aparece?

a) 8  
b) 4  
c) 3  
d) 1

### Questão 191 [M]

Na analogia do vôlei, devolver uma bola ao cesto corresponde a:

a) fork  
b) DOWN  
c) wait  
d) UP

### Questão 192 [M]

Semáforos foram propostos por:

a) Thompson, em 1974  
b) Dijkstra, em 1968  
c) Denning, em 1968  
d) Tanenbaum, em 1987

### Questão 193 [M]

No Core i7, a EPT (Extended Page Table):

a) Traduz os endereços físicos da VM em endereços físicos do hospedeiro  
b) Guarda os registradores da VM  
c) É uma tabela de interrupções  
d) Substitui a TLB

### Questão 194 [D]

Páginas de 4.096 bytes. Tabela de páginas (página→quadro): 0→5, 1→1, 2→0, 3→2, 4→3, 5→4, 6→7, 7→6. Qual o endereço físico do endereço virtual 29.746?

a) 25.650  
b) 29.746  
c) 28.678  
d) 24.576

### Questão 195 [M]

Normalizar 0,110 × 2^5 resulta em:

a) 1,10 × 2^6  
b) 0,0110 × 2^6  
c) 1,10 × 2^4  
d) 11,0 × 2^3

### Questão 196 [M]

Analise:

I. Exceções são síncronas e causadas pelo próprio programa.  
II. Interrupções ocorrem sempre no mesmo lugar em execuções repetidas.  
III. Divisão por zero é exemplo de exceção.  
IV. Pressionar Enter gera uma interrupção.

Está correto:

a) I, II, III e IV  
b) Apenas I, III e IV  
c) Apenas II e IV  
d) Apenas I e II

### Questão 197 [M]

A operação DOWN num semáforo com valor 0:

a) Não faz nada  
b) Deixa o semáforo em −1  
c) Suspende o processo até que outro execute UP  
d) Gera exceção

### Questão 198 [M]

A pilha de registradores do Itanium 2 difere das janelas do UltraSPARC porque:

a) Exige salvar todos os registradores na entrada  
b) Não usa registradores  
c) Tem tamanho fixo por procedimento  
d) O número de registradores visíveis é variável e muda de um procedimento para outro

### Questão 199 [M]

Um programa de 22.865 bytes usa páginas de 4.096 bytes. Quantas páginas ocupa e quanto é desperdiçado por fragmentação interna?

a) 6 páginas, 1.711 bytes  
b) 6 páginas, 0 bytes  
c) 5 páginas, 2.385 bytes  
d) 6 páginas, 2.385 bytes

### Questão 200 [M]

Na divisão sem sinal de 4 bits por restauração, dividendo 1000 (8) e divisor 0100 (4). Ao final:

a) Q = 0000, R = 0010  
b) Q = 0010, R = 0000  
c) Q = 0010, R = 0100  
d) Q = 0011, R = 0000

### Questão 201 [D]

Páginas de 4.096 bytes. Tabela de páginas (página→quadro): 0→1, 1→3, 2→5, 3→7, 4→4, 5→2, 6→6, 7→0. Qual o endereço físico do endereço virtual 25.792?

a) 25.792  
b) 24.582  
c) 24.576  
d) 29.888

### Questão 202 [M]

Na estrutura do Windows 7, a HAL serve para:

a) Gerenciar arquivos  
b) Desenhar janelas  
c) Traduzir chamadas POSIX  
d) Abstrair as diferenças de hardware entre plataformas

### Questão 203 [M]

Na sequência de interrupção, a CPU localiza o novo PC usando o vetor como índice numa tabela (vetor n → endereço 4·n). Para o vetor 5:

a) 40  
b) 5  
c) 20  
d) 10

### Questão 204 [M]

No mapa de bits de espaço livre da aula:

a) 1 = livre e 0 = ocupado  
b) Cada byte representa um arquivo  
c) Guarda-se o nome do arquivo  
d) 1 = unidade ocupada e 0 = unidade disponível

### Questão 205 [M]

O Core i7 executa instruções IA-32 internamente:

a) Quebrando-as em micro-operações semelhantes a RISC  
b) Por emulação em software  
c) Diretamente, sem decodificação  
d) Como pacotes EPIC

### Questão 206 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 2, 5, 1, 6, 1, 2, 5, 1, 1, 1, quantas faltas de página ocorrem com FIFO?

a) 6  
b) 7  
c) 8  
d) 9

### Questão 207 [M]

O conjunto de trabalho W(k, t), de Denning (1968), é:

a) O conjunto de todas as páginas do programa  
b) As páginas sujas  
c) As páginas do SO  
d) O conjunto de páginas usadas nas k referências mais recentes no instante t

### Questão 208 [F]

Qual é o tamanho de célula de memória mais comum?

a) 1 bit  
b) 8 bits  
c) 60 bits  
d) 12 bits

### Questão 209 [M]

Qual a representação de −16 em complemento de dois com 8 bits?

a) 0001 0000  
b) 1111 0000  
c) 1001 0000  
d) 1110 1111

### Questão 210 [M]

O padrão IEEE 754 foi adotado em ___ e revisado em ___:

a) 1991; 2001  
b) 2000; 2019  
c) 1985; 2008  
d) 1975; 1995

### Questão 211 [D]

Páginas de 8.192 bytes. Tabela de páginas (página→quadro): 0→2, 1→0, 2→5, 3→6, 4→7, 5→3, 6→4, 7→1. Qual o endereço físico do endereço virtual 45.494?

a) 40.963  
b) 29.110  
c) 45.494  
d) 24.576

### Questão 212 [M]

Na versão Core i7 de Hanói, qual registrador é usado como ponteiro de quadro?

a) ESP  
b) EIP  
c) EAX  
d) EBP

### Questão 213 [M]

A chamada read recebe, no mínimo:

a) O arquivo aberto, um ponteiro para o buffer e o número de bytes a ler  
b) O PID e a prioridade  
c) O endereço do disco e o setor  
d) Apenas o nome do arquivo

### Questão 214 [M]

Qual operação booleana é simétrica em relação a 0 e 1 e útil na geração de números aleatórios?

a) AND  
b) OR  
c) XOR  
d) NAND

### Questão 215 [D] ★

A adição em ponto flutuante:

a) É associativa só em double  
b) É sempre associativa  
c) É exata  
d) Não é associativa: (1e20 + (−1e20)) + 1 = 1, mas 1e20 + ((−1e20) + 1) = 0

### Questão 216 [M]

Para inverter apenas alguns bits de uma palavra, mantendo os demais, usa-se:

a) OR com uma máscara  
b) XOR com uma máscara  
c) AND com uma máscara  
d) NOT

### Questão 217 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 5, 4, 6, 5, 3, 2, 2, 6, 4, 2, quantas faltas de página ocorrem com LRU?

a) 7  
b) 9  
c) 8  
d) 6

### Questão 218 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de -0,1875?

a) 0xFEC00000  
b) 0xBEC00000  
c) 0xBE400000  
d) 0x3E400000

### Questão 219 [M]

No Core i7, com SIB: base = 3.492, índice = 19, escala = 1, deslocamento = 16. Qual o endereço efetivo?

a) 3.527  
b) 3.511  
c) 3.535  
d) 3.531

### Questão 220 [M]

Qual item NÃO faz parte de um quadro de pilha típico de procedimento?

a) Endereço de retorno  
b) Antigo ponteiro de quadro (FP) e variáveis locais  
c) A tabela de páginas do processo  
d) Parâmetros

### Questão 221 [M]

Por que a E/S é tão diferente entre o nível ISA e o OSM?

a) Por causa do BCD  
b) Porque o nível ISA não tem E/S  
c) Porque o OSM é mais rápido  
d) Por segurança (acesso direto permitiria ler dados de outros usuários) e porque a E/S no nível ISA é tediosa e complexa

### Questão 222 [M]

O padrão de 8 bits 1110 1100, interpretado em complemento de dois, vale:

a) 236  
b) -20  
c) -19  
d) -108

### Questão 223 [M]

Por que a adição em PF é mais complexa que a multiplicação?

a) Porque exige divisão  
b) Porque não pode dar overflow  
c) Porque usa mais bits de expoente  
d) Por causa da necessidade de alinhar os expoentes

### Questão 224 [M]

No UNIX, a organização típica do espaço de endereçamento é:

a) Pilha no início  
b) Dados antes do código  
c) Tudo no mesmo segmento sem ordem  
d) Código no início, dados em seguida e pilha no extremo oposto

### Questão 225 [M]

Os dois métodos clássicos de controle de espaço livre são:

a) TLB e cache  
b) Lista de livres (lacunas) e mapa de bits  
c) LRU e FIFO  
d) FAT e MFT

### Questão 226 [D]

O padrão IEEE 754 de 32 bits 0x41440000 representa o valor:

a) 6,125  
b) -12,25  
c) 12,25  
d) 24,5

### Questão 227 [D]

Some, em complemento de dois com 8 bits, 0011 1010 (58) + 0110 1100 (108). Resultado (descartando o vai-um) e situação:

a) 1010 0110, sem overflow  
b) 1010 0110, com overflow  
c) 1100 1110, sem overflow  
d) 1010 0111, com overflow

### Questão 228 [M]

Endereço virtual de 32 bits e páginas de 16.384 bytes. Como o endereço se divide?

a) 16 bits de página e 16 de deslocamento (65.536 páginas)  
b) 18 bits de página e 14 de deslocamento (262.144 páginas)  
c) 14 bits de página e 18 de deslocamento (16.384 páginas)  
d) 19 bits de página e 13 de deslocamento (524.288 páginas)

### Questão 229 [M]

Por que deslocar à direita números negativos sem extensão de sinal é um problema?

a) A flag Z é sempre ligada  
b) O número dobra  
c) O deslocamento vira rotação  
d) Entram zeros pela esquerda e o número vira positivo

### Questão 230 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 10,75?

a) 0xC12C0000  
b) 0x01AC0000  
c) 0x412C0000  
d) 0x41AC0000

### Questão 231 [M]

Por que instruções do mesmo tamanho da palavra podem desperdiçar espaço?

a) Porque todas precisam ser tão longas quanto a mais longa  
b) Porque exigem alinhamento em 64 bits  
c) Porque exigem vários ciclos de busca  
d) Porque não podem ter opcode

### Questão 232 [F]

Em `MOV R1, 4` (carrega a constante 4 em R1), o operando 4 usa endereçamento:

a) Direto  
b) De registrador  
c) Indireto de registrador  
d) Imediato

### Questão 233 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 5, 6, 6, 2, 5, 1, 1, 2, 6, 4, quantas faltas de página ocorrem com LRU?

a) 5  
b) 8  
c) 7  
d) 6

### Questão 234 [D]

Páginas de 4.096 bytes. Tabela de páginas (página→quadro): 0→3, 1→4, 2→2, 3→6, 4→5, 5→7, 6→0, 7→1. Qual o endereço físico do endereço virtual 17.173?

a) 16.389  
b) 17.173  
c) 20.480  
d) 21.269

### Questão 235 [M]

Vantagem das páginas grandes:

a) Transferência de disco mais eficiente e tabela de páginas menor  
b) Melhor para acessar matrizes por linha armazenadas por coluna  
c) Menos fragmentação interna  
d) Menos memória desperdiçada

### Questão 236 [M]

O termo 'roubo de ciclo' (cycle stealing) refere-se a:

a) A cache roubar blocos da memória  
b) A CPU desligar interrupções  
c) O DMA usar ciclos de barramento que seriam da CPU  
d) O SO tirar a CPU de um processo

### Questão 237 [M]

Endereço virtual de 24 bits e páginas de 4.096 bytes. Como o endereço se divide?

a) 13 bits de página e 11 de deslocamento (8.192 páginas)  
b) 0 bits de página  
c) 1 bits de página  
d) 12 bits de página e 12 de deslocamento (4.096 páginas)

### Questão 238 [M]

Analise, sobre overflow na adição em complemento de dois:

I. Somar um positivo com um negativo nunca dá overflow.  
II. Com operandos de mesmo sinal, há overflow se e somente se o resultado tem sinal oposto.  
III. Todo vai-um saindo do bit mais significativo indica overflow.

Está correto:

a) Apenas I e III  
b) I, II e III  
c) Apenas III  
d) Apenas I e II

### Questão 239 [F]

Quantos movimentos a solução recursiva das Torres de Hanói faz com 6 discos?

a) 32  
b) 64  
c) 63  
d) 36

### Questão 240 [M]

Qual o principal objetivo da predicação?

a) Substituir a memória virtual  
b) Aumentar o número de desvios  
c) Implementar BCD  
d) Eliminar desvios condicionais, deixando a CPU mais simples e o pipeline mais fluido

### Questão 241 [M]

Divisão em PF (32 bits): o expoente polarizado do dividendo é 136 e o do divisor é 123. Qual o expoente polarizado do quociente, antes da normalização?

a) 267  
b) 132  
c) 13  
d) 140

### Questão 242 [M]

Sem TLB, cada acesso do programa à memória exigiria:

a) Um acesso a disco  
b) Dois acessos adicionais para traduzir o endereço, aumento de 200% no tráfego  
c) Nenhum acesso adicional  
d) Metade dos acessos

### Questão 243 [M]

O ponteiro de arquivo:

a) É o mesmo que o PC  
b) Aponta para o diretório  
c) É fixo no início do arquivo  
d) Indica o próximo byte a ser lido, avança a cada read e pode ser reposicionado para acesso aleatório

### Questão 244 [M]

Segundo a aula, o Core i7 é tão irregular por causa de:

a) Compatibilidade, compatibilidade e compatibilidade  
b) Ser RISC  
c) Ter poucas instruções  
d) Economia de transistores

### Questão 245 [M]

O conceito de soquete (socket) veio do:

a) Windows NT  
b) MINIX  
c) System V da AT&T  
d) UNIX de Berkeley (BSD)

### Questão 246 [D]

Impressora (P=2) tem sua ISR rodando; em t=15 a RS232 (P=5) interrompe; em t=20 o disco (P=4) termina. O que acontece?

a) O disco é descartado  
b) O disco interrompe a RS232 imediatamente  
c) O disco fica pendente; quando a RS232 termina, a ISR do disco roda e só depois a impressora retoma  
d) A impressora retoma antes do disco

### Questão 247 [M]

Enquanto roda uma ISR de prioridade n:

a) Todas as interrupções são aceitas  
b) Interrupções de prioridade mais baixa são ignoradas (ficam pendentes) e as de prioridade mais alta entram imediatamente  
c) Só as de prioridade igual entram  
d) Nenhuma interrupção é aceita

### Questão 248 [M]

No UNIX, as camadas gráficas (X Windows, Motif):

a) Substituem a shell no núcleo  
b) Fazem parte do núcleo  
c) Rodam em modo usuário, fora do núcleo  
d) São drivers

### Questão 249 [D]

Quantas operações de soma/subtração o algoritmo de Booth faz com o multiplicador 0101 0101 (8 bits, Q−1 inicial = 0)?

a) 4  
b) 8  
c) 7  
d) 9

### Questão 250 [M]

Na sequência de hardware da interrupção, como o dispositivo se identifica?

a) Escrevendo na tabela de páginas  
b) Colocando um inteiro pequeno (o vetor de interrupção) nas linhas de dados  
c) Enviando seu nome em ASCII  
d) Gerando uma exceção

### Questão 251 [M]

Dividir cada segmento em páginas de tamanho fixo:

a) Aumenta a fragmentação externa  
b) Evita a fragmentação externa, ao custo de uma tabela de páginas por segmento  
c) Elimina a necessidade de tabelas  
d) Impede o compartilhamento

### Questão 252 [M]

Segmentos em memória com segmentação pura são trazidos e retirados do disco por:

a) Paginação por demanda obrigatória  
b) Overlays manuais  
c) DMA sem SO  
d) Permutação (swapping) de segmentos inteiros

### Questão 253 [M]

Uma máquina antiga tem campo de endereço de 16 bits e 4096 palavras de memória. O espaço de endereçamento é de:

a) 32.768 palavras  
b) 4.096 palavras  
c) 16 palavras  
d) 65.536 palavras

### Questão 254 [M]

A compactação resolve a fragmentação externa, mas:

a) Aumenta a fragmentação interna  
b) Exige páginas de 4 MB  
c) Apaga os segmentos  
d) Consome muito tempo de CPU

### Questão 255 [M]

A TLB do ARM do OMAP4430 tem:

a) 128 entradas para instruções e 128 para dados, com suporte a ASID  
b) 16 entradas no total  
c) Nenhuma entrada para instruções  
d) Uma entrada por processo

### Questão 256 [M]

Multiplicação em PF (32 bits): os expoentes polarizados são 119 e 117. Qual o expoente polarizado do resultado, antes da normalização?

a) -18  
b) 236  
c) 109  
d) 110

### Questão 257 [M]

Na divisão em complemento de dois (regra do slide), o sinal do resto é:

a) Igual ao sinal do divisor  
b) Sempre positivo  
c) Igual ao sinal do dividendo  
d) Igual ao sinal do quociente

### Questão 258 [M]

Na Figura 5.17, R3 recebe A+4096 porque:

a) R3 guarda a soma final  
b) O vetor tem 4096 elementos  
c) 4096 é o tamanho da página  
d) O vetor tem 1024 inteiros de 4 bytes, e R3 aponta para o primeiro endereço após o vetor

### Questão 259 [M]

Num monoprocessador, o SO pode garantir a indivisibilidade de UP/DOWN:

a) Aumentando a prioridade do processo  
b) Desabilitando as interrupções durante a operação  
c) Usando DMA  
d) Não é possível

### Questão 260 [M]

Arredondar para 0 (truncar) significa:

a) Transformar em zero  
b) Arredondar para o par  
c) Descartar os bits extras, de modo que a magnitude fica ≤ à do valor exato  
d) Arredondar sempre para cima

### Questão 261 [M]

No algoritmo de Booth, se Q0 Q−1 = 00 ou 11:

a) Soma M  
b) Inverte Q  
c) Subtrai M  
d) Só desloca

### Questão 262 [D]

Páginas de 4.096 bytes. Tabela de páginas (página→quadro): 0→7, 1→3, 2→0, 3→4, 4→2, 5→5, 6→6, 7→1. Qual o endereço físico do endereço virtual 762?

a) 29.434  
b) 7  
c) 28.672  
d) 762

### Questão 263 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 0,15625?

a) 0x3E200000  
b) 0x7EA00000  
c) 0x3EA00000  
d) 0xBE200000

### Questão 264 [F]

A principal limitação do endereçamento direto é que:

a) Não pode ser usado em desvios  
b) Acessa sempre a mesma posição, servindo basicamente para variáveis globais com endereço conhecido na compilação  
c) Só serve para constantes pequenas  
d) Exige dois acessos à memória para achar o endereço

### Questão 265 [F]

A maioria das máquinas tem, no nível ISA, um espaço de endereçamento linear de:

a) 2^16 palavras apenas  
b) 2^8 bytes  
c) 2^32 ou 2^64 bytes  
d) Tamanho igual à RAM instalada

### Questão 266 [M]

O valor de 32 bits 0xCAFEBABE é gravado a partir do endereço 200 numa máquina little-endian. Qual byte fica no endereço 200?

a) 0xFE  
b) 0xBA  
c) 0xBE  
d) 0xCA

### Questão 267 [M] ★

Em IEEE 754, 0,0/0,0 e √(−1) resultam em:

a) 0  
b) +∞  
c) NaN  
d) −∞

### Questão 268 [M] ★

No slide do Hello World, o C chama printf("Hello World!\n"), mas o assembly gerado tem `call puts@PLT`. Por quê?

a) O GCC otimizou: printf com string constante terminada em \n e sem formatação equivale a puts, que é mais barato  
b) puts é uma instrução de máquina do x86-64  
c) Foi um erro de compilação  
d) printf não existe no Linux

### Questão 269 [M]

O produto de dois inteiros sem sinal de n bits pode ter até:

a) n bits  
b) n + 1 bits  
c) n² bits  
d) 2n bits

### Questão 270 [M]

Qual NÃO faz parte do estado de um processo, segundo a aula?

a) Contador de programa (PC)  
b) O código-fonte do programa  
c) Ponteiro de pilha e registradores gerais  
d) Palavra de estado (PSW)

### Questão 271 [M]

Um descritor de segmento do Core i7 tem 8 bytes e contém, entre outros:

a) Apenas o número da página  
b) A tabela de interrupções  
c) O PC do processo  
d) BASE, LIMIT e campos de proteção

### Questão 272 [M]

Em binary32, a faixa de expoentes verdadeiros para números normalizados é:

a) −126 a +127  
b) −128 a +127  
c) 0 a 255  
d) −127 a +128

### Questão 273 [M]

No openmp.c, `#pragma omp parallel` faz:

a) Criar uma equipe de threads que executam o bloco, cada uma com seu ID (omp_get_thread_num)  
b) Criar processos com fork  
c) Rodar o bloco uma vez só  
d) Desabilitar interrupções

### Questão 274 [M]

Qual NÃO é motivo para evitar programas automodificadores?

a) São impossíveis de implementar numa máquina de von Neumann  
b) Não podem ser compartilhados entre processos simultâneos  
c) São difíceis de entender  
d) Quebram a cache de instruções

### Questão 275 [M]

−7 ÷ (−3), pela regra do slide, resulta em:

a) Quociente +2 e resto −1  
b) Quociente +3 e resto +2  
c) Quociente +2 e resto +1  
d) Quociente −2 e resto −1

### Questão 276 [D]

O padrão IEEE 754 de 32 bits 0x3EA00000 representa o valor:

a) 0,625  
b) 0,15625  
c) 0,3125  
d) -0,3125

### Questão 277 [M]

As quatro fases da adição/subtração em PF, na ordem, são:

a) Alinhar, normalizar, verificar zeros e somar  
b) Verificar zeros, alinhar significandos, somar/subtrair significandos e normalizar  
c) Multiplicar expoentes, somar e arredondar  
d) Normalizar, somar, alinhar e verificar zeros

### Questão 278 [F]

Numa máquina que exige alinhamento, um dado de 8 bytes pode começar em qual endereço?

a) 25  
b) 23  
c) 24  
d) 28

### Questão 279 [M]

Os cinco mecanismos que alteram o fluxo de controle têm em comum:

a) Serem síncronos  
b) Serem gerados pelo hardware  
c) Alterar (temporariamente ou não) o endereço no contador de programa  
d) Usarem DMA

### Questão 280 [M]

Dentro de um grupo de instruções da IA-64, as instruções:

a) Devem ser executadas em ordem estrita  
b) Têm apenas dependências RAW  
c) Não têm dependências RAW nem WAW, e só têm dependências WAR restritas  
d) Podem ter qualquer dependência

### Questão 281 [F]

Informação 'em linha' (online) é aquela que:

a) Está na nuvem apenas  
b) Está em um CD que precisa ser inserido  
c) Está impressa  
d) Está acessível diretamente pelo computador, sem intervenção humana

### Questão 282 [M]

O método prático para dividir em complemento de dois é:

a) Usar Booth  
b) Dividir direto sem ajuste  
c) Converter os operandos para valores sem sinal, dividir e depois ajustar os sinais pelas regras  
d) Converter para BCD

### Questão 283 [M]

Uma vantagem do algoritmo de Booth é:

a) Usa ponto flutuante  
b) Funciona com qualquer combinação de sinais em complemento de dois e reduz, em média, o número de somas/subtrações  
c) Só funciona com positivos  
d) Dispensa deslocamentos

### Questão 284 [M]

Deslocar um inteiro positivo k bits à esquerda (sem overflow) equivale a:

a) Dividir por 2^k  
b) Multiplicar por 2^k  
c) Multiplicar por k  
d) Somar k

### Questão 285 [M]

Multiplicar M por 00011110 com Booth exige quantas operações de soma/subtração?

a) 1  
b) 8  
c) 4  
d) 2

### Questão 286 [M]

A ideia central do algoritmo de Booth é:

a) Somar M para cada bit 1  
b) Usar tabela de consulta  
c) Dividir o multiplicador por 2  
d) Trocar cada bloco de 1s do multiplicador por uma subtração no início e uma adição no fim (2^(k+1) − 2^j)

### Questão 287 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de -12,5?

a) 0xC1C80000  
b) 0x41480000  
c) 0x81C80000  
d) 0xC1480000

### Questão 288 [M]

Para expoente de 4 bits (k = 4), a polarização é:

a) 8  
b) 7  
c) 15  
d) 4

### Questão 289 [M]

O valor de 32 bits 0xDEADBEEF é gravado a partir do endereço 200 numa máquina big-endian. Qual byte fica no endereço 200?

a) 0xAD  
b) 0xEF  
c) 0xDE  
d) 0xBE

### Questão 290 [M]

Na segmentação, recompilar um procedimento:

a) Muda os endereços de todos os segmentos  
b) Não afeta o endereço de início dos demais, pois cada um está em seu próprio segmento (n, 0)  
c) Exige relinkar todo o programa  
d) É impossível

### Questão 291 [M]

No algoritmo de Booth, se Q0 Q−1 = 01:

a) Só desloca  
b) A ← A − M e depois desloca  
c) A ← A + M e depois desloca  
d) Zera A

### Questão 292 [M]

Na predicação da IA-64:

a) Os desvios são convertidos em interrupções  
b) O hardware prevê o desvio  
c) Toda instrução é executada, mas só escreve o resultado se o predicado for verdadeiro  
d) Instruções com predicado falso nem são buscadas

### Questão 293 [F]

Fluxo de controle é:

a) O caminho dos dados na ULA  
b) A sequência em que as instruções são executadas dinamicamente, durante a execução  
c) O conjunto de flags da PSW  
d) A ordem estática das instruções na listagem

### Questão 294 [F]

A memória virtual clássica (paginada) é:

a) Unidimensional: endereços de 0 até um máximo, em uma sequência linear  
b) Sem endereços  
c) Bidimensional  
d) Tridimensional

### Questão 295 [M]

No UNIX, fork():

a) Espera o filho terminar  
b) Retorna 0 ao pai  
c) Cria uma cópia do processo chamador e retorna 0 ao filho e o PID do filho ao pai  
d) Substitui a imagem do processo

### Questão 296 [M]

Some, em complemento de dois com 4 bits, 1111 (-1) + 1000 (-8). Resultado (descartando o vai-um) e situação:

a) 0111, sem overflow  
b) 1000, com overflow  
c) 1001, sem overflow  
d) 0111, com overflow

### Questão 297 [M]

Qual a representação de −79 em complemento de dois com 8 bits?

a) 1100 1111  
b) 1011 0001  
c) 1011 0000  
d) 0100 1111

### Questão 298 [M]

Divisão em PF (32 bits): o expoente polarizado do dividendo é 136 e o do divisor é 118. Qual o expoente polarizado do quociente, antes da normalização?

a) 145  
b) 272  
c) 18  
d) 127

### Questão 299 [D] ★

Com 32 bits, quantos valores distintos um float consegue representar no máximo, comparado a um int de 32 bits?

a) Infinitos valores  
b) Apenas 2^23 valores  
c) No máximo 2^32 padrões, como o int; só estão espalhados numa faixa maior (e alguns são NaN)  
d) 2^64 valores

### Questão 300 [M]

Um laço pós-teste com n = 0:

a) Executa o corpo uma vez, o que é incorreto  
b) Não executa o corpo  
c) Gera exceção  
d) Entra em laço infinito

### Questão 301 [M]

Ao fim da divisão por restauração, quociente e resto ficam em:

a) Quociente em A e resto em Q  
b) Quociente em Q e resto em A  
c) Ambos em M  
d) Quociente em M

### Questão 302 [M]

No UNIX, o ancestral comum de todos os processos é:

a) login  
b) init (PID 1)  
c) kernel (PID 2)  
d) shell (PID 0)

### Questão 303 [M]

O exemplo do compilador com várias tabelas que crescem mostra que, numa memória unidimensional:

a) Uma tabela pode encher mesmo havendo espaço livre em outras regiões  
b) As tabelas nunca colidem  
c) A segmentação é desnecessária  
d) O compilador não precisa de tabelas

### Questão 304 [M]

Em 4 bits (C2), calcule M − S com M = 0110 (6) e S = 0011 (3), somando M ao complemento de dois de S:

a) 0100  
b) 1001  
c) 0011  
d) 0011 (overflow)

### Questão 305 [F]

O nível ISA (Instruction Set Architecture) é melhor descrito como:

a) O conjunto de chamadas de sistema do SO  
b) A interface entre o sistema operacional e o usuário  
c) A interface entre os compiladores e o hardware  
d) A camada de microprogramas que interpreta o nível lógico digital

### Questão 306 [M]

Na versão Core i7, o parâmetro n é acessado em:

a) [ESP]  
b) [EBP+4]  
c) [EBP+8]  
d) [EBP−8]

### Questão 307 [F]

Qual a faixa de um inteiro com sinal de 24 bits em complemento de dois?

a) -8.388.607 a 8.388.607  
b) -16.777.216 a 16.777.215  
c) 0 a 16.777.215  
d) -8.388.608 a 8.388.607

### Questão 308 [M]

Qual o valor da expressão em RPN `9 6 8 × × 9 3 + 9 7 × − −`, avaliada com uma pilha?

a) -483  
b) 966  
c) 483  
d) 484

### Questão 309 [M]

Por que os SSDs mudam o debate sobre tamanho de unidade de alocação?

a) Não têm tempo de busca nem atraso rotacional  
b) Usam FAT obrigatoriamente  
c) São mais lentos que HDs  
d) Não têm blocos

### Questão 310 [M]

O valor de 32 bits 0xDEADBEEF é gravado a partir do endereço 200 numa máquina little-endian. Qual byte fica no endereço 200?

a) 0xDE  
b) 0xBE  
c) 0xEF  
d) 0xAD

### Questão 311 [M]

O valor de 32 bits 0x0A0B0C0D é gravado a partir do endereço 200 numa máquina little-endian. Qual byte fica no endereço 200?

a) 0x0B  
b) 0x0A  
c) 0x0C  
d) 0x0D

### Questão 312 [M]

No Core i7, R/M = 100 com MOD ≠ 11 indica:

a) Um imediato de 8 bits  
b) Que há um byte SIB (escala, índice, base)  
c) O registrador ESP como ponteiro  
d) Endereçamento direto

### Questão 313 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 0,625?

a) 0x7FA00000  
b) 0x3FA00000  
c) 0x3F200000  
d) 0xBF200000

### Questão 314 [M]

Endereço virtual de 20 bits e páginas de 512 bytes. Como o endereço se divide?

a) 9 bits de página e 11 de deslocamento (512 páginas)  
b) 10 bits de página e 10 de deslocamento (1.024 páginas)  
c) 12 bits de página e 8 de deslocamento (4.096 páginas)  
d) 11 bits de página e 9 de deslocamento (2.048 páginas)

### Questão 315 [M]

Qual a representação de −113 em complemento de dois com 8 bits?

a) 1000 1111  
b) 0111 0001  
c) 1111 0001  
d) 1000 1110

### Questão 316 [D]

Pelo algoritmo de Booth com 4 bits, M = 0100 (4) e Q = 0101 (5). Qual o conteúdo final de A:Q?

a) 0001 0101 (21)  
b) 0001 0100 (20)  
c) 0001 0110 (22)  
d) 1110 1100 (-20)

### Questão 317 [M]

No Core i7, se a paginação estiver desabilitada:

a) O endereço linear vai para a TLB  
b) O endereço linear já é o endereço físico  
c) O programa não roda  
d) A segmentação também é desligada

### Questão 318 [M]

O padrão de 8 bits 1100 1010, interpretado em complemento de dois, vale:

a) -54  
b) -74  
c) -53  
d) 202

### Questão 319 [D]

Na mesma máquina (16 bits, campos de 4 bits), queremos 14 instruções de 3 endereços (0000–1101) e usamos 1110 e 1111 como escape. Usando todo o resto só para instruções de 2 endereços (opcode de 8 bits), quantas são possíveis?

a) 16  
b) 48  
c) 30  
d) 32

### Questão 320 [M]

O prólogo de um procedimento:

a) Desabilita interrupções  
b) Executa RET  
c) Restaura SP e FP aos valores anteriores  
d) Salva o FP antigo, ajusta o novo FP e avança o SP para reservar as variáveis locais

### Questão 321 [M]

Por que a multiplicação em complemento de dois não funciona 'direto' como a sem sinal?

a) Porque o hardware não tem somador  
b) Porque o resultado tem n bits  
c) Funciona direto sim  
d) Produtos parciais negativos precisam de extensão de sinal, e os bits de um multiplicador negativo não correspondem aos deslocamentos

### Questão 322 [M] ★

Na chamada open("arquivo2", O_WRONLY|O_CREAT, 0644), o 0644 define:

a) O número de bytes  
b) O tamanho do buffer  
c) O descritor  
d) As permissões do arquivo criado (rw-r--r--)

### Questão 323 [M]

Se o vetor de interrupção n aponta para a entrada no endereço 4·n, onde fica a entrada do vetor 8?

a) 64  
b) 8  
c) 32  
d) 16

### Questão 324 [M]

Some, em complemento de dois com 4 bits, 1010 (-6) + 1011 (-5). Resultado (descartando o vai-um) e situação:

a) 0101, com overflow  
b) 0101, sem overflow  
c) 1111, sem overflow  
d) 0110, com overflow

### Questão 325 [M]

Um programa de 7.841 bytes usa páginas de 1.024 bytes. Quantas páginas ocupa e quanto é desperdiçado por fragmentação interna?

a) 8 páginas, 0 bytes  
b) 8 páginas, 351 bytes  
c) 7 páginas, 673 bytes  
d) 8 páginas, 673 bytes

### Questão 326 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 1?

a) 0x00000000  
b) 0x40000000  
c) 0xBF800000  
d) 0x3F800000

### Questão 327 [M]

No problema produtor-consumidor com buffer circular, por que a última posição nunca é usada?

a) Por alinhamento  
b) Para guardar o semáforo  
c) Para guardar o PID  
d) Porque, se fosse, in = out seria ambíguo (buffer cheio ou vazio?)

### Questão 328 [M]

Um número normalizado em base 2 tem a forma:

a) ±bbb × 2^E sem restrição  
b) ±0,1bbb × 2^E  
c) ±1,000 × 10^E  
d) ±1,bbb…b × 2^E, com o 1 inicial implícito

### Questão 329 [M]

No Core i7, com SIB: base = 2.336, índice = 9, escala = 1, deslocamento = 12. Qual o endereço efetivo?

a) 2.345  
b) 2.365  
c) 2.361  
d) 2.357

### Questão 330 [D] ★

Diferença entre concorrência e paralelismo:

a) Concorrência é ter várias tarefas em andamento ao mesmo tempo (podendo intercalar numa CPU); paralelismo é executá-las de fato simultaneamente em várias CPUs  
b) Concorrência exige várias CPUs  
c) Paralelismo só existe em GPUs  
d) São sinônimos

### Questão 331 [M]

Como calcular 10 × n só com deslocamentos e soma?

a) (n << 4) − (n << 1)  
b) (n << 3) + (n << 1)  
c) n << 10  
d) (n << 3) + n

### Questão 332 [M]

O padrão de 8 bits 1101 0000, interpretado em complemento de dois, vale:

a) 208  
b) -48  
c) -47  
d) -80

### Questão 333 [M]

Numa VM, as instruções de E/S:

a) Acessam o dispositivo diretamente  
b) São convertidas em DMA pelo compilador  
c) São proibidas  
d) Não acessam os dispositivos diretamente: causam interrupção ao hipervisor, que decide a política

### Questão 334 [M]

Em complemento de dois, o bit mais significativo de uma palavra de n bits tem peso:

a) 2^n  
b) +2^(n−1)  
c) −2^(n−1)  
d) −1

### Questão 335 [M]

Um programa de 29.074 bytes usa páginas de 4.096 bytes. Quantas páginas ocupa e quanto é desperdiçado por fragmentação interna?

a) 8 páginas, 402 bytes  
b) 7 páginas, 402 bytes  
c) 8 páginas, 3.694 bytes  
d) 8 páginas, 0 bytes

### Questão 336 [M]

Qual a forma RPN da expressão infixa 6 − 4 − 8 × 9?

a) `6 4 8 9 − × −`  
b) `− × 9 8 − 4 6`  
c) `6 4 − 8 9 × −`  
d) `9 8 6 4 − − ×`

### Questão 337 [D]

Um semáforo começa em 3. Processos distintos executam, nesta ordem: down, down, down, down, up, up. Qual o estado final?

a) Semáforo = 1, 0 processo(s) bloqueado(s)  
b) Semáforo = 1, 1 processo(s) bloqueado(s)  
c) Semáforo = 3, 0 processo(s) bloqueado(s)  
d) Semáforo = 2, 0 processo(s) bloqueado(s)

### Questão 338 [F]

Numa máquina que exige alinhamento, um dado de 16 bytes pode começar em qual endereço?

a) 72  
b) 64  
c) 63  
d) 65

### Questão 339 [M]

Multiplicação em PF (32 bits): os expoentes polarizados são 134 e 119. Qual o expoente polarizado do resultado, antes da normalização?

a) -1  
b) 253  
c) 127  
d) 126

### Questão 340 [M]

Um espaço virtual de 64 KB com páginas de 4 KB e memória física de 32 KB tem:

a) 64 páginas e 32 quadros  
b) 8 páginas e 16 quadros  
c) 16 páginas virtuais e 8 quadros de página  
d) 16 páginas e 16 quadros

### Questão 341 [M]

Por que o bit de espera para despertar não resolve o caso geral?

a) Porque só funciona com n processos  
b) Com n processos podem ser necessários n − 1 despertares guardados, e um bit só conta até 1  
c) Porque o bit não existe em hardware  
d) Porque é lento demais

### Questão 342 [M]

Na multiplicação em PF com expoentes polarizados, por que se subtrai a polarização uma vez?

a) Porque a polarização é negativa  
b) Não se subtrai  
c) Para normalizar  
d) Porque, ao somar os dois expoentes polarizados, a polarização foi somada duas vezes

### Questão 343 [M]

Vantagem das páginas pequenas:

a) Tabela de páginas menor  
b) Menos faltas de página em qualquer caso  
c) Uso mais eficiente do disco  
d) Menos fragmentação interna

### Questão 344 [D]

O padrão IEEE 754 de 32 bits 0xC0E00000 representa o valor:

a) -14  
b) -7  
c) -3,5  
d) 7

### Questão 345 [F]

No formato de 32 bits (binary32), os campos são:

a) 1, 11, 52  
b) 1, 7, 24  
c) 1 bit de sinal, 8 bits de expoente, 23 bits de fração  
d) 2, 8, 22

### Questão 346 [D]

Pelo algoritmo de Booth com 4 bits, M = 0011 (3) e Q = 1011 (-5). Qual o conteúdo final de A:Q?

a) 0010 0001 (33)  
b) 1111 0001 (-15)  
c) 0000 1111 (15)  
d) 1111 0010 (-14)

### Questão 347 [M]

A instrução ideal para corrotinas (raramente existente) faria:

a) Um RET seguido de CALL que altera o SP  
b) Um CALL comum  
c) A desabilitação de interrupções  
d) A troca do topo da pilha com o PC, sem alterar o SP

### Questão 348 [M]

A VMCS (Virtual-Machine Control Structure):

a) Define o suporte estendido a interrupções para virtualizar a E/S  
b) É a tabela de páginas da VM  
c) É o disco virtual  
d) É um anel de proteção

### Questão 349 [M]

Some, em complemento de dois com 4 bits, 0111 (7) + 0110 (6). Resultado (descartando o vai-um) e situação:

a) 1101, sem overflow  
b) 1101, com overflow  
c) 1110, com overflow  
d) 0001, sem overflow

### Questão 350 [F]

Inteiros sem sinal são tipicamente usados para:

a) Coordenadas que podem ser negativas  
b) Saldo bancário  
c) Endereços, contadores e tamanhos  
d) Temperatura

### Questão 351 [M]

Qual a representação de −85 em complemento de dois com 8 bits?

a) 0101 0101  
b) 1101 0101  
c) 1010 1011  
d) 1010 1010

### Questão 352 [M]

Para virtualizar o hardware, as instruções comuns (aritméticas, lógicas, controle de fluxo):

a) Causam interrupção ao hipervisor  
b) Basta virtualizar o banco de registradores, salvando-o e restaurando-o nas trocas de VM  
c) Não podem ser executadas  
d) Precisam ser todas emuladas

### Questão 353 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 3, 5, 3, 3, 1, 6, 5, 6, 2, 2, quantas faltas de página ocorrem com FIFO?

a) 4  
b) 7  
c) 6  
d) 5

### Questão 354 [F]

Em uma instrução de dois endereços:

a) Um dos endereços é ao mesmo tempo fonte e destino  
b) Ambos os operandos vêm da pilha  
c) O resultado vai sempre para o acumulador  
d) Há dois operandos fonte e um destino separado

### Questão 355 [M]

Em IEEE 754 de 32 bits, qual o campo de expoente (polarizado) de 13,8125?

a) 129 (10000001)  
b) 131 (10000011)  
c) 3 (00000011)  
d) 130 (10000010)

### Questão 356 [M]

Analise as afirmativas sobre o que faz uma ISA ser boa:

I. Deve poder ser implementada com eficiência em tecnologias atuais e futuras.  
II. Deve fornecer um alvo claro para o código compilado, com regularidade e completude.  
III. Deve ter o maior número possível de modos de endereçamento, mesmo irregulares.

Está correto o que se afirma em:

a) Apenas II e III  
b) Apenas I  
c) I, II e III  
d) Apenas I e II

### Questão 357 [F]

As instruções do nível OSM que o SO acrescenta ao nível ISA são chamadas de:

a) Microinstruções  
b) Chamadas de sistema  
c) Interrupções de hardware  
d) Instruções SIMD

### Questão 358 [M]

Na tabela MOD × R/M do Core i7, MOD = 11 indica:

a) Operando em registrador (palavra ou byte)  
b) Memória com deslocamento de 32 bits  
c) Memória com deslocamento de 8 bits  
d) Memória sem deslocamento

### Questão 359 [M]

O padrão de 8 bits 1101 1110, interpretado em complemento de dois, vale:

a) 222  
b) -33  
c) -94  
d) -34

### Questão 360 [M]

A chamada creat do UNIX é considerada obsoleta porque:

a) Apaga arquivos  
b) open com a flag O_CREAT faz o mesmo  
c) Foi removida do POSIX  
d) Só funciona em BSD

### Questão 361 [M]

Qual a forma RPN da expressão infixa 4 − 3 + 8?

a) `+ 8 − 3 4`  
b) `4 3 8 − +`  
c) `4 3 − 8 +`  
d) `4 3 8 + −`

### Questão 362 [F]

Quantos movimentos a solução recursiva das Torres de Hanói faz com 5 discos?

a) 31  
b) 32  
c) 25  
d) 16

### Questão 363 [M]

Em sistemas de tempo compartilhado, carregar antecipadamente o conjunto de trabalho de um processo é útil porque:

a) Elimina a necessidade de disco  
b) Evita a fragmentação interna  
c) Aumenta o tamanho da página  
d) Cada processo é reiniciado muitas vezes, e evitar uma rajada de faltas a cada reinício economiza tempo

### Questão 364 [M] ★

Algumas máquinas separam os espaços de endereçamento de instruções e de dados. Esse modelo é conhecido como:

a) Arquitetura Harvard (usada, por exemplo, no AVR/ATmega)  
b) Arquitetura von Neumann pura  
c) Arquitetura EPIC  
d) Memória virtual segmentada

### Questão 365 [M]

Em IEEE 754 de 32 bits, qual o campo de expoente (polarizado) de 0,5?

a) 127 (01111111)  
b) 126 (01111110)  
c) 125 (01111101)  
d) -1 (11111111)

### Questão 366 [M]

Sobre onde guardar o endereço de retorno de procedimentos:

a) A 1ª palavra do procedimento é a melhor solução  
b) Guardar numa posição fixa de memória ou na 1ª palavra do procedimento (CDC 6600) falha com recursão; a pilha é a melhor solução  
c) A posição fixa funciona com recursão  
d) A pilha não permite recursão

### Questão 367 [D] ★

Por que o modelo EPIC do Itanium teve dificuldade na prática?

a) Porque era de 32 bits  
b) Porque tinha poucos registradores  
c) Depende de compiladores muito bons para achar paralelismo estático, e rodava mal o código x86 legado  
d) Porque não tinha predicação

### Questão 368 [D]

Páginas de 2.048 bytes. Tabela de páginas (página→quadro): 0→2, 1→1, 2→5, 3→6, 4→3, 5→4, 6→7, 7→0. Qual o endereço físico do endereço virtual 3.617?

a) 2.048  
b) 5.665  
c) 2.049  
d) 3.617

### Questão 369 [M]

A vantagem de usar expoente polarizado é:

a) Aumentar a precisão  
b) Permitir comparar números em PF (não negativos) como se fossem inteiros  
c) Eliminar o bit de sinal  
d) Evitar arredondamentos

### Questão 370 [F]

Qual a faixa de um inteiro com sinal de 6 bits em complemento de dois?

a) -32 a 31  
b) -64 a 63  
c) -31 a 31  
d) 0 a 63

### Questão 371 [F]

Um número em ponto flutuante tem a forma ±S × B^E. Qual campo NÃO é armazenado explicitamente no IEEE 754?

a) O sinal  
b) A base B (implícita, igual a 2)  
c) O expoente  
d) O significando

### Questão 372 [M]

O padrão de 8 bits 1110 0011, interpretado em complemento de dois, vale:

a) 227  
b) -29  
c) -99  
d) -28

### Questão 373 [M]

Aplicando rotação de 1 bit(s) à direita ao byte 0101 0010, obtém-se:

a) 0010 1000  
b) 1010 0100  
c) 0010 1011  
d) 0010 1001

### Questão 374 [M]

No Core i7, com SIB: base = 2.884, índice = 9, escala = 4, deslocamento = 12. Qual o endereço efetivo?

a) 2.932  
b) 2.920  
c) 2.905  
d) 11.584

### Questão 375 [M]

No MULTICS, as combinações recentes (segmento, página) → quadro ficavam em:

a) Tabela GDT  
b) Disco  
c) Uma memória associativa (TLB) de 16 entradas  
d) Registradores de segmento

### Questão 376 [M]

No IEEE 754, qual padrão representa infinito?

a) Expoente 0 e fração 0  
b) Expoente todo 1 e fração ≠ 0  
c) Expoente com todos os bits 1 e fração 0  
d) Expoente 0 e fração ≠ 0

### Questão 377 [M]

Na RPN, os operadores aparecem:

a) Sempre no início da expressão  
b) Em ordem alfabética  
c) Na mesma ordem da infixa  
d) Na ordem em que serão executados durante a avaliação

### Questão 378 [M]

Segundo a aula, grande parte dos transistores do Core i7 é gasta com:

a) Decompor instruções, resolver conflitos e prever desvios  
b) Memória principal  
c) Ponto flutuante  
d) Executar o trabalho útil

### Questão 379 [M]

O bit presente/ausente da tabela de páginas indica:

a) Se a página é de código  
b) A prioridade da página  
c) Se a página virtual está atualmente em algum quadro da memória principal  
d) Se a página foi modificada

### Questão 380 [M]

Quantos processos existem ao final de um programa que executa 2 chamadas fork() em sequência (sem if), contando o original?

a) 3  
b) 4  
c) 5  
d) 2

### Questão 381 [F]

O UNIX foi desenvolvido:

a) Na Microsoft, em 1981  
b) Em Berkeley, em 1991  
c) No MIT, em 1965  
d) No Bell Labs, no início dos anos 1970, por Ken Thompson (depois reescrito em C com Dennis Ritchie)

### Questão 382 [M]

Na divisão por restauração, se após A ← A − M o valor de A fica negativo:

a) O algoritmo termina  
b) Inverte-se Q  
c) Faz-se Q0 = 1 e mantém A  
d) Restaura-se A (soma M de volta) e faz-se Q0 = 0

### Questão 383 [M]

Em relação ao ponto fixo, o ponto flutuante:

a) Representa menos valores distintos com os mesmos bits  
b) Tem precisão maior para todos os valores  
c) É sempre exato  
d) Representa uma faixa muito maior de valores, à custa de precisão variável

### Questão 384 [F]

Uma instrução de zero endereços obtém seus operandos:

a) De registradores fixos codificados no opcode  
b) De um acumulador e de um imediato  
c) Do topo da pilha  
d) De um endereço direto de memória

### Questão 385 [M] ★

Uma instrução LEA (Load Effective Address) do x86:

a) Salva o endereço de retorno  
b) Lê a memória e soma ao acumulador  
c) Carrega uma constante de 64 bits  
d) Calcula o endereço efetivo e o coloca no registrador, sem acessar a memória

### Questão 386 [D] ★

Uma tabela de páginas de um nível, para 32 bits de endereço virtual, páginas de 4 KB e entradas de 4 bytes, ocupa:

a) 4 MB  
b) 16 MB  
c) 4 KB  
d) 1 MB

### Questão 387 [M]

No threads.c do professor, o laço com pthread_join serve para:

a) Sincronizar com semáforos  
b) Matar as threads  
c) O main esperar o término de cada thread antes de encerrar  
d) Criar as threads

### Questão 388 [M] ★

Diferença fundamental entre processo e thread:

a) Threads de um mesmo processo compartilham o espaço de endereçamento; processos têm espaços separados  
b) Processos compartilham a pilha  
c) Não há diferença  
d) Threads têm espaços separados

### Questão 389 [M]

Qual a representação de −68 em complemento de dois com 8 bits?

a) 1011 1100  
b) 1100 0100  
c) 0100 0100  
d) 1011 1011

### Questão 390 [M]

Quais modos de arredondamento dão suporte à aritmética intervalar?

a) Arredondar para +∞ e para −∞  
b) Apenas truncar  
c) Mais próximo e truncar  
d) Apenas mais próximo

### Questão 391 [M]

Banda da cache de instruções de 32 Gbit/s e tamanho médio de instrução de 32 bits. Qual o limite de instruções por segundo (t/r)?

a) 1024 bilhões  
b) 1 bilhões  
c) 4 bilhões  
d) 0,5 bilhões

### Questão 392 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de -1,5?

a) 0x3FC00000  
b) 0x80400000  
c) 0xC0400000  
d) 0xBFC00000

### Questão 393 [D]

Páginas de 2.048 bytes. Tabela de páginas (página→quadro): 0→6, 1→4, 2→2, 3→3, 4→1, 5→5, 6→0, 7→7. Qual o endereço físico do endereço virtual 800?

a) 6  
b) 13.088  
c) 800  
d) 12.288

### Questão 394 [F]

Na instrução indexada `MOV R4, A(R2)`, com A = 169508 e R2 = 0, qual endereço é lido?

a) 169512  
b) 0  
c) 169516  
d) 169508

### Questão 395 [M]

Os 'sinais' no UNIX são:

a) Semáforos  
b) Interrupções de software assíncronas enviadas a processos  
c) Arquivos especiais  
d) Instruções de E/S

### Questão 396 [M]

Quando ocorre uma falta de página, o SO:

a) Aborta o programa  
b) Aumenta o tamanho da página  
c) Pula a instrução  
d) Lê a página do disco, registra o novo local na tabela de páginas e repete a instrução que causou a falha

### Questão 397 [D] ★

Quantos processos existem ao final de `for (i = 0; i < 3; i++) fork();` (contando o original)?

a) 8  
b) 6  
c) 4  
d) 3

### Questão 398 [M]

Overflow de significando na soma (ex.: 1,100 + 1,010 = 10,110) é tratado:

a) Gerando exceção obrigatória  
b) Deslocando o significando à direita e incrementando o expoente  
c) Descartando o bit mais alto  
d) Decrementando o expoente

### Questão 399 [M]

Qual afirmação sobre memória virtual × cache está ERRADA?

a) Páginas (4 KB–16 MB) são muito maiores que blocos de cache (32–128 B)  
b) A MV é gerenciada pelo SO e a cache pelo hardware  
c) Uma falta de página custa muito mais que uma falta de cache  
d) A cache usa os bits de ordem alta do endereço como índice, e a MV usa os de ordem baixa

### Questão 400 [M]

Multiplicação em PF (32 bits): os expoentes polarizados são 131 e 135. Qual o expoente polarizado do resultado, antes da normalização?

a) 140  
b) 266  
c) 12  
d) 139

### Questão 401 [M]

No algoritmo de Booth, se Q0 Q−1 = 10:

a) Só desloca  
b) A ← A − M e depois desloca  
c) Termina o algoritmo  
d) A ← A + M e depois desloca

### Questão 402 [M]

Diferença entre nível ISA e OSM:

a) OSM é executado pelo microprograma  
b) Instruções ISA são executadas direto pela microarquitetura; instruções OSM (chamadas de sistema) são sempre interpretadas pelo SO  
c) Ambas são interpretadas pelo SO  
d) ISA é sempre software

### Questão 403 [D]

Quantas operações de soma/subtração o algoritmo de Booth faz com o multiplicador 0111 1111 (8 bits, Q−1 inicial = 0)?

a) 7  
b) 1  
c) 3  
d) 2

### Questão 404 [M]

Por que um booleano, que em teoria precisa de 1 bit, costuma ocupar 1 byte ou 1 palavra?

a) Porque bits individuais não têm endereço próprio  
b) Para guardar o valor em BCD  
c) Porque o hardware só compara palavras de 64 bits  
d) Porque o IEEE 754 exige

### Questão 405 [D]

Páginas de 8.192 bytes. Tabela de páginas (página→quadro): 0→5, 1→7, 2→2, 3→3, 4→6, 5→0, 6→1, 7→4. Qual o endereço físico do endereço virtual 18.905?

a) 18.905  
b) 16.386  
c) 16.384  
d) 27.097

### Questão 406 [M]

Visão do programador × visão do SO sobre um arquivo:

a) As duas são sempre idênticas  
b) Para o SO, o arquivo é uma sequência de registros lógicos  
c) Para o programador, blocos espalhados  
d) Para o programador, uma sequência linear de bytes; para o SO, uma coleção de unidades de alocação, não necessariamente consecutivas

### Questão 407 [M]

Aplicando deslocamento lógico de 2 bit(s) à direita ao byte 0111 0100, obtém-se:

a) 1101 0001  
b) 0001 1101  
c) 1101 0000  
d) 0001 1100

### Questão 408 [M]

Segundo a aula, mil CPUs de 1 ns em relação a uma CPU de 0,001 ns:

a) São mais caras  
b) São sempre mais lentas  
c) Dispensam software paralelo  
d) Têm, em teoria, a mesma capacidade agregada e são muito mais fáceis e baratas de construir, mas exigem software paralelo

### Questão 409 [D] ★

Para que serve o ASID (Address Space Identifier) na TLB?

a) Substitui a tabela de páginas  
b) Define o tamanho da página  
c) Permite manter traduções de vários processos na TLB sem precisar esvaziá-la a cada troca de contexto  
d) Identifica o dispositivo de E/S

### Questão 410 [M]

Em multiprocessadores, desabilitar interrupções não basta porque:

a) Outras CPUs continuam acessando o mesmo semáforo; são necessárias instruções atômicas (test-and-set, compare-and-swap)  
b) A CPU fica mais lenta  
c) As interrupções não existem  
d) O semáforo fica na cache L1

### Questão 411 [M]

O valor de 32 bits 0xCAFEBABE é gravado a partir do endereço 200 numa máquina big-endian. Qual byte fica no endereço 200?

a) 0xBA  
b) 0xFE  
c) 0xCA  
d) 0xBE

### Questão 412 [M]

Das máquinas de exemplo, qual NÃO tem sistema operacional?

a) ARM OMAP4430 (Linux)  
b) ATmega168  
c) Nenhuma, todas têm  
d) Core i7 (Windows 7)

### Questão 413 [D] ★

No threads.c, cada thread recebe &ids[i] em vez de &i. Por quê?

a) Porque pthread_create não aceita int  
b) Porque i é global  
c) Por desempenho apenas  
d) Se todas recebessem &i, leriam a mesma variável, que muda no laço, o que gera uma condição de disputa

### Questão 414 [M]

Com endereço virtual de 32 bits e páginas de 4 KB, o endereço se divide em:

a) 12 bits de página e 20 de deslocamento  
b) 16 e 16  
c) 22 e 10  
d) 20 bits de página virtual e 12 bits de deslocamento

### Questão 415 [M]

Qual o valor da expressão em RPN `7 9 + 9 4 + + 8 3 × 6 7 − − ×`, avaliada com uma pilha?

a) -725  
b) 726  
c) 725  
d) 1450

### Questão 416 [M] ★

Uma interrupção de relógio (timer) que causa troca de processo é:

a) Uma corrotina  
b) Um desvio condicional  
c) Uma exceção síncrona  
d) Uma interrupção assíncrona externa ao programa

### Questão 417 [D]

O padrão IEEE 754 de 32 bits 0xBF000000 representa o valor:

a) -0,25  
b) 0,5  
c) -1  
d) -0,5

### Questão 418 [F]

Como o número decimal 28 é codificado em BCD empacotado (1 byte)?

a) 0001 1100  
b) 0010 0010  
c) 0010 1000  
d) 1000 0010

### Questão 419 [M]

Na versão de Hanói para Core i7 e ARM usou-se C em vez de Java porque:

a) C é orientado a objetos  
b) printf é mais rápido que println  
c) Java não permite recursão  
d) A biblioteca de E/S Java não está disponível em forma nativa nessas máquinas, e a de C está

### Questão 420 [M]

Analise, sobre Hanói no ARM:

I. Carregar uma constante de 32 bits exige duas instruções (MOVW e MOVT).  
II. O endereço de retorno fica no registrador LR.  
III. Os parâmetros são empilhados em ordem inversa, como no Core i7.

Está correto:

a) Apenas I e III  
b) Apenas I e II  
c) Apenas III  
d) I, II e III

### Questão 421 [D]

Páginas de 2.048 bytes. Tabela de páginas (página→quadro): 0→0, 1→5, 2→4, 3→7, 4→3, 5→2, 6→6, 7→1. Qual o endereço físico do endereço virtual 528?

a) 2.576  
b) 4.624  
c) 0  
d) 528

### Questão 422 [D]

Pelo algoritmo de Booth com 4 bits, M = 1001 (-7) e Q = 1100 (-4). Qual o conteúdo final de A:Q?

a) 0110 1100 (108)  
b) 1110 0100 (-28)  
c) 0001 1100 (28)  
d) 0001 1101 (29)

### Questão 423 [D]

Some, em complemento de dois com 8 bits, 0100 1100 (76) + 0111 1111 (127). Resultado (descartando o vai-um) e situação:

a) 1100 1011, com overflow  
b) 1100 1101, sem overflow  
c) 1100 1100, com overflow  
d) 1100 1011, sem overflow

### Questão 424 [M]

Se o vetor de interrupção n aponta para a entrada no endereço 4·n, onde fica a entrada do vetor 3?

a) 3  
b) 6  
c) 12  
d) 24

### Questão 425 [M]

Qual tamanho de página NÃO é suportado pelo ARM do OMAP4430?

a) 64 KB  
b) 4 KB  
c) 8 KB  
d) 1 MB

### Questão 426 [D] ★

O que é deadlock (impasse)?

a) Uma falta de página  
b) Um processo com prioridade muito baixa  
c) Um conjunto de processos em que cada um espera um evento que só outro processo do conjunto pode causar  
d) Um laço infinito em um único processo

### Questão 427 [M]

Em IEEE 754 de 32 bits, qual o campo de expoente (polarizado) de -3,75?

a) 1 (00000001)  
b) 129 (10000001)  
c) 128 (10000000)  
d) 127 (01111111)

### Questão 428 [M]

A diferença essencial entre procedimento e corrotina é que:

a) A corrotina sempre recomeça do início  
b) Procedimentos são simétricos  
c) Corrotinas não usam pilha nem PC  
d) Na corrotina, quando o controle volta, ela continua de onde parou, e não do início

### Questão 429 [M]

O índice de arquivo do Windows 7 (NTFS), segundo a aula, é:

a) Uma árvore de registros com chave  
b) Uma lista de endereços de blocos  
c) Uma lista de execuções (runs) de blocos consecutivos  
d) Um bitmap

### Questão 430 [M]

Na estrutura do UNIX (Figura 6.31), a shell:

a) É um driver  
b) Roda em modo usuário e não faz parte do núcleo  
c) Faz parte do núcleo  
d) Roda em modo núcleo

### Questão 431 [F]

Para negar um inteiro em complemento de dois:

a) Inverte-se só o bit de sinal  
b) Inverte-se cada bit, sem somar 1  
c) Subtrai-se 1 e inverte-se o sinal  
d) Inverte-se cada bit (incluindo o de sinal) e soma-se 1

### Questão 432 [F]

Qual é o modo de endereçamento mais comum na maioria dos computadores?

a) Direto  
b) De pilha  
c) De registrador  
d) Imediato

### Questão 433 [M]

Das 16 funções booleanas de duas variáveis:

a) Nenhuma ISA implementa XOR  
b) Só o ARM implementa AND  
c) Poucas máquinas implementam todas; AND, OR, NOT e XOR são as mais comuns  
d) Todas as ISAs implementam as 16

### Questão 434 [F]

A memória virtual foi inventada:

a) No MIT, em 1990  
b) Em Manchester, Inglaterra, em 1961 (computador Atlas)  
c) No Bell Labs, em 1970  
d) Na IBM, em 1985

### Questão 435 [M]

Multiplicação em PF (32 bits): os expoentes polarizados são 131 e 117. Qual o expoente polarizado do resultado, antes da normalização?

a) 121  
b) -6  
c) 122  
d) 248

### Questão 436 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 4, 4, 6, 1, 6, 3, 5, 6, 3, 4, quantas faltas de página ocorrem com LRU?

a) 7  
b) 5  
c) 6  
d) 8

### Questão 437 [M]

A resposta da indústria às limitações da IA-32, já que o Itanium não pegou, foi:

a) Mais núcleos por chip (multicore), em vez de trocar a ISA  
b) Adotar a IA-64 em desktops  
c) Voltar para 16 bits  
d) Eliminar caches

### Questão 438 [M]

No Core i7, com SIB: base = 1.908, índice = 12, escala = 8, deslocamento = 12. Qual o endereço efetivo?

a) 2.016  
b) 2.004  
c) 1.932  
d) 15.372

### Questão 439 [F]

Em sua forma mais simples, um arquivo é:

a) Uma sequência de bytes escrita em um dispositivo de E/S  
b) Um bloco de cache  
c) Um segmento de código  
d) Um registrador

### Questão 440 [M]

Sobre RPN, analise:

I. Qualquer fórmula pode ser expressa sem parênteses.  
II. É conveniente para avaliação em computadores com pilha.  
III. A ordem das variáveis muda em relação à notação infixa.

Está correto:

a) Apenas I e III  
b) Apenas I e II  
c) I, II e III  
d) Apenas II e III

### Questão 441 [D]

Páginas de 2.048 bytes. Tabela de páginas (página→quadro): 0→6, 1→0, 2→7, 3→3, 4→5, 5→4, 6→1, 7→2. Qual o endereço físico do endereço virtual 104?

a) 12.392  
b) 6  
c) 104  
d) 12.288

### Questão 442 [M]

Na divisão sem sinal de 4 bits por restauração, dividendo 1100 (12) e divisor 0110 (6). Ao final:

a) Q = 0010, R = 0110  
b) Q = 0011, R = 0000  
c) Q = 0000, R = 0010  
d) Q = 0010, R = 0000

### Questão 443 [M]

O padrão de 8 bits 1110 0100, interpretado em complemento de dois, vale:

a) -100  
b) -27  
c) -28  
d) 228

### Questão 444 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 5,5?

a) 0xC0B00000  
b) 0x01300000  
c) 0x41300000  
d) 0x40B00000

### Questão 445 [M]

No alinhamento dos significandos, desloca-se:

a) Ambos à esquerda  
b) O significando do número menor à direita, incrementando seu expoente  
c) O do maior à esquerda  
d) O do maior à direita

### Questão 446 [M]

Qual a forma RPN da expressão infixa (6 − 7) × 9?

a) `6 7 9 × −`  
b) `6 7 9 − ×`  
c) `× 9 − 7 6`  
d) `6 7 − 9 ×`

### Questão 447 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 3, 3, 1, 6, 6, 4, 1, 3, 6, 3, quantas faltas de página ocorrem com FIFO?

a) 6  
b) 5  
c) 4  
d) 7

### Questão 448 [M]

Sobre registradores no nível ISA, é correto afirmar:

a) MAR e MBR são registradores de uso geral visíveis ao programador  
b) Dividem-se em registradores de uso especial e de uso geral  
c) Registradores de flags não existem no nível ISA  
d) Todos são de uso geral

### Questão 449 [M]

Qual a representação de −43 em complemento de dois com 8 bits?

a) 1101 0101  
b) 0010 1011  
c) 1010 1011  
d) 1101 0100

### Questão 450 [M]

A favor de unidades de alocação GRANDES:

a) Menos desperdício na última unidade  
b) Melhor aproveitamento do espaço  
c) Tempo de busca e atraso rotacional dominam o acesso, então ler muito de uma vez compensa  
d) SSDs têm tempo de busca alto

### Questão 451 [D]

Na chamada recursiva torres(3, 1, 3), quantas vezes o procedimento torres é chamado no total (contando a chamada inicial)?

a) 3  
b) 15  
c) 7  
d) 10

### Questão 452 [M]

Sobre o Windows 3.x, a aula destaca que:

a) Não era um SO de verdade, e sim uma GUI sobre o MS-DOS  
b) Era um SO de 32 bits  
c) Era baseado em UNIX  
d) Tinha memória virtual completa

### Questão 453 [D]

Some, em complemento de dois com 8 bits, 0111 1011 (123) + 0100 1011 (75). Resultado (descartando o vai-um) e situação:

a) 1100 0111, com overflow  
b) 0011 0000, sem overflow  
c) 1100 0110, sem overflow  
d) 1100 0110, com overflow

### Questão 454 [M]

Sobre o modelo de memória do Itanium 2:

a) É sempre little-endian  
b) Não tem ordem de bytes  
c) Pode ser big-endian ou little-endian, conforme um bit ajustado pelo SO  
d) É sempre big-endian

### Questão 455 [M]

Antes da memória virtual, a técnica de sobreposições (overlays) exigia que:

a) O compilador gerasse segmentos  
b) O hardware fizesse tudo automaticamente  
c) O SO paginasse sob demanda  
d) O programador dividisse o programa em partes e gerenciasse o transporte entre disco e memória

### Questão 456 [M] ★

Um mutex pode ser visto como:

a) Um tipo de interrupção  
b) Um semáforo com valor inicial 0  
c) Um semáforo binário com valor inicial 1, usado para exclusão mútua  
d) Um buffer circular

### Questão 457 [M]

Para isolar o segundo caractere de uma palavra de 32 bits com 4 caracteres de 8 bits, usa-se:

a) AND com uma máscara que tem 1s só nos bits desse caractere, depois deslocamento  
b) Rotação de 32 bits  
c) OR com máscara de zeros  
d) XOR com a própria palavra

### Questão 458 [D]

Some, em complemento de dois com 8 bits, 1111 0010 (-14) + 1100 0010 (-62). Resultado (descartando o vai-um) e situação:

a) 1011 0100, sem overflow  
b) 0011 0000, sem overflow  
c) 1011 0100, com overflow  
d) 1011 0101, sem overflow

### Questão 459 [M]

Na representação geométrica, somar k positivo corresponde a:

a) Andar k posições no sentido horário  
b) Ficar parado  
c) Andar k posições no anti-horário  
d) Ir ao ponto oposto

### Questão 460 [D]

Um semáforo começa em 1. Processos distintos executam, nesta ordem: down, up, down, down. Qual o estado final?

a) Semáforo = 0, 1 processo(s) bloqueado(s)  
b) Semáforo = -1, 0 processo(s) bloqueado(s)  
c) Semáforo = 0, 2 processo(s) bloqueado(s)  
d) Semáforo = 1, 1 processo(s) bloqueado(s)

### Questão 461 [M]

Em mainframes tradicionais, um arquivo é visto como:

a) Um diretório  
b) Uma página  
c) Uma sequência de registros lógicos com estrutura bem definida  
d) Uma sequência de bits sem estrutura

### Questão 462 [M]

A propriedade essencial dos semáforos é que UP e DOWN são:

a) Executadas pelo usuário  
b) Opcionais  
c) Indivisíveis (atômicas)  
d) Rápidas

### Questão 463 [M]

Sobre a distribuição dos números representáveis em PF:

a) Não são uniformemente espaçados: são mais densos perto de zero  
b) Só existem inteiros  
c) São uniformemente espaçados  
d) São mais densos longe do zero

### Questão 464 [M]

Máquina com instruções de 16 bits, opcode de 4 bits e endereços de 4 bits, com expansão de opcode: 15 instruções de 3 endereços, 14 de 2, 31 de 1 e 16 de 0. Total de instruções:

a) 64  
b) 76  
c) 80  
d) 61

### Questão 465 [M]

O padrão de 8 bits 1100 0111, interpretado em complemento de dois, vale:

a) 199  
b) -57  
c) -71  
d) -56

### Questão 466 [M]

Para calcular M − S em complemento de dois, o hardware:

a) Soma S ao complemento de M  
b) Tem um subtrator separado  
c) Inverte só o bit de sinal de S  
d) Soma M ao complemento de dois de S

### Questão 467 [M]

Um programa de 26.599 bytes usa páginas de 8.192 bytes. Quantas páginas ocupa e quanto é desperdiçado por fragmentação interna?

a) 3 páginas, 2.023 bytes  
b) 4 páginas, 6.169 bytes  
c) 4 páginas, 0 bytes  
d) 4 páginas, 2.023 bytes

### Questão 468 [M]

O Pentium 4 (e o Core i7) permitem que programas ISA referenciem palavras começando em qualquer endereço. A consequência disso é:

a) A memória deixa de ser endereçada por byte  
b) Acessos não alinhados geram exceção  
c) O desempenho é sempre igual ao de acessos alinhados  
d) Acessos não alinhados funcionam, mas podem ser mais lentos

### Questão 469 [M]

Após cada ISR em um sistema com 8259A, a CPU precisa:

a) Avisar o PIC que a interrupção foi processada  
b) Desligar a NMI  
c) Reiniciar o PIC  
d) Limpar a cache

### Questão 470 [M]

No MULTICS, o endereço tinha 18 bits de segmento e 16 bits de deslocamento. Portanto:

a) Até 262.144 segmentos, cada um com até 65.536 palavras  
b) Até 65.536 segmentos de 262.144 palavras  
c) Até 18 segmentos  
d) Até 34 segmentos de 16 palavras

### Questão 471 [D]

Pelo algoritmo de Booth com 4 bits, M = 0001 (1) e Q = 0111 (7). Qual o conteúdo final de A:Q?

a) 0000 1000 (8)  
b) 1111 1001 (-7)  
c) 0000 0111 (7)  
d) 0000 1001 (9)

### Questão 472 [M]

Aplicando rotação de 1 bit(s) à direita ao byte 1101 1000, obtém-se:

a) 0110 1100  
b) 1011 0000  
c) 1110 1100  
d) 1011 0001

### Questão 473 [M]

O custo de uma falta de página em relação a uma falta de cache é:

a) Menor  
b) Muito maior (milhares ou milhões de ciclos, por envolver o disco) contra dezenas de ciclos  
c) Sempre zero  
d) Igual

### Questão 474 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 7,25?

a) 0x40E80000  
b) 0x41680000  
c) 0xC0E80000  
d) 0x01680000

### Questão 475 [M]

Analise:

I. O segmento é uma entidade lógica que o programador conhece.  
II. Páginas têm tamanho fixo; segmentos podem ter tamanho variável.  
III. O principal problema da segmentação pura é a fragmentação interna.

Está correto:

a) I, II e III  
b) Apenas III  
c) Apenas I e III  
d) Apenas I e II

### Questão 476 [D] ★

Em IEEE 754, a comparação NaN == NaN retorna:

a) Verdadeiro  
b) Gera exceção sempre  
c) Depende do sinal  
d) Falso (NaN é diferente de tudo, inclusive de si mesmo)

### Questão 477 [D] ★

Por que processadores têm flags C e V separadas?

a) C indica overflow para aritmética sem sinal e V para aritmética com sinal; o mesmo somador serve para as duas  
b) C serve apenas para rotações  
c) V é para ponto flutuante  
d) C e V são redundantes

### Questão 478 [F]

Como o número decimal 62 é codificado em BCD empacotado (1 byte)?

a) 0100 0100  
b) 0010 0110  
c) 0110 0010  
d) 0011 1110

### Questão 479 [M] ★

Qual conjunto de características é típico de uma ISA RISC?

a) Instruções de tamanho variável e muitas instruções acessando memória  
b) Operações aritméticas memória-memória  
c) Instruções de tamanho fixo e arquitetura carregue/armazene  
d) Muitos modos de endereçamento irregulares

### Questão 480 [M]

No hardware de multiplicação sem sinal (Figura 10.8), a cada ciclo:

a) Se Q0 = 1, soma-se M a A; depois C, A e Q são deslocados 1 bit à direita  
b) Desloca-se à esquerda  
c) Subtrai-se M de A se Q0 = 0  
d) Soma-se Q a M sempre

### Questão 481 [M]

Na versão ARM, a instrução `pop {r3, r4, r5, r6, r7, pc}` serve para:

a) Criar o quadro de pilha  
b) Desabilitar interrupções  
c) Restaurar os registradores e retornar, pois o LR salvo é carregado no PC  
d) Chamar printf

### Questão 482 [F]

A principal motivação comercial para virtualizar, citada em aula, é:

a) Acelerar ponto flutuante  
b) Hospedagem/nuvem: rodar vários sistemas completos de clientes no mesmo servidor físico  
c) Reduzir o tamanho das instruções  
d) Eliminar o SO

### Questão 483 [M]

Por que instruções mais curtas tendem a tornar o processador mais rápido?

a) Porque a largura de banda da memória/cache não cresceu no ritmo das CPUs, e instruções curtas exigem menos bits buscados  
b) Porque sempre executam em um ciclo  
c) Porque dispensam decodificação  
d) Porque instruções curtas têm mais modos de endereçamento

### Questão 484 [M]

Paginação por demanda significa que:

a) O usuário decide quais páginas carregar  
b) Todas as páginas são carregadas no início  
c) As páginas só são trazidas à memória quando referenciadas  
d) As páginas são carregadas em horário fixo

### Questão 485 [M]

Na divisão em PF com expoentes polarizados:

a) E_res = Ex − Ey + bias, pois a subtração removeu a polarização  
b) E_res = Ex − Ey − bias  
c) E_res = Ex × Ey  
d) E_res = Ex + Ey − bias

### Questão 486 [M]

Com unidades de alocação de 16.384 bytes, um arquivo de 40.000 bytes desperdiça quantos bytes na última unidade?

a) 25.536  
b) 8.192  
c) 9.152  
d) 7.232

### Questão 487 [D]

Pelo algoritmo de Booth com 4 bits, M = 1110 (-2) e Q = 0001 (1). Qual o conteúdo final de A:Q?

a) 0000 0010 (2)  
b) 1111 1110 (-2)  
c) 0000 1110 (14)  
d) 1111 1111 (-1)

### Questão 488 [M]

−7 ÷ 3, pela regra de sinais do slide, resulta em:

a) Quociente −2 e resto −1  
b) Quociente −2 e resto +1  
c) Quociente −3 e resto +2  
d) Quociente +2 e resto −1

### Questão 489 [M]

Quantos processos existem ao final de um programa que executa 4 chamadas fork() em sequência (sem if), contando o original?

a) 15  
b) 4  
c) 5  
d) 16

### Questão 490 [M]

No Core i7, a LDT e a GDT são:

a) Caches L1 e L2  
b) Tabelas de páginas de 1º e 2º nível  
c) Tabelas de interrupção  
d) Local Descriptor Table (uma por programa) e Global Descriptor Table (uma no sistema, inclui o SO)

### Questão 491 [M]

O Itanium 2 tem quantos registradores de uso geral de 64 bits?

a) 32  
b) 128 (32 estáticos + 96 em pilha)  
c) 16  
d) 64

### Questão 492 [M]

Um programa de 3.300 bytes usa páginas de 1.024 bytes. Quantas páginas ocupa e quanto é desperdiçado por fragmentação interna?

a) 3 páginas, 228 bytes  
b) 4 páginas, 796 bytes  
c) 4 páginas, 0 bytes  
d) 4 páginas, 228 bytes

### Questão 493 [D] ★

Qual a diferença entre uma máquina virtual e um contêiner (Docker/Podman)?

a) São a mesma coisa  
b) O contêiner tem seu próprio kernel  
c) A VM virtualiza o hardware e roda um SO convidado completo; o contêiner compartilha o núcleo do hospedeiro e isola só processos  
d) A VM não precisa de hipervisor

### Questão 494 [M]

A principal desvantagem da E/S programada é:

a) Exige controlador DMA  
b) Gera interrupções demais  
c) A CPU fica em espera ocupada (busy waiting) lendo o registrador de estado  
d) Não funciona em sistemas embutidos

### Questão 495 [M]

Endereço virtual de 48 bits e páginas de 4.096 bytes. Como o endereço se divide?

a) 37 bits de página e 11 de deslocamento (137.438.953.472 páginas)  
b) 36 bits de página e 12 de deslocamento (68.719.476.736 páginas)  
c) 12 bits de página e 36 de deslocamento (4.096 páginas)  
d) 24 bits de página e 24 de deslocamento (16.777.216 páginas)

### Questão 496 [M]

Paginação excessiva (thrashing) ocorre tipicamente quando:

a) A TLB é grande demais  
b) O conjunto de trabalho é maior que o número de quadros disponíveis  
c) Não há páginas sujas  
d) A página é muito grande

### Questão 497 [M]

Some, em complemento de dois com 4 bits, 1110 (-2) + 0100 (4). Resultado (descartando o vai-um) e situação:

a) 1010, sem overflow  
b) 0011, sem overflow  
c) 0010, com overflow  
d) 0010, sem overflow

### Questão 498 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 0,375?

a) 0x3EC00000  
b) 0x7F400000  
c) 0xBEC00000  
d) 0x3F400000

### Questão 499 [F]

Quantos movimentos de disco a solução recursiva das Torres de Hanói faz para n = 4?

a) 31  
b) 8  
c) 15  
d) 16

### Questão 500 [M]

O valor de 32 bits 0x11223344 é gravado a partir do endereço 200 numa máquina big-endian. Qual byte fica no endereço 200?

a) 0x11  
b) 0x44  
c) 0x33  
d) 0x22

### Questão 501 [M]

Qual o valor da expressão em RPN `6 1 − 4 − 6 1 − 9 5 − × ×`, avaliada com uma pilha?

a) -20  
b) 40  
c) 20  
d) 21

### Questão 502 [M]

A ideia central de Manchester foi:

a) Usar BCD  
b) Separar o espaço de endereçamento das localizações reais de memória  
c) Aumentar o tamanho da palavra  
d) Eliminar o disco

### Questão 503 [M]

O modo 'PC + deslocamento de 13 bits' do ARM é útil principalmente para:

a) Fazer E/S mapeada  
b) Acessar a pilha do SO  
c) Carregar constantes armazenadas junto ao código  
d) Endereçar vetores bidimensionais

### Questão 504 [M]

No ARM do OMAP4430, o acesso à memória é feito:

a) Por qualquer instrução aritmética  
b) Apenas por LDR e STR  
c) Apenas por PUSH e POP  
d) Apenas por desvios

### Questão 505 [D] ★

Uma forma de hardware para detectar overflow numa soma em complemento de dois é:

a) Verificar apenas o vai-um de saída  
b) Verificar o bit de paridade  
c) Verificar se o vai-um que entra no bit de sinal difere do vai-um que sai dele (XOR dos dois)  
d) Verificar se o resultado é zero

### Questão 506 [M]

A instrução que encerra uma rotina de interrupção devolvendo a CPU ao estado anterior é:

a) RET comum  
b) JMP 0  
c) HLT  
d) RETURN FROM INTERRUPT (IRET no x86)

### Questão 507 [M]

Quantos processos existem ao final de um programa que executa 5 chamadas fork() em sequência (sem if), contando o original?

a) 31  
b) 5  
c) 32  
d) 6

### Questão 508 [M]

O algoritmo FIFO remove:

a) A página usada há mais tempo  
b) A página carregada há mais tempo, independentemente de quando foi referenciada  
c) A página com mais acessos  
d) A página suja mais recente

### Questão 509 [M]

Endereço virtual de 32 bits e páginas de 8.192 bytes. Como o endereço se divide?

a) 16 bits de página e 16 de deslocamento (65.536 páginas)  
b) 20 bits de página e 12 de deslocamento (1.048.576 páginas)  
c) 13 bits de página e 19 de deslocamento (8.192 páginas)  
d) 19 bits de página e 13 de deslocamento (524.288 páginas)

### Questão 510 [M]

Qual a forma RPN da expressão infixa (9 + 3) × (1 + 1)?

a) `9 3 1 1 + + ×`  
b) `× + 1 1 + 3 9`  
c) `9 3 + 1 1 + ×`  
d) `9 3 1 1 × + +`

### Questão 511 [M]

Opcodes e modos de endereçamento ortogonais significa que:

a) Os modos são escolhidos pelo hardware em tempo de execução  
b) Cada opcode admite apenas um modo  
c) São independentes e podem ser combinados de forma regular  
d) Só registradores podem ser operandos

### Questão 512 [M]

Estruturas de alto nível como if e while, quando compiladas para o nível ISA:

a) Eliminam todos os desvios  
b) Viram corrotinas  
c) Viram interrupções  
d) Viram muitos desvios

### Questão 513 [D] ★

Em C, com int de 32 bits, `INT_MAX + 1` em complemento de dois 'dá a volta' para:

a) INT_MAX  
b) INT_MIN (−2.147.483.648), e em C isso é tecnicamente comportamento indefinido para signed  
c) +2.147.483.648  
d) 0

### Questão 514 [M]

Com alocação consecutiva, localizar um byte qualquer do arquivo:

a) Basta conhecer o início do arquivo e fazer uma conta simples  
b) É impossível  
c) Exige um índice por bloco  
d) Exige percorrer uma lista encadeada

### Questão 515 [M]

Para produzir código do nível ISA, o escritor de compiladores precisa conhecer, entre outras coisas:

a) Os detalhes do microprograma de cada instrução  
b) Apenas o conjunto de instruções, pois registradores são invisíveis no nível ISA  
c) A tecnologia de fabricação dos transistores  
d) O modelo de memória, os registradores, os tipos de dados e as instruções disponíveis

### Questão 516 [M]

No algoritmo de Dijkstra (linha férrea Vitória–BH com ramal para o Rio):

a) Tudo vai para o Rio e volta na ordem inversa  
b) O ramal do Rio funciona como fila (FIFO)  
c) Variáveis vão direto para BH; operadores e parênteses consultam o ramal do Rio, que funciona como pilha  
d) Variáveis vão para o Rio e operadores direto para BH

### Questão 517 [M]

Interrupções não mascaráveis (NMI) nas CPUs Intel sinalizam:

a) Chamadas de sistema  
b) Relógio do sistema  
c) Quase catástrofes, como erros de paridade de memória  
d) Teclado

### Questão 518 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 5, 2, 6, 5, 3, 5, 1, 4, 4, 5, quantas faltas de página ocorrem com FIFO?

a) 8  
b) 7  
c) 6  
d) 9

### Questão 519 [F]

No registrador de flags (PSW), qual bit indica vai-um (carry) saindo do bit mais à esquerda?

a) V  
b) C  
c) Z  
d) N

### Questão 520 [M]

Na Figura 6.4, o endereço físico tem 15 bits. Os 3 bits superiores identificam:

a) O segmento  
b) O processo  
c) O quadro de página (8 quadros)  
d) O deslocamento

### Questão 521 [M]

O bug do Y2K está ligado ao BCD em COBOL. Com 8 bits, quantos valores distintos se representam em BCD empacotado (2 dígitos) e em binário puro, respectivamente?

a) 256 e 100  
b) 100 e 128  
c) 100 e 256  
d) 99 e 255

### Questão 522 [M]

Qual o valor da expressão em RPN `5 3 9 + + 6 6 − 8 5 × + ×`, avaliada com uma pilha?

a) 680  
b) -680  
c) 1360  
d) 681

### Questão 523 [M]

Por que o PC usa um controlador de interrupções externo como o 8259A?

a) Para traduzir endereços  
b) Para fazer DMA  
c) Porque a CPU só tem um nível mascarável, e é preciso gerenciar várias prioridades  
d) Para acelerar ponto flutuante

### Questão 524 [M]

No IEEE 754, expoente com todos os bits 1 e fração diferente de 0 representa:

a) Infinito  
b) Número subnormal  
c) Zero  
d) NaN (Not a Number)

### Questão 525 [D]

O padrão IEEE 754 de 32 bits 0x40200000 representa o valor:

a) 1,25  
b) 2,5  
c) -2,5  
d) 5

### Questão 526 [M]

Nos anéis de proteção do Core i7:

a) O nível 0 são os programas do usuário  
b) O nível 0 é o núcleo do SO e o nível 3 são os programas do usuário  
c) O nível 3 gerencia a MMU  
d) Existem 8 níveis

### Questão 527 [M]

Qual a representação de −67 em complemento de dois com 8 bits?

a) 1100 0011  
b) 1011 1101  
c) 0100 0011  
d) 1011 1100

### Questão 528 [M]

Qual a representação de −116 em complemento de dois com 8 bits?

a) 1000 1011  
b) 1111 0100  
c) 0111 0100  
d) 1000 1100

### Questão 529 [M]

Aplicando deslocamento lógico de 2 bit(s) à esquerda ao byte 1000 1111, obtém-se:

a) 0010 0011  
b) 1110 0011  
c) 0011 1100  
d) 0011 1110

### Questão 530 [M]

Com unidades de alocação de 8.192 bytes, um arquivo de 1 bytes desperdiça quantos bytes na última unidade?

a) 16.383  
b) 8.191  
c) 1  
d) 4.096

### Questão 531 [M]

Aplicando rotação de 2 bit(s) à esquerda ao byte 1010 0111, obtém-se:

a) 1110 1001  
b) 0010 1001  
c) 1001 1110  
d) 1001 1100

### Questão 532 [M]

A notação polonesa invertida (RPN) foi nomeada em homenagem a:

a) Alan Turing  
b) Edsger Dijkstra  
c) Jan Łukasiewicz  
d) John von Neumann

### Questão 533 [M]

Qual grupo de instruções do Core i7 serve para BCD?

a) DAA, DAS, AAA, AAS, AAM, AAD  
b) LODS, STOS, MOVS  
c) STC, CLC, STD  
d) SAL, SAR, ROL

### Questão 534 [D]

No esquema da Figura 5.12, por que só 15 (e não 16) instruções de 3 endereços?

a) Porque o registrador 15 é o PC  
b) Porque 1111 é um opcode inválido no hardware  
c) Porque o opcode 1111 foi reservado como escape para as instruções com menos endereços  
d) Porque as instruções de 3 endereços precisam de 5 bits de opcode

### Questão 535 [F]

A instrução que copia de um registrador para a memória é chamada tipicamente de:

a) LOAD  
b) MOVE  
c) JUMP  
d) STORE

### Questão 536 [M]

O padrão POSIX P1003.1 define:

a) Cerca de 60 chamadas de sistema essenciais  
b) O formato de binário  
c) A interface gráfica  
d) Os utilitários ls, cp e grep

### Questão 537 [M]

O padrão de 8 bits 1011 0110, interpretado em complemento de dois, vale:

a) -74  
b) -73  
c) -54  
d) 182

### Questão 538 [F]

Na instrução indexada `MOV R4, A(R2)`, com A = 161412 e R2 = 8, qual endereço é lido?

a) 161420  
b) 161412  
c) 161444  
d) 8

### Questão 539 [M] ★

Sobre os tipos de hipervisor:

a) Tipo 1 roda sobre um SO hospedeiro  
b) VirtualBox é tipo 1  
c) Tipo 1 roda direto no hardware (ex.: ESXi, Xen, Hyper-V); tipo 2 roda sobre um SO hospedeiro (ex.: VirtualBox)  
d) Não existe essa classificação

### Questão 540 [D] ★

Ao estender um valor de 8 bits em complemento de dois para 16 bits (extensão de sinal):

a) Preenchem-se os novos bits com 0  
b) Copia-se o bit de sinal para todos os novos bits à esquerda  
c) Desloca-se à esquerda 8 bits  
d) Preenchem-se com 1

### Questão 541 [M]

Alocação consecutiva é muito usada em:

a) Discos rígidos com arquivos que crescem  
b) Memória cache  
c) Pendrives em uso diário  
d) CD-ROMs, porque o tamanho dos arquivos é conhecido na gravação

### Questão 542 [M]

As chamadas POSIX correspondentes a DOWN e UP de semáforo são:

a) sem_wait() e sem_post()  
b) pthread_create() e pthread_join()  
c) open() e close()  
d) fork() e exec()

### Questão 543 [D] ★

Uma instrução de chamada de sistema (TRAP/SYSCALL/INT 0x80) se parece mais com:

a) Uma exceção provocada intencionalmente pelo programa (síncrona)  
b) Uma corrotina  
c) Uma NMI  
d) Uma interrupção de E/S

### Questão 544 [M]

Divisão em PF (32 bits): o expoente polarizado do dividendo é 124 e o do divisor é 120. Qual o expoente polarizado do quociente, antes da normalização?

a) 131  
b) 258  
c) 4  
d) 117

### Questão 545 [M]

Qual é um princípio de projeto limpo, segundo a aula de ortogonalidade?

a) Proibir o PC como operando  
b) Todos os registradores, inclusive FP, SP e PC, devem ser acessíveis pelos mesmos modos  
c) Usar o máximo de formatos diferentes  
d) Cada opcode deve ter seu próprio formato

### Questão 546 [M]

A ideia central da IA-64 é:

a) Passar trabalho do tempo de execução para o tempo de compilação  
b) Aumentar a complexidade do hardware de escalonamento  
c) Eliminar os registradores  
d) Usar instruções de 1 a 15 bytes

### Questão 547 [D]

Um semáforo começa em 0. Processos distintos executam, nesta ordem: up, up, down. Qual o estado final?

a) Semáforo = 2, 0 processo(s) bloqueado(s)  
b) Semáforo = 1, 1 processo(s) bloqueado(s)  
c) Semáforo = 3, 0 processo(s) bloqueado(s)  
d) Semáforo = 1, 0 processo(s) bloqueado(s)

### Questão 548 [M]

Uma aplicação típica de corrotinas é:

a) Simular processamento paralelo em uma única CPU  
b) Fazer DMA  
c) Tratar erros de paridade  
d) Traduzir endereços virtuais

### Questão 549 [D]

O padrão IEEE 754 de 32 bits 0x3F400000 representa o valor:

a) -0,75  
b) 0,75  
c) 1,5  
d) 0,375

### Questão 550 [M]

Para compilar o exemplo com pthreads e o exemplo com OpenMP, usa-se, respectivamente:

a) -g e -lpthread  
b) -fopenmp e -lpthread  
c) -lm e -O2  
d) -lpthread e -fopenmp

### Questão 551 [D]

O padrão IEEE 754 de 32 bits 0x42420000 representa o valor:

a) 97  
b) -48,5  
c) 24,25  
d) 48,5

### Questão 552 [D]

Na falha fatal da Figura 6.27, o sinal de despertar se perde porque:

a) O SO descarta todos os sinais  
b) O consumidor lê in e out, conclui que o buffer está vazio, mas antes de dormir o produtor coloca um item e manda resume() para um consumidor ainda acordado  
c) O produtor nunca manda resume()  
d) O buffer tem tamanho zero

### Questão 553 [F]

Qual a faixa de um inteiro com sinal de 20 bits em complemento de dois?

a) 0 a 1.048.575  
b) -524.288 a 524.287  
c) -1.048.576 a 1.048.575  
d) -524.287 a 524.287

### Questão 554 [D] ★

No assembly x86-64 do Hello World aparece `movq %rax, %rdi` antes de `call puts@PLT`. Isso acontece porque, na convenção System V AMD64 (Linux):

a) RDI é o ponteiro de pilha  
b) RDI recebe o valor retornado por puts  
c) O primeiro argumento inteiro/ponteiro é passado no registrador RDI  
d) RDI guarda o endereço de retorno

### Questão 555 [M]

Qual NÃO é vantagem da segmentação?

a) Proteção por tipo de segmento  
b) Eliminar a fragmentação externa  
c) Compartilhamento de bibliotecas  
d) Crescimento independente das estruturas

### Questão 556 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 4, 3, 5, 3, 6, 1, 3, 4, 4, 1, quantas faltas de página ocorrem com FIFO?

a) 8  
b) 9  
c) 6  
d) 7

### Questão 557 [D]

Some, em complemento de dois com 8 bits, 0111 0101 (117) + 1000 1100 (-116). Resultado (descartando o vai-um) e situação:

a) 0000 0010, sem overflow  
b) 0000 0001, com overflow  
c) 1110 1001, sem overflow  
d) 0000 0001, sem overflow

### Questão 558 [M]

Um exemplo de proteção por segmento:

a) Segmento de código somente execução; vetor de dados leitura/escrita e nunca execução  
b) Proteção só existe na paginação  
c) Todos os segmentos podem ser executados  
d) Dados são somente execução

### Questão 559 [D]

Um semáforo começa em 1. Processos distintos executam, nesta ordem: down, down, up. Qual o estado final?

a) Semáforo = 1, 0 processo(s) bloqueado(s)  
b) Semáforo = 0, 1 processo(s) bloqueado(s)  
c) Semáforo = 0, 0 processo(s) bloqueado(s)  
d) Semáforo = 2, 0 processo(s) bloqueado(s)

### Questão 560 [D]

Some, em complemento de dois com 8 bits, 0000 0100 (4) + 0101 0111 (87). Resultado (descartando o vai-um) e situação:

a) 0101 1011, com overflow  
b) 0101 1100, sem overflow  
c) 0101 1011, sem overflow  
d) 1010 1101, sem overflow

### Questão 561 [M]

O ARM do OMAP4430 usa:

a) Apenas segmentação  
b) Apenas paginação, com tabela de dois níveis  
c) Nenhuma memória virtual  
d) Segmentação com anéis

### Questão 562 [D]

Quantas operações de soma/subtração o algoritmo de Booth faz com o multiplicador 0011 1100 (8 bits, Q−1 inicial = 0)?

a) 4  
b) 1  
c) 2  
d) 3

### Questão 563 [M]

No produtor-consumidor com semáforos, antes de colocar um item o produtor executa:

a) apenas up(filled)  
b) up(available) e depois down(filled)  
c) down(available) e, depois de colocar, up(filled)  
d) down(filled) e depois up(available)

### Questão 564 [M]

Em 4 bits (C2), calcule M − S com M = 0111 (7) e S = 0100 (4), somando M ao complemento de dois de S:

a) 0011 (overflow)  
b) 1011  
c) 0011  
d) 0100

### Questão 565 [M]

Para acessar um segmento no Core i7, o programa carrega em um registrador de segmento:

a) Um endereço de 64 bits  
b) O número do quadro  
c) Um seletor de 16 bits  
d) Um descritor de 8 bytes

### Questão 566 [M]

A chamada unlink no UNIX:

a) Cria um link simbólico  
b) Remove uma entrada de diretório, decrementando o contador de links  
c) Muda permissões  
d) Fecha o arquivo

### Questão 567 [M] ★

O inteiro de 32 bits 0x12345678 é armazenado numa máquina little-endian a partir do endereço 100. Qual byte fica no endereço 100?

a) 0x78  
b) 0x56  
c) 0x12  
d) 0x87

### Questão 568 [M]

Qual NÃO é benefício da virtualização citado em aula?

a) Eliminar a necessidade de memória virtual  
b) Executar vários SOs ao mesmo tempo  
c) Consolidar várias VMs em um servidor  
d) Migrar VMs para equilibrar carga

### Questão 569 [M]

O padrão de 8 bits 1100 1000, interpretado em complemento de dois, vale:

a) -56  
b) 200  
c) -72  
d) -55

### Questão 570 [F]

Qual a faixa de um inteiro com sinal de 12 bits em complemento de dois?

a) -4.096 a 4.095  
b) -2.048 a 2.047  
c) -2.047 a 2.047  
d) 0 a 4.095

### Questão 571 [M]

Negar o zero em complemento de dois (8 bits):

a) Resulta em −0  
b) Resulta em 0; o vai-um que sai do bit 7 é ignorado  
c) Resulta em −1  
d) Gera overflow

### Questão 572 [M]

Banda da cache de instruções de 128 Gbit/s e tamanho médio de instrução de 16 bits. Qual o limite de instruções por segundo (t/r)?

a) 16 bilhões  
b) 2048 bilhões  
c) 8 bilhões  
d) 4 bilhões

### Questão 573 [M]

O equivalente Win32 de open/creat é:

a) OpenProcess  
b) CreateFile  
c) FindFirstFile  
d) SetFilePointer

### Questão 574 [F]

A instrução INC é a forma monádica de:

a) MUL por 2  
b) ADD com o operando constante 1  
c) SUB com 1  
d) AND com 1

### Questão 575 [D]

Por que o endereçamento indireto de registrador é importante para ponteiros e vetores?

a) Porque dispensa a memória  
b) Porque é o único modo que aceita constantes  
c) Permite referenciar memória sem pôr um endereço completo na instrução, e o endereço pode mudar entre execuções  
d) Porque é mais rápido que o modo de registrador

### Questão 576 [M]

Em 4 bits (C2), calcule M − S com M = 0101 (5) e S = 0000 (0), somando M ao complemento de dois de S:

a) 0101 (overflow)  
b) 0101  
c) 0011  
d) 0110

### Questão 577 [M]

Em uma carga especulativa da IA-64 que falha:

a) Não há exceção imediata: um bit 'envenenado' marca o registrador, e a exceção só ocorre se ele for usado  
b) O programa é abortado  
c) A exceção ocorre imediatamente  
d) O valor zero é carregado sem aviso

### Questão 578 [M]

Os bits de guarda servem para:

a) Detectar paridade  
b) Proteger a memória  
c) Guardar o sinal  
d) Preservar a precisão durante o alinhamento e as operações, antes do arredondamento

### Questão 579 [D] ★

A anomalia de Belady (mais quadros causarem MAIS faltas) pode ocorrer com:

a) Ótimo (OPT)  
b) FIFO  
c) LRU  
d) Nenhum algoritmo

### Questão 580 [F]

Na segmentação, um endereço é formado por:

a) Página e quadro  
b) Base e limite apenas  
c) Apenas um deslocamento  
d) Um par (número do segmento, deslocamento)

### Questão 581 [D]

Com 3 quadros inicialmente vazios e a sequência de referências 2, 6, 5, 1, 2, 5, 1, 6, 5, 3, quantas faltas de página ocorrem com FIFO?

a) 7  
b) 10  
c) 8  
d) 9

### Questão 582 [M]

A política padrão de arredondamento do IEEE 754 é:

a) Arredondar para +∞  
b) Truncar  
c) Arredondar para o mais próximo; em empate, para o par  
d) Arredondar para −∞

### Questão 583 [D]

Some, em complemento de dois com 8 bits, 1001 1001 (-103) + 1011 0100 (-76). Resultado (descartando o vai-um) e situação:

a) 0100 1101, com overflow  
b) 0100 1110, com overflow  
c) 0100 1101, sem overflow  
d) 1110 0101, sem overflow

### Questão 584 [D]

Por que semáforos funcionam para qualquer número de processos?

a) Porque o semáforo é um bit  
b) Porque cada processo tem seu semáforo  
c) Vários podem dormir no mesmo semáforo, organizados em fila, e cada UP libera apenas um  
d) Porque UP libera todos

### Questão 585 [M]

Qual a sequência histórica correta?

a) Windows NT → UNIX  
b) MINIX (1987, Tanenbaum) → Linux (1991, Torvalds)  
c) Linux → BSD → MINIX  
d) Linux (1987) → MINIX (1991)

### Questão 586 [M]

Em IEEE 754 de 32 bits, qual o campo de expoente (polarizado) de 1024?

a) 138 (10001010)  
b) 136 (10001000)  
c) 137 (10001001)  
d) 10 (00001010)

### Questão 587 [F]

No procedimento torres(n, i, j), a estaca auxiliar k é calculada como k = 6 − i − j. Para i = 1 e j = 2:

a) 3  
b) 1  
c) 2  
d) 4

### Questão 588 [M]

Qual o valor da expressão em RPN `5 3 − 4 6 − − 5 8 − 1 9 − × −`, avaliada com uma pilha?

a) -19  
b) -40  
c) 20  
d) -20

### Questão 589 [M]

No endereçamento indexado, o endereço efetivo é:

a) Registrador + deslocamento constante  
b) PC + deslocamento com sinal  
c) Somente o conteúdo do registrador  
d) Topo da pilha

### Questão 590 [M]

Surpreendentemente, entre os algoritmos de alocação de lacunas:

a) O pior ajuste é o melhor  
b) O primeiro ajuste tem melhor desempenho global que o melhor ajuste  
c) Os dois são idênticos  
d) O melhor ajuste é sempre superior

### Questão 591 [M]

Quantos modos básicos de endereçamento tem o AVR ATmega168, segundo a aula?

a) 2: registrador e imediato  
b) 14 modos clássicos  
c) 6, incluindo SIB  
d) 4: registrador, imediato, direto e indireto de registrador

### Questão 592 [F]

Um processo é:

a) Um programa em execução com todas as suas informações de estado  
b) Uma thread do kernel apenas  
c) Uma página de memória  
d) Um arquivo executável em disco

### Questão 593 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de -9,5?

a) 0xC1980000  
b) 0x81980000  
c) 0xC1180000  
d) 0x41180000

### Questão 594 [D]

Páginas de 8.192 bytes. Tabela de páginas (página→quadro): 0→5, 1→3, 2→4, 3→1, 4→0, 5→7, 6→6, 7→2. Qual o endereço físico do endereço virtual 26.373?

a) 9.989  
b) 26.373  
c) 24.577  
d) 8.192

### Questão 595 [M]

Um programa de 6.897 bytes usa páginas de 2.048 bytes. Quantas páginas ocupa e quanto é desperdiçado por fragmentação interna?

a) 3 páginas, 753 bytes  
b) 4 páginas, 1.295 bytes  
c) 4 páginas, 753 bytes  
d) 4 páginas, 0 bytes

### Questão 596 [M]

O que significa SIB no Core i7?

a) Scale, Index, Base  
b) Segment, Instruction, Byte  
c) Stack, Index, Bus  
d) Sign, Immediate, Base

### Questão 597 [M]

No projeto de máquina de 2 endereços da Figura 5.25 (estilo PDP-11/VAX), o pior caso (ADD mem ← mem com dois endereços diretos) gasta quantos ciclos de barramento?

a) 6  
b) 8  
c) 4  
d) 3

### Questão 598 [F]

Qual destas NÃO costuma gerar exceção?

a) Término de uma transferência de disco  
b) Violação de proteção  
c) Opcode indefinido  
d) Divisão por zero

### Questão 599 [D] ★

Em IEEE 754, 1,0/0,0 resulta em:

a) NaN  
b) 0  
c) +∞ (com sinalização de exceção de divisão por zero)  
d) Erro fatal obrigatório

### Questão 600 [M]

No projeto limpo de 3 endereços (Figura 5.24), o bit 23 igual a 1 indica que:

a) A instrução é um desvio  
b) O segundo operando é uma constante imediata de 13 bits  
c) A instrução ocupa duas palavras  
d) Há três registradores

### Questão 601 [M]

Na prática atual, o tamanho mínimo de página é:

a) 1 KB  
b) 4 KB  
c) 64 KB  
d) 512 bytes

### Questão 602 [D]

Qual a representação IEEE 754 de precisão simples (em hexadecimal) de 0,09375?

a) 0x3E400000  
b) 0x3DC00000  
c) 0xBDC00000  
d) 0x7E400000

### Questão 603 [D]

Qual lição de projeto sobre modos de endereçamento foi destacada no fim da Aula 03?

a) Poucos modos, claros e regulares, bastam; modos complexos reduzem instruções mas dificultam o paralelismo  
b) Registradores especiais não precisam ser acessíveis  
c) Quanto mais modos, melhor para o compilador  
d) Modos complexos facilitam o pipeline

### Questão 604 [M]

Com unidades de alocação de 4.096 bytes, um arquivo de 5.000 bytes desperdiça quantos bytes na última unidade?

a) 2.048  
b) 3.192  
c) 7.288  
d) 904

### Questão 605 [M]

No Core i7, com SIB: base = 1.564, índice = 4, escala = 2, deslocamento = 16. Qual o endereço efetivo?

a) 1.588  
b) 1.584  
c) 1.572  
d) 3.152

### Questão 606 [M]

No formato binary64 (double):

a) 11 bits de expoente, polarização 1023 e significando efetivo de 53 bits  
b) 11 bits de expoente e bias 1024  
c) 8 bits de expoente e bias 127  
d) 15 bits de expoente e bias 16383

### Questão 607 [D]

Páginas de 4.096 bytes. Tabela de páginas (página→quadro): 0→2, 1→7, 2→1, 3→6, 4→3, 5→5, 6→4, 7→0. Qual o endereço físico do endereço virtual 30.121?

a) 1.449  
b) 30.121  
c) 28.672  
d) 0

### Questão 608 [M]

Em ISAs sem formato de 3 endereços, a comparação com desvio é feita:

a) Por interrupção  
b) Por uma CMP que ajusta as flags, seguida de um desvio condicional que as testa  
c) Pelo SO  
d) Por uma única instrução de 3 endereços

### Questão 609 [M]

Endereço virtual de 16 bits e páginas de 1.024 bytes. Como o endereço se divide?

a) 7 bits de página e 9 de deslocamento (128 páginas)  
b) 6 bits de página e 10 de deslocamento (64 páginas)  
c) 10 bits de página e 6 de deslocamento (1.024 páginas)  
d) 8 bits de página e 8 de deslocamento (256 páginas)

### Questão 610 [M]

Com números de 3 bits, a comparação '100 > 011?' resulta em:

a) Falso sem sinal, verdadeiro com sinal  
b) Verdadeiro nos dois casos  
c) Verdadeiro sem sinal (4 > 3), falso com sinal (−4 < 3)  
d) Falso nos dois casos

### Questão 611 [F]

Como o número decimal 57 é codificado em BCD empacotado (1 byte)?

a) 0101 0111  
b) 0011 1111  
c) 0111 0101  
d) 0011 1001

---

## Gabarito rápido

**1**-a · **2**-c · **3**-b · **4**-a · **5**-d · **6**-d · **7**-a · **8**-a · **9**-c · **10**-a  
**11**-d · **12**-a · **13**-a · **14**-c · **15**-a · **16**-a · **17**-a · **18**-d · **19**-d · **20**-d  
**21**-d · **22**-a · **23**-d · **24**-d · **25**-b · **26**-a · **27**-d · **28**-c · **29**-b · **30**-a  
**31**-d · **32**-a · **33**-c · **34**-c · **35**-d · **36**-c · **37**-a · **38**-c · **39**-c · **40**-a  
**41**-b · **42**-b · **43**-d · **44**-d · **45**-d · **46**-a · **47**-d · **48**-b · **49**-a · **50**-c  
**51**-c · **52**-c · **53**-b · **54**-c · **55**-a · **56**-c · **57**-b · **58**-d · **59**-a · **60**-d  
**61**-b · **62**-d · **63**-d · **64**-d · **65**-c · **66**-a · **67**-c · **68**-a · **69**-b · **70**-d  
**71**-a · **72**-a · **73**-b · **74**-b · **75**-b · **76**-b · **77**-b · **78**-b · **79**-c · **80**-d  
**81**-d · **82**-c · **83**-d · **84**-a · **85**-a · **86**-b · **87**-b · **88**-c · **89**-a · **90**-d  
**91**-a · **92**-c · **93**-a · **94**-b · **95**-a · **96**-d · **97**-c · **98**-c · **99**-c · **100**-d  
**101**-d · **102**-d · **103**-c · **104**-a · **105**-d · **106**-a · **107**-c · **108**-d · **109**-b · **110**-b  
**111**-a · **112**-d · **113**-a · **114**-d · **115**-b · **116**-a · **117**-b · **118**-c · **119**-c · **120**-b  
**121**-d · **122**-b · **123**-d · **124**-d · **125**-d · **126**-c · **127**-b · **128**-b · **129**-a · **130**-d  
**131**-d · **132**-a · **133**-c · **134**-d · **135**-b · **136**-d · **137**-b · **138**-a · **139**-d · **140**-a  
**141**-a · **142**-c · **143**-a · **144**-d · **145**-c · **146**-b · **147**-c · **148**-a · **149**-a · **150**-a  
**151**-c · **152**-b · **153**-d · **154**-d · **155**-b · **156**-b · **157**-a · **158**-b · **159**-d · **160**-a  
**161**-a · **162**-c · **163**-c · **164**-b · **165**-b · **166**-d · **167**-a · **168**-b · **169**-c · **170**-b  
**171**-b · **172**-c · **173**-a · **174**-c · **175**-c · **176**-c · **177**-a · **178**-c · **179**-a · **180**-b  
**181**-b · **182**-c · **183**-c · **184**-b · **185**-d · **186**-b · **187**-c · **188**-b · **189**-b · **190**-b  
**191**-d · **192**-b · **193**-a · **194**-a · **195**-c · **196**-b · **197**-c · **198**-d · **199**-a · **200**-b  
**201**-a · **202**-d · **203**-c · **204**-d · **205**-a · **206**-b · **207**-d · **208**-b · **209**-b · **210**-c  
**211**-b · **212**-d · **213**-a · **214**-c · **215**-d · **216**-b · **217**-a · **218**-c · **219**-a · **220**-c  
**221**-d · **222**-b · **223**-d · **224**-d · **225**-b · **226**-c · **227**-b · **228**-b · **229**-d · **230**-c  
**231**-a · **232**-d · **233**-d · **234**-d · **235**-a · **236**-c · **237**-d · **238**-d · **239**-c · **240**-d  
**241**-d · **242**-b · **243**-d · **244**-a · **245**-d · **246**-c · **247**-b · **248**-c · **249**-b · **250**-b  
**251**-b · **252**-d · **253**-d · **254**-d · **255**-a · **256**-c · **257**-c · **258**-d · **259**-b · **260**-c  
**261**-d · **262**-a · **263**-a · **264**-b · **265**-c · **266**-c · **267**-c · **268**-a · **269**-d · **270**-b  
**271**-d · **272**-a · **273**-a · **274**-a · **275**-a · **276**-c · **277**-b · **278**-c · **279**-c · **280**-c  
**281**-d · **282**-c · **283**-b · **284**-b · **285**-d · **286**-d · **287**-d · **288**-b · **289**-c · **290**-b  
**291**-c · **292**-c · **293**-b · **294**-a · **295**-c · **296**-d · **297**-b · **298**-a · **299**-c · **300**-a  
**301**-b · **302**-b · **303**-a · **304**-c · **305**-c · **306**-c · **307**-d · **308**-c · **309**-a · **310**-c  
**311**-d · **312**-b · **313**-c · **314**-d · **315**-a · **316**-b · **317**-b · **318**-a · **319**-d · **320**-d  
**321**-d · **322**-d · **323**-c · **324**-a · **325**-b · **326**-d · **327**-d · **328**-d · **329**-d · **330**-a  
**331**-b · **332**-b · **333**-d · **334**-c · **335**-c · **336**-c · **337**-a · **338**-b · **339**-d · **340**-c  
**341**-b · **342**-d · **343**-d · **344**-b · **345**-c · **346**-b · **347**-d · **348**-a · **349**-b · **350**-c  
**351**-c · **352**-b · **353**-d · **354**-a · **355**-d · **356**-d · **357**-b · **358**-a · **359**-d · **360**-b  
**361**-c · **362**-a · **363**-d · **364**-a · **365**-b · **366**-b · **367**-c · **368**-d · **369**-b · **370**-a  
**371**-b · **372**-b · **373**-d · **374**-a · **375**-c · **376**-c · **377**-d · **378**-a · **379**-c · **380**-b  
**381**-d · **382**-d · **383**-d · **384**-c · **385**-d · **386**-a · **387**-c · **388**-a · **389**-a · **390**-a  
**391**-b · **392**-d · **393**-b · **394**-d · **395**-b · **396**-d · **397**-a · **398**-b · **399**-d · **400**-d  
**401**-b · **402**-b · **403**-d · **404**-a · **405**-a · **406**-d · **407**-b · **408**-d · **409**-c · **410**-a  
**411**-c · **412**-b · **413**-d · **414**-d · **415**-c · **416**-d · **417**-d · **418**-c · **419**-d · **420**-b  
**421**-d · **422**-c · **423**-a · **424**-c · **425**-c · **426**-c · **427**-c · **428**-d · **429**-c · **430**-b  
**431**-d · **432**-c · **433**-c · **434**-b · **435**-a · **436**-c · **437**-a · **438**-a · **439**-a · **440**-b  
**441**-a · **442**-d · **443**-c · **444**-d · **445**-b · **446**-d · **447**-b · **448**-b · **449**-a · **450**-c  
**451**-d · **452**-a · **453**-d · **454**-c · **455**-d · **456**-c · **457**-a · **458**-a · **459**-a · **460**-a  
**461**-c · **462**-c · **463**-a · **464**-b · **465**-b · **466**-d · **467**-b · **468**-d · **469**-a · **470**-a  
**471**-c · **472**-a · **473**-b · **474**-a · **475**-d · **476**-d · **477**-a · **478**-c · **479**-c · **480**-a  
**481**-c · **482**-b · **483**-a · **484**-c · **485**-a · **486**-c · **487**-b · **488**-a · **489**-d · **490**-d  
**491**-b · **492**-b · **493**-c · **494**-c · **495**-b · **496**-b · **497**-d · **498**-a · **499**-c · **500**-a  
**501**-c · **502**-b · **503**-c · **504**-b · **505**-c · **506**-d · **507**-c · **508**-b · **509**-d · **510**-c  
**511**-c · **512**-d · **513**-b · **514**-a · **515**-d · **516**-c · **517**-c · **518**-b · **519**-b · **520**-c  
**521**-c · **522**-a · **523**-c · **524**-d · **525**-b · **526**-b · **527**-b · **528**-d · **529**-c · **530**-b  
**531**-c · **532**-c · **533**-a · **534**-c · **535**-d · **536**-a · **537**-a · **538**-a · **539**-c · **540**-b  
**541**-d · **542**-a · **543**-a · **544**-a · **545**-b · **546**-a · **547**-d · **548**-a · **549**-b · **550**-d  
**551**-d · **552**-b · **553**-b · **554**-c · **555**-b · **556**-d · **557**-d · **558**-a · **559**-c · **560**-c  
**561**-b · **562**-c · **563**-c · **564**-c · **565**-c · **566**-b · **567**-a · **568**-a · **569**-a · **570**-b  
**571**-b · **572**-c · **573**-b · **574**-b · **575**-c · **576**-b · **577**-a · **578**-d · **579**-b · **580**-d  
**581**-c · **582**-c · **583**-a · **584**-c · **585**-b · **586**-c · **587**-a · **588**-d · **589**-a · **590**-b  
**591**-d · **592**-a · **593**-c · **594**-a · **595**-b · **596**-a · **597**-a · **598**-a · **599**-c · **600**-b  
**601**-b · **602**-b · **603**-a · **604**-b · **605**-a · **606**-a · **607**-a · **608**-b · **609**-b · **610**-c  
**611**-a

## Gabarito comentado

| Q | Resp. | Assunto | Comentário |
|---|---|---|---|
| 1 | **a** | Inteiros | [−2^4, 2^4 − 1]. |
| 2 | **c** | Ponto flutuante | O significando tem só 24 bits efetivos. |
| 3 | **b** | Tipos de instrução | Custo: roubo de ciclo, compensado pelo ganho. |
| 4 | **a** | Hanói/IA-64 | Figura 5.47. |
| 5 | **d** | Paginação | Simulando: LRU = 6 faltas (FIFO daria 7). As 3 primeiras páginas distintas sempre faltam. |
| 6 | **d** | Endereçamento | Slide 15 da Aula 03. |
| 7 | **a** | Ponto flutuante | A perda de precisão pode ser de fator 16. |
| 8 | **a** | Inteiros | +124 = 0111 1100. Inverte-se: 1000 0011. Soma-se 1: 1000 0100. |
| 9 | **c** | Inteiros | −S = 0000. -4 − (0) = -4. |
| 10 | **a** | Inteiros | Slide 15 da Aula 12. |
| 11 | **d** | Virtualização/E-S OSM | Cada entrada contém o número da unidade seguinte. |
| 12 | **a** | Virtualização/E-S OSM | Usa 1 unidade(s) = 32.768 bytes; 32.768 − 100 = 32.668. |
| 13 | **a** | Tipos de instrução | Deslocamento lógico: entram zeros e os bits que saem se perdem. Rotação: os bits que saem voltam pelo outro lado. Aritmético à direita: o bit de sinal é replicado. |
| 14 | **c** | Paginação | ⌈58.268/8.192⌉ = 8; 8 × 8.192 − 58.268 = 7.268. |
| 15 | **a** | Endereçamento | As variáveis/números mantêm a ordem; os operadores aparecem na ordem em que são executados: 3 7 + 9 1 − +. |
| 16 | **a** | Tipos de instrução | Slide 25 da Aula 04. |
| 17 | **a** | Paginação | A MMU pode estar no chip da CPU ou fora dele. |
| 18 | **d** | Tipos de dados e formatos | Simples = 32 bits (~7 dígitos); duplo = 64 (~15). |
| 19 | **d** | Endereçamento | Endereço = deslocamento (A) + conteúdo do registrador índice (R2). |
| 20 | **d** | Inteiros | Slide 3 da Aula 12. |
| 21 | **d** | Tipos de dados e formatos | Com uma única exceção, todos têm 8 bits. |
| 22 | **a** | Paralelismo/Semáforos | Java passou a usar synchronized, wait/notify e locks. |
| 23 | **d** | Hanói/IA-64 | ADD e SUB predicados: só um escreve. |
| 24 | **d** | Endereçamento | Equivale à infixa 4 − (6 + 4 + (3 + 5)) = -14. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 25 | **b** | Segmentação/Cache | Programa todo no nível lento; subconjunto no nível rápido. |
| 26 | **a** | Ponto flutuante | 3 → sinal 0, expoente polarizado 128 (10000000) = 1 + 127, fração 10000000000000000000000. Bits: 0 10000000 10000000000000000000000 = 0x40400000. |
| 27 | **d** | Tipos de dados e formatos | Slide 10: cadeias delimitadas por \0 (C) ou com campo de comprimento. |
| 28 | **c** | Inteiros | Há um negativo a mais que os positivos. |
| 29 | **b** | Ponto flutuante | Preenche o 'buraco' perto do zero (underflow gradual). |
| 30 | **a** | Paralelismo/Semáforos | Figura 6.25. |
| 31 | **d** | Inteiros | +18 = 0001 0010. Inverte-se: 1110 1101. Soma-se 1: 1110 1110. |
| 32 | **a** | Paginação | Não é implementável, só serve de referência. |
| 33 | **c** | Nível ISA | V = transbordo em complemento de dois. C é o vai-um. |
| 34 | **c** | Paralelismo/Semáforos | DOWN em 0 bloqueia; UP com processo esperando acorda um e mantém o valor; semáforos nunca ficam negativos. |
| 35 | **d** | Tipos de instrução | Equivale a MOVE 0, DST. |
| 36 | **c** | Endereçamento | Equivale à infixa 6 × 2 × 2 + (4 × 3 − 9 × 6) = -18. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 37 | **a** | Nível ISA | Alinhado = endereço múltiplo de 4. |
| 38 | **c** | Paginação | Slide 28 da Aula 07. |
| 39 | **c** | UNIX/Windows | Slide de divisão do mundo UNIX. |
| 40 | **a** | Tipos de dados e formatos | Cada dígito em 4 bits: 3 = 0011, 4 = 0100. Em binário puro, 34 = 0010 0010. |
| 41 | **b** | Inteiros | 1 + -5 = -4. Faixa de 4 bits: -8 a 7. Dentro da faixa → sem overflow. |
| 42 | **b** | Ponto flutuante | Risco: underflow de expoente. |
| 43 | **d** | Tipos de dados e formatos | Apenas o Core i7 tem prefixos. |
| 44 | **d** | Tipos de instrução | Slide 29 da Aula 04. |
| 45 | **d** | Endereçamento | EA = base + índice + deslocamento = 2000 + 12 + 4. |
| 46 | **a** | Virtualização/E-S OSM | Contém metadados e endereços dos blocos. |
| 47 | **d** | Inteiros | Conta-se cada transição 10 ou 01 no par (Q0, Q−1) ao percorrer os bits: 4. Uma soma/subtração por fronteira de bloco de 1s. |
| 48 | **b** | Tipos de dados e formatos | 2^32 palavras × 4 bytes = 16 GB. |
| 49 | **a** | Hanói/IA-64 | Um 'Pentium mais largo'. |
| 50 | **c** | Tipos de dados e formatos | Cada dígito em 4 bits: 2 = 0010, 2 = 0010. Em binário puro, 22 = 0001 0110. |
| 51 | **c** | Nível ISA | Alinhado = endereço múltiplo de 2. |
| 52 | **c** | Paginação | ⌈4.653/1.024⌉ = 5; 5 × 1.024 − 4.653 = 467. |
| 53 | **b** | Nível ISA | O carry auxiliar (do bit 3 para o 4) é usado pelas instruções de ajuste decimal (DAA etc.). |
| 54 | **c** | Ponto flutuante | 0 10000001 10000000000000000000000: sinal 0, expoente 129 − 127 = 2, significando 1,1 (binário). |
| 55 | **a** | Virtualização/E-S OSM | 1 bit por unidade: 1.048.576/8 = 131.072 bytes. |
| 56 | **c** | Inteiros | Booth dá diretamente o produto em complemento de dois de 2n bits: 3 × -5 = -15 = 1111 0001. Multiplicar os padrões como sem sinal daria 0010 0001, que está errado. |
| 57 | **b** | Tipos de dados e formatos | Figura 5.9(b). |
| 58 | **d** | Fluxo de controle | Slide 15 da Aula 05. |
| 59 | **a** | Endereçamento | Equivale à infixa 1 + 8 + (8 − 4) − (5 − 4) × (2 − 9) = 20. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 60 | **d** | Inteiros | 7 + 2 = 9. Faixa de 4 bits: -8 a 7. Fora da faixa: operandos de mesmo sinal e resultado com sinal oposto → overflow. |
| 61 | **b** | Endereçamento | PC + deslocamento com sinal. |
| 62 | **d** | Tipos de dados e formatos | Exemplo de dependência tecnológica (slide 20). |
| 63 | **d** | Virtualização/E-S OSM | 0 + 1.200 + 700 = 1.900. |
| 64 | **d** | Tipos de instrução | Deslocamento lógico: entram zeros e os bits que saem se perdem. Rotação: os bits que saem voltam pelo outro lado. Aritmético à direita: o bit de sinal é replicado. |
| 65 | **c** | Inteiros | 7 = (−3)(−2) + 1. |
| 66 | **a** | Fluxo de controle | Passo 5 das ações de software. |
| 67 | **c** | Segmentação/Cache | Slide 13 da Aula 08. |
| 68 | **a** | Inteiros | −S = 1010. -1 − (6) = -7. |
| 69 | **b** | UNIX/Windows | Slide 11 da Aula 11. |
| 70 | **d** | Paginação | Simulando: LRU = 6 faltas (FIFO daria 7). As 3 primeiras páginas distintas sempre faltam. |
| 71 | **a** | Inteiros | 6 + -8 = -2. Faixa de 4 bits: -8 a 7. Dentro da faixa → sem overflow. |
| 72 | **a** | Hanói/IA-64 | Tira trabalho do tempo de execução e passa para a compilação. |
| 73 | **b** | Fluxo de controle | Slides 25 e 26 da Aula 05. |
| 74 | **b** | Hanói/IA-64 | Convenção de chamada em C. |
| 75 | **b** | Virtualização/E-S OSM | Semelhante ao núcleo de um SO. |
| 76 | **b** | Ponto flutuante | Normalizado, o expoente verdadeiro é -5; somando a polarização 127, dá 122. |
| 77 | **b** | Virtualização/E-S OSM | Slide 11 da Aula 09. |
| 78 | **b** | Inteiros | Conta-se cada transição 10 ou 01 no par (Q0, Q−1) ao percorrer os bits: 2. Uma soma/subtração por fronteira de bloco de 1s. |
| 79 | **c** | Paginação | Slide 21 da Aula 07. |
| 80 | **d** | UNIX/Windows | Comparação final da Aula 11. |
| 81 | **d** | Endereçamento | Equivale à infixa (9 − 9 + 6) × (3 × 1 + 5 × 3) = 108. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 82 | **c** | Ponto flutuante | 0,1 em binário = 0,000110011001100… |
| 83 | **d** | Tipos de instrução | Slide 13 da Aula 04. |
| 84 | **a** | Virtualização/E-S OSM | 1 bit por unidade: 32.768/8 = 4.096 bytes. |
| 85 | **a** | Endereçamento | Equivale à infixa (4 + 8 − 6) × (7 × 4 − 3) = 150. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 86 | **b** | Paginação | Figura 6.6. |
| 87 | **b** | Fluxo de controle | Slide 21 da Aula 05. |
| 88 | **c** | Nível ISA | Alinhada = endereço múltiplo do tamanho (8). Só 24 é múltiplo de 8. |
| 89 | **a** | Paralelismo/Semáforos | 7 downs com sucesso; 3 times suspensos. |
| 90 | **d** | Paralelismo/Semáforos | Figura 6.24. |
| 91 | **a** | Hanói/IA-64 | 3 × 4 = 12 bytes. |
| 92 | **c** | Virtualização/E-S OSM | Slide 23 da Aula 09. |
| 93 | **a** | Tipos de instrução | Slide 09: zera com AND e insere com OR. |
| 94 | **b** | Virtualização/E-S OSM | Slide 9 da Aula 09. |
| 95 | **a** | Hanói/IA-64 | 2^10 − 1. |
| 96 | **d** | Fluxo de controle | Após cada instrução, o PC soma o tamanho da instrução. |
| 97 | **c** | Tipos de dados e formatos | 96 × 10^9 / 24 = 4 × 10^9. |
| 98 | **c** | Tipos de dados e formatos | 48 × 10^9 / 12 = 4 × 10^9. |
| 99 | **c** | Tipos de dados e formatos | O efeito de rede do software legado é o argumento clássico de aula. |
| 100 | **d** | Tipos de instrução | Em complemento de um, NEG ≡ NOT. |
| 101 | **d** | Ponto flutuante | Slide da Aula 13. |
| 102 | **d** | Nível ISA | Little-endian: o byte menos significativo no menor endereço. Big-endian: o mais significativo no menor endereço. |
| 103 | **c** | Segmentação/Cache | No modo 64 bits a segmentação ficou praticamente vestigial. |
| 104 | **a** | Inteiros | [−2^9, 2^9 − 1]. |
| 105 | **d** | Ponto flutuante | Existem dois zeros. |
| 106 | **a** | Tipos de instrução | 18n = 16n + 2n. |
| 107 | **c** | UNIX/Windows | Economiza seeks. |
| 108 | **d** | Tipos de dados e formatos | n bits com sinal: [−2^(n−1), 2^(n−1)−1]. |
| 109 | **b** | Endereçamento | As variáveis/números mantêm a ordem; os operadores aparecem na ordem em que são executados: 6 1 − 4 ×. |
| 110 | **b** | Fluxo de controle | 4 × 32 = 128. |
| 111 | **a** | Paginação | Slide 12 da Aula 07. |
| 112 | **d** | Inteiros | +117 = 0111 0101. Inverte-se: 1000 1010. Soma-se 1: 1000 1011. |
| 113 | **a** | Paralelismo/Semáforos | Figura 6.29. |
| 114 | **d** | Tipos de dados e formatos | X = R27:R26, Y = R29:R28, Z = R31:R30. |
| 115 | **b** | Paralelismo/Semáforos | No modelo independente o pai não tem alça sobre o filho. |
| 116 | **a** | Inteiros | −S = 1101. -5 − (3) = -8. |
| 117 | **b** | Tipos de dados e formatos | Não há soma mem+mem e o alinhamento não é exigido. |
| 118 | **c** | Tipos de dados e formatos | Slide 07 da Aula 02. |
| 119 | **c** | Paralelismo/Semáforos | Slide 19 da Aula 10. |
| 120 | **b** | Paginação | Least Recently Used. |
| 121 | **d** | Ponto flutuante | O produto tem o dobro do tamanho. |
| 122 | **b** | Hanói/IA-64 | Slide 5.8.3. |
| 123 | **d** | Inteiros | 12 = 4 × 3 + 0. Quociente em Q, resto em A. |
| 124 | **d** | Fluxo de controle | Slide 27 da Aula 05. |
| 125 | **d** | Endereçamento | As variáveis/números mantêm a ordem; os operadores aparecem na ordem em que são executados: 3 5 + 6 3 × −. |
| 126 | **c** | Tipos de instrução | Instruções de cadeia do x86. |
| 127 | **b** | Tipos de dados e formatos | Slide 22: por palavra, os endereços ficam menores, mas caracteres precisam ser extraídos. |
| 128 | **b** | Inteiros | Preserva o sinal do produto parcial. |
| 129 | **a** | Inteiros | +31 = 0001 1111. Inverte-se: 1110 0000. Soma-se 1: 1110 0001. |
| 130 | **d** | Inteiros | Peso do bit 7 = −128: −128 + 101 = -27. Sem sinal seria 229; em sinal-magnitude, -101. |
| 131 | **d** | Tipos de instrução | Toda rotação pode ser desfeita por outra rotação. |
| 132 | **a** | Ponto flutuante | 20 → sinal 0, expoente polarizado 131 (10000011) = 4 + 127, fração 01000000000000000000000. Bits: 0 10000011 01000000000000000000000 = 0x41A00000. |
| 133 | **c** | Ponto flutuante | 1 10000100 01000000000000000000000: sinal 1, expoente 132 − 127 = 5, significando 1,01 (binário). |
| 134 | **d** | Tipos de instrução | Comparação dos três conjuntos (slide 30). |
| 135 | **b** | Endereçamento | Indireto de registrador: soma M[R2] = 7 a R1 = 3. |
| 136 | **d** | Virtualização/E-S OSM | 1 bit por unidade: 131.072/8 = 16.384 bytes. |
| 137 | **b** | Tipos de dados e formatos | Slide 27 da Aula 02. |
| 138 | **a** | Inteiros | Conta-se cada transição 10 ou 01 no par (Q0, Q−1) ao percorrer os bits: 4. Uma soma/subtração por fronteira de bloco de 1s. |
| 139 | **d** | Tipos de instrução | Deslocamento lógico: entram zeros e os bits que saem se perdem. Rotação: os bits que saem voltam pelo outro lado. Aritmético à direita: o bit de sinal é replicado. |
| 140 | **a** | Ponto flutuante | Pode virar ±∞. |
| 141 | **a** | Paralelismo/Semáforos | Figura 6.28. |
| 142 | **c** | Paginação | Figura 6.1. |
| 143 | **a** | Paralelismo/Semáforos | 1 ns para ir e 1 ns para voltar (no vácuo; em cobre é ainda mais). |
| 144 | **d** | Tipos de instrução | Slide 26 da Aula 04. |
| 145 | **c** | Paginação | 10.000 páginas tocadas × tamanho da página. |
| 146 | **b** | Endereçamento | Por isso não existe indireção simples por EBP: uma das irregularidades. |
| 147 | **c** | Inteiros | 15 = 6 × 2 + 3. Quociente em Q, resto em A. |
| 148 | **a** | Ponto flutuante | 100 → sinal 0, expoente polarizado 133 (10000101) = 6 + 127, fração 10010000000000000000000. Bits: 0 10000101 10010000000000000000000 = 0x42C80000. |
| 149 | **a** | Ponto flutuante | -2,25 → sinal 1, expoente polarizado 128 (10000000) = 1 + 127, fração 00100000000000000000000. Bits: 1 10000000 00100000000000000000000 = 0xC0100000. |
| 150 | **a** | Endereçamento | Endereço = deslocamento (A) + conteúdo do registrador índice (R2). |
| 151 | **c** | Tipos de dados e formatos | 1 bit por bloco: 4096 bits / 8 = 512 bytes. |
| 152 | **b** | Tipos de instrução | Um nome melhor seria 'duplicação de dados'. |
| 153 | **d** | UNIX/Windows | Figura 6.39. |
| 154 | **d** | Segmentação/Cache | Figura 6.15: cada nível tem 1024 entradas. |
| 155 | **b** | Endereçamento | Na tabela, ARM não tem direto; base indexado só no ARM. |
| 156 | **b** | Ponto flutuante | 0 01111111 11000000000000000000000: sinal 0, expoente 127 − 127 = 0, significando 1,11 (binário). |
| 157 | **a** | Nível ISA | Little-endian: o byte menos significativo no menor endereço. Big-endian: o mais significativo no menor endereço. |
| 158 | **b** | Inteiros | O end-around carry é do complemento de um. |
| 159 | **d** | Fluxo de controle | Slide 9 da Aula 05. |
| 160 | **a** | Tipos de instrução | Slide 18 da Aula 04. |
| 161 | **a** | Tipos de dados e formatos | Slide 11: SP, PC, LV e CPP da Mic-x são ponteiros. |
| 162 | **c** | Tipos de dados e formatos | Campo COND: a instrução executa, mas só escreve o resultado se a condição for atendida. |
| 163 | **c** | Endereçamento | Figura 5.17: registrador, indireto, imediato e relativo ao PC. |
| 164 | **b** | UNIX/Windows | while ((n = read(...)) > 0). |
| 165 | **b** | Tipos de instrução | Slide 23 da Aula 04. |
| 166 | **d** | Ponto flutuante | Slide de alinhamento. |
| 167 | **a** | Paralelismo/Semáforos | Por isso é difícil vencer a barreira do nanossegundo. |
| 168 | **b** | Virtualização/E-S OSM | Slide 29 da Aula 09. |
| 169 | **c** | Hanói/IA-64 | 3 × 41 + 5 = 128. |
| 170 | **b** | Tipos de dados e formatos | Slide 20, lições da história (e o caso x86 × Itanium). |
| 171 | **b** | UNIX/Windows | VirtualAlloc, VirtualFree, VirtualQuery. |
| 172 | **c** | Tipos de dados e formatos | Slide 13: tratamento inteligente de tipos pequenos em cargas e armazenamentos. |
| 173 | **a** | Endereçamento | Ponteiros de 16 bits: 2^16 = 64 KB. |
| 174 | **c** | UNIX/Windows | Usada normalmente logo após fork no filho. |
| 175 | **c** | Paginação | Slide 25 da Aula 07. |
| 176 | **c** | Hanói/IA-64 | Equivale a MOV ESP, EBP; POP EBP. Depois vem RET. |
| 177 | **a** | Paginação | 7 páginas = 28.672; 28.672 − 26.000 = 2.672. |
| 178 | **c** | Tipos de dados e formatos | 64 × 10^9 / 16 = 4 × 10^9. |
| 179 | **a** | Paginação | Slide 14 da Aula 07. |
| 180 | **b** | Tipos de dados e formatos | ATmega não tem PF; o ARM deixa cadeias para o software. |
| 181 | **b** | Ponto flutuante | Pode ser aproximado para zero. |
| 182 | **c** | Endereçamento | As variáveis/números mantêm a ordem; os operadores aparecem na ordem em que são executados: 3 2 × 7 −. |
| 183 | **c** | Nível ISA | As três perguntas do slide são sobre compatibilidade (antecessora, SO antigo, aplicações). Energia não aparece. |
| 184 | **b** | Paginação | O bit sujo na MMU indica se houve escrita. |
| 185 | **d** | Ponto flutuante | 2^(k−1) − 1. |
| 186 | **b** | UNIX/Windows | Figura 6.44. |
| 187 | **c** | UNIX/Windows | Base do 2000, XP, Vista e 7. |
| 188 | **b** | Endereçamento | Variante 2: ponteiro (endereço do vetor) na instrução, índice no registrador. |
| 189 | **b** | Paginação | Simulando: LRU = 4 faltas (FIFO daria 5). As 3 primeiras páginas distintas sempre faltam. |
| 190 | **b** | UNIX/Windows | O pai e os 3 filhos chegam todos ao printf final. |
| 191 | **d** | Paralelismo/Semáforos | Cesto = semáforo; bolas = recursos; times = processos. |
| 192 | **b** | Paralelismo/Semáforos | Slide 23 da Aula 10. |
| 193 | **a** | Virtualização/E-S OSM | Mantida pelo hipervisor. |
| 194 | **a** | Paginação | 29.746 = página 7 × 4.096 + deslocamento 1074. A página 7 está no quadro 6: 6 × 4.096 + 1074 = 25.650. |
| 195 | **c** | Ponto flutuante | Desloca-se a vírgula uma casa à direita e decrementa-se o expoente. |
| 196 | **b** | Fluxo de controle | Interrupções são assíncronas e podem variar a cada execução. |
| 197 | **c** | Paralelismo/Semáforos | Semáforos são inteiros não negativos. |
| 198 | **d** | Hanói/IA-64 | O próprio procedimento decide quantos precisa. |
| 199 | **a** | Paginação | ⌈22.865/4.096⌉ = 6; 6 × 4.096 − 22.865 = 1.711. |
| 200 | **b** | Inteiros | 8 = 4 × 2 + 0. Quociente em Q, resto em A. |
| 201 | **a** | Paginação | 25.792 = página 6 × 4.096 + deslocamento 1216. A página 6 está no quadro 6: 6 × 4.096 + 1216 = 25.792. |
| 202 | **d** | UNIX/Windows | Hardware Abstraction Layer. |
| 203 | **c** | Fluxo de controle | 4 × 5 = 20. |
| 204 | **d** | Virtualização/E-S OSM | Figura 6.22(b). |
| 205 | **a** | Hanói/IA-64 | Custa área de chip, tempo e complexidade. |
| 206 | **b** | Paginação | Simulando: FIFO = 7 faltas (LRU daria 6). As 3 primeiras páginas distintas sempre faltam. |
| 207 | **d** | Paginação | Muda devagar, então dá para prever. |
| 208 | **b** | Nível ISA | Slide: o mais comum é 8 bits, mas já se usaram de 1 a 60 bits. |
| 209 | **b** | Inteiros | +16 = 0001 0000. Inverte-se: 1110 1111. Soma-se 1: 1111 0000. |
| 210 | **c** | Ponto flutuante | Slide da Aula 13. |
| 211 | **b** | Paginação | 45.494 = página 5 × 8.192 + deslocamento 4534. A página 5 está no quadro 3: 3 × 8.192 + 4534 = 29.110. |
| 212 | **d** | Hanói/IA-64 | PUSH EBP; MOV EBP, ESP. |
| 213 | **a** | Virtualização/E-S OSM | Pode retornar menos bytes que o pedido. |
| 214 | **c** | Tipos de instrução | AND tende a remover 1s, OR a inserir 1s, XOR é simétrico. |
| 215 | **d** | Ponto flutuante | Consequência do arredondamento. |
| 216 | **b** | Tipos de instrução | x XOR 1 inverte, x XOR 0 mantém. |
| 217 | **a** | Paginação | Simulando: LRU = 7 faltas (FIFO daria 6). As 3 primeiras páginas distintas sempre faltam. |
| 218 | **c** | Ponto flutuante | -0,1875 → sinal 1, expoente polarizado 124 (01111100) = -3 + 127, fração 10000000000000000000000. Bits: 1 01111100 10000000000000000000000 = 0xBE400000. |
| 219 | **a** | Endereçamento | EA = escala × índice + base + deslocamento = 1×19 + 3492 + 16 = 3527. |
| 220 | **c** | Fluxo de controle | Anatomia do quadro (slide 14). |
| 221 | **d** | Virtualização/E-S OSM | Slide 12 da Aula 09. |
| 222 | **b** | Inteiros | Peso do bit 7 = −128: −128 + 108 = -20. Sem sinal seria 236; em sinal-magnitude, -108. |
| 223 | **d** | Ponto flutuante | Slide da Aula 13. |
| 224 | **d** | UNIX/Windows | Figura 6.33. |
| 225 | **b** | Virtualização/E-S OSM | Figura 6.22. |
| 226 | **c** | Ponto flutuante | 0 10000010 10001000000000000000000: sinal 0, expoente 130 − 127 = 3, significando 1,10001 (binário). |
| 227 | **b** | Inteiros | 58 + 108 = 166. Faixa de 8 bits: -128 a 127. Fora da faixa: operandos de mesmo sinal e resultado com sinal oposto → overflow. |
| 228 | **b** | Paginação | 16.384 = 2^14 → 14 bits de deslocamento; sobram 18 para a página. |
| 229 | **d** | Tipos de instrução | Por isso existe o deslocamento aritmético (arrasta o sinal). |
| 230 | **c** | Ponto flutuante | 10,75 → sinal 0, expoente polarizado 130 (10000010) = 3 + 127, fração 01011000000000000000000. Bits: 0 10000010 01011000000000000000000 = 0x412C0000. |
| 231 | **a** | Tipos de dados e formatos | Trade-off central do slide 19. |
| 232 | **d** | Endereçamento | Figura 5.16: o operando está na própria instrução. |
| 233 | **d** | Paginação | Simulando: LRU = 6 faltas (FIFO daria 5). As 3 primeiras páginas distintas sempre faltam. |
| 234 | **d** | Paginação | 17.173 = página 4 × 4.096 + deslocamento 789. A página 4 está no quadro 5: 5 × 4.096 + 789 = 21.269. |
| 235 | **a** | Paginação | Slide 29 da Aula 07. |
| 236 | **c** | Tipos de instrução | Slide 26 da Aula 04. |
| 237 | **d** | Paginação | 4.096 = 2^12 → 12 bits de deslocamento; sobram 12 para a página. |
| 238 | **d** | Inteiros | Overflow pode ocorrer com ou sem carry: (−4)+(+4) tem carry e não tem overflow. |
| 239 | **c** | Hanói/IA-64 | 2^6 − 1. |
| 240 | **d** | Hanói/IA-64 | Slide 5.8.5. |
| 241 | **d** | Ponto flutuante | (136) − (123) + 127 = 140. |
| 242 | **b** | Segmentação/Cache | Com tabela de dois níveis. |
| 243 | **d** | Virtualização/E-S OSM | No UNIX, lseek reposiciona. |
| 244 | **a** | Tipos de instrução | Piada clássica do Tanenbaum repetida no slide 28. |
| 245 | **d** | UNIX/Windows | Berkeley também adicionou memória virtual para o VAX. |
| 246 | **c** | Fluxo de controle | Figura 5.43. |
| 247 | **b** | Fluxo de controle | Slide 28 da Aula 05. |
| 248 | **c** | UNIX/Windows | Fiel à filosofia de núcleo pequeno. |
| 249 | **b** | Inteiros | Conta-se cada transição 10 ou 01 no par (Q0, Q−1) ao percorrer os bits: 8. Uma soma/subtração por fronteira de bloco de 1s. |
| 250 | **b** | Fluxo de controle | Passo 3 do slide 25. |
| 251 | **b** | Segmentação/Cache | Estratégia do MULTICS. |
| 252 | **d** | Segmentação/Cache | Slide 12 da Aula 08. |
| 253 | **d** | Paginação | Depende só do número de bits do endereço: 2^16. |
| 254 | **d** | Segmentação/Cache | Move os segmentos para o início da memória. |
| 255 | **a** | Segmentação/Cache | Slide 23 da Aula 08. |
| 256 | **c** | Ponto flutuante | (119) + (117) − 127 = 109 (verdadeiro: -8 + -10 = -18). |
| 257 | **c** | Inteiros | E sinal(Q) = sinal(D) × sinal(V), com \|R\| < \|V\|. |
| 258 | **d** | Endereçamento | 1024 × 4 = 4096 bytes. |
| 259 | **b** | Paralelismo/Semáforos | Em multiprocessadores precisa de TSL, CAS ou spinlocks. |
| 260 | **c** | Ponto flutuante | Slide de políticas. |
| 261 | **d** | Inteiros | Meio de um bloco de 0s ou de 1s. |
| 262 | **a** | Paginação | 762 = página 0 × 4.096 + deslocamento 762. A página 0 está no quadro 7: 7 × 4.096 + 762 = 29.434. |
| 263 | **a** | Ponto flutuante | 0,15625 → sinal 0, expoente polarizado 124 (01111100) = -3 + 127, fração 01000000000000000000000. Bits: 0 01111100 01000000000000000000000 = 0x3E200000. |
| 264 | **b** | Endereçamento | Slide 6 da Aula 03. |
| 265 | **c** | Nível ISA | Slide 11: único espaço linear de 2^32 ou 2^64. |
| 266 | **c** | Nível ISA | Little-endian: o byte menos significativo no menor endereço. Big-endian: o mais significativo no menor endereço. |
| 267 | **c** | Ponto flutuante | Operações inválidas geram NaN. |
| 268 | **a** | Nível ISA | Otimização clássica do GCC. puts já acrescenta o \n. |
| 269 | **d** | Inteiros | Por isso o resultado fica em A (alta) e Q (baixa). |
| 270 | **b** | Paralelismo/Semáforos | Estado = PC, PSW, SP e registradores. |
| 271 | **d** | Segmentação/Cache | Slide 18 da Aula 08. |
| 272 | **a** | Ponto flutuante | Os padrões 0 e 255 são reservados. |
| 273 | **a** | UNIX/Windows | Normalmente uma thread por núcleo. |
| 274 | **a** | Endereçamento | Foi justamente ideia de von Neumann; hoje é considerada prática ruim. |
| 275 | **a** | Inteiros | −7 = (−3)(2) + (−1). |
| 276 | **c** | Ponto flutuante | 0 01111101 01000000000000000000000: sinal 0, expoente 125 − 127 = -2, significando 1,01 (binário). |
| 277 | **b** | Ponto flutuante | Slide da Aula 13. |
| 278 | **c** | Nível ISA | Alinhado = endereço múltiplo de 8. |
| 279 | **c** | Fluxo de controle | Slide 5 da Aula 05. |
| 280 | **c** | Hanói/IA-64 | Se o grupo violar as regras, o comportamento é indefinido. |
| 281 | **d** | Virtualização/E-S OSM | Offline exige intervenção (inserir fita, CD, pendrive). |
| 282 | **c** | Inteiros | Slide 31 da Aula 12. |
| 283 | **b** | Inteiros | Slide 26 da Aula 12. |
| 284 | **b** | Tipos de instrução | Slide 14 da Aula 04. |
| 285 | **d** | Inteiros | 30 = 32 − 2: uma subtração e uma soma. |
| 286 | **d** | Inteiros | Ex.: 00011110 = 2^5 − 2^1. |
| 287 | **d** | Ponto flutuante | -12,5 → sinal 1, expoente polarizado 130 (10000010) = 3 + 127, fração 10010000000000000000000. Bits: 1 10000010 10010000000000000000000 = 0xC1480000. |
| 288 | **b** | Ponto flutuante | 2^(4−1) − 1 = 7. |
| 289 | **c** | Nível ISA | Little-endian: o byte menos significativo no menor endereço. Big-endian: o mais significativo no menor endereço. |
| 290 | **b** | Segmentação/Cache | Slide 8 da Aula 08. |
| 291 | **c** | Inteiros | Fim de um bloco de 1s. |
| 292 | **c** | Hanói/IA-64 | then e else viram uma sequência só, com predicados diferentes. |
| 293 | **b** | Fluxo de controle | Slide 4 da Aula 05. |
| 294 | **a** | Segmentação/Cache | Slide 4 da Aula 08. |
| 295 | **c** | UNIX/Windows | execve substitui a imagem; wait espera. |
| 296 | **d** | Inteiros | -1 + -8 = -9. Faixa de 4 bits: -8 a 7. Fora da faixa: operandos de mesmo sinal e resultado com sinal oposto → overflow. |
| 297 | **b** | Inteiros | +79 = 0100 1111. Inverte-se: 1011 0000. Soma-se 1: 1011 0001. |
| 298 | **a** | Ponto flutuante | (136) − (118) + 127 = 145. |
| 299 | **c** | Ponto flutuante | O ganho é faixa, não quantidade. |
| 300 | **a** | Tipos de instrução | O FORTRAN antes de 1977 tinha esse problema. |
| 301 | **b** | Inteiros | Exemplo 7 ÷ 3: Q = 0010, A = 0001. |
| 302 | **b** | UNIX/Windows | Figura 6.43. |
| 303 | **a** | Segmentação/Cache | Motiva a segmentação. |
| 304 | **c** | Inteiros | −S = 1101. 6 − (3) = 3. |
| 305 | **c** | Nível ISA | Slide 2 da Aula 01: o nível ISA é a interface entre compiladores e hardware. |
| 306 | **c** | Hanói/IA-64 | As duas primeiras palavras são ligação (retorno e EBP salvo). |
| 307 | **d** | Inteiros | [−2^23, 2^23 − 1]. |
| 308 | **c** | Endereçamento | Equivale à infixa 9 × (6 × 8) − (9 + 3 − 9 × 7) = 483. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 309 | **a** | Virtualização/E-S OSM | Slide 26 da Aula 09. |
| 310 | **c** | Nível ISA | Little-endian: o byte menos significativo no menor endereço. Big-endian: o mais significativo no menor endereço. |
| 311 | **d** | Nível ISA | Little-endian: o byte menos significativo no menor endereço. Big-endian: o mais significativo no menor endereço. |
| 312 | **b** | Endereçamento | Figura 5.26: R/M = 100 → SIB. Por isso não há deslocamento relativo simples a ESP. |
| 313 | **c** | Ponto flutuante | 0,625 → sinal 0, expoente polarizado 126 (01111110) = -1 + 127, fração 01000000000000000000000. Bits: 0 01111110 01000000000000000000000 = 0x3F200000. |
| 314 | **d** | Paginação | 512 = 2^9 → 9 bits de deslocamento; sobram 11 para a página. |
| 315 | **a** | Inteiros | +113 = 0111 0001. Inverte-se: 1000 1110. Soma-se 1: 1000 1111. |
| 316 | **b** | Inteiros | Booth dá diretamente o produto em complemento de dois de 2n bits: 4 × 5 = 20 = 0001 0100. Multiplicar os padrões como sem sinal daria 0001 0100, que está errado. |
| 317 | **b** | Segmentação/Cache | Figura 6.14. |
| 318 | **a** | Inteiros | Peso do bit 7 = −128: −128 + 74 = -54. Sem sinal seria 202; em sinal-magnitude, -74. |
| 319 | **d** | Tipos de dados e formatos | Cada prefixo de escape (1110 e 1111) libera 16 opcodes de 8 bits: 2 × 16 = 32. |
| 320 | **d** | Fluxo de controle | O epílogo faz o inverso. No Core i7: ENTER e LEAVE. |
| 321 | **d** | Inteiros | Ex.: 1011 × 1101 sem sinal dá 143, que em C2 seria −113, e não +15. |
| 322 | **d** | UNIX/Windows | Octal: dono lê/escreve, grupo e outros só leem. |
| 323 | **c** | Fluxo de controle | 4 × 8 = 32. |
| 324 | **a** | Inteiros | -6 + -5 = -11. Faixa de 4 bits: -8 a 7. Fora da faixa: operandos de mesmo sinal e resultado com sinal oposto → overflow. |
| 325 | **b** | Paginação | ⌈7.841/1.024⌉ = 8; 8 × 1.024 − 7.841 = 351. |
| 326 | **d** | Ponto flutuante | 1 → sinal 0, expoente polarizado 127 (01111111) = 0 + 127, fração 00000000000000000000000. Bits: 0 01111111 00000000000000000000000 = 0x3F800000. |
| 327 | **d** | Paralelismo/Semáforos | Figura 6.25. |
| 328 | **d** | Ponto flutuante | O bit implícito não precisa ser armazenado. |
| 329 | **d** | Endereçamento | EA = escala × índice + base + deslocamento = 1×9 + 2336 + 12 = 2357. |
| 330 | **a** | Paralelismo/Semáforos | Liga-se à Figura 6.24. |
| 331 | **b** | Tipos de instrução | 10n = 8n + 2n. (16n − 2n = 14n.) |
| 332 | **b** | Inteiros | Peso do bit 7 = −128: −128 + 80 = -48. Sem sinal seria 208; em sinal-magnitude, -80. |
| 333 | **d** | Virtualização/E-S OSM | Slide 8 da Aula 09. |
| 334 | **c** | Inteiros | Os demais bits têm peso positivo 2^i. |
| 335 | **c** | Paginação | ⌈29.074/4.096⌉ = 8; 8 × 4.096 − 29.074 = 3.694. |
| 336 | **c** | Endereçamento | As variáveis/números mantêm a ordem; os operadores aparecem na ordem em que são executados: 6 4 − 8 9 × −. |
| 337 | **a** | Paralelismo/Semáforos | DOWN em 0 bloqueia; UP com processo esperando acorda um e mantém o valor; semáforos nunca ficam negativos. |
| 338 | **b** | Nível ISA | Alinhado = endereço múltiplo de 16. |
| 339 | **d** | Ponto flutuante | (134) + (119) − 127 = 126 (verdadeiro: 7 + -8 = -1). |
| 340 | **c** | Paginação | Figura 6.3. |
| 341 | **b** | Paralelismo/Semáforos | Precisa-se de um contador atômico: o semáforo. |
| 342 | **d** | Ponto flutuante | E_res = Ex + Ey − bias. |
| 343 | **d** | Paginação | Páginas grandes aproveitam melhor o disco e têm tabelas menores. |
| 344 | **b** | Ponto flutuante | 1 10000001 11000000000000000000000: sinal 1, expoente 129 − 127 = 2, significando 1,11 (binário). |
| 345 | **c** | Ponto flutuante | Significando efetivo = 24 bits com o bit implícito. |
| 346 | **b** | Inteiros | Booth dá diretamente o produto em complemento de dois de 2n bits: 3 × -5 = -15 = 1111 0001. Multiplicar os padrões como sem sinal daria 0010 0001, que está errado. |
| 347 | **d** | Fluxo de controle | Uma palavra entra e uma sai: o SP não muda. |
| 348 | **a** | Virtualização/E-S OSM | Slide 10 da Aula 09. |
| 349 | **b** | Inteiros | 7 + 6 = 13. Faixa de 4 bits: -8 a 7. Fora da faixa: operandos de mesmo sinal e resultado com sinal oposto → overflow. |
| 350 | **c** | Tipos de dados e formatos | Slide 06: sem sinal para endereços, contadores, tamanhos. |
| 351 | **c** | Inteiros | +85 = 0101 0101. Inverte-se: 1010 1010. Soma-se 1: 1010 1011. |
| 352 | **b** | Virtualização/E-S OSM | Slide 8 da Aula 09. |
| 353 | **d** | Paginação | Simulando: FIFO = 5 faltas (LRU daria 6). As 3 primeiras páginas distintas sempre faltam. |
| 354 | **a** | Tipos de dados e formatos | Figura 5.9(c): o destino também é origem. |
| 355 | **d** | Ponto flutuante | Normalizado, o expoente verdadeiro é 3; somando a polarização 127, dá 130. |
| 356 | **d** | Nível ISA | I e II são os dois critérios do slide. III contraria a ideia de regularidade. |
| 357 | **b** | Paginação | Ex.: ler dados de um arquivo. |
| 358 | **a** | Endereçamento | MOD = 11: dois registradores. |
| 359 | **d** | Inteiros | Peso do bit 7 = −128: −128 + 94 = -34. Sem sinal seria 222; em sinal-magnitude, -94. |
| 360 | **b** | UNIX/Windows | Figura 6.35. |
| 361 | **c** | Endereçamento | As variáveis/números mantêm a ordem; os operadores aparecem na ordem em que são executados: 4 3 − 8 +. |
| 362 | **a** | Hanói/IA-64 | 2^5 − 1. |
| 363 | **d** | Paginação | Slide 21 da Aula 07. |
| 364 | **a** | Nível ISA | Harvard = memórias/espaços separados para código e dados. O AVR guarda o programa na flash e os dados na SRAM. |
| 365 | **b** | Ponto flutuante | Normalizado, o expoente verdadeiro é -1; somando a polarização 127, dá 126. |
| 366 | **b** | Tipos de instrução | Slide 20 da Aula 04. |
| 367 | **c** | Hanói/IA-64 | Comentário clássico sobre o 'Itanic' e o sucesso do AMD64. |
| 368 | **d** | Paginação | 3.617 = página 1 × 2.048 + deslocamento 1569. A página 1 está no quadro 1: 1 × 2.048 + 1569 = 3.617. |
| 369 | **b** | Ponto flutuante | A ordem dos padrões é a mesma dos inteiros sem sinal. |
| 370 | **a** | Inteiros | [−2^5, 2^5 − 1]. |
| 371 | **b** | Ponto flutuante | A base é implícita. |
| 372 | **b** | Inteiros | Peso do bit 7 = −128: −128 + 99 = -29. Sem sinal seria 227; em sinal-magnitude, -99. |
| 373 | **d** | Tipos de instrução | Deslocamento lógico: entram zeros e os bits que saem se perdem. Rotação: os bits que saem voltam pelo outro lado. Aritmético à direita: o bit de sinal é replicado. |
| 374 | **a** | Endereçamento | EA = escala × índice + base + deslocamento = 4×9 + 2884 + 12 = 2932. |
| 375 | **c** | Segmentação/Cache | Slide 16 da Aula 08. |
| 376 | **c** | Ponto flutuante | Fração ≠ 0 com expoente todo 1 = NaN. |
| 377 | **d** | Endereçamento | Observação da Figura 5.22. |
| 378 | **a** | Hanói/IA-64 | Analogia dos epiciclos antes de Copérnico. |
| 379 | **c** | Paginação | Figura 6.4. |
| 380 | **b** | UNIX/Windows | Cada fork duplica todos os processos: 2^2. |
| 381 | **d** | UNIX/Windows | Primeira versão em assembly do PDP-7. |
| 382 | **d** | Inteiros | Se A ≥ 0, Q0 = 1. |
| 383 | **d** | Ponto flutuante | Mesmo número de padrões de bits, espalhados em escala logarítmica. |
| 384 | **c** | Tipos de dados e formatos | Instrução sem endereço = máquina de pilha (ex.: IADD da IJVM). |
| 385 | **d** | Tipos de instrução | Muito usada também para aritmética rápida (ex.: x*5 = x + 4x). |
| 386 | **a** | Paginação | 2^20 entradas × 4 B = 4 MB. Por isso se usam tabelas de dois níveis. |
| 387 | **c** | UNIX/Windows | Sem join, o main poderia terminar antes. |
| 388 | **a** | UNIX/Windows | Por isso threads precisam de mutex. |
| 389 | **a** | Inteiros | +68 = 0100 0100. Inverte-se: 1011 1011. Soma-se 1: 1011 1100. |
| 390 | **a** | Ponto flutuante | Dão os limites superior e inferior garantidos. |
| 391 | **b** | Tipos de dados e formatos | 32 × 10^9 / 32 = 1 × 10^9. |
| 392 | **d** | Ponto flutuante | -1,5 → sinal 1, expoente polarizado 127 (01111111) = 0 + 127, fração 10000000000000000000000. Bits: 1 01111111 10000000000000000000000 = 0xBFC00000. |
| 393 | **b** | Paginação | 800 = página 0 × 2.048 + deslocamento 800. A página 0 está no quadro 6: 6 × 2.048 + 800 = 13.088. |
| 394 | **d** | Endereçamento | Endereço = deslocamento (A) + conteúdo do registrador índice (R2). |
| 395 | **b** | UNIX/Windows | Slide 11 da Aula 11. |
| 396 | **d** | Paginação | Slide 20 da Aula 07. |
| 397 | **a** | UNIX/Windows | Cada fork duplica todos os processos existentes: 2^3. |
| 398 | **b** | Ponto flutuante | 10,110 → 1,0110 × 2^(E+1). |
| 399 | **d** | Segmentação/Cache | É o contrário: MV usa bits de ordem alta; cache, de ordem baixa. |
| 400 | **d** | Ponto flutuante | (131) + (135) − 127 = 139 (verdadeiro: 4 + 8 = 12). |
| 401 | **b** | Inteiros | Início de um bloco de 1s (lendo da direita). |
| 402 | **b** | Paginação | Slide 3 da Aula 07. |
| 403 | **d** | Inteiros | Conta-se cada transição 10 ou 01 no par (Q0, Q−1) ao percorrer os bits: 2. Uma soma/subtração por fronteira de bloco de 1s. |
| 404 | **a** | Tipos de dados e formatos | Slide 10: bits não são endereçáveis individualmente. |
| 405 | **a** | Paginação | 18.905 = página 2 × 8.192 + deslocamento 2521. A página 2 está no quadro 2: 2 × 8.192 + 2521 = 18.905. |
| 406 | **d** | Virtualização/E-S OSM | Slide 21 da Aula 09. |
| 407 | **b** | Tipos de instrução | Deslocamento lógico: entram zeros e os bits que saem se perdem. Rotação: os bits que saem voltam pelo outro lado. Aritmético à direita: o bit de sinal é replicado. |
| 408 | **d** | Paralelismo/Semáforos | Slide 6 da Aula 10. |
| 409 | **c** | Segmentação/Cache | Evita o flush da TLB. |
| 410 | **a** | Paralelismo/Semáforos | Slide 28 da Aula 10. |
| 411 | **c** | Nível ISA | Little-endian: o byte menos significativo no menor endereço. Big-endian: o mais significativo no menor endereço. |
| 412 | **b** | Paginação | Microcontrolador de sistemas embutidos. |
| 413 | **d** | UNIX/Windows | Detalhe clássico de aula prática. |
| 414 | **d** | Paginação | 4 KB = 2^12. |
| 415 | **c** | Endereçamento | Equivale à infixa (7 + 9 + (9 + 4)) × (8 × 3 − (6 − 7)) = 725. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 416 | **d** | Fluxo de controle | Base do escalonamento preemptivo. |
| 417 | **d** | Ponto flutuante | 1 01111110 00000000000000000000000: sinal 1, expoente 126 − 127 = -1, significando 1,0 (binário). |
| 418 | **c** | Tipos de dados e formatos | Cada dígito em 4 bits: 2 = 0010, 8 = 1000. Em binário puro, 28 = 0001 1100. |
| 419 | **d** | Hanói/IA-64 | Slide da Aula 06. |
| 420 | **b** | Hanói/IA-64 | No ARM, os parâmetros vão em r0, r1, r2. |
| 421 | **d** | Paginação | 528 = página 0 × 2.048 + deslocamento 528. A página 0 está no quadro 0: 0 × 2.048 + 528 = 528. |
| 422 | **c** | Inteiros | Booth dá diretamente o produto em complemento de dois de 2n bits: -7 × -4 = 28 = 0001 1100. Multiplicar os padrões como sem sinal daria 0110 1100, que está errado. |
| 423 | **a** | Inteiros | 76 + 127 = 203. Faixa de 8 bits: -128 a 127. Fora da faixa: operandos de mesmo sinal e resultado com sinal oposto → overflow. |
| 424 | **c** | Fluxo de controle | 4 × 3 = 12. |
| 425 | **c** | Segmentação/Cache | Suporta 4 KB, 64 KB, 1 MB e 16 MB. |
| 426 | **c** | Paralelismo/Semáforos | O exemplo dos dois processos dormindo para sempre é um impasse. |
| 427 | **c** | Ponto flutuante | Normalizado, o expoente verdadeiro é 1; somando a polarização 127, dá 128. |
| 428 | **d** | Fluxo de controle | Relação simétrica × hierárquica. |
| 429 | **c** | Virtualização/E-S OSM | UNIX usa lista de endereços de blocos. |
| 430 | **b** | UNIX/Windows | Fácil adicionar novas shells. |
| 431 | **d** | Inteiros | Em sinal-magnitude bastaria inverter o bit de sinal. |
| 432 | **c** | Endereçamento | Registradores são rápidos e os endereços deles são curtos. |
| 433 | **c** | Tipos de instrução | Slide 07 da Aula 04. |
| 434 | **b** | Paginação | Fotheringham, 1961. |
| 435 | **a** | Ponto flutuante | (131) + (117) − 127 = 121 (verdadeiro: 4 + -10 = -6). |
| 436 | **c** | Paginação | Simulando: LRU = 6 faltas (FIFO daria 7). As 3 primeiras páginas distintas sempre faltam. |
| 437 | **a** | Hanói/IA-64 | Último slide da Aula 06. |
| 438 | **a** | Endereçamento | EA = escala × índice + base + deslocamento = 8×12 + 1908 + 12 = 2016. |
| 439 | **a** | Virtualização/E-S OSM | Slide 14 da Aula 09. |
| 440 | **b** | Endereçamento | A ordem das variáveis é a mesma; só a dos operadores muda (Figura 5.22). |
| 441 | **a** | Paginação | 104 = página 0 × 2.048 + deslocamento 104. A página 0 está no quadro 6: 6 × 2.048 + 104 = 12.392. |
| 442 | **d** | Inteiros | 12 = 6 × 2 + 0. Quociente em Q, resto em A. |
| 443 | **c** | Inteiros | Peso do bit 7 = −128: −128 + 100 = -28. Sem sinal seria 228; em sinal-magnitude, -100. |
| 444 | **d** | Ponto flutuante | 5,5 → sinal 0, expoente polarizado 129 (10000001) = 2 + 127, fração 01100000000000000000000. Bits: 0 10000001 01100000000000000000000 = 0x40B00000. |
| 445 | **b** | Ponto flutuante | Os dígitos perdidos têm significado relativamente pequeno. |
| 446 | **d** | Endereçamento | As variáveis/números mantêm a ordem; os operadores aparecem na ordem em que são executados: 6 7 − 9 ×. |
| 447 | **b** | Paginação | Simulando: FIFO = 5 faltas (LRU daria 6). As 3 primeiras páginas distintas sempre faltam. |
| 448 | **b** | Nível ISA | Slide 12: duas categorias, uso especial (PC, SP, PSW...) e uso geral. |
| 449 | **a** | Inteiros | +43 = 0010 1011. Inverte-se: 1101 0100. Soma-se 1: 1101 0101. |
| 450 | **c** | Virtualização/E-S OSM | Slide 26 da Aula 09. |
| 451 | **d** | Hanói/IA-64 | torres(3) chama torres(2), torres(1) e torres(2), e cada torres(2) chama 3 torres(1): 1 + 3 + 6 = 10. São 7 movimentos impressos. |
| 452 | **a** | UNIX/Windows | Slide 13 da Aula 11. |
| 453 | **d** | Inteiros | 123 + 75 = 198. Faixa de 8 bits: -128 a 127. Fora da faixa: operandos de mesmo sinal e resultado com sinal oposto → overflow. |
| 454 | **c** | Hanói/IA-64 | Slide 5.8.3. |
| 455 | **d** | Paginação | Slide 7 da Aula 07. |
| 456 | **c** | Paralelismo/Semáforos | down antes da região crítica, up depois. |
| 457 | **a** | Tipos de instrução | Slide 08 da Aula 04. |
| 458 | **a** | Inteiros | -14 + -62 = -76. Faixa de 8 bits: -128 a 127. Dentro da faixa → sem overflow. |
| 459 | **a** | Inteiros | Subtrair é o anti-horário. |
| 460 | **a** | Paralelismo/Semáforos | DOWN em 0 bloqueia; UP com processo esperando acorda um e mantém o valor; semáforos nunca ficam negativos. |
| 461 | **c** | Virtualização/E-S OSM | Figura 6.20. |
| 462 | **c** | Paralelismo/Semáforos | Garantia do SO, não do programador. |
| 463 | **a** | Ponto flutuante | O espaçamento cresce com o expoente. |
| 464 | **b** | Tipos de dados e formatos | 15 + 14 + 31 + 16 = 76 (Figura 5.12). |
| 465 | **b** | Inteiros | Peso do bit 7 = −128: −128 + 71 = -57. Sem sinal seria 199; em sinal-magnitude, -71. |
| 466 | **d** | Inteiros | Figura 10.6: B passa pelo complementador. |
| 467 | **b** | Paginação | ⌈26.599/8.192⌉ = 4; 4 × 8.192 − 26.599 = 6.169. |
| 468 | **d** | Nível ISA | O alinhamento existe para eficiência. O x86 aceita desalinhado, com custo extra (pode precisar de dois acessos). |
| 469 | **a** | Fluxo de controle | Sinal de fim de interrupção (EOI). |
| 470 | **a** | Segmentação/Cache | 2^18 e 2^16. |
| 471 | **c** | Inteiros | Booth dá diretamente o produto em complemento de dois de 2n bits: 1 × 7 = 7 = 0000 0111. Multiplicar os padrões como sem sinal daria 0000 0111, que está errado. |
| 472 | **a** | Tipos de instrução | Deslocamento lógico: entram zeros e os bits que saem se perdem. Rotação: os bits que saem voltam pelo outro lado. Aritmético à direita: o bit de sinal é replicado. |
| 473 | **b** | Segmentação/Cache | Slide 29 da Aula 08. |
| 474 | **a** | Ponto flutuante | 7,25 → sinal 0, expoente polarizado 129 (10000001) = 2 + 127, fração 11010000000000000000000. Bits: 0 10000001 11010000000000000000000 = 0x40E80000. |
| 475 | **d** | Segmentação/Cache | O problema é a fragmentação externa. |
| 476 | **d** | Ponto flutuante | Truque: x != x só é verdadeiro se x for NaN. |
| 477 | **a** | Inteiros | O programa escolhe qual flag testar. |
| 478 | **c** | Tipos de dados e formatos | Cada dígito em 4 bits: 6 = 0110, 2 = 0010. Em binário puro, 62 = 0011 1110. |
| 479 | **c** | Tipos de dados e formatos | RISC: formato fixo, fácil de decodificar, só LOAD/STORE acessam memória. |
| 480 | **a** | Inteiros | Após n ciclos, o produto está em A:Q. |
| 481 | **c** | Hanói/IA-64 | O push salvou lr; o pop coloca esse valor em pc. |
| 482 | **b** | Virtualização/E-S OSM | Consolidação de servidores. |
| 483 | **a** | Tipos de dados e formatos | Slide 21: a restrição mais comum é a memória não fornecer instruções na velocidade que a CPU consome. |
| 484 | **c** | Paginação | Analogia de alimentar o bebê quando ele chora. |
| 485 | **a** | Ponto flutuante | Slide de divisão. |
| 486 | **c** | Virtualização/E-S OSM | Usa 3 unidade(s) = 49.152 bytes; 49.152 − 40.000 = 9.152. |
| 487 | **b** | Inteiros | Booth dá diretamente o produto em complemento de dois de 2n bits: -2 × 1 = -2 = 1111 1110. Multiplicar os padrões como sem sinal daria 0000 1110, que está errado. |
| 488 | **a** | Inteiros | −7 = 3 × (−2) + (−1). |
| 489 | **d** | UNIX/Windows | Cada fork duplica todos os processos: 2^4. |
| 490 | **d** | Segmentação/Cache | Slide 17 da Aula 08. |
| 491 | **b** | Hanói/IA-64 | Mais 128 de ponto flutuante. |
| 492 | **b** | Paginação | ⌈3.300/1.024⌉ = 4; 4 × 1.024 − 3.300 = 796. |
| 493 | **c** | Virtualização/E-S OSM | Comparação muito comum quando se fala de nuvem. |
| 494 | **c** | Tipos de instrução | Slide 24 da Aula 04. |
| 495 | **b** | Paginação | 4.096 = 2^12 → 12 bits de deslocamento; sobram 36 para a página. |
| 496 | **b** | Paginação | Nenhum algoritmo resolve, exceto um oráculo. |
| 497 | **d** | Inteiros | -2 + 4 = 2. Faixa de 4 bits: -8 a 7. Dentro da faixa → sem overflow. |
| 498 | **a** | Ponto flutuante | 0,375 → sinal 0, expoente polarizado 125 (01111101) = -2 + 127, fração 10000000000000000000000. Bits: 0 01111101 10000000000000000000000 = 0x3EC00000. |
| 499 | **c** | Hanói/IA-64 | 2^n − 1. |
| 500 | **a** | Nível ISA | Little-endian: o byte menos significativo no menor endereço. Big-endian: o mais significativo no menor endereço. |
| 501 | **c** | Endereçamento | Equivale à infixa (6 − 1 − 4) × ((6 − 1) × (9 − 5)) = 20. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 502 | **b** | Paginação | Slide 10 da Aula 07. |
| 503 | **c** | Endereçamento | Slide 28 da Aula 03. |
| 504 | **b** | Endereçamento | Arquitetura carregue/armazene. |
| 505 | **c** | Inteiros | Equivalente à regra do sinal oposto. |
| 506 | **d** | Fluxo de controle | Restaura PC e PSW. |
| 507 | **c** | UNIX/Windows | Cada fork duplica todos os processos: 2^5. |
| 508 | **b** | Paginação | Implementado com contadores por quadro. |
| 509 | **d** | Paginação | 8.192 = 2^13 → 13 bits de deslocamento; sobram 19 para a página. |
| 510 | **c** | Endereçamento | As variáveis/números mantêm a ordem; os operadores aparecem na ordem em que são executados: 9 3 + 1 1 + ×. |
| 511 | **c** | Endereçamento | Slide 22 da Aula 03. |
| 512 | **d** | Fluxo de controle | Nota do slide 9. |
| 513 | **b** | Inteiros | Overflow de inteiro com sinal. |
| 514 | **a** | Virtualização/E-S OSM | Slide 22 da Aula 09. |
| 515 | **d** | Nível ISA | O slide de propriedades do nível ISA lista modelo de memória, quantos e quais registradores, tipos de dados e instruções. |
| 516 | **c** | Endereçamento | Figura 5.20. |
| 517 | **c** | Fluxo de controle | Slide 29 da Aula 05. |
| 518 | **b** | Paginação | Simulando: FIFO = 7 faltas (LRU daria 6). As 3 primeiras páginas distintas sempre faltam. |
| 519 | **b** | Nível ISA | C = carry. V = overflow, Z = zero, N = negativo. |
| 520 | **c** | Paginação | 15 = 3 (quadro) + 12 (deslocamento). |
| 521 | **c** | Tipos de dados e formatos | 2 dígitos decimais = 00..99 (100 valores); 8 bits binários = 256. |
| 522 | **a** | Endereçamento | Equivale à infixa (5 + (3 + 9)) × (6 − 6 + 8 × 5) = 680. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 523 | **c** | Fluxo de controle | O PIC retém ou repassa interrupções conforme a prioridade. |
| 524 | **d** | Ponto flutuante | qNaN (silencioso) ou sNaN (sinalizador). |
| 525 | **b** | Ponto flutuante | 0 10000000 01000000000000000000000: sinal 0, expoente 128 − 127 = 1, significando 1,01 (binário). |
| 526 | **b** | Segmentação/Cache | Modelo herdado do MULTICS. |
| 527 | **b** | Inteiros | +67 = 0100 0011. Inverte-se: 1011 1100. Soma-se 1: 1011 1101. |
| 528 | **d** | Inteiros | +116 = 0111 0100. Inverte-se: 1000 1011. Soma-se 1: 1000 1100. |
| 529 | **c** | Tipos de instrução | Deslocamento lógico: entram zeros e os bits que saem se perdem. Rotação: os bits que saem voltam pelo outro lado. Aritmético à direita: o bit de sinal é replicado. |
| 530 | **b** | Virtualização/E-S OSM | Usa 1 unidade(s) = 8.192 bytes; 8.192 − 1 = 8.191. |
| 531 | **c** | Tipos de instrução | Deslocamento lógico: entram zeros e os bits que saem se perdem. Rotação: os bits que saem voltam pelo outro lado. Aritmético à direita: o bit de sinal é replicado. |
| 532 | **c** | Endereçamento | Lógico polonês J. Łukasiewicz. |
| 533 | **a** | Tipos de instrução | Slide 28: grupo BCD. |
| 534 | **c** | Tipos de dados e formatos | Expansão de opcode: um valor do campo de 4 bits vira código de escape. |
| 535 | **d** | Tipos de instrução | LOAD: memória → registrador; STORE: registrador → memória. |
| 536 | **a** | UNIX/Windows | O P1003.2 define os utilitários. |
| 537 | **a** | Inteiros | Peso do bit 7 = −128: −128 + 54 = -74. Sem sinal seria 182; em sinal-magnitude, -54. |
| 538 | **a** | Endereçamento | Endereço = deslocamento (A) + conteúdo do registrador índice (R2). |
| 539 | **c** | Virtualização/E-S OSM | Classificação de Popek e Goldberg, bem comum em aula. |
| 540 | **b** | Inteiros | Preserva o valor numérico. |
| 541 | **d** | Virtualização/E-S OSM | Em HD e SSD a alocação não consecutiva é a regra. |
| 542 | **a** | Paralelismo/Semáforos | Referência do slide 30 da Aula 10. |
| 543 | **a** | Fluxo de controle | É síncrona e reproduzível, mas proposital. |
| 544 | **a** | Ponto flutuante | (124) − (120) + 127 = 131. |
| 545 | **b** | Endereçamento | Slide 22 da Aula 03. |
| 546 | **a** | Hanói/IA-64 | O compilador decide com antecedência. |
| 547 | **d** | Paralelismo/Semáforos | DOWN em 0 bloqueia; UP com processo esperando acorda um e mantém o valor; semáforos nunca ficam negativos. |
| 548 | **a** | Fluxo de controle | Pseudoparalelismo (slide 19). |
| 549 | **b** | Ponto flutuante | 0 01111110 10000000000000000000000: sinal 0, expoente 126 − 127 = -1, significando 1,1 (binário). |
| 550 | **d** | UNIX/Windows | Comentários nos arquivos do zip. |
| 551 | **d** | Ponto flutuante | 0 10000100 10000100000000000000000: sinal 0, expoente 132 − 127 = 5, significando 1,100001 (binário). |
| 552 | **b** | Paralelismo/Semáforos | Resultado: os dois dormem para sempre. |
| 553 | **b** | Inteiros | [−2^19, 2^19 − 1]. |
| 554 | **c** | Nível ISA | Em x86-64 os primeiros argumentos vão em registradores (RDI, RSI, RDX, RCX, R8, R9), diferente do cdecl de 32 bits, que usa a pilha. |
| 555 | **b** | Segmentação/Cache | A segmentação por permutação gera fragmentação externa. |
| 556 | **d** | Paginação | Simulando: FIFO = 7 faltas (LRU daria 6). As 3 primeiras páginas distintas sempre faltam. |
| 557 | **d** | Inteiros | 117 + -116 = 1. Faixa de 8 bits: -128 a 127. Dentro da faixa → sem overflow. |
| 558 | **a** | Segmentação/Cache | Tentar desviar para um vetor de PF é violação de proteção. |
| 559 | **c** | Paralelismo/Semáforos | DOWN em 0 bloqueia; UP com processo esperando acorda um e mantém o valor; semáforos nunca ficam negativos. |
| 560 | **c** | Inteiros | 4 + 87 = 91. Faixa de 8 bits: -128 a 127. Dentro da faixa → sem overflow. |
| 561 | **b** | Segmentação/Cache | Slide 22 da Aula 08. |
| 562 | **c** | Inteiros | Conta-se cada transição 10 ou 01 no par (Q0, Q−1) ao percorrer os bits: 2. Uma soma/subtração por fronteira de bloco de 1s. |
| 563 | **c** | Paralelismo/Semáforos | O consumidor faz o inverso. |
| 564 | **c** | Inteiros | −S = 1100. 7 − (4) = 3. |
| 565 | **c** | Segmentação/Cache | O seletor indica LDT/GDT, índice e nível de privilégio. |
| 566 | **b** | UNIX/Windows | O arquivo some quando o contador chega a 0. |
| 567 | **a** | Nível ISA | Little-endian guarda o byte menos significativo no menor endereço. |
| 568 | **a** | Virtualização/E-S OSM | Slides 4 e 7 da Aula 09. |
| 569 | **a** | Inteiros | Peso do bit 7 = −128: −128 + 72 = -56. Sem sinal seria 200; em sinal-magnitude, -72. |
| 570 | **b** | Inteiros | [−2^11, 2^11 − 1]. |
| 571 | **b** | Inteiros | 1111 1111 + 1 = 1 0000 0000. |
| 572 | **c** | Tipos de dados e formatos | 128 × 10^9 / 16 = 8 × 10^9. |
| 573 | **b** | UNIX/Windows | Figura 6.39. |
| 574 | **b** | Tipos de instrução | Slide 15 da Aula 04. |
| 575 | **c** | Endereçamento | Slide 8 da Aula 03. |
| 576 | **b** | Inteiros | −S = 0000. 5 − (0) = 5. |
| 577 | **a** | Hanói/IA-64 | Se o valor nunca for usado, a exceção nunca acontece. |
| 578 | **d** | Ponto flutuante | Sem eles, x − y pode perder um fator de 2 de precisão. |
| 579 | **b** | Paginação | LRU e OPT são algoritmos de pilha e não sofrem a anomalia. |
| 580 | **d** | Segmentação/Cache | Memória bidimensional. |
| 581 | **c** | Paginação | Simulando: FIFO = 8 faltas (LRU daria 7). As 3 primeiras páginas distintas sempre faltam. |
| 582 | **c** | Ponto flutuante | Arredondar para o par evita polarização cumulativa. |
| 583 | **a** | Inteiros | -103 + -76 = -179. Faixa de 8 bits: -128 a 127. Fora da faixa: operandos de mesmo sinal e resultado com sinal oposto → overflow. |
| 584 | **c** | Paralelismo/Semáforos | Slide 28 da Aula 10. |
| 585 | **b** | UNIX/Windows | Torvalds estudou o MINIX em Helsinque. |
| 586 | **c** | Ponto flutuante | Normalizado, o expoente verdadeiro é 10; somando a polarização 127, dá 137. |
| 587 | **a** | Hanói/IA-64 | 6 − 1 − 2 = 3. |
| 588 | **d** | Endereçamento | Equivale à infixa 5 − 3 − (4 − 6) − (5 − 8) × (1 − 9) = -20. Operando → empilha; operador → desempilha dois, opera e empilha o resultado. |
| 589 | **a** | Endereçamento | EA = Reg + Desl. |
| 590 | **b** | Segmentação/Cache | O melhor ajuste deixa lacunas minúsculas e inúteis. |
| 591 | **d** | Endereçamento | Slide 29 da Aula 03. |
| 592 | **a** | Paginação | Memória, registradores, PC, estado de E/S etc. |
| 593 | **c** | Ponto flutuante | -9,5 → sinal 1, expoente polarizado 130 (10000010) = 3 + 127, fração 00110000000000000000000. Bits: 1 10000010 00110000000000000000000 = 0xC1180000. |
| 594 | **a** | Paginação | 26.373 = página 3 × 8.192 + deslocamento 1797. A página 3 está no quadro 1: 1 × 8.192 + 1797 = 9.989. |
| 595 | **b** | Paginação | ⌈6.897/2.048⌉ = 4; 4 × 2.048 − 6.897 = 1.295. |
| 596 | **a** | Endereçamento | Escala ∈ {1, 2, 4, 8}. |
| 597 | **a** | Endereçamento | 1 instrução + 2 endereços + 2 leituras + 1 escrita = 6 (96 bits de instrução). |
| 598 | **a** | Fluxo de controle | O término de E/S é interrupção (externa, assíncrona). |
| 599 | **c** | Ponto flutuante | 0,0/0,0 é que dá NaN. |
| 600 | **b** | Endereçamento | Formato 2: imediato. |
| 601 | **b** | Paginação | A tendência favorece páginas maiores. |
| 602 | **b** | Ponto flutuante | 0,09375 → sinal 0, expoente polarizado 123 (01111011) = -4 + 127, fração 10000000000000000000000. Bits: 0 01111011 10000000000000000000000 = 0x3DC00000. |
| 603 | **a** | Endereçamento | Slide 30 da Aula 03. |
| 604 | **b** | Virtualização/E-S OSM | Usa 2 unidade(s) = 8.192 bytes; 8.192 − 5.000 = 3.192. |
| 605 | **a** | Endereçamento | EA = escala × índice + base + deslocamento = 2×4 + 1564 + 16 = 1588. |
| 606 | **a** | Ponto flutuante | binary128: 15 bits e bias 16383. |
| 607 | **a** | Paginação | 30.121 = página 7 × 4.096 + deslocamento 1449. A página 7 está no quadro 0: 0 × 4.096 + 1449 = 1.449. |
| 608 | **b** | Tipos de instrução | Slide 17 da Aula 04. |
| 609 | **b** | Paginação | 1.024 = 2^10 → 10 bits de deslocamento; sobram 6 para a página. |
| 610 | **c** | Tipos de instrução | A CPU não sabe; o programador escolhe a instrução. |
| 611 | **a** | Tipos de dados e formatos | Cada dígito em 4 bits: 5 = 0101, 7 = 0111. Em binário puro, 57 = 0011 1001. |

## Questões por assunto

| Assunto | Questões |
|---|---|
| Inteiros | 95 |
| Ponto flutuante | 78 |
| Paginação | 74 |
| Endereçamento | 58 |
| Tipos de instrução | 41 |
| Tipos de dados e formatos | 41 |
| Virtualização/E-S OSM | 37 |
| UNIX/Windows | 36 |
| Hanói/IA-64 | 32 |
| Paralelismo/Semáforos | 32 |
| Fluxo de controle | 30 |
| Segmentação/Cache | 29 |
| Nível ISA | 28 |
