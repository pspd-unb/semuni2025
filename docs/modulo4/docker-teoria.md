# Containerização

## I. Containerização e Containers

**Containerização** é um método de implantar aplicações de software executando-as em ambientes isolados chamados **containers**. Essa abordagem abstrai as aplicações do ambiente em que elas rodam, permitindo implantação fácil e consistente — seja em um data center privado, em uma nuvem pública ou na máquina local de um desenvolvedor.

### O que são Containers?

Containers são **processos isolados** que executam componentes de uma aplicação. Eles são instâncias executáveis de uma imagem, fornecendo um ambiente protegido (*sandbox*). Containers aproveitam os **mecanismos de baixo nível do sistema operacional (SO) hospedeiro**, geralmente usando virtualização em nível de sistema operacional no Linux, para alcançar o isolamento. O Docker utiliza uma tecnologia chamada **namespaces** para fornecer esse espaço de trabalho isolado.

### Containers vs. Máquinas Virtuais (VMs)

A abordagem com containers difere significativamente do uso de máquinas virtuais:

* **VMs** executam aplicações dentro de um sistema operacional convidado separado, o que requer a virtualização de hardware sobre o sistema operacional hospedeiro. Isso gera uma sobrecarga computacional considerável.
* **Containers** são leves e compartilham o kernel do sistema operacional hospedeiro. Eles contêm tudo o que é necessário para executar a aplicação (arquivos, binários, bibliotecas e configurações), sem depender de dependências pré-instaladas no host. Isso permite melhor aproveitamento de recursos e a execução de mais aplicações em menos infraestrutura.

### Características dos Containers

Containers são valorizados por sua consistência e eficiência:

* **Autossuficientes:** Cada container possui todos os arquivos e dependências de que precisa para funcionar.
* **Isolados:** Containers rodam de forma isolada, reduzindo sua influência no host e em outros containers, aumentando a segurança.
* **Portáteis:** Containers podem ser executados em qualquer ambiente de forma consistente, oferecendo portabilidade de carga de trabalho e apoiando o conceito de “construa uma vez, execute em qualquer lugar”.
* **Independentes:** Cada container é gerenciado de forma independente; excluir um container não afeta os demais.

---

## II. Docker: A Plataforma

**Docker** é definido como um projeto *open source* e uma plataforma aberta para desenvolver, empacotar e executar aplicações. É uma ferramenta que automatiza a implantação de software dentro de containers. O principal benefício do Docker é permitir que usuários **empacotem uma aplicação com todas as suas dependências em uma unidade padronizada** para desenvolvimento de software.

### Arquitetura do Docker

O Docker opera utilizando uma **arquitetura cliente-servidor**:

| Componente                    | Descrição                                                                                                                                                                           | Citação |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| **Docker Daemon (`dockerd`)** | Serviço em segundo plano que roda no sistema hospedeiro, escutando requisições da API do Docker e gerenciando objetos Docker (como imagens, containers, redes e volumes).           |         |
| **Docker Client (`docker`)**  | Ferramenta de linha de comando (CLI) principal usada pelos usuários. Envia comandos (como `docker run`) para o daemon Docker executar.                                              |         |
| **Docker Desktop**            | Aplicativo para Mac, Windows ou Linux que inclui o Docker daemon, o cliente Docker, o Docker Compose e outras ferramentas essenciais, simplificando o processo de instalação e uso. |         |

### Casos de Uso do Docker

O Docker simplifica consideravelmente o ciclo de vida de desenvolvimento de software (fluxos CI/CD) ao oferecer:

* **Entrega Rápida e Consistente:** Desenvolvedores podem trabalhar em ambientes padronizados usando containers locais, o que facilita o compartilhamento, o teste e a implantação de atualizações em produção.
* **Escalabilidade Dinâmica:** A portabilidade e leveza do Docker tornam simples o gerenciamento dinâmico de cargas de trabalho, permitindo escalar aplicações ou encerrá-las quase em tempo real.
* **Eficiência:** O Docker é uma alternativa mais econômica a VMs baseadas em hipervisores, permitindo maior densidade de execução e melhor aproveitamento da capacidade dos servidores.

---

