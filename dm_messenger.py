"""
DM MESSENGER - ENVIO DE MENSAGENS EM MASSA
Sistema SaaS moderno para envio de comunicados em massa via Discord DM
Com cálculo de tempo estimado, timer visual e relatórios detalhados
"""

import discord
import asyncio
import sys
import time
from datetime import datetime, timedelta
import json
import os

# =========================
# CONFIGURAÇÕES
# =========================

class Config:
    """Configurações do sistema"""
    DISCORD_TOKEN = "Seu_TokenBot_aqui"
    GUILD_ID = 1234567890
    OWNER_ID = 1234567890
    DELAY_BETWEEN_MESSAGES = 20  # segundos
    
    # Relatório
    REPORT_FILE = "dm_report.json"
    LOG_FILE = "dm_messenger.log"

# =========================
# MENSAGEM
# =========================

MESSAGE = """Escreva sua mensagem aqui
Voce pode usar:
- Links
- Emojis
- Imagens
Bom uso, troque essa mensagem sem remover as aspas.
"""

# =========================
# UTILS
# =========================

def format_time(seconds: int) -> str:
    """Formata segundos em tempo legível"""
    if seconds < 60:
        return f"{seconds} segundos"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes} minutos e {remaining_seconds} segundos"
    else:
        hours = seconds // 3600
        remaining_minutes = (seconds % 3600) // 60
        return f"{hours} horas e {remaining_minutes} minutos"

