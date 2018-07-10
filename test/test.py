from InvestopediaApi import ita

client = ita.Account("akeredoluadebola@yahoo.com","8]ev}6-xgW7%")

print(client.get_open_trades())
#print(client.get_current_securities())

#client.trade("GOOG", ita.Action.buy, 10)
#client.trade("MSFT", ita.Action.sell, 9)
#client.trade("TSLA", ita.Action.short, 8)
#client.trade("CMI", ita.Action.cover, 5)