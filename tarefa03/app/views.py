from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    user_list = [
    {"nome": "Ana Beatriz Souza", "matricula": "2023001", "idade": 20, "cidade": "Natal"},
    {"nome": "Lucas Henrique Lima", "matricula": "2023002", "idade": 22, "cidade": "Mossoró"},
    {"nome": "Mariana Costa Silva", "matricula": "2023003", "idade": 19, "cidade": "Caicó"},
    {"nome": "João Pedro Rocha", "matricula": "2023004", "idade": 21, "cidade": "Parnamirim"},
    {"nome": "Clara Fernandes Melo", "matricula": "2023005", "idade": 20, "cidade": "Assú"},
    {"nome": "Rafael Oliveira Dantas", "matricula": "2023006", "idade": 23, "cidade": "São Gonçalo do Amarante"},
    {"nome": "Isabela Martins", "matricula": "2023007", "idade": 18, "cidade": "Currais Novos"},
    {"nome": "Diego Araújo", "matricula": "2023008", "idade": 24, "cidade": "Macau"},
    {"nome": "Vitória Almeida", "matricula": "2023009", "idade": 21, "cidade": "Pau dos Ferros"},
    {"nome": "Gabriel Monteiro", "matricula": "2023010", "idade": 22, "cidade": "Santa Cruz"},
]
    context= {
        "usuarios": user_list
    }


    return render(request,"usuarios.html", context)