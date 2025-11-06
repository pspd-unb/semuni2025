# CI/CD - Continuous Integration & Continuous Deployment

## O que é CI/CD?

**CI/CD** é uma metodologia de desenvolvimento que combina **Continuous Integration (CI)** e **Continuous Deployment/Delivery (CD)** para automatizar o processo de desenvolvimento, teste e deployment de software.

### Continuous Integration (CI)
**Integração Contínua** é a prática de integrar código frequentemente ao repositório principal, onde cada integração é verificada por builds automáticos e testes.

**Benefícios:**
- ✅ Detecção precoce de bugs
- ✅ Redução de conflitos de merge
- ✅ Feedback rápido para desenvolvedores
- ✅ Melhoria na qualidade do código

### Continuous Deployment/Delivery (CD)
**Continuous Delivery:** Código sempre pronto para produção, mas deployment manual
**Continuous Deployment:** Deployment automático em produção após passar por todos os testes

**Benefícios:**
- ✅ Releases mais frequentes e confiáveis
- ✅ Redução de riscos de deployment
- ✅ Time-to-market mais rápido
- ✅ Rollbacks automáticos

## Pipeline CI/CD

Um pipeline CI/CD típico inclui as seguintes etapas:

```mermaid
graph LR
    A[Code Push] --> B[Build]
    B --> C[Unit Tests]
    C --> D[Integration Tests]
    D --> E[Security Scan]
    E --> F[Deploy Staging]
    F --> G[E2E Tests]
    G --> H[Deploy Production]
```

### Etapas do Pipeline

1. **Source/Trigger** - Push de código ou merge request
2. **Build** - Compilação e criação de artefatos
3. **Test** - Execução de testes automatizados
4. **Security** - Análise de vulnerabilidades
5. **Package** - Criação de imagens Docker ou pacotes
6. **Deploy** - Deployment em ambientes
7. **Monitor** - Monitoramento pós-deployment

## Principais Tecnologias CI/CD

### Plataformas de CI/CD

#### GitLab CI/CD
- ✅ Integrado ao GitLab
- ✅ Runners próprios ou compartilhados
- ✅ Arquivo `.gitlab-ci.yml`
- ✅ Docker Registry integrado

#### GitHub Actions
- ✅ Integrado ao GitHub
- ✅ Marketplace de actions
- ✅ Workflows em YAML
- ✅ Runners gratuitos e self-hosted

#### Jenkins
- ✅ Open source e extensível
- ✅ Plugins abundantes
- ✅ Pipeline as Code (Jenkinsfile)
- ✅ Distribuído

#### Azure DevOps
- ✅ Ecossistema Microsoft
- ✅ Azure Pipelines
- ✅ Integração com Azure
- ✅ Agentes próprios ou Microsoft

#### CircleCI
- ✅ Cloud-native
- ✅ Configuração YAML
- ✅ Docker-first
- ✅ Orbs (pacotes reutilizáveis)

### Ferramentas Complementares

#### Controle de Versão
- **Git** - Controle de versão distribuído
- **GitFlow** - Modelo de branching
- **Semantic Versioning** - Versionamento semântico

#### Testes
- **Jest/Mocha** - Testes JavaScript
- **JUnit** - Testes Java
- **PyTest** - Testes Python
- **Selenium** - Testes E2E
- **SonarQube** - Qualidade de código

#### Containerização
- **Docker** - Containerização
- **Kubernetes** - Orquestração
- **Helm** - Gerenciamento de deployments K8s

#### Monitoramento
- **Prometheus** - Métricas
- **Grafana** - Dashboards
- **ELK Stack** - Logs
- **Sentry** - Error tracking

## CI/CD com GitLab - Passo a Passo

### 1. Configuração Inicial

#### Estrutura do Projeto
```
projeto/
├── .gitlab-ci.yml          # Configuração CI/CD
├── Dockerfile              # Imagem Docker
├── docker-compose.yml      # Desenvolvimento local
├── k8s/                    # Manifests Kubernetes
│   ├── deployment.yaml
│   └── service.yaml
└── src/                    # Código fonte
```

### 2. Arquivo .gitlab-ci.yml Básico

```yaml
# Definir stages do pipeline
stages:
  - build
  - test
  - security
  - package
  - deploy

# Variáveis globais
variables:
  DOCKER_REGISTRY: registry.gitlab.com
  IMAGE_NAME: $CI_REGISTRY_IMAGE
  DOCKER_DRIVER: overlay2

# Configurações globais
before_script:
  - echo "Starting pipeline for $CI_COMMIT_REF_NAME"

# Stage: Build
build:
  stage: build
  image: node:18-alpine
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour
  only:
    - main
    - develop
    - merge_requests
```

