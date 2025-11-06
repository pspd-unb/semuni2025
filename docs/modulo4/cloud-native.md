# Introdução ao Cloud Computing e ao Cloud Native

## Cloud Computing

A **computação em nuvem** é definida como a **disponibilidade sob demanda** de recursos computacionais, como armazenamento e infraestrutura, entregues como **serviços pela Internet**.
Esse modelo elimina a necessidade de indivíduos e empresas gerenciarem seus próprios recursos físicos, permitindo que **paguem apenas pelo que utilizam**.

### Contraste com a TI Tradicional

Tradicionalmente, adquirir recursos computacionais era um processo **lento e caro**.
As empresas precisavam comprar **servidores físicos e infraestrutura** por meio de processos que podiam levar meses, exigindo um **espaço físico especializado**, com energia e refrigeração adequadas, além de uma **equipe técnica** para gerenciá-los.
Esse modelo tradicional é **difícil de escalar** quando a demanda aumenta ou os negócios crescem, frequentemente resultando em **superdimensionamento de recursos** e **baixa taxa de utilização**.

A computação em nuvem **resolve esses problemas** ao oferecer recursos computacionais **escaláveis e sob demanda**.

### Como Funciona a Computação em Nuvem

Os **modelos de serviço em nuvem** operam com base no **compartilhamento de recursos, softwares e informações sob demanda** pela Internet.

1. **Recursos Compartilhados:** Empresas ou indivíduos pagam para acessar um **pool virtual** de recursos compartilhados, incluindo computação, armazenamento e rede.
2. **Gerenciamento Remoto:** Esses recursos ficam hospedados em **servidores remotos**, pertencentes e gerenciados pelos provedores de serviço.
3. **Conectividade:** A nuvem utiliza uma **rede (geralmente a Internet)** para conectar os usuários à plataforma em nuvem, onde eles solicitam e acessam os serviços contratados.
4. **Troca de Dados:** Um **servidor central** gerencia toda a comunicação entre os dispositivos clientes e os servidores, facilitando a troca de informações. **Segurança e privacidade** são componentes essenciais dessa comunicação.


### Principais Modelos de Serviço (Controle e Responsabilidade)

As fontes identificam **três modelos principais de serviço**, escolhidos de acordo com o nível de controle, flexibilidade e gerenciamento desejado:

#### **Infraestrutura como Serviço (IaaS):**

   * **O que oferece:** Acesso sob demanda a serviços de infraestrutura de TI, incluindo computação, armazenamento, rede e virtualização.
   * **Nível de controle:** O IaaS oferece o **maior controle** sobre os recursos de TI, sendo o modelo mais próximo do ambiente tradicional **on-premise** (local).

#### **Plataforma como Serviço (PaaS):**

   * **O que oferece:** Todos os recursos de hardware e software necessários para o **desenvolvimento de aplicações** na nuvem.
   * **Foco:** Permite que as empresas se concentrem totalmente no **desenvolvimento de software**, sem se preocupar com a infraestrutura subjacente.

#### **Software como Serviço (SaaS):**

   * **O que oferece:** Uma **pilha completa de aplicativos** entregue como serviço.
   * **Gerenciamento:** O provedor é responsável por **toda a infraestrutura, manutenção e atualização** do software. O SaaS normalmente é uma **aplicação de uso final**.


### Modelos de Implantação (Localização e Propriedade)

Existem **três modelos distintos** de implantação da computação em nuvem:

#### **Nuvem Pública (Public Cloud):**

   * Operada por **provedores terceirizados de serviços em nuvem**.
   * Oferece recursos de computação, armazenamento e rede pela Internet, permitindo acesso **sob demanda** a recursos compartilhados conforme as necessidades da empresa.

#### **Nuvem Privada (Private Cloud):**

   * Construída, gerenciada e de propriedade de **uma única organização**, hospedada **em seus próprios data centers** (também conhecida como *on-premise*).
   * Oferece **maior controle, segurança e gestão de dados**, mantendo os benefícios de recursos compartilhados internamente.

#### **Nuvem Híbrida (Hybrid Cloud):**

   * Combina os modelos **público e privado**.
   * Permite que as empresas aproveitem os **serviços da nuvem pública** enquanto mantêm a **segurança e conformidade** típicas das arquiteturas privadas.


