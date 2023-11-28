import random
class Phase:
    Menu = 1
    Setting = 2

class Category:
    Space = 1
    Heart = 2
    Diamond = 3
    Club = 4
    
    def getAll():
        return [Category.Space, Category.Heart, Category.Diamond, Category.Club]

class CardType:
    Normal = 0
    BlackJack = 1
    FiveCards = 2
    Over = 3

class PokerCard:
    def __init__(self, num, category, hide = False):
        self.category = category
        self.num = num
        self.hide = hide
    def __str__(self):
        if self.hide:
            print("|ＸＸ|",end="")
        else:
            if self.category == Category.Space:
                print("|♠",end="")
            elif self.category == Category.Heart:
                print("|♥", end="")
            elif self.category == Category.Diamond:
                print("|♦", end="")
            elif self.category == Category.Club:
                print("|♣", end="")
            if (self.num == 11):
                print(" "+"J|", end="")
            elif(self.num == 12):
                print(" "+"Q|", end="")
            elif(self.num == 13):
                print(" "+"K|", end="")
            elif(self.num == 1):
                print(" "+"A|", end="")
            else:
                print(" "+str(self.num)+"|", end="")
        return ""

def settingGame():
    print("======遊戲設置======")
    money = 0
    rivalMoney = 0
    while (money == 0):
        try:
            money = int(input("初始金額："))
        except:
            print("請輸入數字！")
    rivalMoney = money
    gameStart(money,rivalMoney)

def prepareCard():
    cards = []
    for category in Category.getAll():
        for num in range(1,14):
            cards.append(PokerCard(num, category))
    return cards

def printPlayerCards(cards,rivalCards, showRival=False):
    print("================")
    print(f"你的手牌：( {countCards(cards)}點 )")
    for card in cards:
        print(card)
    if showRival:
        print(f"對手手牌：( {countCards(rivalCards)}點 )")
    else:
        print("對手手牌：")
    for card in rivalCards:
        print(card)
    print("================\n\n")

def randomAddCard(cards:list,num,allCards:list):
    chooseCards = random.sample(allCards, num)
    cards.extend(chooseCards)
    for card in chooseCards:
        allCards.remove(card)
    return cards, allCards

def countCards(cards:list):
    sum = 0
    aceCount = 0
    for card in cards:
        if card.num >= 10 :
            sum += 10
        elif card.num == 1 :
            aceCount += 1
        else:
            sum += card.num

    for i in range(aceCount):
        if sum + 11 <= 21:
            sum += 11
        else:
            sum += 1
    return sum

def blackJack(allCards):
    yourCards = []
    rivalCards = []
    yourCards, allCards = randomAddCard(yourCards,2,allCards)
    rivalCards, allCards = randomAddCard(rivalCards,2,allCards)
    rivalCards[0].hide = True
    isWin = False
    currentPoint = countCards(yourCards)
    rivalPoints = countCards(rivalCards)

    currentType = CardType.Normal
    rivalType = CardType.Normal

    while True:
        currentPoint = countCards(yourCards)
        currentType = CardType.Normal
        if currentPoint > 21:
            currentType = CardType.Over
            print("你的點數爆了")
            isWin = False
            break
        else:
            if len(yourCards) >= 5:
                print("過五關!!!")
                currentType = CardType.FiveCards
            elif len(yourCards) == 2 and currentPoint == 21:
                print("Black Jack!!!")
                currentType = CardType.BlackJack
        printPlayerCards(yourCards,rivalCards)
        cmd = ''
        while cmd != "1" and cmd != "2":
            cmd = input("是否再要一張？(1.要, 2.不要)")
        if cmd == "1":
            yourCards, allCards = randomAddCard(yourCards,1,allCards)
        else:
            break
    rivalCards[0].hide = False
    if currentType == CardType.BlackJack or currentType == CardType.Normal:
        while True:
            rivalPoints = countCards(rivalCards)
            rivalType = CardType.Normal
            if rivalPoints > 21:
                print("對手點數爆了")
                isWin = True
                rivalType = CardType.Over
                break
            elif len(rivalCards) == 2 and rivalPoints == 21:
                print("Black Jack!!!")
                rivalType = CardType.BlackJack
                break
            elif rivalPoints >= currentPoint and rivalPoints >= 16:
                isWin = False
                break
            printPlayerCards(yourCards,rivalCards,showRival=True)
            if rivalPoints < currentPoint or rivalPoints < 16:
                rivalCards, allCards = randomAddCard(rivalCards,1,allCards)
    
    printPlayerCards(yourCards,rivalCards,showRival=True)
    if currentType == CardType.FiveCards:
        return True, 3
    elif currentType == CardType.BlackJack and rivalType != CardType.BlackJack:
        return True, 2
    elif currentType != CardType.BlackJack  and rivalType == CardType.BlackJack:
        return False, 2
    elif currentPoint == rivalPoints:
        return True, 0
    else:
        return isWin, 1
    
def gameStart(money, rivalMoney):
    print("======遊戲開始======")
    while money > 0 and rivalMoney > 0:
        cards = prepareCard()
        while True:
            payment = 0
            while payment == 0:
                try:
                    payment = int(input("輸入下注金額："))
                except:
                    print("請輸入數字！")
            if payment <= money and payment <= rivalMoney:
                break
            else:
                print("金額不足")
        isWin, scale = blackJack(cards)
        if scale == 0:
            print("平手")
        else:
            if isWin:
                money += payment * scale
                rivalMoney -= payment * scale
                print(f"你贏了{payment * scale}元")
            else:
                money -= payment * scale
                rivalMoney += payment * scale
                print(f"你輸了{payment * scale}元")
        print("\n")
        print(f"你的錢 : {money}, 對手的錢 : {rivalMoney}")

        if money <= 0 or rivalMoney <= 0:
            break
        
        print("1.繼續遊戲")
        print("2.回選單")
        cmd = ''
        while cmd != "1" and cmd != "2":
            cmd = input("請輸入選項(1,2)")
        if cmd == "2":
            break

if __name__ == "__main__":
    while(True):
        print("1.開始遊戲")
        print("2.結束遊戲")
        cmd = ''
        while cmd != "1" and cmd != "2":
            cmd = input("請輸入選項(1,2)")
        if cmd == "1":
            settingGame()
        else:
            break