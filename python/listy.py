
def ile_dni(miesiac):
    dni_w_roku = {"styczen":31 , "luty":28, "marzec":31, "kwiecien":30, "maj":31, "czerwiec":30, "lipiec":31, "sierpien":31, "wrzesien":30, "pazdzoiernik":31, "listopad":30, "grudzien":31}
    return dni_w_roku[miesiac]

def a(c):
    b = {"styczen":"january" , "luty":"february", "marzec":"march", "kwiecien":"april", "maj":"may", "czerwiec":"june", "lipiec":"july", "sierpien":"august", "wrzesien":"september", "pazdzoiernik":"october", "listopad":"november", "grudzien":"december"}
    return b[c]


x=sum(dni_w_roku)/len(dni_w_roku)