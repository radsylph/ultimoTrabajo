from handlers import get_players_by_team, get_best_players_by_team, get_best_teams, get_best_players_by_position, get_lift_supp_conf
import pandas as pd

file_path = './DATA.xlsx'
df = pd.read_excel(file_path)

if __name__ == "__main__": # esta es la par
    stats = ['Posición', 'Partidos', 'Turnos', 'Anotadas', 'Hit', 'Dobles', 'Triples', 'HR', 'Impulsadas', 'Boletos R', 'Ponches', 'Boletos', 'Bases Robadas', 'Ave', 'OBP', 'SLG', 'OPS']
    print("Bienvenido al sistema de análisis de béisbol")
    print("¿Qué deseas hacer?")
    print("1. obtener todos los jugadores de un equipo")
    print("2. Obtener los mejores jugadores por equipo")
    print("3. Obtener los mejores equipos por estadística")
    print("4. Obtener los mejores jugadores por posición")
    print("5. Obtener el lift, soporte y confianza de las anotadas y los hits")
    seleccion = input()
    if seleccion == '1':
        get_players_by_team(df)
    elif seleccion == '2':
        print('Escribe el número de jugadores que deseas obtener')
        n = int(input())
        get_best_players_by_team(df, n)
    elif seleccion == '3':
        print('Escribe el número de equipos que deseas obtener')
        n = int(input())
        get_best_teams(df, n)
    elif seleccion == '4':
        print('Escribe el número de jugadores que deseas obtener')
        n = int(input())
        get_best_players_by_position(df, n)
    elif seleccion == '5':
        get_lift_supp_conf()
    else:
        print('Opción no válida, por favor elige una opción válida')