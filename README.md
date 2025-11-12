# Dados Meteorológicos Diários de Curitiba

Aplicação web desenvolvida em **Python - Flask** que consulta os dados meteorológicos de **Curitiba – PR** por meio da API do **OpenWeatherMap**, salva os resultados das pesquisas em um arquivo JSON e exibe as informações atuais em um **mapa interativo** com base Esri e uma tabela lateral organizada.

**url do projeto:**  
[https://dados-diarios-meteorologicos-cwb.onrender.com/](https://dados-diarios-meteorologicos-cwb.onrender.com/)

## Funcionalidades
- Consulta diária automática à API OpenWeatherMap (essa funcionalidade deve ser aplicada individualmente caso queira).  
- Armazenamento dos dados coletados em `dados_meteorologicos.json`.  
- Exibição das informações meteorológicas mais recentes em uma página HTML.  
- Mapa com base visual Esri e dados apresentados em tabela ao lado.  
- Contador de número total de consultas realizadas.

## Estrutura do Projeto
```
dados_meteorologicos_curitiba/
│
├── app.py                     # Aplicação Flask principal
├── dados_meteorologia_cwb.py  # Script que coleta os dados meteorológicos
├── dados_diarios.json         # Histórico salvo de consultas
├── requirements.txt           # Dependências do projeto
└── templates/
    └── index.html             # Página HTML exibida com o mapa e os dados
```

## Instalação e Execução Local
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/Dados_diarios_meteorologicos_CWB.git
   cd Dados_diarios_meteorologicos_CWB
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   # ou
   source venv/bin/activate   # Linux/Mac
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação Flask:
   ```bash
   python app.py
   ```
5. Acesse no navegador:
   ```
   http://127.0.0.1:5000
   ```

## Agendamento da Coleta Diária (Windows)
Para automatizar a execução do script `dados_meteorologia_cwb.py` e coletar os dados meteorológicos automaticamente:

1. Abra o **Agendador de Tarefas do Windows**.  
2. Clique em **Criar Tarefa**.  
3. Na aba **Geral**, dê um nome como:  
   ```
   Coleta_Diaria_Meteorologia
   ```
4. Na aba **Disparadores**, clique em **Novo** e configure:  
   - Iniciar tarefa: **Diariamente**  
   - Hora: escolha o horário desejado para a execução  
5. Na aba **Ações**, clique em **Novo** e configure:  
   - **Ação:** Iniciar um programa  
   - **Programa/script:** caminho do Python (exemplo)  
     ```
     C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python311\python.exe
     ```
   - **Adicionar argumentos (opcional):**  
     ```
     "C:\Users\SeuUsuario\dados_meteorologicos_curitiba\dados_meteorologia_cwb.py"
     ```
   - **Iniciar em (opcional):**  
     ```
     C:\Users\SeuUsuario\dados_meteorologicos_curitiba
     ```
6. Clique em **OK** para salvar.

O script será executado automaticamente todos os dias, atualizando o arquivo `dados_meteorologicos.json`.

## Para fazer o Deploy na Render
- Tipo de serviço: **Web Service**
- Build Command: *(deixe em branco)*
- Start Command:
  ```
  gunicorn app:app
  ```

## API Utilizada
- [OpenWeatherMap](https://openweathermap.org/api)

## Licença
Este projeto está em domínio público sob a [Unlicense](https://unlicense.org).