def save_report(report: dict):
    """Salva relatório em arquivo JSON"""
    try:
        with open(Config.REPORT_FILE, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n📄 Relatório salvo em: {Config.REPORT_FILE}")
    except Exception as e:
        print(f"⚠️ Erro ao salvar relatório: {e}")

def log_message(msg: str):
    """Registra mensagem no log"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {msg}"
    print(log_entry)
    try:
        with open(Config.LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')
    except:
        pass

# =========================
# CLASSE PRINCIPAL
# =========================

class DMMessenger:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.members = True
        self.intents.guilds = True
        self.intents.dm_messages = True
        self.bot = discord.Client(intents=self.intents)
        self.start_time = None
        
        # Estatísticas
        self.stats = {
            'total_members': 0,
            'success_count': 0,
            'skip_count': 0,
            'error_count': 0,
            'blocked_dms': 0,
            'started_at': None,
            'finished_at': None,
            'estimated_time': None,
            'actual_time': None
        }
        
        @self.bot.event
        async def on_ready():
            await self.on_ready()
    
    async def show_header(self):
        """Exibe cabeçalho estilizado"""
        print("""
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
║            Sistema SaaS de Envio em Massa                    ║
║                    By Lucas Fortes                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    async def show_menu(self):
        """Exibe menu interativo"""
        print("\n" + "═"*60)
        print("📋 MENU PRINCIPAL")
        print("═"*60)
        print("""
  ╔══════════════════════════════════════════════════════════╗
  ║  [1] 🚀 ENVIO COMPLETO     - Enviar para todos os membros  ║
  ║  [2] 🔍 MODO TESTE         - Enviar apenas para você       ║
  ║  [3] 📊 VER RELATÓRIO      - Visualizar último relatório   ║
  ║  [4] ⚙️  CONFIGURAR DELAY  - Alterar tempo entre envios    ║
  ║  [5] 📝 PREVIEW MENSAGEM   - Visualizar mensagem           ║
  ║  [6] 🚪 SAIR               - Finalizar programa            ║
  ╚══════════════════════════════════════════════════════════╝
        """)
        
        while True:
            try:
                opcao = input("👉 Digite sua opção (1-6): ")
                
                if opcao == "1":
                    await self.full_send()
                    break
                elif opcao == "2":
                    await self.test_mode()
                    break
                elif opcao == "3":
                    self.show_report()
                elif opcao == "4":
                    self.configure_delay()
                elif opcao == "5":
                    self.preview_message()
                elif opcao == "6":
                    print("\n👋 Saindo... Até logo!")
                    sys.exit(0)
                else:
                    print("❌ Opção inválida! Digite 1-6")
            except KeyboardInterrupt:
                print("\n\n👋 Saindo...")
                sys.exit(0)
    
    def preview_message(self):
        """Mostra preview da mensagem"""
        print("\n" + "═"*60)
        print("📝 PREVIEW DA MENSAGEM")
        print("═"*60)
        print("\n" + MESSAGE + "\n")
        print("═"*60)
        input("Pressione ENTER para continuar...")
    
    def configure_delay(self):
        """Configura o delay entre mensagens"""
        print("\n" + "═"*60)
        print("⚙️ CONFIGURAÇÃO DE DELAY")
        print("═"*60)
        print(f"Delay atual: {Config.DELAY_BETWEEN_MESSAGES} segundos")
        try:
            novo_delay = int(input("Novo delay (em segundos, mínimo 5): "))
            if novo_delay >= 5:
                Config.DELAY_BETWEEN_MESSAGES = novo_delay
                print(f"✅ Delay atualizado para {novo_delay} segundos!")
            else:
                print("❌ Delay mínimo é 5 segundos!")
        except ValueError:
            print("❌ Valor inválido!")
        input("\nPressione ENTER para continuar...")
    
    def show_report(self):
        """Mostra relatório da última execução"""
        try:
            if os.path.exists(Config.REPORT_FILE):
                with open(Config.REPORT_FILE, 'r', encoding='utf-8') as f:
                    report = json.load(f)
                
                print("\n" + "═"*60)
                print("📊 RELATÓRIO DA ÚLTIMA EXECUÇÃO")
                print("═"*60)
                print(f"""
╔══════════════════════════════════════════════════════════════╗
║                       📈 ESTATÍSTICAS                        ║
╠══════════════════════════════════════════════════════════════╣
║  ✅ Enviadas com sucesso:  {report.get('success_count', 0):<30} ║
║  ⏭️  Puladas (Owner):        {report.get('skip_count', 0):<30} ║
║  🚫 Bloqueadas/Erros:       {report.get('error_count', 0):<30} ║
║  📊 Total processados:      {report.get('total_processed', 0):<30} ║
╠══════════════════════════════════════════════════════════════╣
║                        ⏱️  TEMPO                             ║
╠══════════════════════════════════════════════════════════════╣
║  ⏰ Início:              {report.get('started_at', 'N/A'):<30} ║
║  🏁 Término:             {report.get('finished_at', 'N/A'):<30} ║
║  ⏱️ Duração total:        {report.get('actual_time', 'N/A'):<30} ║
║  ⏳ Tempo estimado:       {report.get('estimated_time', 'N/A'):<30} ║
╚══════════════════════════════════════════════════════════════╝
                """)
            else:
                print("\n📭 Nenhum relatório encontrado. Execute o envio primeiro!")
        except Exception as e:
            print(f"❌ Erro ao ler relatório: {e}")
        
        input("\nPressione ENTER para continuar...")
    
    async def show_progress_bar(self, current, total, success, errors, start_time, member_name):
        """Exibe barra de progresso animada"""
        percent = (current / total) * 100
        bar_length = 30
        filled = int(bar_length * current // total)
        bar = '█' * filled + '░' * (bar_length - filled)
        
        elapsed = time.time() - start_time
        if current > 0:
            remaining = (elapsed / current) * (total - current)
            remaining_str = format_time(int(remaining))
        else:
            remaining_str = "calculando..."
        
        elapsed_str = format_time(int(elapsed))
        
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║  📨 ENVIANDO MENSAGENS                                       ║
╠══════════════════════════════════════════════════════════════╣
║  [{bar}] {percent:.1f}%                                      ║
║                                                              ║
║  👤 Processando: {member_name[:30]:<30}                     ║
║  📊 Progresso: {current}/{total}                            ║
║  ✅ Sucessos: {success}  ❌ Erros: {errors}                ║
║  ⏱️  Tempo decorrido: {elapsed_str:<25}                     ║
║  ⏳ Tempo restante: {remaining_str:<25}                     ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    async def test_mode(self):
        """Modo de teste - envia apenas para o owner"""
        print("\n" + "═"*60)
        print("🔍 MODO DE TESTE")
        print("═"*60)
        
        confirm = input("Enviar mensagem de teste para você? (s/N): ")
        if confirm.upper() != "S":
            print("❌ Teste cancelado.")
            return
        
        await self.bot.login(Config.DISCORD_TOKEN)
        await self.bot.connect()
    
    async def full_send(self):
        """Envia mensagens para todos os membros"""
        await self.bot.login(Config.DISCORD_TOKEN)
        await self.bot.connect()
    
    async def on_ready(self):
        """Evento quando o bot está pronto"""
        await self.show_header()
        
        guild = self.bot.get_guild(Config.GUILD_ID)
        if not guild:
            print(f"❌ Servidor com ID {Config.GUILD_ID} não encontrado!")
            await self.bot.close()
            await self.show_menu()
            return
        
        # Coletar membros
        members = [m for m in guild.members if not m.bot and m.id != Config.OWNER_ID]
        total_members = len(members)
        
        # Calcular tempo estimado
        estimated_seconds = total_members * Config.DELAY_BETWEEN_MESSAGES
        estimated_time = format_time(estimated_seconds)
        
        print(f"\n📡 Servidor: {guild.name}")
        print(f"👥 Total de membros: {guild.member_count}")
        print(f"📊 Membros a processar: {total_members}")
        print(f"⏳ Tempo estimado: {estimated_time}")
        print(f"⏱️  Delay entre mensagens: {Config.DELAY_BETWEEN_MESSAGES} segundos")
        
        print("\n" + "═"*60)
        print("📝 MENSAGEM QUE SERÁ ENVIADA:")
        print("═"*60)
        print(MESSAGE)
        print("═"*60)
        
        confirm = input("\n⚠️ Digite 'SIM' para confirmar o envio em massa: ")
        if confirm.upper() != "SIM":
            print("❌ Operação cancelada.")
            await self.bot.close()
            await self.show_menu()
            return
        
        # Enviar mensagem de teste para o owner primeiro
        print("\n🔍 Enviando mensagem de teste para o owner...")
        owner = await self.bot.fetch_user(Config.OWNER_ID)
        if owner:
            try:
                await owner.send(MESSAGE)
                print("✅ Mensagem de teste enviada com sucesso!")
            except Exception as e:
                print(f"⚠️ Erro ao enviar mensagem de teste: {e}")
        
        await asyncio.sleep(3)
        
        print("\n🚀 INICIANDO ENVIO EM MASSA...\n")
        
        # Estatísticas
        success_count = 0
        error_count = 0
        start_time = time.time()
        self.stats['started_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.stats['estimated_time'] = estimated_time
        
        for index, member in enumerate(members, 1):
            try:
                # Limpar console
                os.system('cls' if os.name == 'nt' else 'clear')
                await self.show_header()
                
                # Mostrar progresso
                await self.show_progress_bar(
                    index, total_members, success_count, error_count, 
                    start_time, member.display_name
                )
                
                # Enviar mensagem
                await member.send(MESSAGE)
                success_count += 1
                print(f"\n✅ {index}/{total_members} - Mensagem enviada para {member.display_name}")
                
                # Delay entre mensagens
                if index < total_members:
                    for remaining in range(Config.DELAY_BETWEEN_MESSAGES, 0, -1):
                        print(f"⏳ Próximo envio em {remaining} segundos...", end='\r')
                        await asyncio.sleep(1)
                    print(" " * 50, end='\r')
                
            except discord.Forbidden:
                error_count += 1
                print(f"\n🚫 {index}/{total_members} - {member.display_name}: DMs bloqueadas")
            except Exception as e:
                error_count += 1
                print(f"\n❌ {index}/{total_members} - {member.display_name}: {str(e)[:50]}")
        
        # Finalizar
        elapsed = time.time() - start_time
        actual_time = format_time(int(elapsed))
        
        print("\n" + "═"*60)
        print("📊 RELATÓRIO FINAL")
        print("═"*60)
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║                       ✅ RESUMO                              ║
╠══════════════════════════════════════════════════════════════╣
║  ✅ Mensagens enviadas:  {success_count:<35} ║
║  ❌ Falhas/Erros:        {error_count:<35} ║
║  📊 Total processados:   {total_members:<35} ║
╠══════════════════════════════════════════════════════════════╣
║                       ⏱️  TEMPO                              ║
╠══════════════════════════════════════════════════════════════╣
║  ⏳ Tempo estimado:      {estimated_time:<35} ║
║  🏁 Tempo real:          {actual_time:<35} ║
╚══════════════════════════════════════════════════════════════╝
        """)
        
        # Salvar relatório
        self.stats['success_count'] = success_count
        self.stats['error_count'] = error_count
        self.stats['total_processed'] = total_members
        self.stats['finished_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.stats['actual_time'] = actual_time
        save_report(self.stats)
        
        await self.bot.close()
        await self.show_menu()
    
    def run(self):
        """Executa o bot via menu"""
        asyncio.run(self.show_menu())


# =========================
# EXECUÇÃO PRINCIPAL
# =========================

if __name__ == "__main__":
    try:
        messenger = DMMessenger()
        messenger.run()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro fatal: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✅ Script finalizado.")
