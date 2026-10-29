from FortniteBot import FortniteBot

bot1 = FortniteBot()
bot2 = FortniteBot()
bot3 = FortniteBot()


bot1.take_damage(5)
bot2.take_damage(20)

print(bot1.health)
print(bot2.health)
print(bot3.health)
FortniteBot.health = 95 #this changes ALL bots health (applies to class overall isntead of individual instances)