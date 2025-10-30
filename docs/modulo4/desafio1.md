# 🚀 Desafio 1: Do Dev ao Deploy - Containerize Tudo!

## 🎯 Seu Desafio

Bem-vindo ao **Desafio 1**! Aqui você vai colocar a mão na massa e transformar uma aplicação completa em um ambiente totalmente containerizado, automatizado e pronto para produção. 

Você recebeu uma aplicação **Django + Next.js** que funciona... mas só localmente. Seu desafio? Fazer ela rodar em containers, criar pipelines de CI/CD e preparar tudo para um deploy profissional! 💪

### 🎮 Regras do Jogo

!!! tip "Como Jogar"
    - Cada fase do desafio deve ser concluída em um **commit separado**
    - Sua aplicação deve funcionar no final de cada etapa
    - Use os tutoriais como guias, mas sinta-se livre para explorar!
    - Trabalhe no seu próprio ritmo, mas complete todas as fases

!!! info "Prepare seu Ambiente"
    Antes de começar, faça um fork do repositório original e crie seu próprio repositório privado. Assim você pode experimentar à vontade sem medo de errar!

## 🎮 Fases do Desafio

### 🐳 Fase 1: Containerize o Ambiente de DEV

**Objetivo**: Transformar sua aplicação em containers que rodam perfeitamente no seu ambiente de desenvolvimento!

Sua aplicação tem duas partes: um **backend** em Django e um **frontend** em Next.js. Atualmente ela usa SQLite, mas você vai precisar do Postgres.

**Missão**:
- Crie um `Dockerfile` para o backend (Django)
- Crie um `Dockerfile` para o frontend (Next.js)
- Configure tudo em modo desenvolvimento com:
    - ✅ Debug habilitado
    - ✅ Hot reload ativado (suas mudanças no código aparecem instantaneamente!)
    - ✅ Variáveis de ambiente para DEV

!!! success "Checkpoint"
    Ao final desta fase, você deve conseguir rodar cada container individualmente e ver suas mudanças de código refletidas imediatamente!

---

### 🎼 Fase 2: Orquestre Tudo com Docker Compose (DEV)

**Objetivo**: Fazer todos os serviços conversarem entre si!

**Missão**:
- Crie um arquivo `docker-compose.yml` que combine:
    - 🎨 Container do Frontend
    - 🔧 Container do Backend  
    - 🗄️ Container do Postgres
- Configure as redes para que tudo se comunique

!!! success "Checkpoint"
    Vitória! Com um simples `docker compose up`, toda sua aplicação deve subir funcionando perfeitamente! 🎉

---

### ⚙️ Fase 3: Pipeline de CI - Automatize a Qualidade

**Objetivo**: Criar um pipeline que verifica automaticamente se seu código está em ordem!

**Missão**: Configure o Gitlab CI com as seguintes etapas:

=== "3.1 Build 🔨"
    
    Garanta que sua aplicação compila sem erros

=== "3.2 Testes 🧪"
    
    Crie testes unitários simples para:
    
    - Frontend (pelo menos 1 teste)
    - Backend (pelo menos 1 teste)

=== "3.3 Lint 🧹"
    
    Configure linters para manter seu código limpo e padronizado

!!! warning "Desafio Extra"
    Mostre que seu pipeline funciona! Faça commits que:
    
    1. ❌ Quebram o build (e veja o pipeline falhar)
    2. ❌ Falham nos testes
    3. ❌ Não passam no lint
    4. ✅ Passam em tudo!

---

### 🏭 Fase 4: Containers de PRODUÇÃO - Otimize!

**Objetivo**: Criar containers otimizados e seguros para produção!

**Missão**:
- Crie novos `Dockerfiles` baseados em **Alpine Linux** (super leve!)
- Configure tudo em modo produção:
    - ❌ Debug desabilitado
    - ✅ Código otimizado e minificado
    - ✅ Build dos arquivos estáticos do frontend
    - ✅ Tudo autocontido nos containers

!!! tip "Pro Tip"
    Containers de produção devem ser leves, rápidos e seguros. Pense em tamanho e segurança!

---

### 🚀 Fase 5: Stack Completo de PRODUÇÃO

**Objetivo**: Monte a stack completa pronta para o mundo real!

**Missão**: Crie o `docker-compose-prod.yml` com:

- 🎨 Frontend servido pelo Nginx
- 🔧 Backend em produção
- 🗄️ Postgres com credenciais de produção (não use as mesmas de DEV!)
- 🔒 SSL configurado (HTTPS na porta 443)
- 🔄 Redirecionamento de HTTP (80) para HTTPS (443)

!!! success "Checkpoint Final de Produção"
    Sua aplicação deve:
    
    - ✅ Subir com `docker compose -f docker-compose-prod.yml up`
    - ✅ Ser acessível APENAS via HTTPS
    - ✅ Não expor portas desnecessárias
    - ✅ Estar segura e otimizada!

