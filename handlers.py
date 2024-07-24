import pandas as pd

file_path = './DATA.xlsx'
df = pd.read_excel(file_path)

def get_lift_supp_conf():
    threshold_anotadas = df['Anotadas'].mean()
    threshold_hit = df['Hit'].mean()
    df['Anotadas_bin'] = df['Anotadas'] >= threshold_anotadas
    df['Hit_bin'] = df['Hit'] >= threshold_hit
    basket = df[['Anotadas_bin', 'Hit_bin']]
    support_anotadas = basket['Anotadas_bin'].mean()
    support_hit = basket['Hit_bin'].mean()
    support_anotadas_hit = (basket['Anotadas_bin'] & basket['Hit_bin']).mean()
    confidence_anotadas_hit = support_anotadas_hit / support_anotadas
    lift_anotadas_hit = confidence_anotadas_hit / support_hit
    print(f'Soporte de todas las anotadas Anotadas: {support_anotadas}')
    print(f'Soporte de Hit: {support_hit}')
    print(f'Soporte de Anotadas y Hit: {support_anotadas_hit}')
    print(f'Confianza de Anotadas -> Hit: {confidence_anotadas_hit}')
    print(f'Lift de Anotadas -> Hit: {lift_anotadas_hit}')

def get_players_by_team(df):
    teams = df['Team'].unique()
    print(f'Los equipos disponibles son: {teams}')
    print('Escribe el nombre del equipo para obtener los jugadores')
    team_name = input().upper()
    if team_name not in teams:
        print('El equipo no existe, escribe un equipo válido')
        return
    team_players = df[df['Team'] == team_name]
    print(team_players[['Player', 'Team']])  # Asumiendo que hay una columna 'Player'
    return team_players

def get_best_players_by_team(df, top_n):
    teams = df['Team'].unique()
    print(f'Los equipos disponibles son: {teams}')
    print('Escribe el nombre del equipo para obtener los mejores jugadores')
    team_name = input().upper()
    stats = ['Posición', 'Partidos', 'Turnos', 'Anotadas', 'Hit', 'Dobles', 'Triples', 'HR', 'Impulsadas', 'Boletos R', 'Ponches', 'Boletos', 'Bases Robadas', 'Ave', 'OBP', 'SLG', 'OPS']
    print(f'Las estadísticas disponibles son: {stats}')
    print('Escribe la estadística por la que deseas obtener los mejores jugadores')
    stat = input()
    if team_name not in teams:
        print('El equipo no existe, escribe un equipo válido')
        return
    if stat not in df.columns:
        print('Estadística no válida, por favor elige una de las estadísticas disponibles')
        return
    team_players = df[df['Team'] == team_name].sort_values(by=stat, ascending=False)
    best_players = team_players.head(top_n)
    if best_players.empty:
        print(f'No se encontraron jugadores para el equipo {team_name}')
    else:
        print(f'Los mejores {top_n} jugadores del equipo {team_name} basados en {stat} son:')
        print(best_players[['Player', 'Team', stat]])  # Asumiendo que hay una columna 'Player'
    return best_players

def get_best_players_by_position(df,top_n):
    positions = df['Posición'].unique()
    print(f'Las posiciones disponibles son: {positions}')
    print('Escribe la posición para obtener los mejores jugadores')
    position = input().upper()
    stats = ['Posición', 'Partidos', 'Turnos', 'Anotadas', 'Hit', 'Dobles', 'Triples', 'HR', 'Impulsadas', 'Boletos R', 'Ponches', 'Boletos', 'Bases Robadas', 'Ave', 'OBP', 'SLG', 'OPS']
    print(f'Las estadísticas disponibles son: {stats}')
    print('Escribe la estadística por la que deseas obtener los mejores jugadores')
    stat = input()
    if position not in positions:
        print('La posición no existe, escribe una posición válida')
        return
    if stat not in df.columns:
        print('Estadística no válida, por favor elige una de las estadísticas disponibles')
        return
    position_players = df[df['Posición'] == position].sort_values(by=stat, ascending=False)
    best_players = position_players.head(top_n)
    if best_players.empty:
        print(f'No se encontraron jugadores para la posición {position}')
    else:
        print(f'Los mejores {top_n} jugadores de la posición {position} basados en {stat} son:')
        print(best_players[['Player', 'Posición', 'Team', stat]])
    return best_players


def get_best_teams(df, top_n):
    stats = df.columns.drop(['Player', 'Team', 'Posición'])  # Asumiendo estas columnas existen
    print(f'Las estadísticas disponibles son: {stats}')
    print('Escribe la estadística por la que deseas obtener los mejores equipos')
    stat = input()
    if stat not in stats:
        print('Estadística no válida')
        return
    team_stats = df.groupby('Team')[stat].sum().sort_values(ascending=False)
    best_teams = team_stats.head(top_n)
    if best_teams.empty:
        print(f'No se encontraron equipos basados en la estadística {stat}')
    else:
        print(f'Los mejores {top_n} equipos basados en {stat} son:')
        for team, value in best_teams.items():
            print(f'Equipo: {team}, {stat}: {value}')
    return best_teams
    stats = ['Posición', 'Partidos', 'Turnos', 'Anotadas', 'Hit', 'Dobles', 'Triples', 'HR', 'Impulsadas', 'Boletos R', 'Ponches', 'Boletos', 'Bases Robadas', 'Ave', 'OBP', 'SLG', 'OPS']
    print(f'Las estadísticas disponibles son: {stats}')
    print('Escribe la estadística por la que deseas obtener los mejores equipos')
    stat = input()
    team_stats = df.groupby('Team')[stat].sum().sort_values(ascending=False)
    best_teams = team_stats.head(top_n)
    
    if best_teams.empty:
        print(f'No se encontraron equipos basados en la estadística {stat}')
    else:
        print(f'Los mejores {top_n} equipos basados en {stat} son:')
        for team, value in best_teams.items():
            print(f'Equipo: {team}, {stat}: {value}')
    
    return best_teams