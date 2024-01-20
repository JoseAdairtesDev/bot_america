import requests 
import telebot
import time

#####################################

api_key = '6565387841:AAHvFSCCotZidBJeY0wQzneLfwDm7VOy4dk'
chat_id = '-1002105339201'  # ID DO GRUPO

#####################################

bot = telebot.TeleBot(token=api_key)

##################################################################

resultado_ = None 

arrays_validos = []

###############################################################################
lista_24colun = []
lista_24duzi = []
#############################################################################

colun = None 

duzia = None 

##################################################################################

array = [['api-american', 'brasileira', 'AMERICANA'], 
['api-aovivo', 'aovivo', 'AO VIVO'], 
['apibucharest', 'bucharest', 'BUCHAREST'], 
['apiimmersive', 'Immersive', 'IMMERSIVE'], 
['api-maltaroulette', 'malta', 'MALTA'], 
['api-roullete', 'roulette', 'ROULETTE'],
['api-speedroullete', 'brasileira', 'SPEED'],
['api-turkce', 'turkce', 'TURKCE'], 
['api-viproulette', 'viproulette', 'VIP']
]

x = 0

####################################################################################################

def colunas(x):
    
    global colun
    
    colun = []
    
    for i in x:
        
        if float(i) in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36] and float(i) != 0:
            
            colun.append('CO3')
            
        elif float(i) in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35] and float(i) != 0:
            
            colun.append('CO2') 

        elif float(i) in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34] and float(i) != 0:

            colun.append('CO1')  

        elif float(i) in [0]:

            colun.append('0')  
    
    # print(f'COLUNAS: {colun}')
    
    return colun 

#####################################################################################################

def duzias(x):
    
    global duzia
    
    duzia = []
    
    for i in x:
        
        if float(i) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] and float(i) != 0:
            
            duzia.append('D1')
            
        elif float(i) in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] and float(i) != 0:
            
            duzia.append('D2') 

        elif float(i) in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] and float(i) != 0:

            duzia.append('D3')

        elif float(i) in [0]:

            duzia.append('0')  

                                
    # print(f'DUZIAS: {duzia}')
    
    return duzia       
        
############################################################################

def contando_colunas(numero, i):
    
    global lista_24colun
    
        
    if len(lista_24colun) == 0:
        lista_24colun.insert(0, numero)
        return
    
    elif numero != lista_24colun[0]:
        
        lista_24colun.insert(0, numero)
                
        if len(lista_24colun) == 24:        
            bot.send_message(chat_id=chat_id, text=f'ESTRATÉGIA DETECTADA EM COLUNAS NA {array[i][2]}')
                  
        elif len(lista_24colun) == 25: 
            bot.send_message(chat_id=chat_id, text=f'ESTRATÉGIA CONFIRMADA EM DUZIAS NA {array[i][2]} ULTIMA COLUNA {numero}') 
            lista_24colun = [] 
                  
        return lista_24colun

    elif numero == lista_24colun[0]:
        lista_24colun = []        
        return 
    
   
########################################################################
   
def contando_duzias(numero, i):
    
    global lista_24duzi   
    
            
    if len(lista_24duzi) == 0:
        lista_24duzi.insert(0, numero)
        return    
    
    elif numero != lista_24duzi[0]:
        
        lista_24duzi.insert(0, numero)
        
        if len(lista_24duzi) == 24:        
            bot.send_message(chat_id=chat_id, text=f'ESTRATÉGIA DETECTADA EM DUZIAS NA {array[i][2]}')   
            # lista_24duzi = []     
        
        elif len(lista_24duzi) == 25: 
            bot.send_message(chat_id=chat_id, text=f'ESTRATÉGIA CONFIRMADA EM DUZIAS NA {array[i][2]} ULTIMA DUZIA {numero}') 
            lista_24duzi = [] 
                    
        return lista_24duzi
    
    elif numero == lista_24duzi[0]:
        lista_24duzi = []           
        return 
    
##############################################################################


def imprimir_se_diferente(novo_array, o):
    global arrays_validos
    if not any((novo_array == array) for array in arrays_validos):
        colunas(novo_array)
        duzias(novo_array)        
        contando_colunas(colun[0], o)
        contando_duzias(duzia[0], o)
        print(novo_array)        
        print(lista_24duzi)
        print(lista_24colun)
        print(f'ROLETA {array[o][2]}')  
        print('_________________________')      
        arrays_validos.append(novo_array)



################################################################################

def api_():
    
    global resultado_
    global array
    global x
        
    url = f'https://{array[x][0]}.000webhostapp.com/'

    resultado_= requests.get(url).json()[f"{array[x][1]}"]
    
    return resultado_, x


##############################################################################



while True:
    
    try:
        
        api_()
        
        imprimir_se_diferente(resultado_, x)
        
    except:
        pass
        
  
        
       
        
 