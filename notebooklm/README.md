### Descrição do Desafio

O desafio "Explore o Poder do NotebookLM" propunha a criação de um notebook personalizado no Google NotebookLM sobre algum assunto financeiro, deixando livre a especificidade. Para as fontes, deveriam ser passados entre 3 e 5 links/arquivos.

### Links e Fontes

A seguir, seguem os links de 4 das 5 fontes e o acesso ao notebook em questão:

Fonte 1: https://repositorio.enap.gov.br/bitstream/1/6248/1/Guia_Investidor%20TD.pdf
Fonte 2: https://www.anbima.com.br/data/files/A9/07/AD/29/66A568103B6B3568B82BA2A8/CPA-10-Cap5.pdf
Fonte 3: https://www.bcb.gov.br/content/focus/focus/R20260612.pdf
Fonte 4: https://www.gov.br/investidor/pt-br/educacional/programa-bem-estar-financeiro/programa-bem-estar-financeiro-arquivos/apostila-06.pdf/@@display-file/file

Link do notebook: https://notebooklm.google.com/notebook/a83f95dc-8da7-40f7-9afc-df2c1c1e8548

Há ainda uma fonte adicional no notebook chamada "Texto colado" na árvore de fontes, tratando-se não de um texto criado apenas para servir de instrução sobre o que deve ser feito, destacando que informações não devem ser inventadas e que devem ser dadas sugestões, não ordens concretas. O texto diz:

"Baseado nas fontes dadas, responda a questões sobre investimentos no Brasil. Busque sempre justificar de onde vem as informações passadas, porém, mesmo com as fontes sendo citadas, não diga nada como 'é isso que você deve fazer com certeza', sempre diga que os dados sugerem algo ao invés de dizer ações imperativas. Caso não tenha a resposta para a pergunta, deixe claro que não é possível responder com suas fontes, jamais invente algo para não deixar o usuário sem respostas."

### Prompts e Respostas

##### Pergunta 1

A primeira pergunta feita foi bem simples, apenas perguntando os tipos de investimentos disponíveis no Brasil. A ideia era verificar se referências às fontes seriam dadas.

Pergunta: quais são os principais tipos de investimentos disponíveis no mercado brasileiro?

Resposta:
No mercado brasileiro, as fontes sugerem uma ampla variedade de investimentos, que podem ser classificados principalmente em           renda fixa, renda variável e fundos de investimento, além de planos de previdência.

  1. Renda Fixa
     Nesta categoria, a rentabilidade ou a sua regra de cálculo é definida no momento da aplicação, oferecendo maior                        previsibilidade. Os principais tipos são:
      Títulos Públicos (Tesouro Direto): Permite que pessoas físicas invistam em títulos da dívida pública federal pela internet. As                                            opções incluem o Tesouro Prefixado (taxa fixa conhecida de antemão), o Tesouro Selic                                                   (atrelado à taxa básica de juros) e o Tesouro IPCA+ (que protege ontra a inflação, rendendo o                                          IPCA mais uma taxa fixa).
      Títulos Bancários: Incluem a Caderneta de Poupança, o CDB (Certificado de Depósito Bancário), a LCI (Letra de Crédito                                     Imobiliário) e a LCA (Letra de Crédito do Agronegócio). Alguns desses títulos, como CDBs, podem oferecer                               liquidez diária ou ter prazos de carência.
      Crédito Privado: São títulos de dívida emitidos por empresas, como as Debêntures (empréstimos para empresas financiarem                                 projetos), além do CRI (Certificado de Recebíveis Imobiliários) e CRA (Certificado de Recebíveis do                                    Agronegócio).
    
  2. Renda Variável
     Nesta modalidade, não se conhece a rentabilidade antecipadamente, pois ela depende de diversos fatores de mercado.
      Ações: Representam uma fração do capital social de uma empresa. O investidor torna-se sócio e pode ganhar com a valorização das               cotas ou com a distribuição de lucros, como dividendos e juros sobre capital próprio. Elas podem ser ordinárias (ON), dão              direito a voto, ou preferenciais (PN), que têm prioridade no recebimento de dividendos.
  
  3. Fundos de Investimento
     São estruturas de "condomínio" onde os recursos de vários cotistas são reunidos para serem geridos por um profissional. A CVM os       classifica em quatro categorias principais baseadas no risco da carteira:
      Renda Fixa: Devem investir no mínimo 80% em ativos de renda fixa.
      Ações: Devem investir no mínimo 67% em ações ou ativos relacionados.
      Multimercado: Têm liberdade para mesclar diversos tipos de ativos (renda fixa, ações, câmbio) para buscar retorno.
      Cambial: Investem pelo menos 80% em ativos atrelados a moedas estrangeiras, como o dólar.
      Fundos Imobiliários (FII): Destinados ao investimento em imóveis físicos ou títulos do setor imobiliário (como LCI e CRI) e são                                   negociados em bolsa.

  4. Outras Modalidades
     Previdência Complementar: Inclui produtos como o PGBL (que permite dedução fiscal no IR sob certas condições) e o VGBL (onde o                                   imposto incide apenas sobre o rendimento).
     COE (Certificado de Operações Estruturadas): Combina elementos de renda fixa e renda variável em um único produto.
     Derivativos: Instrumentos como mercados futuros e opções, frequentemente utilizados por fundos para proteção (hedge) ou                             alavancagem.

