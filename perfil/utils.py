import requests

def mês(num:int) -> str:
    if num == 1:
        return 'Janeiro'
    elif num == 2:
        return 'Fevereiro'
    elif num == 3:
        return 'Março'
    elif num == 4:
        return 'Abril'
    elif num == 5:
        return 'Maio'
    elif num == 6:
        return 'Junho'
    elif num == 7:
        return 'Julho'
    elif num == 8:
        return 'Agosto'
    elif num == 9:
        return 'Setembro'
    elif num == 10:
        return 'Outubro'
    elif num == 11:
        return 'Novembro'
    elif num == 12:
        return 'Dezembro'

def num_valid(num:str) -> int:
    valid = num
    if num[0:2] != '55':
        valid = '+55' + num
    else:
        valid = '+' + num
    
    requests.post('https://textbelt.com/text', {
      'phone': f'{valid}',
      'message': 'Agradecemos por utilizar nossa plataforma💜! Contato do desenvolvedor: ...',
      'key': '9850d2003f242855986870c7b190bb68ec53ec6aTSyTv0LHHHrN9wpjhylPQKgeu',
    })

