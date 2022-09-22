def kvn_round(string):
    return sum(int(i) for i in string.split())/ len(string.split())

def kvn_push(string, team, total):
    count = kvn_round(string) 
    print('Баллы за раунд -', count)
    total += count
    print(f'Общий счет команды {team} равен {total}')
    return count
    
teams = {'Ежики': 0, 'Бонбончики': 0, 'Хорошки': 0}

for rnd in range(3):
    print(['Итак, начнем игру с раунда - Разминка', 'Следующий раунд - Импровизация', 'Последний на сегодня раунд - Новый формат'][rnd])
    print()
    
    for team, total in teams.items():
        string = input(f'Оценки команды {team}: ')
        teams[team] = teams.get(team, 0) + kvn_push(string, team, total)
        print()
    if rnd == 2:
        continue
    winner_round = max(teams, key=lambda team: teams[team])
    winner_score_round = max(teams.values())
    print(f'По итогу раунда лидирует команда {winner_round} со счетом {winner_score_round}')
    print()
else:
    winner = max(teams, key=lambda team: teams[team])
    winner_score = max(teams.values())
    print('Игра окончена!')
    print('Победила команда,', winner, 'со счетом', winner_score)
    print('Поздравляем победителей лавровым венком!')

    #TODO
    '''сделать вывод имени команды победителя
    мб в будущем сделать ввод команд
    добавить текст спонсорских сообщений до начала игры, после каждого раунда и в конце игры
    '''