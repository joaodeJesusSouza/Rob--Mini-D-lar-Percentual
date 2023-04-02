# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:55:52 2022

@author: João
"""

import MetaTrader5 as mt5
import pandas as pd
import time
import datetime
import sys

mt5.initialize()

df_taxas = []

data=datetime.datetime.now()
hr = time.strftime('%H:%M:%S')
data=datetime.datetime.now()
data_A=datetime.datetime(2022, 5, 31)
account_info=mt5.account_info()
ctalgda = (account_info[0])
nome = (account_info[24])

# Conta Demo Rico Cleverson
#cta_autorizada = 3000825647 
#cta_autorizada2 = '30------47'
#nome2 = ' Cleverson - Rico - DEMO'

# Conta Mara Modal
#cta_autorizada = 3524460
#nome2 = ' Mara - Modal - REAL'

# Conta Demo XP João
#cta_autorizada = 93059907 
#cta_autorizada2 = '93----07'
#nome2 = ' João - XP - DEMO'

# Renata
#cta_autorizada = 2980505 
#cta_autorizada2 = '29---05'
#nome2 = ' Renata - BTG - REAL'

# Rubinho
#cta_autorizada = 1000744605 
#cta_autorizada2 = '10------05' 
#nome2 = ' Ruben - Clear - REAL'

# # Conta Demo Rico João 
cta_autorizada = 3000165639 
cta_autorizada2 = '30------39'
nome2 = ' João - Rico - DEMO'

# Conta Demo Rico João II
#cta_autorizada = 3000662347
#cta_autorizada2 = '30------47'
#nome2 = ' João - Rico - DEMO'



corretora = (account_info[27])
positions_total = mt5.positions_total()
ordens_abertas = mt5.orders_total()
info_posicoes=mt5.positions_get()
hr_inicial = '09:03:30'
hr_final = '18:00:00'
hr_final2 = '17:59:57'

ibov = '10:00:00'
djones = '10:30:00'
saldo = (account_info[10])
saldo1 = (account_info[10])
lucro = saldo-saldo1

TICKET = 0
intervalo = 'U'
ordem = 0 
lucro_final = 0
taxa_bmf = 0.40
emolumentos = 0.75
corretagem = 0.05  # Valor de corretagem da Genial
taxas1 = taxa_bmf+emolumentos+corretagem
taxa = taxas1*(-2)
imposto_renda = 0
operacoes = len(df_taxas)
taxas_final = sum(df_taxas)
saldo_final = lucro+taxas_final

vartk = 1.0
# Variação de stop loss
varstplss = 3.5

lot = 1
deviation = 0 
        
pr_ibov = 0
pr_djones = 0           

print("...", sep='\n')
time.sleep(1)
print("... ROBÔ MINI DÓLAR - Percentual ", sep='\n')
if data < data_A:  
    print("...", sep='\n')
    time.sleep(1)
    print('... Licença válida até 30 de Maio de 2022 para conta DEMO !!!', sep='\n')
    time.sleep(2)
    print("...", sep='\n')
    time.sleep(1)
    if ctalgda == cta_autorizada:    
        print("... Conta logada = Conta autorizada ", sep='\n')
        time.sleep(1)
        print("...", sep='\n')
        time.sleep(1)
        print(f'... Conta: {cta_autorizada2} | Cliente: {nome2} | Corretora: {corretora}')
        print("...", sep='\n')
        time.sleep(1)
        #symbol = (input('Ativo: '))
        symbol = 'WDOM22'
        #lot = (input('Quantida de contratos: '))
        
        ativo = symbol
        mt5.symbol_select(symbol, True)
        tick = mt5.symbol_info_tick(symbol)
        price = tick.last
        pr = tick.last
        positions_total=mt5.positions_total()
        account_info=mt5.account_info()
       
        profit = 150*lot  #(float(input('... Pontos de take profit do dia: ')))
        take = profit/10
        lossdodia = profit*(-1.3334)  #(float(input('... Pontos de loss do dia: ')))
        VW = lossdodia
        rou = round(VW, 0)
        ro1 = rou+0.25 
        ro2 = rou+0.50
        ro3 = rou-0.25
        ro4 = rou-0.50
        if VW == ro2:
            VW = ro2
        elif rou > VW:
            if VW <= rou and VW > ro3:
                VW = rou
            elif VW <= ro3 and VW > ro4:
                VW = ro4
        elif rou == VW:
            VW = rou
        elif rou < VW:
            if VW >= rou and VW < ro1:
                VW = rou
            elif VW >= ro1 and VW < ro2:
                VW = ro2
        lossdodia = VW
        profit2 = (profit/10) #Lucro em pontos
        lossdodia2 = (lossdodia/10) #Loss em pontos
        saldo = (account_info[10])
        soma = ((saldo-saldo1)/10)/lot
        
        print(f'... Ativo: {symbol} | Lotes: {lot} | Saldo da conta: R$ {saldo} | Meta: R$: {profit:,.2f} | Stop Loss: R$ {lossdodia:,.2f}', sep='\n')
        time.sleep(2)
        
        def fechacompra():
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": TICKET,
                "symbol": ativo,
                "volume": float(lot),             
                "type": mt5.ORDER_TYPE_SELL,
                "price": tick.last,
                "deviation": deviation,
                "magic": 25368598,
                "type_time": mt5.ORDER_TIME_DAY,
                "type_filling": mt5.ORDER_FILLING_RETURN,
            }
            result = mt5.order_send(request)
            
            
        def fechavenda() :   
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": TICKET,
                "symbol": ativo,
                "volume": float(lot),             
                "type": mt5.ORDER_TYPE_BUY,
                "price": tick.last,
                "deviation": deviation,
                "magic": 25368598,
                "type_time": mt5.ORDER_TIME_DAY,
                "type_filling": mt5.ORDER_FILLING_RETURN,
            }
            result = mt5.order_send(request)              
            
        # Maxima1 > Maxima0
        def venda1():
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": ativo,
                "volume": float(lot),            
                "type": mt5.ORDER_TYPE_SELL,
                "price": tick.last,
                "sl": Hcdl1+varstplss,
                "deviation": deviation,
                "magic": 25368598,
                "type_time": mt5.ORDER_TIME_DAY,
                "type_filling": mt5.ORDER_FILLING_RETURN,
            }
            result = mt5.order_send(request)              
            # get position based on ticket_id
            position = mt5.positions_get()
            # check if position exists
            if position:
                position = position[0]
                # get position data
                TICKET = position.ticket
                order_type = position.type
                if order_type == 0:
                    ordem = 'C'
                elif order_type == 1:
                    ordem = 'V'
                price_current = position.price_current
                price_open = position.price_open
                price = price_open
                sl = position.sl
                tp = position.tp
                df_taxas.append(taxa)
                
                
        # Maxima1 < Maxima0
        def venda2():
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": ativo,
                "volume": float(lot),            
                "type": mt5.ORDER_TYPE_SELL,
                "price": tick.last,
                "sl": Hcdl0+varstplss,
                "deviation": deviation,
                "magic": 25368598,
                "type_time": mt5.ORDER_TIME_DAY,
                "type_filling": mt5.ORDER_FILLING_RETURN,
            }
            result = mt5.order_send(request)              
            # get position based on ticket_id
            position = mt5.positions_get()
            # check if position exists
            if position:
                position = position[0]
                # get position data
                TICKET = position.ticket
                order_type = position.type
                if order_type == 0:
                    ordem = 'C'
                elif order_type == 1:
                    ordem = 'V'
                price_current = position.price_current
                price_open = position.price_open
                price = price_open
                sl = position.sl
                tp = position.tp
                df_taxas.append(taxa)
                
                
        # Minima1 < Minima0
        def compra1():
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": ativo,
                "volume": float(lot),             
                "type": mt5.ORDER_TYPE_BUY,
                "price": pr,
                "sl": Lcdl1-varstplss,
                "deviation": deviation,
                "magic": 25368598,
                "type_time": mt5.ORDER_TIME_DAY,
                "type_filling": mt5.ORDER_FILLING_RETURN,
            }
            result = mt5.order_send(request)             
            # get position based on ticket_id
            position = mt5.positions_get()
            # check if position exists
            if position:
                position = position[0]
                # get position data
                TICKET = position.ticket
                order_type = position.type
                if order_type == 0:
                    ordem = 'C'
                elif order_type == 1:
                    ordem = 'V'
                price_current = position.price_current
                price_open = position.price_open
                price = price_open
                sl = position.sl
                tp = position.tp
                df_taxas.append(taxa)
                
                
        #Minima1 > Minima0
        def compra2():
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": ativo,
                "volume": float(lot),             
                "type": mt5.ORDER_TYPE_BUY,
                "price": pr,
                "sl": Lcdl0-varstplss,
                "deviation": deviation,
                "magic": 25368598,
                "type_time": mt5.ORDER_TIME_DAY,
                "type_filling": mt5.ORDER_FILLING_RETURN,
            }
            result = mt5.order_send(request)             
            # get position based on ticket_id
            position = mt5.positions_get()
            # check if position exists
            if position:
                position = position[0]
                # get position data
                TICKET = position.ticket
                order_type = position.type
                if order_type == 0:
                    ordem = 'C'
                elif order_type == 1:
                    ordem = 'V'
                price_current = position.price_current
                price_open = position.price_open
                price = price_open
                sl = position.sl
                tp = position.tp
                df_taxas.append(taxa)
        
        while hr < hr_final and saldo_final>=lossdodia and saldo_final<=profit:
                hr = time.strftime('%H:%M:%S')
                print("...", sep='\n')
                time.sleep(1)
                while hr < hr_inicial:
                    hr = time.strftime('%H:%M:%S')
                    print(f'... Hora: {hr} | Aguardando horário para inicio das operações .... às {hr_inicial}', end='\r')
                    time.sleep(1)
                    #print( "...", sep='\n') 
                    pass
                if hr >= hr_inicial:
                    print(f'... Hora: {hr} | Dentro do horário das operações- Início {hr_inicial} - Término {hr_final}', sep='\n')
                    print( "...", sep='\n')
                    time.sleep(1)
                    print('... Iniciando o robô............', sep='\n')
                    print("...", sep='\n')
                    time.sleep(1)
                                 # preço do inicio do dia
                    dados_dia = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, 1)
                    pr0 = dados_dia['open'][0]
                    # Calculo dos percentuais do preço de inicio do dia
                    perc = 0.25
                    
                    pp10 = (pr0 + (pr0 * 2.50) / 100).round(1)
                    VW = pp10
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp10 = VW
                      
                    pp9 = (pr0 + (pr0 * 2.25) / 100).round(1)
                    VW = pp9
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp9 = VW
                    
                    pp8 = (pr0 + (pr0 * 2.00) / 100).round(1)
                    VW = pp8
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp8 = VW
                        
                    pp7 = (pr0 + (pr0 * 1.75) / 100).round(1)
                    VW = pp7
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp7 = VW
                   
                    pp6 = (pr0 + (pr0 * 1.50) / 100).round(1)
                    VW = pp6
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp6 = VW
                                    
                    pp5 = (pr0+(pr0*1.25)/100).round(1)
                    VW = pp5
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp5 = VW
                       
                    pp4 = (pr0 + (pr0 * 1.00) / 100).round(1)
                    VW = pp4
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp4 = VW
                    
                    pp3 = (pr0 + (pr0 * 0.75) / 100).round(1)
                    VW = pp3
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp3 = VW
                    
                    pp2 = (pr0 + (pr0 * 0.50) / 100).round(1) 
                    VW = pp2
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp2 = VW
                    
                    pp1=(pr0+(pr0*0.25)/100).round(1)
                    VW = pp1
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pp1 = VW
                   
                    pn1=pr0+(pr0*(-0.25)/100).round(1)
                    VW = pn1
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn1 = VW
                    
                    pn2=pr0+(pr0*(-0.50)/100).round(1)  
                    VW = pn2
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn2 = VW
                    
                    pn3=pr0+(pr0*(-0.75)/100).round(1)  
                    VW = pn3
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn3 = VW
                   
                    pn4=pr0+(pr0*(-1.00)/100).round(1)  
                    VW = pn4
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn4 = VW
                   
                    pn5=pr0+(pr0*(-1.25)/100).round(1)
                    VW = pn5
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn5 = VW
                   
                    pn6=pr0+(pr0*(-1.50)/100).round(1)
                    VW = pn6
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn6 = VW
                   
                    pn7=pr0+(pr0*(-1.75)/100).round(1) 
                    VW = pn7
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn7 = VW
                   
                    pn8=pr0+(pr0*(-2.00)/100).round(1)
                    VW = pn8
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn8 = VW
                   
                    pn9=pr0+(pr0*(-2.25)/100).round(1)
                    VW = pn9
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn9 = VW
                   
                    pn10=pr0+(pr0*(-2.50)/100).round(1)
                    VW = pn10
                    rou = round(VW, 0)
                    ro1 = rou+0.25 
                    ro2 = rou+0.50
                    ro3 = rou-0.25
                    ro4 = rou-0.50
                    if VW == ro2:
                        VW = ro2
                    elif rou > VW:
                        if VW <= rou and VW > ro3:
                            VW = rou
                        elif VW <= ro3 and VW > ro4:
                            VW = ro4
                    elif rou == VW:
                        VW = rou
                    elif rou < VW:
                        if VW >= rou and VW < ro1:
                            VW = rou
                        elif VW >= ro1 and VW < ro2:
                            VW = ro2
                    pn10 = VW
                    account_info=mt5.account_info()
                    saldo = (account_info[10])
                    soma = (saldo - saldo1)/10
                    taxas_total = sum(df_taxas)
                    saldo2 = lucro+taxas_total
                    if saldo2 > 0:
                        imposto_de_renda = saldo2*0.01
                        saldo_final = saldo2-imposto_de_renda
                    elif saldo2 < 0:
                        saldo_final = saldo2
                    print('... Robô ligado ..Aguardando padrão da estratégia para abrir uma ordem !.-------', sep='\n')
                    time.sleep(1)
                    print("...", sep='\n')             
                
                    while hr < hr_final and saldo_final>=lossdodia and saldo_final<=profit:
                        hr = time.strftime("%H:%M:%S")
                        mt5.symbol_select(symbol, True)
                        tick = mt5.symbol_info_tick(symbol)
                        positions_total = mt5.positions_total()
                        if positions_total == 0:
                            ordem = 'N'
                            alvo = 0
                        position = mt5.positions_get()
                        account_info=mt5.account_info()
                        ordens_abertas = mt5.orders_total()
                        pr = tick.last
                        soma = ((saldo - saldo1)/10)/lot
                        lucro = (saldo-saldo1)
                        taxas_total = sum(df_taxas)
                        operacoes = len(df_taxas)
                        saldo2 = lucro+taxas_final
                        if saldo2 > 0:
                            imposto_de_renda = saldo2*0.01
                            saldo_final = saldo2-imposto_de_renda
                        elif saldo2 < 0:
                            saldo_final = saldo2
                        #Candle 0    
                        cdl0 = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, 1)
                        op0 = cdl0['open'][0]
                        cl0 = cdl0['close'][0]
                        Hcdl0 = cdl0['high'][0]
                        Lcdl0 = cdl0['low'][0]
                        #print(f' Abertura Candle 1: {op1} | Fechamento Candle 1: {cl1} | MXCdl1: {Hcdl1} | MNCdl1: {Lcdl1} |', end='\r')
                        # Candle 1
                        cdl1 = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 1, 1)
                        op1 = cdl1['open'][0]
                        cl1 = cdl1['close'][0]
                        Hcdl1 = cdl1['high'][0]
                        Lcdl1 = cdl1['low'][0]
                        #print(f' Abertura Candle 1: {op1} | Fechamento Candle 1: {cl1} | MXCdl1: {Hcdl1} | MNCdl1: {Lcdl1} |', end='\r')
                        #função de calculo da vwap do candle
                        vwap1 = ((Lcdl1 + cl1 + Hcdl1)/3)
                        #print(vwap1)
                        VW = vwap1
                        rou = round(VW, 0)
                        ro1 = rou+0.25 
                        ro2 = rou+0.50
                        ro3 = rou-0.25
                        ro4 = rou-0.50
                        if VW == ro2:
                            VW = ro2
                        elif rou > VW:
                            if VW <= rou and VW > ro3:
                                VW = rou
                            elif VW <= ro3 and VW > ro4:
                                VW = ro4
                        elif rou == VW:
                            VW = rou
                        elif rou < VW:
                            if VW >= rou and VW < ro1:
                                VW = rou
                            elif VW >= ro1 and VW < ro2:
                                VW = ro2
                        vwap1 = VW 
                        #Candle 2
                        cdl2 = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 2, 1)
                        op2 = cdl2['open'][0]
                        cl2 = cdl2['close'][0]
                        Hcdl2 = cdl2['high'][0]
                        Lcdl2 = cdl2['low'][0]
                        #print(f' Abertura Candle 2: {op2} | Fechamento Candle 1: {cl2} | MXCdl1: {Hcdl2} | MNCdl1: {Lcdl2} |', end='\r')
                        #função de calculo da vwap do candle
                        vwap2 = ((Lcdl2 + cl2 + Hcdl2)/3)
                        #print(vwap1)
                        VY = vwap2
                        rou = round(VY, 0)
                        ro1 = rou+0.25 
                        ro2 = rou+0.50
                        ro3 = rou-0.25
                        ro4 = rou-0.50
                        if VY == ro2:
                            VY = ro2
                        elif rou > VY:
                            if VY <= rou and VY > ro3:
                                VY = rou
                            elif VY <= ro3 and VY > ro4:
                                VY = ro4
                        elif rou == VY:
                            VY = rou
                        elif rou < VY:
                            if VY >= rou and VY < ro1:
                                VY = rou
                            elif VY >= ro1 and VY < ro2:
                                VY = ro2
                        vwap2 = VY 
                        # get position based on ticket_id
                        position = mt5.positions_get()
                        #print(TICKET)
                        # check if position exists
                        if position:
                            position = position[0]
                            # get position data
                            TICKET = position.ticket
                            price_current = position.price_current
                            price_open = position.price_open
                            order_type = position.type
                            if order_type == 0:
                                # Comprado
                                ordem = 'C'
                                if soma<=0:
                                    alvo = price_open+8.5
                                elif profit-saldo_final<=70.0:
                                    alvo1=profit-saldo_final
                                    VW = alvo1
                                    rou = round(VW, 0)
                                    ro1 = rou+0.25 
                                    ro2 = rou+0.50
                                    ro3 = rou-0.25
                                    ro4 = rou-0.50
                                    if VW == ro2:
                                        VW = ro2
                                    elif rou > VW:
                                        if VW <= rou and VW > ro3:
                                            VW = rou
                                        elif VW <= ro3 and VW > ro4:
                                            VW = ro4
                                    elif rou == VW:
                                        VW = rou
                                    elif rou < VW:
                                        if VW >= rou and VW < ro1:
                                            VW = rou
                                        elif VW >= ro1 and VW < ro2:
                                            VW = ro2
                                    alvo1 = VW
                                    
                                    taxas_pts = (taxas_total/10)*-1
                                    VW = taxas_pts
                                    rou = round(VW, 0)
                                    ro1 = rou+0.25 
                                    ro2 = rou+0.50
                                    ro3 = rou-0.25
                                    ro4 = rou-0.50
                                    if VW == ro2:
                                        VW = ro2
                                    elif rou > VW:
                                        if VW <= rou and VW > ro3:
                                            VW = rou
                                        elif VW <= ro3 and VW > ro4:
                                            VW = ro4
                                    elif rou == VW:
                                        VW = rou
                                    elif rou < VW:
                                        if VW >= rou and VW < ro1:
                                            VW = rou
                                        elif VW >= ro1 and VW < ro2:
                                            VW = ro2
                                    taxas_pts = VW
                                    alvo = price_open+alvo1+taxas_pts
                            elif order_type == 1:
                                # Vendido
                                ordem = 'V'
                                if soma<=0:
                                    alvo = price_open-8.5
                                elif profit-saldo_final<=70.0:
                                    alvo1=profit-saldo_final
                                    VW = alvo1
                                    rou = round(VW, 0)
                                    ro1 = rou+0.25 
                                    ro2 = rou+0.50
                                    ro3 = rou-0.25
                                    ro4 = rou-0.50
                                    if VW == ro2:
                                        VW = ro2
                                    elif rou > VW:
                                        if VW <= rou and VW > ro3:
                                            VW = rou
                                        elif VW <= ro3 and VW > ro4:
                                            VW = ro4
                                    elif rou == VW:
                                        VW = rou
                                    elif rou < VW:
                                        if VW >= rou and VW < ro1:
                                            VW = rou
                                        elif VW >= ro1 and VW < ro2:
                                            VW = ro2
                                    alvo1 = VW
                                    taxas_pts = (taxas_total/10)*-1
                                    VW = taxas_pts
                                    rou = round(VW, 0)
                                    ro1 = rou+0.25 
                                    ro2 = rou+0.50
                                    ro3 = rou-0.25
                                    ro4 = rou-0.50
                                    if VW == ro2:
                                        VW = ro2
                                    elif rou > VW:
                                        if VW <= rou and VW > ro3:
                                            VW = rou
                                        elif VW <= ro3 and VW > ro4:
                                            VW = ro4
                                    elif rou == VW:
                                        VW = rou
                                    elif rou < VW:
                                        if VW >= rou and VW < ro1:
                                            VW = rou
                                        elif VW >= ro1 and VW < ro2:
                                            VW = ro2
                                    taxas_pts = VW
                                    alvo = price_open-alvo1-taxas_pts
                            sl = position.sl
                            tp = position.tp
                            ativo = position.symbol
                        
                        if saldo2 > 0:
                            imposto_de_renda = saldo2*0.01
                            saldo_final = saldo2-imposto_de_renda
                        elif saldo2 < 0:
                            saldo_final = saldo2
                        print(f'... Hora: {hr} | {ordem} | Alvo: R$ {alvo:,.1f} | Preço: {pr} | Pontos: {soma} | Operações: {operacoes} | Taxas: R$ {taxas_final:,.2f} | Saldo: R$ {saldo_final:,.2f} | ', end='\r')
                        
                        if positions_total >= 1:
                            # Comprado
                            if order_type == 0:
                                if pr>price:
                                    request = {
                                        "action": mt5.TRADE_ACTION_SLTP,
                                        "position": TICKET,
                                        "symbol": ativo,
                                        "sl": pr-7.5,
                                        "tp": alvo,
                                        "deviation": deviation,
                                        "magic": 25368598,
                                    }
    
                                    # enviamos a solicitação de negociação
                                    result = mt5.order_send(request)
                                    price = tick.last
                                
                                elif positions_total >= 1 and hr >= hr_final2:
                                    fechacompra()
                               
                            elif order_type == 1:
                                # Vendido
                                if pr<price:
                                    request = {
                                        "action": mt5.TRADE_ACTION_SLTP,
                                        "position": TICKET,
                                        "symbol": ativo,
                                        "sl": pr+7.50,
                                        "tp": alvo,
                                        "deviation": deviation,
                                        "magic": 25368598,
                                    }
                                    # enviamos a solicitação de negociação
                                    result = mt5.order_send(request)
                                    price = tick.last
                                
                                elif positions_total >= 1  and hr >= hr_final2:
                                    fechavenda()
    
                        elif positions_total == 0:
                            if pr<=pp10 and pr>=pp9:
                                percA = pp10
                                percB = pp9
                                percBB = pp8
                                intervalo = 'A'
                            
                                # VENDA pp10     
                                #Padrão 1                                                                                                                                         Padrão                                                                                           Padrão 4                                                                                                            Padrão 5
                                if cl1<op1 and Lcdl1<=pp10-3.0 and cl0>op0 and Hcdl0>=pp10+1.5 and pr==pp10-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                #Padrão 2        
                                elif cl1>op1 and Hcdl1>=pp10-1.0 and Hcdl1<=percA+2.5 and cl1<pp10-1.0 and Hcdl0>=pp10+1.0 and pr==pp10-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3 
                                elif cl1<op1 and Lcdl1<=pp10-0.50 and cl1==pp10 and op0==pp10 and Hcdl0>=pp10+1.5 and pr==pp10-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp10 and op1>=pp10+3.0 and Lcdl0==pp10 and op0-Lcdl0>=3.0 and pr==pp10-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # PAdrão 5
                                elif cl1<op1 and pp10-Lcdl1>=4 and Hcdl1>=pp10+2.0 and pp10-op0>=2 and Hcdl0==pp10 and pr==pp10-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                # COMPRA pp9    #Padrão 1
                                elif cl1>op1 and Hcdl1>=pp9+3.0 and cl0<op0 and Lcdl0<=pp9-1.5 and pr==pp9+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pp9-1.0 and Lcdl1>=percB-2.5 and cl1>pp9+1.0 and Lcdl0<=pp9-1.0 and pr==pp9+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pp9+0.50 and cl1==pp9 and op0==pp9 and Lcdl0<=pp9-1.5 and pr == pp9+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp9 and op1<=pp9-3.0 and Hcdl0==pp9 and Hcdl0-op0>=3.0 and pr==pp9+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp9>=4 and Lcdl1<=pp9+2.0 and op0-pp9>=2 and Lcdl0==pp9 and pr==pp9+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pp9>=3.5 and cl1>op1 and op1-pp9>=2.5 and Lcdl0<=pp9 and pr==pp9+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                    
                    
                            elif pr<=pp9 and pr>=pp8:
                                percAA = pp10
                                percA = pp9
                                percB = pp8
                                percBB = pp7
                                intervalo = 'B'
              
                    # Venda pp9 # Padrão 1
                                if cl1<op1 and Lcdl1<=pp9-3.0 and cl0>op0 and Hcdl0>=pp9+1.5 and pr==pp9-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pp9-1.0 and Hcdl1<=percA+2.5 and cl1<pp9-1.0 and Hcdl0>=pp9+1.0 and pr==pp9-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pp9-0.50 and cl1==pp9 and op0==pp9 and Hcdl0>=pp9+1.5 and pr==pp9-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp9 and op1>=pp9+3.0 and Lcdl0==pp9 and op0-Lcdl0>=3.0 and pr==pp9-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp9-Lcdl1>=4 and Hcdl1>=pp9+2.0 and pp9-op0>=2 and Hcdl0==pp9 and pr==pp9-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
                # COMPRA pp8    Padrão 1
                                elif cl1>op1 and Hcdl1>=pp8+3.0 and cl0<op0 and Lcdl0<=pp8-1.5 and pr==pp8+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pp8-1.0 and Lcdl1>=percB-2.5 and cl1>pp8+1.0 and Lcdl0<=pp8-1.0 and pr==pp8+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pp8+0.50 and cl1==pp8 and op0==pp8 and Lcdl0<=pp8-1.5 and pr == pp8+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp8 and op1<=pp8-3.0 and Hcdl0==pp8 and Hcdl0-op0>=3.0 and pr==pp8+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp8>=4 and Lcdl1<=pp8+2.0 and op0-pp8>=2 and Lcdl0==pp8 and pr==pp8+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pp8>=3.5 and cl1>op1 and op1-pp8>=2.5 and Lcdl0<=pp8 and pr==pp8+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                    
                            elif pr<=pp8 and pr>=pp7:
                                percAA = pp9
                                percA = pp8
                                percB = pp7
                                percBB = pp6
                                intervalo = 'C'
            
                # VENDA pp8     Padrão 1 
                                if cl1<op1 and Lcdl1<=pp8-3.0 and cl0>op0 and Hcdl0>=pp8+1.5 and pr==pp8-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pp8-1.0 and Hcdl1<=percA+2.5 and cl1<pp8-1.0 and Hcdl0>=pp8+1.0 and pr==pp8-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pp8-0.50 and cl1==pp8 and op0==pp8 and Hcdl0>=pp8+1.5 and pr==pp8-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp8 and op1>=pp8+3.0 and Lcdl0==pp8 and op0-Lcdl0>=3.0 and pr==pp8-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp8-Lcdl1>=4 and Hcdl1>=pp8+2.0 and pp8-op0>=2 and Hcdl0==pp8 and pr==pp8-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
              # COMPRA pp7      Padrão 1
                                elif cl1>op1 and Hcdl1>=pp7+3.0 and cl0<op0 and Lcdl0<=pp7-1.5 and pr==pp7+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pp7-1.0 and Lcdl1>=percB-2.5 and cl1>pp7+1.0 and Lcdl0<=pp7-1.0 and pr==pp7+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pp7+0.50 and cl1==pp7 and op0==pp7 and Lcdl0<=pp7-1.5 and pr == pp7+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp7 and op1<=pp7-3.0 and Hcdl0==pp7 and Hcdl0-op0>=3.0 and pr==pp7+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp7>=4 and Lcdl1<=pp7+2.0 and op0-pp7>=2 and Lcdl0==pp7 and pr==pp7+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pp7>=3.5 and cl1>op1 and op1-pp7>=2.5 and Lcdl0<=pp7 and pr==pp7+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                    
                            elif pr<=pp7 and pr>=pp6:
                                percAA = pp8
                                percA = pp7
                                percB = pp6
                                percBB = pp5
                                intervalo = 'D'       
            
                # VENDA pp7     Padrão 1
                                if cl1<op1 and Lcdl1<=pp7-3.0 and cl0>op0 and Hcdl0>=pp7+1.5 and pr==pp7-1.0:  
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pp7-1.0 and Hcdl1<=percA+2.5 and cl1<pp7-1.0 and Hcdl0>=pp7+1.0 and pr==pp7-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pp7-0.50 and cl1==pp7 and op0==pp7 and Hcdl0>=pp7+1.5 and pr==pp7-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp7 and op1>=pp7+3.0 and Lcdl0==pp7 and op0-Lcdl0>=3.0 and pr==pp7-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp7-Lcdl1>=4 and Hcdl1>=pp7+2.0 and pp7-op0>=2 and Hcdl0==pp7 and pr==pp7-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pp6      Padrão 1
                                elif cl1>op1 and Hcdl1>=pp6+3.0 and cl0<op0 and Lcdl0<=pp6-1.5 and pr==pp6+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pp6-1.0 and Lcdl1>=percB-2.5 and cl1>pp6+1.0 and Lcdl0<=pp6-1.0 and pr==pp6+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # PAdrão 3
                                elif cl1>op1 and Hcdl1>=pp6+0.50 and cl1==pp6 and op0==pp6 and Lcdl0<=pp6-1.5 and pr == pp6+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp6 and op1<=pp6-3.0 and Hcdl0==pp6 and Hcdl0-op0>=3.0 and pr==pp6+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp6>=4 and Lcdl1<=pp6+2.0 and op0-pp6>=2 and Lcdl0==pp6 and pr==pp6+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pp6>=3.5 and cl1>op1 and op1-pp6>=2.5 and Lcdl0<=pp6 and pr==pp6+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                            
                            elif pr<=pp6 and pr>=pp5:
                                percAA = pp7
                                percA = pp6
                                percB = pp5
                                percBB = pp4
                                intervalo = 'E'
             
                    # VENDA pp6    Padrão 1
                                if cl1<op1 and Lcdl1<=pp6-3.0 and cl0>op0 and Hcdl0>=pp6+1.5 and pr==pp6-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pp6-1.0 and Hcdl1<=percA+2.5 and cl1<pp6-1.0 and Hcdl0>=pp6+1.0 and pr==pp6-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pp6-0.50 and cl1==pp6 and op0==pp6 and Hcdl0>=pp6+1.5 and pr==pp6-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp6 and op1>=pp6+3.0 and Lcdl0==pp6 and op0-Lcdl0>=3.0 and pr==pp6-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp6-Lcdl1>=4 and Hcdl1>=pp6+2.0 and pp6-op0>=2 and Hcdl0==pp6 and pr==pp6-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pp5      Padrão 1
                                elif cl1>op1 and Hcdl1>=pp5+3.0 and cl0<op0 and Lcdl0<=pp5-1.5 and pr==pp5+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # PAdrão 2
                                elif cl1<op1 and Lcdl1<=pp5-1.0 and Lcdl1>=percB-2.5 and cl1>pp5+1.0 and Lcdl0<=pp5-1.0 and pr==pp5+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pp5+0.50 and cl1==pp5 and op0==pp5 and Lcdl0<=pp5-1.5 and pr==pp5+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # PAdrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp5 and op1<=pp5-3.0 and Hcdl0==pp5 and Hcdl0-op0>=3.0 and pr==pp5+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp5>=4 and Lcdl1<=pp5+2.0 and op0-pp5>=2 and Lcdl0==pp5 and pr==pp5+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pp5>=3.5 and cl1>op1 and op1-pp5>=2.5 and Lcdl0<=pp5 and pr==pp5+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                    
                            elif pr<=pp5 and pr>=pp4:
                                percAA = pp6
                                percA = pp5
                                percB = pp4
                                percBB = pp3
                                intervalo = 'F'
                                
                 # VENDA pp5    Padrão 1
                                if cl1<op1 and Lcdl1<=pp5-3.0 and cl0>op0 and Hcdl0>=pp5+1.5 and pr==pp5-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pp5-1.0 and Hcdl1<=percA+2.5 and cl1<pp5-1.0 and Hcdl0>=pp5+1.0 and pr==pp5-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # PAdrão 3
                                elif cl1<op1 and Lcdl1<=pp5-0.50 and cl1==pp5 and op0==pp5 and Hcdl0>=pp5+1.5 and pr==pp5-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp5 and op1>=pp5+3.0 and Lcdl0==pp5 and op0-Lcdl0>=3.0 and pr==pp5-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp5-Lcdl1>=4 and Hcdl1>=pp5+2.0 and pp5-op0>=2 and Hcdl0==pp5 and pr==pp5-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pp4      Padrão 1
                                elif cl1>op1 and Hcdl1>=pp4+3.0 and cl0<op0 and Lcdl0<=pp4-1.5 and pr==pp4+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pp4-1.0 and Lcdl1>=percB-2.5 and cl1>pp4+1.0 and Lcdl0<=pp4-1.0 and pr==pp4+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pp4+0.50 and cl1==pp4 and op0==pp4 and Lcdl0<=pp4-1.5 and pr == pp4+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # PAdrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp4 and op1<=pp4-3.0 and Hcdl0==pp4 and Hcdl0-op0>=3.0 and pr==pp4+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp4>=4 and Lcdl1<=pp4+2.0 and op0-pp4>=2 and Lcdl0==pp4 and pr==pp4+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pp4>=3.5 and cl1>op1 and op1-pp4>=2.5 and Lcdl0<=pp4 and pr==pp4+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pp4 and pr>=pp3:
                                percAA = pp5
                                percA = pp4
                                percB = pp3
                                percBB = pp2
                                intervalo = 'G'
                                
                 # VENDA pp4    Padrão 1
                                if cl1<op1 and Lcdl1<=pp4-3.0 and cl0>op0 and Hcdl0>=pp4+1.5 and pr==pp4-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # PAdrão 2
                                elif cl1>op1 and Hcdl1>=pp4-1.0 and Hcdl1<=percA+2.5 and cl1<pp4-1.0 and Hcdl0>=pp4+1.0 and pr==pp4-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # PAdrão 3
                                elif cl1<op1 and Lcdl1<=pp4-0.50 and cl1==pp4 and op0==pp4 and Hcdl0>=pp4+1.5 and pr==pp4-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp4 and op1>=pp4+3.0 and Lcdl0==pp4 and op0-Lcdl0>=3.0 and pr==pp4-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp4-Lcdl1>=4 and Hcdl1>=pp4+2.0 and pp4-op0>=2 and Hcdl0==pp4 and pr==pp4-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                               
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                
              # COMPRA pp3      Padrão 1
                                elif cl1>op1 and Hcdl1>=pp3+3.0 and cl0<op0 and Lcdl0<=pp3-1.5 and pr==pp2+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pp3-1.0 and Lcdl1>=percB-2.5 and cl1>pp3+1.0 and Lcdl0<=pp3-1.0 and pr==pp3+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pp3+0.50 and cl1==pp3 and op0==pp3 and Lcdl0<=pp3-1.5 and pr == pp3+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp3 and op1<=pp3-3.0 and Hcdl0==pp3 and Hcdl0-op0>=3.0 and pr==pp3+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp3>=4 and Lcdl1<=pp3+2.0 and op0-pp3>=2 and Lcdl0==pp3 and pr==pp3+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pp3>=3.5 and cl1>op1 and op1-pp3>=2.5 and Lcdl0<=pp3 and pr==pp3+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pp3 and pr>=pp2:
                                percAA = pp4
                                percA = pp3
                                percB = pp2
                                percBB = pp1
                                intervalo = 'H'
                                
                 # VENDA pp3#   Padrão 1
                                if cl1<op1 and Lcdl1<=pp3-3.0 and cl0>op0 and Hcdl0>=pp3+1.5 and pr==pp3-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pp3-1.0 and Hcdl1<=percA+2.5 and cl1<pp3-1.0 and Hcdl0>=pp3+1.0 and pr==pp3-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pp3-0.50 and cl1==pp3 and op0==pp3 and Hcdl0>=pp3+1.5 and pr==pp3-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp3 and op1>=pp3+3.0 and Lcdl0==pp3 and op0-Lcdl0>=3.0 and pr==pp3-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp3-Lcdl1>=4 and Hcdl1>=pp3+2.0 and pp3-op0>=2 and Hcdl0==pp3 and pr==pp3-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pp2      Padrão 1
                                elif cl1>op1 and Hcdl1>=pp2+3.0 and cl0<op0 and Lcdl0<=pp2-1.5 and pr==pp2+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pp2-1.0 and Lcdl1>=percB-2.5 and cl1>pp2+1.0 and Lcdl0<=pp2-1.0 and pr==pp2+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # PAdrão 3
                                elif cl1>op1 and Hcdl1>=pp2+0.50 and cl1==pp2 and op0==pp2 and Lcdl0<=pp2-1.5 and pr == pp2+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp2 and op1<=pp2-3.0 and Hcdl0==pp2 and Hcdl0-op0>=3.0 and pr==pp2+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp2>=4 and Lcdl1<=pp2+2.0 and op0-pp2>=2 and Lcdl0==pp2 and pr==pp2+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pp2>=3.5 and cl1>op1 and op1-pp2>=2.5 and Lcdl0<=pp2 and pr==pp2+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pp2 and pr>=pp1:
                                percAA = pp3
                                percA = pp2
                                percB = pp1
                                percBB = pr0
                                intervalo = 'I'
                                
                # VENDA pp2     Padrão 1
                                if cl1<op1 and Lcdl1<=pp2-3.0 and cl0>op0 and Hcdl0>=pp2+1.5 and pr==pp2-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pp2-1.0 and Hcdl1<=percA+2.5 and cl1<pp2-1.0 and Hcdl0>=pp2+1.0 and pr==pp2-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # PAdrão 3
                                elif cl1<op1 and Lcdl1<=pp2-0.50 and cl1==pp2 and op0==pp2 and Hcdl0>=pp2+1.5 and pr==pp2-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp2 and op1>=pp10+3.0 and Lcdl0==pp2 and op0-Lcdl0>=3.0 and pr==pp2-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp2-Lcdl1>=4 and Hcdl1>=pp2+2.0 and pp2-op0>=2 and Hcdl0==pp2 and pr==pp2-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pp1      Padrão 1
                                elif cl1>op1 and Hcdl1>=pp1+3.0 and cl0<op0 and Lcdl0<=pp1-1.5 and pr==pp1+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pp1-1.0 and Lcdl1>=percB-2.5 and cl1>pp1+1.0 and Lcdl0<=pp1-1.0 and pr==pp1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pp1+0.50 and cl1==pp1 and op0==pp1 and Lcdl0<=pp1-1.5 and pr == pp1+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pp1 and op1<=pp1-3.0 and Hcdl0==pp1 and Hcdl0-op0>=3.0 and pr==pp1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pp1>=4 and Lcdl1<=pp1+2.0 and op0-pp1>=2 and Lcdl0==pp1 and pr==pp1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # PAdrão 6
                                elif cl2>op2 and Hcdl2-pp1>=3.5 and cl1>op1 and op1-pp1>=2.5 and Lcdl0<=pp1 and pr==pp1+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pp1 and pr>=pr0:
                                percAA = pp2
                                percA = pp1
                                percB = pr0
                                percBB = pn1
                                intervalo = 'J'            
                                
                # VENDA pp1     Padrão 1
                                if cl1<op1 and Lcdl1<=pp1-3.0 and cl0>op0 and Hcdl0>=pp1+1.5 and pr==pp1-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pp1-1.0 and Hcdl1<=percA+2.5 and cl1<pp1-1.0 and Hcdl0>=pp1+1.0 and pr==pp1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pp1-0.50 and cl1==pp1 and op0==pp1 and Hcdl0>=pp1+1.5 and pr==pp1-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # PAdrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pp1 and op1>=pp1+3.0 and Lcdl0==pp1 and op0-Lcdl0>=3.0 and pr==pp1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pp1-Lcdl1>=4 and Hcdl1>=pp1+2.0 and pp1-op0>=2 and Hcdl0==pp1 and pr==pp1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pr0      Padrão 1
                                elif cl1>op1 and Hcdl1>=pr0+3.0 and cl0<op0 and Lcdl0<=pr0-1.5 and pr==pr0+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pr0-1.0 and Lcdl1>=percB-2.5 and cl1>pr0+1.0 and Lcdl0<=pr0-1.0 and pr==pr0+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pr0+0.50 and cl1==pr0 and op0==pr0 and Lcdl0<=pr0-1.5 and pr == pr0+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pr0 and op1<=pr0-3.0 and Hcdl0==pr0 and Hcdl0-op0>=3.0 and pr==pr0+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pr0>=4 and Lcdl1<=pr0+2.0 and op0-pr0>=2 and Lcdl0==pr0 and pr==pr0+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pr0>=3.5 and cl1>op1 and op1-pr0>=2.5 and Lcdl0<=pr0 and pr==pr0+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pr0 and pr>=pn1:
                                percAA = pp1
                                percA = pr0
                                percB = pn1
                                percBB = pn2
                                intervalo = 'k'
                                
                 # VENDA pr0    Padrão 1
                                if cl1<op1 and Lcdl1<=pr0-3.0 and cl0>op0 and Hcdl0>=pr0+1.5 and pr==pr0-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pr0-1.0 and Hcdl1<=percA+2.5 and cl1<pr0-1.0 and Hcdl0>=pr0+1.0 and pr==pr0-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pr0-0.50 and cl1==pr0 and op0==pr0 and Hcdl0>=pr0+1.5 and pr==pr0-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pr0 and op1>=pr0+3.0 and Lcdl0==pr0 and op0-Lcdl0>=3.0 and pr==pr0-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pr0-Lcdl1>=4 and Hcdl1>=pr0+2.0 and pr0-op0>=2 and Hcdl0==pr0 and pr==pr0-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pn1      Padrão 1
                                elif cl1>op1 and Hcdl1>=pn1+3.0 and cl0<op0 and Lcdl0<=pn1-1.5 and pr==pn1+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn1-1.0 and Lcdl1>=percB-2.5 and cl1>pn1+1.0 and Lcdl0<=pn1-1.0 and pr==pn1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn1+0.50 and cl1==pn1 and op0==pn1 and Lcdl0<=pn1-1.5 and pr==pn1+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn1 and op1<=pn1-3.0 and Hcdl0==pn1 and Hcdl0-op0>=3.0 and pr==pn1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn1>=4 and Lcdl1<=pn1+2.0 and op0-pn1>=2 and Lcdl0==pn1 and pr==pn1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pn1>=3.5 and cl1>op1 and op1-pn1>=2.5 and Lcdl0<=pn1 and pr==pn1+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pn1 and pr>=pn2:
                                percAA = pr0
                                percA = pn1
                                percB = pn2
                                percBB = pn3
                                intervalo = 'L'
                                
                # VENDA pn1     Padrão 1
                                if cl1<op1 and Lcdl1<=pn1-3.0 and cl0>op0 and Hcdl0>=pn1+1.5 and pr==pn1-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pn1-1.0 and Hcdl1<=percA+2.5 and cl1<pn1-1.0 and Hcdl0>=pn1+1.0 and pr==pn1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pn1-0.50 and cl1==pn1 and op0==pn1 and Hcdl0>=pn1+1.5 and pr==pn1-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn1 and op1>=pn1+3.0 and Lcdl0==pn1 and op0-Lcdl0>=3.0 and pr==pn1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pn1-Lcdl1>=4 and Hcdl1>=pn1+2.0 and pn1-op0>=2 and Hcdl0==pn1 and pr==pn1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
              # COMPRA pn2      Padrão 1
                                elif cl1>op1 and Hcdl1>=pn2+3.0 and cl0<op0 and Lcdl0<=pn2-1.5 and pr==pn2+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn2-1.0 and Lcdl1>=percB-2.5 and cl1>pn2+1.0 and Lcdl0<=pn2-1.0 and pr==pn2+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn2+0.50 and cl1==pn2 and op0==pn2 and Lcdl0<=pn2-1.5 and pr==pn2+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn2 and op1<=pn2-3.0 and Hcdl0==pn2 and Hcdl0-op0>=3.0 and pr==pn2+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn2>=4 and Lcdl1<=pn2+2.0 and op0-pn2>=2 and Lcdl0==pn2 and pr==pn2+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pn2>=3.5 and cl1>op1 and op1-pn2>=2.5 and Lcdl0<=pn2 and pr==pn2+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                            
                            elif pr<=pn2 and pr>=pn3:
                                percAA = pn1
                                percA = pn2
                                percB = pn3
                                percBB = pn4
                                intervalo = 'M'            
                                
                # VENDA pn2     Padrão 1
                                if cl1<op1 and Lcdl1<=pn2-3.0 and cl0>op0 and Hcdl0>=pn2+1.5 and pr==pn2-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pn2-1.0 and Hcdl1<=percA+2.5 and cl1<pn2-1.0 and Hcdl0>=pn2+1.0 and pr==pn2-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # PAdrão 3
                                elif cl1<op1 and Lcdl1<=pn2-0.50 and cl1==pn2 and op0==pn2 and Hcdl0>=pn2+1.5 and pr==pn2-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn2 and op1>=pn1+3.0 and Lcdl0==pn2 and op0-Lcdl0>=3.0 and pr==pn2-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pn2-Lcdl1>=4 and Hcdl1>=pn2+2.0 and pn2-op0>=2 and Hcdl0==pn2 and pr==pn2-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pn3      Padrão 1
                                elif cl1>op1 and Hcdl1>=pn3+3.0 and cl0<op0 and Lcdl0<=pn3-1.5 and pr==pn3+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn3-1.0 and Lcdl1>=percB-2.5 and cl1>pn3+1.0 and Lcdl0<=pn3-1.0 and pr==pn3+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn3+0.50 and cl1==pn3 and op0==pn3 and Lcdl0<=pn3-1.5 and pr==pn3+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn3 and op1<=pn3-3.0 and Hcdl0==pn3 and Hcdl0-op0>=3.0 and pr==pn3+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn3>=4 and Lcdl1<=pn3+2.0 and op0-pn3>=2 and Lcdl0==pn3 and pr==pn3+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pn3>=3.5 and cl1>op1 and op1-pn3>=2.5 and Lcdl0<=pn3 and pr==pn3+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pn3 and pr>=pn4:
                                percAA = pn2
                                percA = pn3
                                percB = pn4
                                percBB = pn5
                                intervalo = 'N'             
                                
                # VENDA pn3     Padrão 1
                                if cl1<op1 and Lcdl1<=pn3-3.0 and cl0>op0 and Hcdl0>=pn3+1.5 and pr==pn3-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pn3-1.0 and Hcdl1<=percA+2.5 and cl1<pn3-1.0 and Hcdl0>=pn3+1.0 and pr==pn3-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pn3-0.50 and cl1==pn3 and op0==pn3 and Hcdl0>=pn3+1.5 and pr==pn3-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn3 and op1>=pn3+3.0 and Lcdl0==pn3 and op0-Lcdl0>=3.0 and pr==pn3-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # PAdrão 5
                                elif cl1<op1 and pn3-Lcdl1>=4 and Hcdl1>=pn3+2.0 and pn3-op0>=2 and Hcdl0==pn3 and pr==pn3-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
              # COMPRA pn4      Padrão 1
                                elif cl1>op1 and Hcdl1>=pn4+3.0 and cl0<op0 and Lcdl0<=pn4-1.5 and pr==pn4+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn4-1.0 and Lcdl1>=percB-2.5 and cl1>pn4+1.0 and Lcdl0<=pn4-1.0 and pr==pn4+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=percB+0.50 and cl1==percB and op0==percB and Lcdl0<=percB-1.5 and pr==percB+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # PAdrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn4 and op1<=pn1-3.0 and Hcdl0==pn4 and Hcdl0-op0>=3.0 and pr==pn4+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn4>=4 and Lcdl1<=pn4+2.0 and op0-pn4>=2 and Lcdl0==pn4 and pr==pn4+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pn4>=3.5 and cl1>op1 and op1-pn4>=2.5 and Lcdl0<=pn4 and pr==pn4+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            
                            elif pr<=pn4 and pr>=pn5:
                                percAA = pn3
                                percA = pn4
                                percB = pn5
                                percBB = pn6
                                intervalo = 'O' 
                                
                # VENDA pn4     Padrão 1
                                if cl1<op1 and Lcdl1<=pn4-3.0 and cl0>op0 and Hcdl0>=pn4+1.5 and pr==pn4-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pn4-1.0 and Hcdl1<=percA+2.5 and cl1<pn4-1.0 and Hcdl0>=pn4+1.0 and pr==pn4-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pn4-0.50 and cl1==pn4 and op0==pn4 and Hcdl0>=pn4+1.5 and pr==pn4-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn4 and op1>=pn4+3.0 and Lcdl0==pn4 and op0-Lcdl0>=3.0 and pr==pn4-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pn4-Lcdl1>=4 and Hcdl1>=pn4+2.0 and pn4-op0>=2 and Hcdl0==pn4 and pr==pn4-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
               # COMPRA pn5     Padrão 1
                                elif cl1>op1 and Hcdl1>=pn5+3.0 and cl0<op0 and Lcdl0<=pn5-1.5 and pr==pn5+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn5-1.0 and Lcdl1>=percB-2.5 and cl1>pn5+1.0 and Lcdl0<=pn5-1.0 and pr==pn5+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn5+0.50 and cl1==pn5 and op0==pn5 and Lcdl0<=pn5-1.5 and pr==pn5+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn5 and op1<=pn5-3.0 and Hcdl0==pn5 and Hcdl0-op0>=3.0 and pr==pn5+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn5>=4 and Lcdl1<=pn5+2.0 and op0-pn5>=2 and Lcdl0==pn5 and pr==pn5+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pn5>=3.5 and cl1>op1 and op1-pn5>=2.5 and Lcdl0<=pn5 and pr==pn5+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pn5 and pr>=pn6:
                                percAA = pn4
                                percA = pn5
                                percB = pn6
                                percBB = pn7
                                intervalo = 'P'            
                                
                # VENDA pn5     Padrão 1
                                if cl1<op1 and Lcdl1<=pn5-3.0 and cl0>op0 and Hcdl0>=pn5+1.5 and pr==pn5-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pn5-1.0 and Hcdl1<=percA+2.5 and cl1<pn5-1.0 and Hcdl0>=pn5+1.0 and pr==pn5-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pn5-0.50 and cl1==pn5 and op0==pn5 and Hcdl0>=pn5+1.5 and pr==pn5-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn5 and op1>=pn5+3.0 and Lcdl0==pn5 and op0-Lcdl0>=3.0 and pr==pn5-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pn5-Lcdl1>=4 and Hcdl1>=pn5+2.0 and pn5-op0>=2 and Hcdl0==pn5 and pr==pn5-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pn6      Padrão 1
                                elif cl1>op1 and Hcdl1>=pn6+3.0 and cl0<op0 and Lcdl0<=pn6-1.5 and pr==pn6+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn6-1.0 and Lcdl1>=percB-2.5 and cl1>pn6+1.0 and Lcdl0<=pn6-1.0 and pr==pn6+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn6+0.50 and cl1==pn6 and op0==pn6 and Lcdl0<=pn6-1.5 and pr==pn6+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn6 and op1<=pn6-3.0 and Hcdl0==pn6 and Hcdl0-op0>=3.0 and pr==pn6+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn6>=4 and Lcdl1<=pn6+2.0 and op0-pn6>=2 and Lcdl0==pn6 and pr==pn6+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pn6>=3.5 and cl1>op1 and op1-pn6>=2.5 and Lcdl0<=pn6 and pr==pn6+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                
                            elif pr<=pn6 and pr>=pn7:
                                percAA = pn5
                                percA = pn6
                                percB = pn7
                                percBB = pn8
                                intervalo = 'Q' 
                                
                # VENDA pn6     Padrão 1
                                if cl1<op1 and Lcdl1<=pn6-3.0 and cl0>op0 and Hcdl0>=pn6+1.5 and pr==pn6-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
                                # Padrão 2        
                                elif cl1>op1 and Hcdl1>=pn6-1.0 and Hcdl1<=percA+2.5 and cl1<pn6-1.0 and Hcdl0>=pn6+1.0 and pr==pn6-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pn6-0.50 and cl1==pn6 and op0==pn6 and Hcdl0>=pn6+1.5 and pr==pn6-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn6 and op1>=pn6+3.0 and Lcdl0==pn6 and op0-Lcdl0>=3.0 and pr==pn6-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pn6-Lcdl1>=4 and Hcdl1>=pn6+2.0 and pn6-op0>=2 and Hcdl0==pn6 and pr==pn6-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
              # COMPRA pn7      Padrão 1
                                elif cl1>op1 and Hcdl1>=pn7+3.0 and cl0<op0 and Lcdl0<=pn7-1.5 and pr==pn7+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn7-1.0 and Lcdl1>=percB-2.5 and cl1>pn7+1.0 and Lcdl0<=pn7-1.0 and pr==pn7+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn7+0.50 and cl1==pn7 and op0==pn7 and Lcdl0<=pn7-1.5 and pr==pn7+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn7 and op1<=pn7-3.0 and Hcdl0==pn7 and Hcdl0-op0>=3.0 and pr==pn7+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn7>=4 and Lcdl1<=pn7+2.0 and op0-pn7>=2 and Lcdl0==pn7 and pr==pn7+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-pn7>=3.5 and cl1>op1 and op1-pn7>=2.5 and Lcdl0<=pn7 and pr==pn7+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pn7 and pr>=pn8:
                                percAA = pn6
                                percA = pn7
                                percB = pn8
                                percBB = pn9
                                intervalo = 'R'
                                
                # VENDA pn7     Padrão 1
                                if cl1<op1 and Lcdl1<=pn7-3.0 and cl0>op0 and Hcdl0>=pn7+1.5 and pr==pn7-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pn7-1.0 and Hcdl1<=percA+2.5 and cl1<pn7-1.0 and Hcdl0>=pn7+1.0 and pr==pn7-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pn7-0.50 and cl1==pn7 and op0==pn7 and Hcdl0>=pn7+1.5 and pr==pn7-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn7 and op1>=pn7+3.0 and Lcdl0==pn7 and op0-Lcdl0>=3.0 and pr==pn7-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pn7-Lcdl1>=4 and Hcdl1>=pn7+2.0 and pn7-op0>=2 and Hcdl0==pn7 and pr==pn7-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
                # COMPRA pn8    Padrão 1
                                elif cl1>op1 and Hcdl1>=pn8+3.0 and cl0<op0 and Lcdl0<=pn8-1.5 and pr==pn8+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn8-1.0 and Lcdl1>=percB-2.5 and cl1>pn8+1.0 and Lcdl0<=pn8-1.0 and pr==pn8+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn8+0.50 and cl1==pn8 and op0==pn8 and Lcdl0<=pn8-1.5 and pr==pn8+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn8 and op1<=pn8-3.0 and Hcdl0==pn8 and Hcdl0-op0>=3.0 and pr==pn8+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn8>=4 and Lcdl1<=pn8+2.0 and op0-pn8>=2 and Lcdl0==pn8 and pr==pn8+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-percB>=3.5 and cl1>op1 and op1-percB>=2.5 and Lcdl0<=percB and pr==percB+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pn8 and pr>=pn9:
                                percAA = pn7
                                percA = pn8
                                percB = pn9
                                percBB = pn10
                                intervalo = 'S'
                                
                # VENDA pn8     Padrão 1
                                if cl1<op1 and Lcdl1<=pn8-3.0 and cl0>op0 and Hcdl0>=pn8+1.5 and pr==pn8-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pn8-1.0 and Hcdl1<=percA+2.5 and cl1<pn8-1.0 and Hcdl0>=pn8+1.0 and pr==pn8-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pn8-0.50 and cl1==pn8 and op0==pn8 and Hcdl0>=pn8+1.5 and pr==pn8-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn8 and op1>=pn8+3.0 and Lcdl0==pn8 and op0-Lcdl0>=3.0 and pr==pn8-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pn8-Lcdl1>=4 and Hcdl1>=pn8+2.0 and pn8-op0>=2 and Hcdl0==pn8 and pr==pn8-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
                # COMPRA pn9    Padrão 1
                                elif cl1>op1 and Hcdl1>=pn9+3.0 and cl0<op0 and Lcdl0<=pn9-1.5 and pr==pn9+1.0: 
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn9-1.0 and Lcdl1>=percB-2.5 and cl1>pn9+1.0 and Lcdl0<=pn9-1.0 and pr==pn9+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn9+0.50 and cl1==pn9 and op0==pn9 and Lcdl0<=pn9-1.5 and pr==pn9+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn9 and op1<=pn9-3.0 and Hcdl0==pn9 and Hcdl0-op0>=3.0 and pr==pn9+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn9>=4 and Lcdl1<=pn9+2.0 and op0-pn9>=2 and Lcdl0==pn9 and pr==pn9+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-percB>=3.5 and cl1>op1 and op1-percB>=2.5 and Lcdl0<=percB and pr==percB+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 7
                                elif op1<percBB and cl1>percB and percB-vwap1>=5 and Hcdl0<=vwap1 and pr==vwap1+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                            elif pr<=pn9 and pr>=pn10:
                                percAA = pn8
                                percA = pn9
                                percB = pn10
                                intervalo = 'T'
                                
                # VENDA pn9     Padrão 1
                                if cl1<op1 and Lcdl1<=pn9-3.0 and cl0>op0 and Hcdl0>=pn9+1.5 and pr==pn9-1.0: 
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 2
                                elif cl1>op1 and Hcdl1>=pn9-1.0 and Hcdl1<=percA+2.5 and cl1<pn9-1.0 and Hcdl0>=pn9+1.0 and pr==pn9-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 3
                                elif cl1<op1 and Lcdl1<=pn9-0.50 and cl1==pn9 and op0==pn9 and Hcdl0>=pn9+1.5 and pr==pn9-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 4
                                elif cl1<op1 and cl1-Lcdl1>=3.0 and Lcdl1==pn9 and op1>=pn9+3.0 and Lcdl0==pn9 and op0-Lcdl0>=3.0 and pr==pn9-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 5
                                elif cl1<op1 and pn9-Lcdl1>=4 and Hcdl1>=pn9+2.0 and pn9-op0>=2 and Hcdl0==pn9 and pr==pn9-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 6
                                elif cl2<op2 and percA-Lcdl2>=3.5 and cl1<op1 and percA-op1>=2.5 and Hcdl0>=percA and pr==percA-1.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 7
                                elif op1>percAA and cl1<percA and vwap1-percA>=5 and Lcdl0>=vwap1 and pr==vwap1-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 8
                                elif cl2<op2 and vwap2-percA>=3 and cl2<percA and cl1<op1 and op0<=percA-2 and Hcdl0>=vwap2 and pr==vwap2-2.0:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                        
                                # Padrão 9 
                                elif cl2>op2 and Hcdl2>=percA+1 and cl2<percA and  Hcdl1>=percA and cl1<percA and op0<percA and Hcdl0>=percA+1 and pr==percA-1.5:
                                    if Hcdl1>Hcdl0:
                                        venda1()
                                    elif Hcdl1<Hcdl0:
                                        venda2()
                                
             # COMPRA pn10      Padrão 1
                                elif cl1>op1 and Hcdl1>=pn10+3.0 and cl0<op0 and Lcdl0<=pn10-1.5 and pr==pn10+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 2
                                elif cl1<op1 and Lcdl1<=pn10-1.0 and Lcdl1>=percB-2.5 and cl1>pn10+1.0 and Lcdl0<=pn10-1.0 and pr==pn10+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 3
                                elif cl1>op1 and Hcdl1>=pn10+0.50 and cl1==pn10 and op0==pn10 and Lcdl0<=pn10-1.5 and pr==pn10+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 4
                                elif cl1>op1 and Hcdl1-cl1>=3.0 and Hcdl1==pn10 and op1<=pn10-3.0 and Hcdl0==pn10 and Hcdl0-op0>=3.0 and pr==pn10+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 5
                                elif cl1>op1 and Hcdl1-pn10>=4 and Lcdl1<=pn10+2.0 and op0-pn10>=2 and Lcdl0==pn10 and pr==pn10+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 6
                                elif cl2>op2 and Hcdl2-percB>=3.5 and cl1>op1 and op1-percB>=2.5 and Lcdl0<=percB and pr==percB+1.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                # Padrão 8 
                                elif cl2>op2 and percB-vwap2>=3 and cl2>percB and cl1>op1 and op0-percB>=2 and Lcdl0<=vwap2 and pr==vwap2+2.0:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
                                 # Padrão 9 
                                elif cl2<op2 and Lcdl2<=percB-1 and cl2>percB and  Lcdl1<=percB and cl1>percB and op0>percB and Lcdl0<=percB-1 and pr==percB+1.5:
                                    if Lcdl1<Lcdl0:
                                        compra1()
                                    elif Lcdl1>Lcdl0:
                                        compra2()
                                        
if data>data_A:
    print("... Periodo de teste Finalizado !", sep='\n')
    time.sleep(1)
    print("...",sep='\n')
    time.sleep(10)
    print('... Robô finalizado com sucesso!', sep='\n')
    time.sleep(10)
    print("...", sep='\n') 
 
elif ctalgda != cta_autorizada:
    print("... Conta logada diferente da conta autorizada !", sep='\n')
    time.sleep(1)
    print("...",sep='\n')
    time.sleep(10)
    print('... Robô finalizado com sucesso!', sep='\n')
    time.sleep(10)
    print("...", sep='\n') 


elif saldo_final>=profit:
    print("...", sep='\n') 
    time.sleep(2)
    print(f'... Meta do dia alcançada as {hr}, R$ {saldo_final:,.2f}')
    time.sleep(2)
    print("...", sep='\n') 
    print('... Por favor !!! Volte só amanhã ou no próximo dia útil !!', sep='\n')
    time.sleep(2)
    # concluímos a conexão ao terminal MetaTrader 5
    mt5.shutdown()
    time.sleep(10)
    print('... Robô finalizado com sucesso!', sep='\n')
    time.sleep(10)
    print("...", sep='\n') 
                    
elif saldo_final<=lossdodia:
    print("...", sep='\n') 
    time.sleep(2)
    print(f'... Stop loss do dia alcançada as {hr}, R$ {lossdodia:,.2f}')
    time.sleep(2)
    print("...", sep='\n') 
    print('... Por favor !!! Volte só amanhã ou no próximo dia útil !!', sep='\n')
    time.sleep(2)
    # concluímos a conexão ao terminal MetaTrader 5
    mt5.shutdown()
    time.sleep(10)
    print('... Robô finalizado com sucesso!', sep='\n')
    time.sleep(10)
    print("...", sep='\n')      

elif hr>=hr_final:
    print("...", sep='\n') 
    time.sleep(1)
    print(f'... Volume: {positions_total} | Hora: {hr} | Saldo: {saldo_final:,.2f} | Pontos: {soma} |', sep='\n')
    time.sleep(1)
    print( "...",sep='\n') 
    time.sleep(2)
    print("... Finalizando as operações por limite de horário definido - {}".format(hr_final), sep='\n') 
    time.sleep(2)
    print("...", sep='\n')
    # concluímos a conexão ao terminal MetaTrader 5
    mt5.shutdown()
    time.sleep(10)
    print('... Robô finalizado com sucesso!', sep='\n')
    time.sleep(10)
    print("...", sep='\n')   