### Benefícios da Computação em Nuvem

A adoção da **arquitetura em nuvem** oferece diversas vantagens:

* **Econômica:** As empresas **pagam apenas pelo que usam**, evitando superdimensionar data centers e permitindo que as equipes de TI foquem em iniciativas estratégicas.
* **Flexível e Escalável:** A nuvem permite **acesso de qualquer lugar** com conexão à Internet, possibilitando escalar recursos rapidamente conforme a demanda.
* **Eficiente:** Empresas podem desenvolver e colocar novas aplicações em produção **de forma ágil**, sem se preocupar com a infraestrutura física.
* **Segura:** A segurança na nuvem costuma ser **mais robusta** do que a de data centers corporativos, devido às medidas avançadas e à presença de **especialistas dedicados** dos provedores.
* **Valor Estratégico:** Como os provedores oferecem **as inovações mais recentes** como serviço, as empresas obtêm **vantagens competitivas** e **maior retorno sobre o investimento (ROI)**, evitando tecnologias que se tornariam obsoletas rapidamente.


### Casos de Uso e Indicadores de Adoção

A computação em nuvem tem **aplicações amplas** e tende a se tornar o **ambiente padrão de TI corporativo**, graças à velocidade da inovação e à necessidade de alto desempenho.

#### Casos de Uso Comuns

* **Escalabilidade de Infraestrutura:** Facilita lidar com **flutuações na demanda computacional**, comum em setores como o varejo.
* **Recuperação de Desastres:** Permite **backup seguro de recursos digitais**, sem a necessidade de construir novos data centers apenas para continuidade de negócios.
* **Armazenamento de Dados:** Apoia data centers sobrecarregados ao armazenar **grandes volumes de dados**, facilitando o acesso, análise e backup.
* **Desenvolvimento de Aplicações:** Fornece **ferramentas e plataformas** para criar e testar aplicações rapidamente, reduzindo o tempo de lançamento no mercado.
* **Análise de Big Data:** Disponibiliza recursos praticamente **ilimitados** para processar grandes volumes de dados, acelerando **pesquisas e geração de insights**.

#### Indicadores de Adequação à Nuvem

Organizações que enfrentam desafios além da capacidade dos data centers tradicionais são **fortes candidatas** à adoção da nuvem.
Esses casos incluem:

* Crescimento acelerado dos negócios que **excede a capacidade atual de infraestrutura**.
* **Baixa utilização** dos recursos existentes.
* **Grandes volumes de dados** sobrecarregando o armazenamento local.
* **Lentidão** em respostas com infraestrutura local.
* **Atrasos no desenvolvimento de produtos** devido a limitações de infraestrutura.
* **Problemas de fluxo de caixa** causados por altos custos de infraestrutura.
* **Usuários distribuídos** ou acesso predominante por **dispositivos móveis**.


## Cloud Native

Cloud native é uma abordagem fundamental para construir e executar aplicações escaláveis que aproveitam ao máximo os serviços e modelos de entrega baseados em nuvem. O termo se refere menos ao **local onde a aplicação está hospedada** e mais a **como ela é construída e implantada**. Ser cloud native envolve adaptar-se às novas possibilidades e limitações oferecidas pela nuvem em comparação com a infraestrutura tradicional local (*on-premises*).

Cloud native é frequentemente citado como o objetivo final para a construção ou migração de aplicações hoje. É um termo útil para descrever sistemas distribuídos, baseados em nuvem, containerizados e compostos por microsserviços cooperativos, gerenciados dinamicamente por infraestrutura automatizada como código.

### Arquitetura e Princípios Cloud Native

Uma característica principal da arquitetura cloud native é o contraste com aplicações tradicionais e monolíticas.

* **Monolítico vs. Cloud Native:** Aplicações monolíticas tradicionais precisam ser construídas, testadas e implantadas como uma única unidade, criando dependências próximas que dificultam mudanças, testes, implantações e operação à medida que crescem. Em contraste, arquiteturas cloud native decompõem componentes em **serviços fracamente acoplados** para ajudar a gerenciar a complexidade e melhorar a velocidade, a agilidade e a escala da entrega de software. Aplicações cloud native são projetadas desde o início para aproveitar a natureza distribuída e elástica da nuvem.