### 3. Pipeline Completo para Aplicação Node.js

```yaml
stages:
  - build
  - test
  - security
  - package
  - deploy-staging
  - deploy-production

variables:
  NODE_VERSION: "18"
  DOCKER_REGISTRY: $CI_REGISTRY
  IMAGE_NAME: $CI_REGISTRY_IMAGE
  STAGING_URL: https://app-staging.exemplo.com
  PRODUCTION_URL: https://app.exemplo.com

# Cache para node_modules
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/

# Build da aplicação
build:
  stage: build
  image: node:${NODE_VERSION}-alpine
  script:
    - npm ci
    - npm run build
    - echo "Build completed successfully"
  artifacts:
    paths:
      - dist/
      - node_modules/
    expire_in: 1 hour
  only:
    - main
    - develop
    - merge_requests

# Testes unitários
test:unit:
  stage: test
  image: node:${NODE_VERSION}-alpine
  script:
    - npm run test:unit
    - npm run test:coverage
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
    paths:
      - coverage/
  only:
    - main
    - develop
    - merge_requests

# Testes de integração
test:integration:
  stage: test
  image: node:${NODE_VERSION}-alpine
  services:
    - postgres:13
    - redis:6-alpine
  variables:
    POSTGRES_DB: test_db
    POSTGRES_USER: test_user
    POSTGRES_PASSWORD: test_pass
    DATABASE_URL: postgresql://test_user:test_pass@postgres:5432/test_db
  script:
    - npm run test:integration
  only:
    - main
    - develop

# Análise de segurança com SAST
security:sast:
  stage: security
  image: node:${NODE_VERSION}-alpine
  script:
    - npm audit --audit-level high
    - npx retire --severity medium
  allow_failure: true
  only:
    - main
    - develop

# Build da imagem Docker
package:
  stage: package
  image: docker:20.10.16
  services:
    - docker:20.10.16-dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $IMAGE_NAME:$CI_COMMIT_SHA .
    - docker build -t $IMAGE_NAME:latest .
    - docker push $IMAGE_NAME:$CI_COMMIT_SHA
    - docker push $IMAGE_NAME:latest
  only:
    - main
    - develop

# Deploy em staging
deploy:staging:
  stage: deploy-staging
  image: alpine/helm:latest
  environment:
    name: staging
    url: $STAGING_URL
  script:
    - apk add --no-cache curl
    - helm upgrade --install app-staging ./k8s/helm-chart 
      --set image.tag=$CI_COMMIT_SHA 
      --set ingress.host=$STAGING_URL
      --namespace staging
      --create-namespace
  only:
    - develop

# Deploy em produção (manual)
deploy:production:
  stage: deploy-production
  image: alpine/helm:latest
  environment:
    name: production
    url: $PRODUCTION_URL
  script:
    - helm upgrade --install app-prod ./k8s/helm-chart 
      --set image.tag=$CI_COMMIT_SHA 
      --set ingress.host=$PRODUCTION_URL
      --namespace production
      --create-namespace
  when: manual
  only:
    - main
```

### 4. Configurações Avançadas

#### Multi-environment com Review Apps
```yaml
# Review apps para merge requests
review:
  stage: deploy
  image: alpine/helm:latest
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    url: https://$CI_COMMIT_REF_SLUG.review.exemplo.com
    on_stop: stop_review
  script:
    - helm upgrade --install review-$CI_COMMIT_REF_SLUG ./k8s/helm-chart
      --set image.tag=$CI_COMMIT_SHA
      --set ingress.host=$CI_COMMIT_REF_SLUG.review.exemplo.com
      --namespace review
  only:
    - merge_requests

# Parar review app
stop_review:
  stage: deploy
  image: alpine/helm:latest
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    action: stop
  script:
    - helm uninstall review-$CI_COMMIT_REF_SLUG --namespace review
  when: manual
  only:
    - merge_requests
```

#### Deploy com Blue-Green
```yaml
deploy:blue-green:
  stage: deploy
  image: kubectl:latest
  script:
    # Deploy na versão blue
    - kubectl set image deployment/app-blue app=$IMAGE_NAME:$CI_COMMIT_SHA
    - kubectl rollout status deployment/app-blue
    
    # Testes de smoke
    - curl -f http://blue.exemplo.com/health
    
    # Switch do tráfego
    - kubectl patch service app-service -p '{"spec":{"selector":{"version":"blue"}}}'
    
    # Aguardar e verificar
    - sleep 30
    - curl -f http://app.exemplo.com/health
  when: manual
  only:
    - main
```

