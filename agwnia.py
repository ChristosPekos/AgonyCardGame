import random
def deck():
    """H sunarthsh auth dhmiourgei mia trapoula, ta fulla ths opoias anakateuontai.H trapoula einai mia lista"""
    cards = []
    symbols = ['♥','♣','♦','♠']
    jqka = [('J',10),('Q',10),('K',10),('A',11)]
    deck = []
    for i in range(2,11):
        cards.append(str(i))
    for k in range(4):
        for q in range(9):
            deck.append((cards[q],symbols[k],int(cards[q])))
        for t in range(0,4):
            deck.append((jqka[t][0],symbols[k],jqka[t][1]))
    random.shuffle(deck)
    return deck
    """>>> deck()
    [('9', '♣', 9), ('Q', '♥', 10), ('3', '♦', 3), ('9', '♥', 9), ('10', '♥', 10), ('7', '♠', 7), ('4', '♥', 4), ('6', '♥', 6), ('8', '♠', 8), ('A', '♥', 11),
    ('6', '♠', 6), ('J', '♠', 10), ('5', '♣', 5), ('Q', '♦', 10), ('7', '♣', 7), ('2', '♥', 2), ('A', '♣', 11), ('4', '♠', 4), ('8', '♥', 8), ('K', '♠', 10),
    ('Q', '♠', 10), ('K', '♣', 10), ('J', '♥', 10), ('Q', '♣', 10), ('2', '♦', 2), ('3', '♣', 3), ('K', '♥', 10), ('A', '♦', 11), ('6', '♣', 6), ('9', '♦', 9),
    ('8', '♣', 8), ('3', '♠', 3), ('2', '♠', 2), ('K', '♦', 10), ('J', '♦', 10), ('6', '♦', 6), ('3', '♥', 3), ('10', '♣', 10), ('10', '♠', 10), ('7', '♥', 7), ('10', '♦', 10),
    ('4', '♣', 4), ('5', '♥', 5), ('8', '♦', 8), ('5', '♦', 5), ('7', '♦', 7), ('5', '♠', 5), ('9', '♠', 9), ('2', '♣', 2), ('4', '♦', 4), ('J', '♣', 10), ('A', '♠', 11)]
    """

def match(card1,card2):
    """H sunarthsh auth elegxei an h card1 tairiazei me thn card2 ws pros ton arithmo/figoura h seira.An tairiazoun, epistrefei True,alliws False.
    Sto paixnidi ths agwnias,o Assos tairiazei me ola ta fula aneksarthtou seiras"""
    flag = 0
    if card1[0] == card2[0]:
        flag = 1
    if card1[1] == card2[1]:
        flag = 1
    if card1[0] == 'A':
        flag = 1
    if flag == 1:
        return True
    else:
        return False
    """>>> match(('9', '♣', 9), ('Q', '♥', 10))
       False
       >>> match(('3', '♦', 3),('3', '♣', 3))
       True
       >>> match(('5', '♥', 5),('10', '♥', 10))
       True
       >>> match(('A', '♠', 11),('6', '♦', 6))
       True
    """

def givecards(deckk,numofplayers):
    """dhmiourgei ena dictionary opou se kathe paixth antistoixoun apo 7 fulla"""
    players = []
    fulla_paixtwn = {}
    for i in range(1,numofplayers+1):
        player = []
        y = 0
        while y <= 6:
            player.append(deckk.pop(y))
            y+=1
        players.append(player)
    z = 0
    for d in range(1,numofplayers+1):
        fulla_paixtwn[d] = players[z]
        z +=1
    return fulla_paixtwn
    """>>> gamedeck = deck()
       >>> arithmos_paixtwn = 4
       >>> givecards(gamedeck,arithmos_paixtwn)
       {1: [('6', '♣', 6), ('10', '♥', 10), ('Q', '♣', 10), ('3', '♣', 3), ('6', '♥', 6), ('10', '♠', 10), ('6', '♠', 6)],
        2: [('7', '♥', 7), ('8', '♠', 8), ('A', '♦', 11), ('5', '♦', 5), ('A', '♣', 11), ('5', '♣', 5), ('A', '♠', 11)],
        3: [('10', '♣', 10), ('J', '♠', 10), ('4', '♦', 4), ('K', '♥', 10), ('3', '♠', 3), ('3', '♥', 3), ('K', '♣', 10)],
        4: [('8', '♦', 8), ('6', '♦', 6), ('2', '♠', 2), ('J', '♣', 10), ('5', '♠', 5), ('J', '♥', 10), ('8', '♥', 8)]}
    """

