# Containerização - Prática Docker

## Principais Comandos Docker

### Comandos Básicos de Imagens

```bash
# Listar todas as imagens locais
docker images

# Buscar uma imagem no Docker Hub
docker search nginx

# Baixar uma imagem do registro
docker pull ubuntu:20.04

# Remover uma imagem
docker rmi nginx:latest

# Construir uma imagem a partir de um Dockerfile
docker build -t minha-app:1.0 .

# Construir com argumentos
docker build --build-arg NODE_VERSION=18 -t minha-app .
```

### Comandos de Containers

```bash
# Executar um container
docker run hello-world

# Executar em modo interativo
docker run -it ubuntu:20.04 /bin/bash

# Executar em background (daemon)
docker run -d nginx

# Executar mapeando portas
docker run -p 8080:80 nginx

# Executar com volumes
docker run -v /host/path:/container/path nginx

# Executar com variáveis de ambiente
docker run -e NODE_ENV=production minha-app

# Listar containers em execução
docker ps

# Listar todos os containers (incluindo parados)
docker ps -a

# Parar um container
docker stop container_id

# Iniciar um container parado
docker start container_id

# Reiniciar um container
docker restart container_id

# Remover um container
docker rm container_id

# Remover todos os containers parados
docker container prune
```

### Comandos de Logs e Monitoramento

```bash
# Visualizar logs de um container
docker logs container_id

# Seguir logs em tempo real
docker logs -f container_id

# Executar comando em container em execução
docker exec -it container_id /bin/bash

# Inspecionar detalhes de um container
docker inspect container_id

# Verificar estatísticas de uso
docker stats

# Verificar processos em execução no container
docker top container_id
```

### Comandos de Limpeza

```bash
# Remover containers parados, redes não utilizadas, imagens órfãs
docker system prune

# Remover tudo (incluindo volumes)
docker system prune -a --volumes

# Remover apenas imagens não utilizadas
docker image prune

# Remover apenas volumes não utilizados
docker volume prune
```

## Dockerfile - Passo a Passo

### 1. Estrutura Básica

Um Dockerfile é um arquivo de texto que contém instruções para construir uma imagem Docker. Aqui estão as principais cláusulas:

### 2. Principais Instruções do Dockerfile

#### FROM - Imagem Base
```dockerfile
# Define a imagem base (sempre a primeira instrução)
FROM ubuntu:20.04

# Ou uma imagem mais específica
FROM node:18-alpine

# Multi-stage build
FROM node:18 AS builder
```

#### WORKDIR - Diretório de Trabalho
```dockerfile
# Define o diretório de trabalho dentro do container
WORKDIR /app

# Todos os comandos subsequentes serão executados neste diretório
```

#### COPY e ADD - Copiar Arquivos
```dockerfile
# Copiar arquivos do host para o container
COPY package.json ./
COPY src/ ./src/

# Copiar tudo do contexto atual
COPY . .

# ADD também pode extrair arquivos e baixar URLs
ADD arquivo.tar.gz /app/
```

#### RUN - Executar Comandos
```dockerfile
# Executar comandos durante a construção da imagem
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências Node.js
RUN npm install

# Múltiplas instruções RUN (cada uma cria uma nova camada)
RUN mkdir -p /app/logs
RUN chown -R node:node /app
```

#### EXPOSE - Expor Portas
```dockerfile
# Documenta as portas que o container usa
EXPOSE 3000
EXPOSE 8080 443
```

#### ENV - Variáveis de Ambiente
```dockerfile
# Definir variáveis de ambiente
ENV NODE_ENV=production
ENV PORT=3000
ENV DATABASE_URL=postgresql://user:pass@db:5432/myapp
```

#### USER - Usuário de Execução
```dockerfile
# Definir usuário para executar comandos
USER node

# Criar usuário personalizado
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs
USER nextjs
```

#### CMD e ENTRYPOINT - Comando de Execução
```dockerfile
# CMD - comando padrão (pode ser sobrescrito)
CMD ["npm", "start"]
CMD ["node", "server.js"]

# ENTRYPOINT - ponto de entrada fixo
ENTRYPOINT ["docker-entrypoint.sh"]

# Combinação ENTRYPOINT + CMD
ENTRYPOINT ["node"]
CMD ["server.js"]
```

### 3. Exemplo Prático - Aplicação Node.js

Aqui está um exemplo completo de Dockerfile para uma aplicação Node.js:

```dockerfile
# Usar imagem base do Node.js
FROM node:18-alpine

# Definir variáveis de ambiente
ENV NODE_ENV=production
ENV PORT=3000

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY package*.json ./

# Instalar dependências
RUN npm ci --only=production && npm cache clean --force

# Criar usuário não-root para segurança
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# Copiar código da aplicação
COPY --chown=nextjs:nodejs . .

# Mudar para usuário não-root
USER nextjs

# Expor porta
EXPOSE 3000

# Comando para executar a aplicação
CMD ["npm", "start"]
```

### 4. Exemplo com Multi-Stage Build

Para aplicações que precisam de compilação:

```dockerfile
# Stage 1: Build
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine AS production

WORKDIR /app

# Copiar apenas os arquivos necessários do stage anterior
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./

RUN npm ci --only=production

EXPOSE 3000
CMD ["npm", "start"]
```

### 5. Boas Práticas

#### Use .dockerignore
Crie um arquivo `.dockerignore` para excluir arquivos desnecessários:

```
node_modules
npm-debug.log
.git
.gitignore
README.md
.env
coverage
.nyc_output
```

#### Otimize as Camadas
```dockerfile
# ❌ Ruim - cria muitas camadas
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN rm -rf /var/lib/apt/lists/*

# ✅ Bom - uma única camada
RUN apt-get update && \
    apt-get install -y curl git && \
    rm -rf /var/lib/apt/lists/*
```

#### Use Imagens Pequenas
```dockerfile
# ✅ Prefira imagens alpine (menores)
FROM node:18-alpine

# ✅ Ou use distroless para produção
FROM gcr.io/distroless/nodejs18-debian11
```

### 6. Comandos para Construir e Executar

```bash
# Construir a imagem
docker build -t minha-app:latest .

# Executar o container
docker run -p 3000:3000 minha-app:latest

# Executar com variáveis de ambiente
docker run -p 3000:3000 -e NODE_ENV=development minha-app:latest

# Executar com volume para desenvolvimento
docker run -p 3000:3000 -v $(pwd):/app minha-app:latest
```

### 7. Dockerfile para Diferentes Tecnologias

#### Python/Django
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### Java/Spring Boot
```dockerfile
FROM openjdk:17-jre-slim

WORKDIR /app

COPY target/app.jar app.jar

EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
```

#### Go
```dockerfile
# Multi-stage para Go
FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY go.* ./
RUN go mod download

COPY . .
RUN go build -o main .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/

COPY --from=builder /app/main .
CMD ["./main"]
```