O objetivo fundamental das arquiteturas cloud native é aumentar a velocidade de entrega de software e a confiabilidade dos serviços, ao mesmo tempo em que desenvolve uma cultura de responsabilidade compartilhada entre os participantes do desenvolvimento. Essa abordagem se apoia em vários pilares fundamentais ou blocos tecnológicos:

#### 1. Microsserviços

Microsserviços são componentes ou serviços discretos e reutilizáveis que compõem uma única aplicação.

* **Composição:** Microsserviços dividem uma aplicação em serviços menores e leves que podem ser facilmente compostos e conectados por meio de APIs (Application Programming Interfaces).
* **Independência:** Eles são fracamente acoplados e implantáveis de forma independente. Isso permite que equipes implantem e escalem componentes separadamente.
* **Pilha Tecnológica:** Microsserviços geralmente possuem sua própria pilha tecnológica, incluindo banco de dados e modelo de dados, e se comunicam via APIs REST, *message brokers* ou *event streaming*.
* **Resiliência:** Por serem independentes, se um microsserviço falhar, a aplicação como um todo pode continuar funcionando.

#### 2. Containers e Orquestração

Containers são as unidades de computação *de facto* das aplicações cloud native modernas.

* **Containers:** São componentes leves e executáveis que empacotam o código-fonte da aplicação (código dos microsserviços) junto com todos os elementos necessários, incluindo dependências e bibliotecas do sistema operacional, para executar o código de forma consistente em qualquer ambiente.
* **Portabilidade:** Containers proporcionam portabilidade de carga de trabalho, apoiando o conceito de “construa uma vez, execute em qualquer lugar”, o que facilita bastante o desenvolvimento e a implantação.
* **Eficiência:** Containers são menores, mais eficientes em recursos e mais portáteis que máquinas virtuais (VMs). Eles executam diretamente na CPU real, sem a sobrecarga da virtualização.
* **Orquestração (ex.: Kubernetes):** À medida que o número de microsserviços cresce, plataformas de orquestração de containers como o **Kubernetes** tornam-se essenciais para gerenciar containers em escala. O Kubernetes oferece supervisão, controle sobre implantação, reparo de falhas e balanceamento de carga entre containers. Ele abstrai detalhes específicos da nuvem, fornecendo uma definição portátil de como o software deve ser executado.

#### 3. DevOps

DevOps é uma mudança cultural e metodológica essencial para o desenvolvimento de aplicações cloud native.

* **Colaboração e Automação:** DevOps envolve a colaboração entre equipes de desenvolvimento e operações de TI para automatizar processos de infraestrutura e entrega de software.
* **Propósito Compartilhado:** Cria uma cultura onde as equipes se comunicam em torno de um propósito comum, permitindo que aplicações sejam construídas, testadas e lançadas mais rapidamente.
* **Infraestrutura como Código:** DevOps traz habilidades de desenvolvimento para a operação, utilizando ferramentas e fluxos de trabalho que automatizam o provisionamento da infraestrutura na nuvem.

#### 4. Integração Contínua e Entrega Contínua (CI/CD)

Pipelines de CI/CD dependem fortemente de automação para otimizar o processo de entrega de software.

* **CI (Continuous Integration):** Envolve desenvolvedores integrando com frequência pequenas alterações em uma base de código compartilhada, permitindo identificar e resolver problemas mais rapidamente.
* **CD (Continuous Delivery):** Automatiza a construção, o teste e a implantação de alterações de aplicação sem necessidade de períodos de inatividade programados. Isso garante lançamentos mais confiáveis e menos arriscados, possibilitando entregas rápidas e frequentes de novos serviços.

#### 5. APIs Declarativas e Infraestrutura Imutável

Aplicações cloud native aproveitam conceitos tecnológicos modernos em sua arquitetura:

* **APIs Declarativas:** Sistemas cloud native usam APIs para conectar microsserviços fracamente acoplados. Uma API declarativa especifica *o que* um serviço deseja de dados e *quais* resultados pode fornecer, em vez de definir os passos exatos para atingir o resultado.
* **Infraestrutura Imutável:** Esse princípio significa que os servidores que hospedam aplicações cloud native permanecem inalterados após a implantação. Se for necessário mudar algo, o servidor antigo é descartado e a aplicação é movida para um novo servidor de alto desempenho, tornando o processo de implantação previsível.

### Benefícios do Cloud Native

A abordagem cloud native oferece diversos benefícios:

| Categoria                            | Benefícios Específicos                                                                                                                                                                                                                                                                               |
| :----------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Velocidade e Agilidade**           | Aumenta a produtividade e a velocidade dos desenvolvedores. Permite inovação mais rápida devido a serviços menores e fracamente acoplados, possibilitando que equipes trabalhem de forma autônoma. Facilita a construção, teste e implantação rápidos, levando produtos ao mercado mais rapidamente. |
| **Confiabilidade e Disponibilidade** | Proporciona alta disponibilidade e resiliência, pois reduz a complexidade operacional e oferece *autoscaling* e *self-healing*. As implantações tornam-se mais confiáveis e menos arriscadas.                                                                                                        |
| **Escalabilidade**                   | Alcança maior escalabilidade com automação de infraestrutura, balanceando carga conforme a demanda e permitindo que equipes otimizem custo e desempenho.                                                                                                                                             |
| **Eficiência de Custos**             | Reduz significativamente os custos operacionais ao permitir compartilhamento de recursos e consumo sob demanda. Diminui despesas operacionais de longo prazo (OpEx), já que o investimento em manutenção de infraestrutura física é reduzido.                                                        |
| **Portabilidade e Segurança**        | Aplicações cloud native são projetadas para rodar praticamente em qualquer lugar, facilitando sua migração entre ambientes. Elas reduzem a superfície de ataque e são mais fáceis de atualizar e corrigir, resultando em maior segurança.                                                            |

### Desafios do Cloud Native

Apesar das vantagens, adotar o modelo cloud native apresenta alguns desafios e compensações:

* **Resistência Cultural:** A implementação bem-sucedida exige mudanças culturais significativas, indo além da adoção de novas ferramentas. Pode haver resistência em adotar as melhores práticas de DevOps.
* **Complexidade de Sistemas Distribuídos:** Lidar com sistemas distribuídos e inúmeros componentes pode ser desafiador se as ferramentas ou processos corretos para gerenciamento, desenvolvimento, teste e implantação não estiverem bem estabelecidos. É necessário administrar muitos serviços pequenos e discretos, em vez de uma única aplicação.
* **Gestão de Custos:** Há risco de aumento nos custos operacionais e tecnológicos sem estratégias adequadas de monitoramento e otimização do uso de recursos em ambientes de nuvem.
* **Lacuna de Habilidades:** Pode faltar pessoal com as competências tecnológicas necessárias para trabalhar e integrar uma pilha tecnológica cloud native mais complexa.

Cloud native é considerado uma **jornada contínua** de iteração e melhoria constante, e não um projeto único de múltiplos anos. Organizações que simplesmente adotam uma abordagem de “*lift and shift*” — migrando aplicações sem reestruturá-las com base nos princípios cloud native — perderão muitos dos benefícios potenciais.


### Bibliografia

[1] **ARUDEL, John; DOMINGUS, Justin.** *Cloud Native DevOps with Kubernetes: Building, Deploying and Scaling Modern Applications in the Cloud.* 1. ed. O'Reilly, 2019.

[2] **Google Cloud.** *What is cloud native?*. Disponível em: <https://cloud.google.com/learn/what-is-cloud-native?hl=en>. Acesso em: 29 out. 2025.

[3] **IBM.** *What is cloud native?*. Disponível em: <https://www.ibm.com/think/topics/cloud-native>. Acesso em: 29 out. 2025.

[4] **AWS.** *What is cloud native?*. Disponível em: <https://aws.amazon.com/what-is/cloud-native/>. Acesso em: 29 out. 2025.

[5] **Google Cloud.** *What is cloud computing?*. Disponível em: <https://cloud.google.com/learn/what-is-cloud-computing?hl=pt-BR>. Acesso em: 06 nov. 2025.