def draw_card(closed_pile,cards):
    if closed_pile!=0:
        cards.append(closed_pile[0])
        closed_pile.remove(closed_pile[0])
    return cards

def pontoi_paixtwn(vathm):
    """H sunarthsh auth metraei tous vathmous pou sugkentrwse enas paixths me vash ta fulla pou tou emeinan"""
    pontoii = 0
    arithmos_full = len(vathm)
    if len(vathm) != 0:
        for m in range(arithmos_full):    
            pontoii += vathm[m][2]
    return pontoii
    """>>> fulla_paixth = [('8', '♦', 8), ('6', '♦', 6), ('2', '♠', 2), ('J', '♣', 10)]
       >>> pontoi_paixtwn(fulla_paixth)
       26
    """
    
def pinakas_paixtwn(arithmospaixtwn):
    """H sunarthsh auth dhmiourgei ena dictionary sto opoio tha prosmetrountai oi vathmoi enws paixth"""
    pinaka = {}
    for k in range(1,arithmospaixtwn+1):
        pinaka[k] = 0
    return pinaka
    """>>> numberofplayers = 4
       >>> pinakas_paixtwn(numberofplayers)
       {1: 0, 2: 0, 3: 0, 4: 0}
    """

def endofclosedpile(closed_pile,open_pile):
    """an ta fulla ths kleisths trapoulas teleiwsoun,ola ta fulla ths anoixths ektos apo to anoixto
    metaferontai sthn kleisth trapoula kai anakatevontai
    """
    for t in range(1,len(open_pile)):
        closed_pile.append(open_pile.pop())
    print('Tote tha travikseis ena fullo','\n\n')
    random.shuffle(closed_pile)
    

def eightcard(open_pile,cardsofplayer,closed_pile):
    """Otan enas paixths riksei 8, ksanapaizei. An den exei fullo, tote tha traviksei ena apo thn kleisth trapoula.
    Enas paixths mporei na riksei osa 8 exei sth seira kai na ksanapaizei
    """
    while open_pile[0][0] == '8':
        print('ksanapaizeis')
        print('to anoixto fullo einai to ', open_pile[0],'\n\n')
        print('Ta fulla sou einai:',cardsofplayer)
        exwfullo2 = str(input('Exeis fullo na paikseis? [nai/oxi]: '))
        if len(cardsofplayer) == 1:
            if cardsofplayer[0][0] == '8':
                print('Den mporeis na vgeis me 8, opote tha travikseis ena fullo')
                draw_card(open_pile,cardsofplayer)
        if exwfullo2 == 'nai' :
            fullo2 = int(input('Grapse ton arithmo tou fullou pou theleis na paikseis, : '))
            
                
                    
                    
            
            if match(cardsofplayer[fullo2-1],open_pile[0]):
                open_pile.insert(0,cardsofplayer[fullo2-1])
                cardsofplayer.remove(cardsofplayer[fullo2-1])
                print('epaikses epituxws to fullo','\n\n')
        elif exwfullo2 == 'oxi' :
            
            print('Tote tha travikseis ena fullo','\n\n')
            draw_card(closed_pile,cardsofplayer)
            break
            
        