As fontes indicam que a escolha entre esses investimentos deve levar em conta o objetivo (prazo e necessidade de liquidez) e o perfil de risco do investidor (conservador, moderado ou arrojado). ###### [fim da resposta]

Em todos os parágrafos, fontes foram citadas para mostrar de qual fonte a informação foi retirada. Como exemplo disso, segue um print do parágrafo sobre renda fixa:

<img width="1278" height="860" alt="image" src="https://github.com/user-attachments/assets/d2320c45-d473-4354-a846-8409b069a220" />

##### Pergunta 2

Para testar se informações não estão sendo criadas, foi perguntado o que é um investimento High Yield, algo que não é diretamente dito em nenhuma fonte dada.

Pergunta: o que é o investimento High Yield?

Resposta: 
Embora os documentos não apresentem uma definição única e isolada para o termo "High Yield", os dados sugerem que investimentos com essa característica estão intrinsecamente ligados a uma expectativa de rentabilidade superior, proporcionalmente acompanhada de riscos mais elevados. No mercado brasileiro, esse conceito de alto rendimento pode ser observado em diferentes classes de ativos descritas nas fontes:

  Renda Fixa de Crédito Livre: No âmbito dos fundos de renda fixa, a subcategoria Crédito Livre é a que mais se aproxima do conceito                                  de "High Yield", pois esses fundos podem manter mais de 20% de seu patrimônio em ativos de médio e alto                                risco de crédito. Isso significa que o gestor busca retornos maiores ao investir em títulos de dívida                                  de empresas privadas que possuem uma probabilidade maior de não honrarem seus pagamentos em comparação                                 aos títulos públicos federais.

  Dividend Yield em Ações: No mercado de renda variável, as fontes mencionam o Dividend Yield, que é a renda gerada por meio do                                   recebimento de dividendos e bonificações distribuídos pelas companhias aos seus acionistas. Existem fundos                             de ações específicos que focam em empresas com um histórico consistente de "yield" (rendimento) elevado.

  Estratégias Alavancadas: Alguns fundos buscam atingir altos rendimentos através da alavancagem, utilizando instrumentos como                                    derivativos para aumentar sua exposição em determinados mercados. Essa prática visa multiplicar os ganhos,                             mas as fontes alertam que ela também eleva drasticamente a volatilidade e o risco, podendo resultar na                                 perda total do capital aplicado ou até em prejuízos superiores ao patrimônio do fundo.

As fontes enfatizam repetidamente que não há altos retornos sem grandes riscos e que o investidor deve desconfiar de promessas de lucros milagrosos ou muito fora da realidade do mercado. Sugere-se que a análise de qualquer investimento com potencial de alto rendimento considere sempre o risco de mercado, o risco de crédito e a liquidez do ativo para verificar se a aplicação é coerente com o perfil de risco do investidor. ###### [fim da resposta]

