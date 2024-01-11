from task import Task

# instanciar a classe
task_web = Task()
# Abrir o link no navegador
task_web.open_link("http://127.0.0.1:8000/logar_usuario/")
# Fazer o Login
task_web.make_login()
# Entrar na tela e fazer o cadastro dos pacientes.
task_web.create_registration("dados.csv")