def agwnia():
    """To paixnidi ths agwnias ksekinaei"""
    anoixta_fulla = []

    arithmos_paixtwn = int(input('Dwse mou ton arithmo twn paixtwn: ' ))
    
    print("\n")

   


    flagpaixnidiou = 0
    while 1:
        if flagpaixnidiou == 1:
            break
        print("Mia kainouria partida ksekinaei",'\n\n')
        trapoula = deck()
        paixtes_fulla = givecards(trapoula,arithmos_paixtwn)
        anoixta_fulla.append(trapoula.pop(0))
        pinakas_vathmwn = pinakas_paixtwn(arithmos_paixtwn)
        flagpartidas = 0
        flagofnine = 0
        flagofseven = 0
        flagoface = 0
        
        
        while 1:
            
            for k,v in paixtes_fulla.items():
                
                if len(trapoula) == 0:
                    endofclosedpile(trapoula,anoixta_fulla)
                """edw antimetwpizetai h periptwsh sthn opoia o paixths rixnei 9"""
                if flagofnine == 1:
                    print('paixth ', k, ', xaneis thn seira sou','\n\n')
                    flagofnine = 0
                    continue
                
                   
                
                """edw antimetwpizetai h periptwsh sthn opoia o paixths rixnei 7"""
                if flagofseven == 1:
                        
                    print('paixth ' , k ,', Tha travikseis 2 fulla','\n\n')
                    draw_card(trapoula,v)
                    draw_card(trapoula,v)
                    flagofseven = 0
                
                
                
                print('to anoixto fullo einai to ' , anoixta_fulla[0],'\n\n')
                
                

                     
                    
                    
                    
                
                        
                        
                    
                print('paixth ' , k,', Ta fulla sou einai:',v)
                exwfullo = str(input('Exeis fullo na paikseis? [nai/oxi]: '))
                print('\n\n')
                if exwfullo == 'nai' :
                    print("\n\n")
                    
                    if len(v) == 1:
                        if v[0][0] == '8':
                            print('Den mporeis na vgeis me 8, opote tha travikseis ena fullo')
                            draw_card(trapoula,v)
                    fullo=int(input('Grapse ton arithmo tou fullou pou theleis na paikseis: '))
                    if match(v[fullo-1],anoixta_fulla[0]):
                        anoixta_fulla.insert(0,v[fullo-1])
                        v.remove(v[fullo-1])
                        print('epaikses epituxws to fullo','\n\n')
                        print("\n\n")
                        """edw to paixnidi lamvanei to mhnuma pws o paixths epaikse 9"""
                        if anoixta_fulla[0][0] == '9':
                            flagofnine = 1
                        """edw antimetwpizetai h periptwsh sthn opoia o paixths rixnei 8"""
                        if anoixta_fulla[0][0] == '8':
                            eightcard(anoixta_fulla,v,trapoula)
                        """"""
                        if anoixta_fulla[0][0] == '7':
                            flagofseven = 1
                        """edw to paixnidi lamvanei to mhnuma pws o paixths epaikse 9"""    
                        if anoixta_fulla[0][0] == 'A':
                            flagoface = 1
                        
                    
                    
                            
                            
                            
                    """Ti sumvainei an o paixths epaikse to teleutaio tou fullo"""
                    if len(v) == 0:
                        print("paixth,",k," kerdises thn partida")
                        for t in range(1,arithmos_paixtwn+1):
                            pinakas_vathmwn[t] += pontoi_paixtwn(paixtes_fulla[t]) 
                        """edw prosmetrountai oi pontoi twn paixtwn"""
                    



                elif exwfullo =='oxi':

                    print('Tote tha travikseis ena fullo','\n\n')
                    draw_card(trapoula,v)



                        
                elif exwfullo == 'exit':
                    
                    flagpartidas =1
                    flagpaixnidiou = 1
                    break
                
                if len(v) == 0:
                    """se periptwsh pou teleiwsei h partida, parousiazontai oi vathmoi twn paixtwn"""
                    flagpartidas = 1
                    for o in range(1,arithmos_paixtwn+1):
                        if pinakas_vathmwn[o] >=50:
                            flagpaixnidiou = 1
                        print('paixth ', o, ', oi pontoi sou einai: ',pinakas_vathmwn[o])
                    break
            if flagpartidas == 1:
                break
    print('To paixnidi teleiwse')
    

agwnia()