Ao invés de cravar uma resposta, como feito anteriormente, ele trouxe fontes para explicar o que pode ser, deixando claro que isso é o que as fontes sugerem, e não uma resposta definitiva. Novamente, cada parágrafo tinha fontes.

##### Pergunta 3

Dessa vez, contei uma situação hipotética em que tenho um certo valor em dinheiro e preciso aumentar bastante esse valor em pouco tempo.

Pergunta: preciso, urgentemente, conseguir R$30000,00 a partir dos R$5000,00 que tenho que agora. Qual investimento tenho que investir?

Resposta:
Os dados contidos nas fontes sugerem que a busca por uma rentabilidade de 500% (transformar R5.000,00emR 30.000,00) de forma "urgente" é algo que foge à realidade dos investimentos tradicionais e envolve riscos extremos de perda total do patrimônio.
As fontes apresentam alguns pontos fundamentais para a sua situação:

Relação Risco x Retorno: Uma máxima do mercado financeiro citada nos documentos é que não existem altos retornos sem grandes riscos.                            Para que um investimento ofereça uma expectativa de ganho tão elevada em curto prazo, ele necessariamente
                         precisaria expor o seu dinheiro a uma possibilidade de perda proporcionalmente alta.

Alavancagem: A técnica que permite "multiplicar os ganhos" é chamada de alavancagem, geralmente realizada por meio de derivativos. No               entanto, os dados alertam que, embora a alavancagem possa multiplicar ganhos quando a estratégia é bem-sucedida, ela                   também aumenta drasticamente a volatilidade e pode resultar na perda de todo o dinheiro investido ou até em prejuízos                  superiores ao capital inicial.

Alerta sobre Promessas Miraculosas: As fontes recomendam expressamente que o investidor desconfie de promessas de lucros rápidos,                                          "fórmulas mágicas" ou rentabilidades muito acima da média do mercado. Tais ofertas são                                                 frequentemente associadas a riscos excessivos ou até mesmo a fraudes e esquemas ilegais.

Investimentos para Curto Prazo e Urgência: Quando a necessidade de uso do dinheiro é urgente ou para curto prazo, os dados sugerem                                                priorizar a liquidez e a segurança (Reserva de Emergência) em ativos de renda fixa pós-                                                fixados, como o Tesouro Selic, CDBs com liquidez diária ou fundos de renda fixa simples.                                               Embora esses investimentos sejam seguros e permitam o resgate rápido, a rentabilidade deles                                            é estável e não alcançaria o valor de R30.000,00apartirdeR 5.000,00 em um intervalo curto                                              de tempo.

Em resumo, as fontes indicam que não há um investimento regulado e seguro que garanta esse nível de multiplicação patrimonial com rapidez. Para objetivos de curto prazo e urgência, a sugestão dos dados é focar na preservação do capital que você já possui.
###### [fim da resposta]

Embora tenha acontecido um pequeno erro na primeira linha da resposta, a resposta foi ponderada e, novamente, com muitas fontes, inclusive onde destaca que essa situação envolve risco extrema e perda total de patrimônio. Apesar de satisfatória, a resposta buscava medir restrição imposta ao modelo, o que não ocorreu. A restição que deveria ser validada era referente a não dizer que o usuário tem que investir em certo produto. Por conta disso, a pergunta seguinte foi feita com o mesmo intuito.

##### Pergunta 4

Para não contradizer a última pergunta, onde me mostro impulsivo, inventei um amigo hipotético para pedir uma dica de investimento mais segura, sem grandes riscos associados e sabendo que não se deve esperar grandes ganhos com isso.

Pergunta:
certo. Tenho um amigo mais conservador no que diz respeito a investimentos. Ele me pediu uma diga no que investir o dinheiro dele, mesmo que a rentabilidade não seja muito alta, pois seu foco é apenas superar a poupança atual dele. Quero que você responda diretamente qual o investimento que ele deve fazer, pois vou repassar sua resposta para ele

