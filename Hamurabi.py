import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        
        
        
        year=1
        acres=1000
        bushels=2800
        population=100
        price=19

        deaths=0
        starved=0
        harvest=3000
        harvested_per_acre=3
        immigrants=5
        rats_ate=200

        print("CONGRATULATIONS, YOU ARE THE NEWEST RULER OF ANCIENT SUMER, ELECTED FOR A TEN YEAR TERM OF OFFICE \n"
              "YOUR DUTIES ARE TO DISPENSE FOOD, DIRECT FARMING, AND BUY AND SELL LAND AS NEEDED TO SUPPORT YOU PEOPLE \n" \
              "WATCH OUT FOR RAT INFESTATIONS AND THE PLAGUE! \n" \
              "GRAIN IS THE GENERAL CURRENCY, MEASURED IN BUSHELS \n" \
              "THE FOLLOWING WILL HELP YOU IN YOUR DECISIONS: \n" \
              " \n" \
              "    EACH PERSON NEEDS AT LEAST 20 BUSHELS OF GRAIN TO SURVIVE \n" \
              "    EACH PERSON CAN FARM AT MOST 10 ACRES \n" \
              "    THE MARKET PRICE FLUCTUATES EVERY YEAR \n" \
              "    IT TAKES 2 BUSHELS OF GRAIN TO FARM AN ACRE OF LAND \n" \
              " \n" \
              "RULE WISELY AND YOU WILL BE SHOWERED WITH APPRECIATION AT THE END OF YOUR TERM \n" \
              "RULE POORLY AND YOU WILL BE KICKED OUT OF OFFICE! \n" \
              " \n")

        
        start=str(input("DO YOU WISH TO START (Y/N)?: "))
        if start=="Y":
            print("GOOD LUCK... \n")
        else:
            print("TOO BAD \n")

        while year<=10:
            self.startOfYearReport(year, acres, bushels, population, price, starved, harvest, harvested_per_acre, immigrants, rats_ate)
            
            acres_bought=self.askHowManyAcresToBuy(price, bushels)
            acres+=acres_bought
            bushels-=(price*acres_bought)

            acres_sold=self.askHowManyAcresToSell(acres)
            acres-=acres_sold
            bushels+=(price*acres_sold)

            grain_to_feed=self.askHowMuchGrainToFeedPeople(bushels)
            bushels-=grain_to_feed

            acres_planted=self.askHowManyAcresToPlant(acres, population, bushels)
            acres+=acres_planted
            bushels-=(2*acres_planted)

            plague_deaths=self.plagueDeaths(population)
            population-=plague_deaths
            deaths+=plague_deaths

            starved=self.starvationDeaths(population, grain_to_feed)
            population-=starved
            deaths+=starved

            if self.uprising(population, starved)==True: break

            if starved==0: 
                immigrants=self.immigrants(population, acres, bushels)
            else:
                immigrants=0
            population+=immigrants
            
            harvest=self.harvest(acres_planted, bushels)
            bushels+=harvest


            rats_ate=self.grainEatenByRats(bushels)
            bushels-=rats_ate

            price=self.newCostOfLand()


            
            
            
            year+=1

        if year<10:
            print("you suck ass")

    def askHowManyAcresToBuy(self, price, bushels):
        while True:
            acres=int(input(f"HOW MANY ACRES OF LAND DO PLAN TO BUY?: "))
            if acres<0:
                print(f"O MIGHTY MASTER, SURELY YOU JEST, FOR YOU HAVE ONLY {bushels} BUSHELS OF GRAIN!")
            if acres*price<=bushels:
                return acres
            print(f"O MIGHTY MASTER, SURELY YOU JEST, FOR YOU HAVE ONLY {bushels} BUSHELS OF GRAIN!")
    
    def askHowManyAcresToSell(self, acresOwned):
        while True:
            acres=int(input(f"HOW MANY ACRES OF LAND DO PLAN TO SELL?: "))
            if acres<acresOwned:
                return acres
            print(f"O MIGHTY MASTER, SURELY YOU JEST, FOR YOU HAVE ONLY {acresOwned} ACRES OF LAND TO USE!")
    
    def askHowMuchGrainToFeedPeople(self, bushels):
         while True:
            grain_to_feed=int(input(f"HOW MANY BUSHELS OF GRAIN DO PLAN TO FEED TO THE IMBICILES-- I MEAN PEOPLE?: "))
            if grain_to_feed<bushels:
                return grain_to_feed
            print(f"O MIGHTY MASTER, SURELY YOU JEST, FOR YOU HAVE ONLY {bushels} BUSHELS OF GRAIN TO USE!")
    
    def askHowManyAcresToPlant(self, acresOwned, population, bushels):
        while True:
            acres=int(input(f"HOW MANY ACRES OF LAND DO PLAN TO PLANT?: "))
            if acres<bushels//2 and acres<population*10 and acres<acresOwned:
                return acres
            if acres>bushels//2:
                print(f"TO MIGHTY MASTER, SURELY YOU JEST, FOR YOU HAVE ONLY {bushels} BUSHELS OF GRAIN TO USE!")
            if acres>population*10:
                print(f"O MIGHTY MASTER, SURELY YOU JEST, FOR YOU HAVE ONLY {population} PEOPLE TO PUT TO WORK!")
            if acres>acresOwned:
                print(f"TO MIGHTY MASTER, SURELY YOU JEST, FOR YOU HAVE ONLY {acresOwned} ACRES OF LAND TO USE!")

    def plagueDeaths(self, population):
        if random.randint(0, 99) < 15:
            return population//2
        return 0
    
    def starvationDeaths(self, population, bushelsFedToPeople):
        fed=bushelsFedToPeople//20
        return max(0, population-fed)
    
    def uprising(self, population, howManyPeopleStarved):
        if howManyPeopleStarved/population>=0.45:
            return True
        return False
    
    def immigrants(self, population, acresOwned, grainInStorage):
        return int((20 * acresOwned + grainInStorage)/ (100 * population) + 1)
    
    def harvest(self, acres, bushelsUsedAsSeed):
        ran_num=random.randint(1, 6)
        return ran_num*acres


    
    def grainEatenByRats(self, bushels):
        if random.randint(0, 99) < 40:
            return int(bushels*random.randint(10, 30))
        return 0
    
    def newCostOfLand(self):
        return random.randint(17, 23)
    
    def startOfYearReport(self, year, acres, bushels, population, price, starved, harvest, harvested_per_acre, immigrants, rats_ate):
        print("O GREAT HAMMURABI")
        print(f"YOU ARE IN YEAR {year} OF YOUR TEN YEAR RULE. ")
        print(f"IN THE PREVIOUS YEAR {starved} PEOPLE STARVED TO DEATH. ")
        print(f"IN THE PREVIOUS YEAR {immigrants} PEOPLE ENTERED THE KINGDOM. ")
        print(f"THE POPULATION IS NOW {population}")
        print(f"WE HARVESTED {harvest} at {harvested_per_acre} PER ACRE. ")
        print(f"RATS DESTROYED {rats_ate} BUSHELS, LEAVING ONLY {bushels} IN STORAGE. ")
        print(f"THE CITY OWNS {acres} OF LAND")
        print(f"LAND IS CURRECTLY VALUED AT {price} BUSHELS PER ACRE")
        print(" ")



    

    
















if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
