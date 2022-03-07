from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/convenios")
def read_convenios():
    convenios = [{"id":1,"convenio":"Rhyzio"},
                {"id":1,"convenio":"ALLIANZ SAÚDE"},
                {"id":2,"convenio":"AMEPLAN SAÚDE"},
                {"id":3,"convenio":"AMIL FACIL"},
                {"id":4,"convenio":"AMIL SAÚDE"},
                {"id":5,"convenio":"BIOSAÚDE"},
                {"id":6,"convenio":"BIOVIDA SAÚDE"},
                {"id":7,"convenio":"BLUE MED SAÚDE"},
                {"id":8,"convenio":"BRADESCO SAÚDE"},
                {"id":9,"convenio":"CLASSES LABORIOSAS"},
                {"id":10,"convenio":"CRUZ AZUL SAÚDE"},
                {"id":11,"convenio":"GS SAÚDE"},
                {"id":12,"convenio":"GOLDEN CROSS"},
                {"id":13,"convenio":"HAPVIDA"},
                {"id":14,"convenio":"HEALTH SANTARIS"},
                {"id":15,"convenio":"INTERCLINICAS SAÚDE"}]
    return convenios 

@app.get("/preparos")
def read_preparos():
    preparos = [{"id":1,"preparo":"Ginnie"},
                {"id":1,"preparo":"A coleta de sangue deve ser realizada preferencialmente com o paciente em jejum de acordo com o exame a ser realizado"},
                {"id":2,"preparo":"4h para dosagem de prolactina recomendando-se um repouso de 30 minutos antes da coleta para quem fez exercícios físicos"},
                {"id":3,"preparo":"Após esta coleta o paciente deverá fazer uma refeição normal do seu dia a dia"},
                {"id":4,"preparo":"Realizar a coleta preferencialmente pela manhã no dia da entrega ao laboratório"},
                {"id":5,"preparo":"ta dieta deverá ser iniciada 48 horas (dois dias) antes do início da coleta do material"},
                {"id":6,"preparo":"4h para dosagem de prolactina recomendando-se um repouso de 30 minutos antes da coleta para quem fez exercícios físicos"},
                {"id":7,"preparo":"A coleta de sangue deve ser realizada preferencialmente com o paciente em jejum de acordo com o exame a ser realizado"},
                {"id":8,"preparo":"A coleta de sangue deve ser realizada preferencialmente com o paciente em jejum de acordo com o exame a ser realizado"},
                {"id":9,"preparo":"ta dieta deverá ser iniciada 48 horas (dois dias) antes do início da coleta do material"},
                {"id":10,"preparo":"Realizar a coleta preferencialmente pela manhã no dia da entrega ao laboratório"},
                {"id":11,"preparo":"Após esta coleta o paciente deverá fazer uma refeição normal do seu dia a dia"},
                {"id":12,"preparo":"ta dieta deverá ser iniciada 48 horas (dois dias) antes do início da coleta do material"},
                {"id":13,"preparo":"Após esta coleta o paciente deverá fazer uma refeição normal do seu dia a dia"},
                {"id":14,"preparo":"ta dieta deverá ser iniciada 48 horas (dois dias) antes do início da coleta do material"},
                {"id":15,"preparo":"I4h para dosagem de prolactina recomendando-se um repouso de 30 minutos antes da coleta para quem fez exercícios físicos"}]
    return preparos

@app.get("/exames")
def read_exames():
    exames = [{"id":1,"exame":"Felodipine"},
            {"id":1,"exame":"Hemograma"},
            {"id":2,"exame":"Colesterol"},
            {"id":3,"exame":"Ureia e Creatinina"},
            {"id":4,"exame":"Papanicolau"},
            {"id":5,"exame":"Exames de urina"},
            {"id":6,"exame":"Exames de fezes"},
            {"id":7,"exame":"Glicemia"},
            {"id":8,"exame":"Transaminases (ALT e AST) ou TGP e TGO"},
            {"id":9,"exame":"Mamografia"},
            {"id":10,"exame":"Desintometria óssea"},
            {"id":11,"exame":"Ressonância Magnética"},
            {"id":12,"exame":"Tomografia Computadorizada"},
            {"id":13,"exame":"Ultra-sonografia"},
            {"id":14,"exame":"Ecografia tridimensional"},
            {"id":15,"exame":"Ecodopler"}]
    return exames