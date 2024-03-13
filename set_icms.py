# DEFINIR SE É OU NÃO COM DADOS INFORMADOS.
# LINHA 1 VALOR TEM QUE SER 0 SE FOR COM DADOS INFORMADOS E 1 SE FOR SEM DADOS INFORMADOS.
# LINHA 6 VALOR TEM QUE SER 1 SE FOR COM DADOS INFORMADOS E 0 SE FOR SEM DADOS INFORMADOS.
# LINHA 7 VALOR TEM QUE SER 9 SE FOR COM DADOS INFORMADOS E 2 SE FOR SEM DADOS INFORMADOS.
# LINHA 19 VALOR TEM QUE SER 0 SE FOR COM DADOS INFORMADOS E 1 SE FOR SEM DADOS INFORMADOS.

# DEFINIR OS VALORES DADOS INFORMADOS.
# LINHA 11 É REFERENTE AO ICMS ST.
# LINHA 12 É REFERENTE AO ICMS DIFAL.
# LINHA 8 TEM QUE SER A SOMA DA LINHA 11 E 12.

from calendar import monthrange
from typing import List

def format_mount_range(DATE: List[int]) -> str:
    end_month_range = monthrange(DATE[1], DATE[0])
    if DATE[0] < 10:
        return f'010{DATE[0]}{DATE[1]}|{end_month_range[1]}0{DATE[0]}{DATE[1]}'
    else:
        return f'01{DATE[0]}{DATE[1]}|{end_month_range[1]}{DATE[0]}{DATE[1]}'    

def set_values(FILEPATH, ICMS_ST, DATE: List[int]):
    end_month_range = format_mount_range(DATE)
    with open(FILEPATH, 'r', encoding='ISO-8859-15') as file:
        text = file.readlines()
        # VALIDANDO SE OS VALORES ESTÃO CORRETOS
        if text[1] != "|0001|0|\n":
            text[1] = "|0001|0|\n"
        if text[6] != "|G001|0|\n":
            text[6] = "|G001|0|\n"
        if text[7] != f'|G020|2|{end_month_range}|\n':
            text[7] = f'|G020|2|{end_month_range}|\n'
        if text[19] != "|9001|0|\n":
            text[19] = "|9001|0|\n"
        # SETANDO OS VALORES
        text[11] = str(f"|G605|2|||{float(ICMS_ST):.2f}|\n").replace(".", ",")
        ICMS_DIFAL = str(f"{(text[12].split('|')[5])}").replace(".", ",")
        text[12] = f"|G605|3|||{ICMS_DIFAL}|\n"
        total = str(f"{(ICMS_ST + float(ICMS_DIFAL.replace(",", "."))):.2f}").replace(".", ",")
        text[8] = f"|G600|||{total}|\n"
        with open(FILEPATH, 'w', encoding='ISO-8859-15') as file:
            file.writelines(text)