### 5. GitLab Runner Configuration

#### Configurar GitLab Runner (Self-hosted)
```bash
# Instalar GitLab Runner
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
sudo apt-get install gitlab-runner

# Registrar runner
sudo gitlab-runner register \
  --url "https://gitlab.com/" \
  --registration-token "YOUR_TOKEN" \
  --executor "docker" \
  --docker-image "alpine:latest" \
  --description "docker-runner" \
  --tag-list "docker,aws" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"
```

#### Runner com Docker-in-Docker
```toml
# /etc/gitlab-runner/config.toml
[[runners]]
  name = "docker-runner"
  url = "https://gitlab.com/"
  token = "YOUR_TOKEN"
  executor = "docker"
  [runners.docker]
    tls_verify = false
    image = "docker:20.10.16"
    privileged = true
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
    shm_size = 0
```

### 6. Boas Práticas CI/CD

#### Segurança
```yaml
# Usar secrets do GitLab
variables:
  DATABASE_URL: $DATABASE_URL  # Variável protegida
  API_KEY: $API_KEY           # Variável mascarada

# Scan de vulnerabilidades
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Container-Scanning.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml
```

#### Performance
```yaml
# Cache inteligente
cache:
  key: 
    files:
      - package-lock.json
  paths:
    - node_modules/

# Paralelização de jobs
test:
  parallel: 3
  script:
    - npm run test -- --testPathPattern=$((CI_NODE_INDEX-1))
```

#### Monitoramento
```yaml
# Notificações Slack
notify:slack:
  stage: .post
  image: alpine:latest
  script:
    - apk add --no-cache curl
    - |
      curl -X POST -H 'Content-type: application/json' \
      --data '{"text":"Deploy completed: '$PRODUCTION_URL'"}' \
      $SLACK_WEBHOOK_URL
  when: on_success
  only:
    - main
```

### 7. Exemplo com Múltiplos Ambientes

```yaml
# Configuração por ambiente
.deploy_template: &deploy_template
  image: alpine/helm:latest
  script:
    - helm upgrade --install $APP_NAME ./k8s/helm-chart
      --set image.tag=$CI_COMMIT_SHA
      --set ingress.host=$APP_URL
      --set resources.limits.memory=$MEMORY_LIMIT
      --namespace $NAMESPACE
      --create-namespace

deploy:development:
  <<: *deploy_template
  stage: deploy
  environment:
    name: development
    url: https://app-dev.exemplo.com
  variables:
    APP_NAME: app-dev
    APP_URL: app-dev.exemplo.com
    NAMESPACE: development
    MEMORY_LIMIT: 512Mi
  only:
    - develop

deploy:staging:
  <<: *deploy_template
  stage: deploy
  environment:
    name: staging
    url: https://app-staging.exemplo.com
  variables:
    APP_NAME: app-staging
    APP_URL: app-staging.exemplo.com
    NAMESPACE: staging
    MEMORY_LIMIT: 1Gi
  only:
    - main

deploy:production:
  <<: *deploy_template
  stage: deploy
  environment:
    name: production
    url: https://app.exemplo.com
  variables:
    APP_NAME: app-prod
    APP_URL: app.exemplo.com
    NAMESPACE: production
    MEMORY_LIMIT: 2Gi
  when: manual
  only:
    - main
```

## Troubleshooting Comum

### Problemas Frequentes

1. **Build falha por dependências**
   ```yaml
   # Solução: Cache e retry
   cache:
     key: ${CI_COMMIT_REF_SLUG}
     paths:
       - node_modules/
   
   retry:
     max: 2
     when: runner_system_failure
   ```

2. **Testes flaky**
   ```yaml
   # Solução: Retry em testes
   test:
     retry:
       max: 3
       when:
         - unknown_failure
         - script_failure
   ```

3. **Deploy timeout**
   ```yaml
   # Solução: Timeout customizado
   deploy:
     timeout: 10m
     script:
       - kubectl rollout status deployment/app --timeout=600s
   ```

### Monitoramento de Pipeline

```yaml
# Métricas de pipeline
pipeline:metrics:
  stage: .post
  image: alpine:latest
  script:
    - echo "Pipeline duration: $CI_PIPELINE_DURATION"
    - echo "Jobs failed: $CI_PIPELINE_FAILED_JOBS"
  when: always
```