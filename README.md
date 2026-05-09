<div align="center">

<img src="https://imgur.com/mcrdIGs.png" alt="Nexus Plataforms Banner" width="100%">

<br>
<br>

# 📨 DM MESSENGER v2.0

## *Sistema SaaS de Envio em Massa para Discord*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Discord](https://img.shields.io/badge/Discord-API-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/developers/docs/intro)
[![License](https://img.shields.io/badge/License-MIT-00D4AA?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

[![Status](https://img.shields.io/badge/Status-Online-2ea44f?style=flat-square)](https://github.com/LucasDesignerF/dm-messenger)
[![GitHub](https://img.shields.io/badge/GitHub-LucasDesignerF-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/LucasDesignerF)
[![Discord](https://img.shields.io/badge/Discord-Nexus_Plataforms-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/sFhQDjW534)

<br>

<img src="https://img.shields.io/badge/Interface-SaaS-00ACC1?style=for-the-badge&logo=cloud&logoColor=white">
<img src="https://img.shields.io/badge/Delay_Inteligente-20s-FF6D00?style=for-the-badge&logo=timer&logoColor=white">
<img src="https://img.shields.io/badge/Relatórios-JSON-FFCA28?style=for-the-badge&logo=json&logoColor=black">

</div>

---

## 📋 Índice

- [🎯 Visão Geral](#-visão-geral)
- [✨ Funcionalidades](#-funcionalidades)
- [📊 Preview do Sistema](#-preview-do-sistema)
- [🚀 Instalação](#-instalação)
- [⚙️ Configuração](#️-configuração)
- [🎮 Como Usar](#-como-usar)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [📊 Relatórios e Logs](#-relatórios-e-logs)
- [⚠️ Limitações e Boas Práticas](#️-limitações-e-boas-práticas)
- [🛠️ Tecnologias](#️-tecnologias)
- [👥 Créditos](#-créditos)
- [📄 Licença](#-licença)

---

## 🎯 Visão Geral

> **DM Messenger** é uma ferramenta SaaS (Software as a Service) profissional para envio de mensagens em massa via Direct Message (DM) no Discord. Desenvolvida para servidores que precisam comunicar novidades, atualizações ou avisos importantes para sua comunidade de forma eficiente e segura.

<div align="center">
  
![Preview](https://img.shields.io/badge/🎯_Envio_Inteligente-20_segundos_entre_mensagens-00D4AA?style=for-the-badge)
![Preview](https://img.shields.io/badge/📊_Relatórios_Detalhados-JSON_e_Logs-5865F2?style=for-the-badge)
![Preview](https://img.shields.io/badge/⏱️_Tempo_Estimado-Cálculo_automático-FF6D00?style=for-the-badge)

</div>

### 🌟 Diferenciais

| Característica | Descrição |
|----------------|-----------|
| **⚡ Delay Inteligente** | 20 segundos entre mensagens para evitar rate limit do Discord |
| **📊 Cálculo de Tempo** | Estima automaticamente o tempo total de envio |
| **📈 Barra de Progresso** | Visualização em tempo real do andamento |
| **📄 Relatórios JSON** | Salva estatísticas completas da execução |
| **🔍 Modo de Teste** | Envia mensagem apenas para você antes do envio em massa |
| **⚙️ Delay Configurável** | Ajuste o tempo entre mensagens conforme necessidade |

---

## ✨ Funcionalidades

### 🚀 **Envio Inteligente**
- ✅ Delay automático de 20 segundos entre mensagens
- ✅ Timer regressivo visual no console
- ✅ Pula automaticamente bots e o próprio owner
- ✅ Tratamento de erros (DMs bloqueadas, rate limit)

### 📊 **Interface Moderna**
- ✅ ASCII art estilizado
- ✅ Barra de progresso animada
- ✅ Menu interativo com 6 opções
- ✅ Cores e formatação visual

### 📈 **Relatórios Detalhados**
- ✅ Salva estatísticas em JSON
- ✅ Logs completos da execução
- ✅ Comparação tempo estimado vs real
- ✅ Contagem de sucessos e erros

### 🔧 **Configurações Flexíveis**
- ✅ Delay configurável (mínimo 5 segundos)
- ✅ Preview da mensagem antes de enviar
- ✅ Modo de teste seguro
- ✅ Visualização de relatórios anteriores

---

## 📊 Preview do Sistema

### Menu Principal
```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ██████╗ ███╗   ███╗     ███████╗███████╗███╗   ██╗██████╗ ███████╗
║   ██╔══██╗████╗ ████║     ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝
║   ██║  ██║██╔████╔██║     ███████╗█████╗  ██╔██╗ ██║██║  ██║███████╗
║   ██║  ██║██║╚██╔╝██║     ╚════██║██╔══╝  ██║╚██╗██║██║  ██║╚════██║
║   ██████╔╝██║ ╚═╝ ██║     ███████║███████╗██║ ╚████║██████╔╝███████║
║   ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝
║                                                              ║
║                   DM MESSENGER v2.0                          ║
║            Sistema SaaS de Envio em Massa                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════
📋 MENU PRINCIPAL
════════════════════════════════════════════════════════════════

  ╔══════════════════════════════════════════════════════════╗
  ║  [1] 🚀 ENVIO COMPLETO     - Enviar para todos os membros ║
  ║  [2] 🔍 MODO TESTE         - Enviar apenas para você       ║
  ║  [3] 📊 VER RELATÓRIO      - Visualizar último relatório   ║
  ║  [4] ⚙️  CONFIGURAR DELAY  - Alterar tempo entre envios    ║
  ║  [5] 📝 PREVIEW MENSAGEM   - Visualizar mensagem           ║
  ║  [6] 🚪 SAIR               - Finalizar programa            ║
  ╚══════════════════════════════════════════════════════════╝
```

### Barra de Progresso
```
╔══════════════════════════════════════════════════════════════╗
║  📨 ENVIANDO MENSAGENS                                       ║
╠══════════════════════════════════════════════════════════════╣
║  [████████████████████████░░░░░░] 78.5%                      ║
║                                                              ║
║  👤 Processando: Usuario123                                 ║
║  📊 Progresso: 157/200                                      ║
║  ✅ Sucessos: 150  ❌ Erros: 7                              ║
║  ⏱️ Tempo decorrido: 52 minutos                            ║
║  ⏳ Tempo restante: 14 minutos                             ║
╚══════════════════════════════════════════════════════════════╝
```

### Relatório Final
```
╔══════════════════════════════════════════════════════════════╗
║                       ✅ RESUMO                              ║
╠══════════════════════════════════════════════════════════════╣
║  ✅ Mensagens enviadas:  150                                 ║
║  ❌ Falhas/Erros:        7                                   ║
║  📊 Total processados:   157                                 ║
╠══════════════════════════════════════════════════════════════╣
║                       ⏱️ TEMPO                               ║
╠══════════════════════════════════════════════════════════════╣
║  ⏳ Tempo estimado:      52 minutos                          ║
║  🏁 Tempo real:          48 minutos                          ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🚀 Instalação

### Pré-requisitos

```bash
🐍 Python 3.11+
🤖 Discord Bot Token
📦 Permissão `Manage Roles` no servidor
```

### Passo a Passo

```bash
# 1. Clone o repositório
git clone https://github.com/LucasDesignerF/dm-messenger.git
cd dm-messenger

# 2. Crie ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instale dependências
pip install discord.py

# 4. Configure o token no script
# Edite o arquivo dm_messenger.py e cole seu token

# 5. Execute
python dm_messenger.py
```

---

## ⚙️ Configuração

### 1. Criar um Bot no Discord

1. Acesse [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em **"New Application"** e dê um nome
3. Vá em **"Bot"** → **"Add Bot"**
4. Copie o **Token** (⚠️ Mantenha em segredo!)
5. Ative as **Intents**:
   - ✅ `Server Members Intent`
   - ✅ `Message Content Intent`

### 2. Configurar o Script

Edite o arquivo `dm_messenger.py` e altere:

```python
class Config:
    DISCORD_TOKEN = "SEU_TOKEN_AQUI"  # Cole seu token
    GUILD_ID = 1291985673594736662    # ID do seu servidor
    OWNER_ID = 1219787450583486500    # Seu ID
```

### 3. Encontrar IDs

| ID | Como encontrar |
|----|----------------|
| **GUILD_ID** | Ativar Modo Desenvolvedor → Clique direito no servidor → Copiar ID |
| **OWNER_ID** | Ativar Modo Desenvolvedor → Clique direito em você → Copiar ID |

---

## 🎮 Como Usar

### Opção 1: Envio Completo
1. Execute `python dm_messenger.py`
2. Escolha opção `[1]`
3. Confirme digitando `SIM`
4. Acompanhe a barra de progresso
5. Veja o relatório final

### Opção 2: Modo Teste
1. Escolha opção `[2]`
2. Receba a mensagem no seu DM
3. Verifique se está correta

### Opção 3: Ver Relatório
1. Escolha opção `[3]`
2. Visualize estatísticas da última execução

### Opção 4: Configurar Delay
1. Escolha opção `[4]`
2. Digite novo delay (mínimo 5 segundos)
3. Configuração salva automaticamente

---

## 📁 Estrutura do Projeto

```
dm-messenger/
├── dm_messenger.py      # Script principal
├── dm_report.json       # Relatório da última execução
├── dm_messenger.log     # Logs completos
├── README.md            # Documentação
└── LICENSE              # Licença MIT
```

---

## 📊 Relatórios e Logs

### JSON Report (`dm_report.json`)
```json
{
  "success_count": 150,
  "error_count": 7,
  "total_processed": 157,
  "started_at": "2025-01-15 14:30:00",
  "finished_at": "2025-01-15 15:18:00",
  "estimated_time": "52 minutos",
  "actual_time": "48 minutos"
}
```

### Log File (`dm_messenger.log`)
```
[2025-01-15 14:30:00] 🚀 Iniciando envio em massa...
[2025-01-15 14:30:05] ✅ Mensagem enviada para Usuario1
[2025-01-15 14:30:25] ✅ Mensagem enviada para Usuario2
[2025-01-15 14:30:45] 🚫 Usuario3: DMs bloqueadas
```

---

## ⚠️ Limitações e Boas Práticas

### ⚡ Rate Limit do Discord
- **Limite:** ~50 mensagens por segundo por bot
- **Nossa solução:** Delay de 20 segundos (muito abaixo do limite)
- **Recomendação:** Nunca reduzir abaixo de 5 segundos

### 🚫 DMs Bloqueadas
- Usuários com DMs bloqueadas não receberão mensagem
- O script registra essas falhas no relatório
- Não há como contornar essa limitação

### 👑 Hierarquia de Cargos
- O bot não pode enviar DM para usuários com cargo superior
- O bot precisa estar no servidor

---

## 🛠️ Tecnologias

<div align="center">

| Tecnologia | Versão | Finalidade |
|------------|--------|------------|
| ![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square) | 3.11+ | Linguagem principal |
| ![discord.py](https://img.shields.io/badge/discord.py-2.4+-5865F2?style=flat-square) | 2.4+ | API do Discord |
| ![JSON](https://img.shields.io/badge/JSON-Relatórios-000000?style=flat-square) | - | Armazenamento de dados |

</div>

---

## 👥 Créditos

<div align="center">

### Desenvolvido com ❤️ por

| ![LucasDev](https://img.shields.io/badge/Lucas_Designer-000?style=for-the-badge&logo=github&logoColor=white) | ![Nexus Plataforms](https://img.shields.io/badge/Nexus_Plataforms-5865F2?style=for-the-badge&logo=discord&logoColor=white) |
|-----------|-------------|
| [@LucasDesignerF](https://github.com/LucasDesignerF) | Nexus Plataforms |

</div>

### 🔗 Links

- **GitHub:** [github.com/LucasDesignerF](https://github.com/LucasDesignerF)
- **Discord:** [discord.gg/sFhQDjW534](https://discord.gg/sFhQDjW534)
- **Repositório DM Messenger:** [github.com/LucasDesignerF/dm-messenger](https://github.com/LucasDesignerF/dm-messenger)

---

## 📄 Licença

```
MIT License

Copyright (c) 2025 LucasDesignerF - Nexus Plataforms

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

<div align="center">

## ⭐ **Dê uma estrela no GitHub se gostou do projeto!** ⭐

---

### 📞 Suporte

[![Discord](https://img.shields.io/badge/Entre_no_Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/sFhQDjW534)
[![GitHub](https://img.shields.io/badge/Ver_no_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/LucasDesignerF)

---

**DM Messenger © 2025 | Nexus Plataforms**

*"Comunicação eficiente para sua comunidade Discord"*

</div>
