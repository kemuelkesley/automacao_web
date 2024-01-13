from task import Task

# instanciar a classe
task_web = Task()


input_user = task_web.user_data()
input_password = task_web.user_password()

# Aguardar usuário pressionar Enter para abrir o navegador
input("Pressione Enter para abrir o navegador e iniciar a tarefa...")

task_web.open_browser()

# Abrir o link no navegador
task_web.open_link("http://127.0.0.1:8000/logar_usuario/")

# Fazer o Login
task_web.make_login()
# Entrar na tela e fazer o cadastro dos pacientes.
task_web.create_registration("dados.csv")