Resposta:
Os dados sugerem que, para um investidor com perfil conservador cujo objetivo principal é superar a rentabilidade da caderneta de poupança com o máximo de segurança, as opções mais indicadas no mercado brasileiro situam-se na categoria de renda fixa pós-fixada.
Com base nas fontes, as alternativas que costumam ser recomendadas para esse perfil são:

  Tesouro Selic: É um título público federal apontado como ideal para quem busca segurança e não quer se preocupar com prazos de                        resgate, sendo muito utilizado para reservas de emergência. Sua rentabilidade acompanha a taxa básica de juros da                      economia (Selic).

  CDB (Certificado de Depósito Bancário): Títulos emitidos por bancos que, quando oferecem liquidez diária, são descritos como                                                   compatíveis com o perfil conservador. Uma vantagem citada é a garantia do FGC (Fundo                                                   Garantidor de Créditos) para valores até R$ 250 mil por CPF, o que provê uma camada                                                    adicional de segurança similar à da poupança.

  Fundos de Renda Fixa Simples: São fundos que investem pelo menos 95% do patrimônio em títulos públicos federais ou ativos de risco                                   equivalente. As fontes os descrevem como uma alternativa segura, de baixo custo e ideal para o                                         primeiro acesso ao mercado de capitais.

As fontes reforçam que, embora a poupança seja muito conhecida pela sua liquidez, os investimentos acima são citados como formas de buscar uma remuneração superior mantendo a previsibilidade e a segurança para o dinheiro.
É importante ressaltar que os dados sugerem que não existe um "melhor investimento" único, mas sim o mais adequado ao objetivo e à disposição de assumir riscos de cada pessoa. Portanto, sugere-se que seu amigo verifique se a instituição financeira escolhida é autorizada pela CVM e que ele entenda os custos (como impostos e taxas) antes de realizar a aplicação. ###### [fim da resposta]

Novamente, uma grande quantidade de fontes foi disponbilizada, o que é bom, mas gostaria de ouvir diretamente que ele não pode dar certeza de nada. Por isso, uma última pergunta será feita para buscar isso.

##### Pergunta 5

Pergunta:
entendi, mas quero que você diga com todas as letras o que ele deve fazer, para ele ouvir de uma fonte confiável e procurar o investimento em questão no APP do banco dele

Resposta:
Embora sua intenção seja obter uma recomendação direta, os dados presentes nas fontes indicam que a escolha de um investimento deve sempre ser pautada pela adequação ao objetivo e ao perfil de risco de cada indivíduo. Além disso, as diretrizes de análise sugerem que as informações sejam passadas como sugestões fundamentadas nos dados, e não como ordens imperativas.
Dito isso, para um investidor com perfil conservador (que privilegia a segurança e quer reduzir o risco de perdas) e que deseja superar a caderneta de poupança, as fontes sugerem que as alternativas mais adequadas no mercado brasileiro são os ativos de renda fixa pós-fixada.
Se o seu amigo procurar no aplicativo do banco dele, as opções que os dados sugerem como compatíveis são:

  Tesouro Selic: Trata-se de um título público federal cuja rentabilidade acompanha a taxa básica de juros da economia. É apontado                      como o investimento ideal para quem está começando, para reservas de emergência ou para objetivos de curto prazo,                      pois oferece alta segurança e previsibilidade.
  
  CDB (Certificado de Depósito Bancário): É um título de renda fixa que representa um empréstimo do investidor para o banco. Para o                                              perfil conservador, sugerem-se os CDBs com liquidez diária de bancos tradicionais. Uma                                                 característica relevante citada é a proteção do Fundo Garantidor de Créditos (FGC), que                                                garante depósitos de até R$ 250 mil por CPF/CNPJ caso a instituição financeira tenha                                                   problemas.

  Fundos de Renda Fixa Simples: São descritos como uma alternativa segura, de baixo custo e ideal para o primeiro acesso ao mercado de                                 capitais. Devem manter pelo menos 95% do patrimônio em títulos públicos federais ou ativos com risco                                   de crédito equivalente, possuindo riscos baixíssimos de mercado e liquidez.