---

### 🎯 Fase 6: Deploy Contínuo - Automatize Tudo!

**Objetivo**: O grand finale! Deploy automático após passar no CI!

**Missão**:
- Configure o CD para publicar automaticamente suas imagens no **Container Registry** do Gitlab
- O deploy só deve acontecer se TODAS as etapas de CI passarem
- Publique as imagens de produção do frontend e backend

!!! success "🏆 Desafio Completo!"
    Parabéns! Você criou um pipeline completo de DevOps, do desenvolvimento ao deploy automatizado! 🎊


## 📊 Checklist do Desafio

Acompanhe seu progresso:

| Fase | Descrição | Status |
|------|-----------|--------|
| 🐳 **Fase 1** | Containerização da Aplicação (DEV) | ⬜ |
| 🎼 **Fase 2** | Docker Compose - Stack Completa (DEV) | ⬜ |
| ⚙️ **Fase 3** | Integração Contínua (CI) | ⬜ |
| &nbsp;&nbsp;&nbsp;↳ 3.1 | Build automatizado | ⬜ |
| &nbsp;&nbsp;&nbsp;↳ 3.2 | Testes unitários | ⬜ |
| &nbsp;&nbsp;&nbsp;↳ 3.3 | Lint do código | ⬜ |
| 🏭 **Fase 4** | Containers Otimizados (PROD) | ⬜ |
| 🚀 **Fase 5** | Stack Completa com SSL (PROD) | ⬜ |
| 🎯 **Fase 6** | Deploy Contínuo (CD) | ⬜ |

!!! quote "Dica de Ouro"
    Não tenha pressa! É melhor completar cada fase com qualidade do que correr e ficar preso depois. Cada fase constrói sobre a anterior! 🏗️


---

## 📦 Sobre o Projeto Base

Você vai trabalhar com uma aplicação fullstack moderna: **Django + Next.js**

### 🗂️ Estrutura do Projeto

O projeto está organizado como um monorepo (tudo em um só lugar!):

```bash
.
├── api                          # Backend Django
│   ├── config
│   ├── core_apps
│   ├── manage.py
│   ├── pytest.ini
│   └── requirements.txt
│   └── ...
├── README.md
└── web                          # Frontend NextJS
    ├── components.json
    ├── next.config.mjs
    ├── package.json
    ├── package-lock.json
    ├── public
    ├── src
    ├── tsconfig.json
    └── ...
```

### 🏃 Quer Testar Localmente Primeiro?

Antes de containerizar, você pode rodar a aplicação localmente para entender como ela funciona!

#### 🔧 Pré-requisitos

!!! info "Ferramentas Necessárias"
    - Python 3.11+
    - Node.js 20+ e npm
    - Git

#### 📥 Clone o Projeto

```bash
git clone https://github.com/FGA-GCES/trabalho-individual-2024-2.git
cd trabalho-individual-2024-2
```

#### 🔧 Configurando o Backend (Django)

```bash
# Entre no diretório do backend
cd api

# Criar e ativar um ambiente virtual (Linux/MacOS)
python -m venv venv
source venv/bin/activate

# No Windows:
???

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

!!! success "Backend Rodando!"
    Acesse: `http://localhost:8000` ✅

#### 🎨 Configurando o Frontend (Next.js)

```bash
# Entre no diretório do frontend
cd web

# Instale as dependências
npm install

# Crie um arquivo .env.local baseado no exemplo
cp .env.example .env.local

# Inicie o servidor de desenvolvimento
npm run dev
```

!!! success "Frontend Rodando!"
    Acesse: `http://localhost:3000` 🎉

---

## 🎓 Dicas para o Sucesso

!!! tip "Estratégias Vencedoras"
    
    **📖 Leia a Documentação**: Docker e Gitlab CI têm ótimas docs - use-as!
    
    **🔍 Debug Incrementalmente**: Teste cada pequena mudança antes de avançar
    
    **💾 Commit Frequentemente**: Pequenos commits funcionais são seus amigos
    
    **🤝 Colabore**: Stuck? Pergunte! DevOps é sobre colaboração
    
    **🧪 Teste Localmente**: Sempre teste localmente antes de fazer push

!!! warning "Armadilhas Comuns"
    
    - ⚠️ Não usar as mesmas credenciais de DEV em PROD
    - ⚠️ Esquecer de expor as portas corretas nos containers
    - ⚠️ Não configurar as variáveis de ambiente adequadamente
    - ⚠️ Ignorar os logs quando algo falha

## 🏆 Critérios de Sucesso

Você completou o desafio quando:

✅ Todos os containers funcionam perfeitamente  
✅ O pipeline de CI/CD está verde  
✅ A aplicação roda em modo produção com SSL  
✅ Você consegue fazer deploy automatizado  
✅ O código está documentado e organizado  

**Boa sorte, e que a força do Docker esteja com você!** 🐳✨
