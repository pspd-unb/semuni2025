# Introdução ao Cloud Native

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