## III. Conceitos e Terminologia Fundamentais do Docker

### Imagens

**Imagens** são os modelos de uma aplicação e formam a base dos containers. Elas são *templates* de somente leitura que contêm instruções e configurações para criar um container.

* **Camadas:** As imagens são compostas por múltiplas **camadas**, cada uma representando um conjunto de alterações no sistema de arquivos. Essa estrutura torna as imagens leves, pois apenas as camadas modificadas precisam ser reconstruídas.
* **Criação de Imagens:** As imagens são criadas por meio de um **Dockerfile**, um arquivo de texto simples contendo uma lista de comandos (semelhantes aos comandos Linux) que automatizam o processo de construção da imagem.
* **Tipos:** Imagens sem pai são chamadas de **imagens base** (ex.: Ubuntu, Busybox), enquanto aquelas que se constroem sobre outras são **imagens filhas**. Imagens oficialmente mantidas pelo Docker são **imagens oficiais**, e as criadas e compartilhadas por usuários são **imagens de usuário**.
* **Gerenciamento de Imagens:** O comando `docker pull` baixa uma imagem de um registro, e `docker images` exibe uma lista de imagens disponíveis localmente.

### Registro (Docker Hub)

Um **Registro Docker** é um local centralizado para armazenar e compartilhar imagens de containers.

* O **Docker Hub** é o registro público padrão usado pelo Docker para buscar imagens.
* Um **repositório** é uma coleção de imagens relacionadas dentro de um registro, geralmente organizadas por projeto.
* O comando `docker push` é usado para publicar uma imagem em um registro.

### Containers (Gerenciamento via CLI)

Containers são criados a partir de imagens usando o comando `docker run`.

* O comando `docker run` inicializa o container e executa um comando especificado dentro dele. A flag `-it` pode ser usada para rodar o container em modo interativo.
* O comando `docker ps` mostra todos os containers em execução, enquanto `docker ps -a` exibe todos os containers, inclusive os que já foram encerrados.
* O comando `docker rm` é usado para excluir containers. A flag `--rm` pode ser usada junto ao `docker run` para excluir automaticamente o container após ele ser encerrado.

### Redes do Docker

A rede é essencial para que aplicações com múltiplos containers possam se comunicar.

* A **rede bridge** é a rede padrão na qual os containers são executados.
* **Redes bridge definidas pelo usuário** permitem que containers conectados à mesma rede se comuniquem entre si, permanecendo isolados de containers em outras redes.
* Quando containers são executados em uma rede definida pelo usuário, eles obtêm **descoberta automática de serviços**, permitindo comunicação por nome de container (ex.: `es`) em vez de endereços IP fixos, que podem mudar.

### Docker Compose

**Docker Compose** é uma ferramenta projetada especificamente para **definir e executar aplicações Docker com múltiplos containers**.

* **Configuração:** O Compose usa um único arquivo YAML (por exemplo, `docker-compose.yml` ou `compose.yaml`) para definir de forma declarativa todos os serviços que compõem a aplicação, junto com suas configurações (imagens, portas, redes, volumes).
* **Execução:** O comando `docker-compose up` inicia todo o conjunto de serviços e cria automaticamente uma rede para conectá-los.
* **Finalidade:** O Compose simplifica o gerenciamento de aplicações complexas, tornando-o ideal para ambientes de desenvolvimento e teste.

### Bibliografia

[1] **Prakhar Srivastav** *Docker Curriculum*. Disponível em: <https://docker-curriculum.com/#conclusion>. Acesso em: 29 out. 2025.

[2] **Docker Docs.** *What is docker compose?*. Disponível em: <https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/>. Acesso em: 29 out. 2025.

[3] **Docker Docs.** *What is a container?*. Disponível em: <https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/>. Acesso em: 29 out. 2025.

[4] **Docker Docs.** *What is a registry?*. Disponível em: <https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/>. Acesso em: 29 out. 2025.

[5] **Docker Docs.** *What is an image?*. Disponível em: <https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/>. Acesso em: 29 out. 2025.

[6] **Docker Docs.** *Docker Overview*. Disponível em: <https://docs.docker.com/get-started/docker-overview/>. Acesso em: 29 out. 2025.