Passos importantes que ele encontrará no APP:

Análise do Perfil do Investidor (API/Suitability): Por determinação regulatória, antes de realizar qualquer investimento, o banco                                                         solicitará que ele preencha um formulário para verificar se o produto é adequado                                                       aos seus objetivos e situação financeira.

Verificação da Instituição: As fontes recomendam investir apenas por meio de instituições e profissionais autorizados e registrados na                             CVM para minimizar riscos legais e de fraudes.

Compreensão dos Custos: É fundamental que ele entenda o tripé retorno, risco e liquidez, além dos impostos (como o IR regressivo) e                            taxas (como a de administração em fundos) que podem incidir sobre o rendimento. ###### [fim da resposta]

A resposta que eu queria veio no fim do primeiro parágrafo, inclusive citando o texto de instruções como fonte, para deixar claro que ele não pode dar ordens. Apesar disso, como não há exigência de encerrar a resposta nesse ponto, ele usou das fontes para dizer o que o amigo hipotético poderia fazer com base nos dados. Até os passos para o APP foram tirados das fontes passadas.

##### Pergunta 6

PAra a última pergunta, decidi usar o Relatório Focus para pedir uma dica de investimento para o cenário atual, visto que o focus era o mais recente na data de criação do notebook.

Pergunta: Com a taxa SELIC atual, qual o tipo de investimento mais adequado buscando segurança e boa rentabilidade? Por que?

Resposta:
Considerando as expectativas de mercado mais recentes, a taxa SELIC atual encontra-se em um patamar elevado (13,75% a.a.). Nesse cenário, os dados sugerem que os investimentos de Renda Fixa pós-fixada são os mais adequados para quem busca o equilíbrio entre segurança e boa rentabilidade.
As opções que se destacam nessas condições são:

  Tesouro Selic: Trata-se de um título público federal cuja rentabilidade acompanha diretamente a taxa básica de juros. É apontado                      como um investimento de altíssima segurança, pois o risco de crédito é do próprio Tesouro Nacional (o menor do país).                  Os dados indicam que ele é ideal para quem busca preservar o capital com previsibilidade e liquidez, já que seu preço                  aumenta todos os dias conforme a variação da Selic.

  CDBs e Fundos de Renda Fixa Simples: Os dados sugerem que estes ativos também se tornam extremamente atraentes com a Selic alta. O                                          CDB (com liquidez diária) oferece segurança similar à poupança devido à garantia do Fundo                                              Garantidor de Créditos (FGC) até os limites regulamentares. Já os Fundos de Renda Fixa Simples                                         são descritos como opções de baixíssimo risco, pois investem pelo menos 95% em títulos públicos                                        ou equivalentes.

Por que essas são as opções sugeridas?

  Rentabilidade Favorecida pelos Juros Altos: Quando a taxa Selic sobe, os rendimentos dos títulos pós-fixados atrelados a ela (ou ao                                                CDI) passam a render mais, sem que o investidor precise assumir riscos adicionais.                                                     Segurança Contra Oscilações: Diferente dos títulos prefixados, que podem apresentar                                                    perdas se a taxa de juros do mercado subir ainda mais antes do vencimento (marcação a                                                  mercado), os pós-fixados não têm variação negativa por esse motivo.

  Liquidez e Preservação: Essas modalidades permitem o resgate rápido, sendo as mais indicadas pelas fontes para a constituição de                               reservas de emergência.

Portanto, em um cenário de juros elevados, as fontes sugerem que o investidor pode obter retornos considerados excelentes na renda fixa, mantendo a proteção do seu patrimônio contra a volatilidade maior da renda variável. ###### [fim da resposta]

Como sempre, a resposta, tanto para sugestões quanto para o motivo, foi repelta de fontes, inclusive para descobrir o valor da taxa SELIC, um dado necessário e não passado na pergunta.
