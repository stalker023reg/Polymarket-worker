
RPC = {
    'POLYGON': 'https://polygon-bor-rpc.publicnode.com',
    'BASE': 'https://base-rpc.publicnode.com'
}

WALLET_SLEEP = [230, 600] #задержка между кошельками | так же включается себя задержку между парами
RANDOMIZE = False #перемешать порядок кошельков

TIMEOUT = 10_000 #таумаут на появление элемента на странице
PROXY_MODE = 'HTTP' #HTTP или SOCKS5

#=======FORKS RUNNER===============

TOTAL_AMOUNT = [50,80] #объем вилки (суммарный для всех аккаунтов в одной вилке)
SLEEP_BETWEEN_WALLETS_IN_FORK = [50, 450] #ожидание между кошельками внутри одной вилки
SLEEP_BETWEEN_FORKS = [290, 1300] #ожидание между вилками 
BETS_DEVIATION_PERCENT = 0 # на сколько процентов может отклоняться объем вилки, чтобы баланс не был 1 к 1 | чтобы отключить - 0

#Настройки ниже только для режима smart forks

BET_MORE_ON_HIGHEST_CHANCE = True # ставить больше на наибольшую вероятность, 
#при включенной функции софт будет делать перевес в сторону наибольшей вероятности так, 
#что при наиболее вероятном исходе вилка будет бесплатной
#Но при менее вероятном исходе будет теряться бОльший процент (~5% при спереде 1, ~8% при спреде 2)

CUSTOM_POOL_OF_MARKETS = [
    "https://polymarket.com/sports/nba/games/week/25/nba-cha-tor-2025-04-09",
    "https://polymarket.com/sports/nba/games/week/25/nba-por-uta-2025-04-09",
    "https://polymarket.com/sports/nba/games/week/25/nba-okc-phx-2025-04-09"
]



#=======BETS RUNNER================

#Поделит количество кошельков на столько частей сколько маркетов и откроет по ним сделки 
PERCENT_OF_BALANCE_TO_BET = [3,9] #процент от баланса сколько ставить

#Откуда взять маркет слаг? Нужно зайти на страничку нужного маркета и посмотреть на ссылку в адресной строке 
#https://polymarket.com/event/will-trump-create-a-national-bitcoin-reserve-in-his-first-100-days
#то, что идет после /event/ - и есть слаг - "will-trump-create-a-national-bitcoin-reserve-in-his-first-100-days"
#Если в маркете много разных исходов, то надо указать нужный исход точно так же как на сайте, третьим элементом в списке
#если исход один, то третий элемент не указывать

MARKET_BETS = [
    # ['will-trump-create-a-national-bitcoin-reserve-in-his-first-100-days', 'YES'], - вариант с 1 исходом
    # ['what-will-trump-say-during-crypto-summit-on-friday', 'YES', 'TikTok'], - вариант с нексколькими исходами


] #маркеты на которые хотим поставить ставки

#=======RELAY DEPOSIT================
CHAINS_BRIDGE_FROM = ['ARBITRUM', 'OPTIMISM', 'BASE']
MIN_BALANCE_TO_SEE = 10

#=======BINANCE DEPOSIT==============
AMOUNT_TO_DEPOSIT = [17,23]
API_KEY     = ""
API_SECRET  = ""

#=======WITHDRAW FROM POLYMARKET=====
AMOUNT_TO_WITHDRAW = [18, 23]
WITHDRAW_ALL = False

#=======UTILITY SETTINGS=============

ERR_ATTEMPTS = 3
MAX_BALANCE_WAIT = 500
MAX_GAS_PRICE = 500
MAX_TX_WAIT = 500
ETH_GAS_MULT = 1


#=======[REDACTED] RUNNER================
MARKET_ID = '' #condition id
TOKEN_ID = ''

AMOUNT_OF_TRADES = None
SLEEP_BETWEEN_TRADES =  None
MAX_WAIT_IF_SOMEONE_ELSE_IS_IN_MARKET = None
IGNORE_ASK_SIZE = None
