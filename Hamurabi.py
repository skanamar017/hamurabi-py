import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        self.people=100
        self.bushels=2800
        self.acres=1000
        self.price=19
        

    # other methods go here
    def askHowManyAcresToBuy(self, price, bushels):
        answer=int(input("HOW MANY ACRES OF LAND DO YOU PLAN ON BUYING?: "))

        max_acres=self.bushels//self.price
        while answer>max_acres:
            answer=int(input(f"THINK AGAIN, O MIGHTY MASTER. YOU ONLY HAVE ENOUGH BUSHELS TO BUY {max_acres} ACRES. NOW, THEN, HOW MANY ACRES OF LAND DO YOU PLAN ON BUYING?:"))
        
        self.acres+=answer
        self.bushels-=(answer*self.price)

        return answer


    def askHowManyAcresToSell(self, acresOwned):
        answer=int(input("HOW MANY ACRES OF LAND DO YOU PLAN ON SELLING?: "))
        
        while answer>self.acres:
            answer=int(input(f"THINK AGAIN, O MIGHTY MASTER. YOU ONLY HAVE {self.acres} ACRES. NOW, THEN, HOW MANY ACRES OF LAND DO YOU PLAN ON SELLING?:"))

        self.acres-=answer
        self.bushels+=(answer*self.price)
        
        return answer


    def askHowMuchGrainToFeedPeople(self, bushels):
        answer=int(input("HOW MANY BUSHELS OF GRAIN DO YOU WISH TO FEED YOUR PEOPLE?: "))
        
        while answer>self.bushels:
            answer=int(input(f"THINK AGAIN, O MIGHTY MASTER. YOU ONLY HAVE {self.bushels} OF GRAIN. NOW, THEN, HOW MANY BUSHELS OF GRAIN DO YOU WISH TO FEED YOUR PEOPLE?: "))
        
        #Each person needs at least 20 bushels of grain per year to survive

        return answer

    def askHowManyAcresToPlant(self, acresOwned, population, bushels):
        answer=int(input("HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED?: "))

        while answer>self.bushels//2 or answer>self.people*10 or answer>self.acres:
            while answer>self.bushels//2: #2 bushels to plant 1 acre
                answer=int(input(f"THINK AGAIN, O MIGHTY MASTER. YOU ONLY HAVE ENOUGH BUSHELS TO PLANT {self.bushels//2} ACRES. NOW, THEN, HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED?: "))
            while answer>self.people*10: #Each person can farm at most 10 acres of land
                answer=int(input(f"THINK AGAIN, O MIGHTY MASTER. YOU ONLY HAVE ENOUGH PEOPLE TO PLANT {self.people*10} ACRES. NOW, THEN, HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED?: "))
            while answer>self.acres:
                answer=int(input(f"THINK AGAIN, O MIGHTY MASTER. YOU ONLY HAVE {self.acres} AVAILIBLE. NOW, THEN, HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED?: "))

        self.acres+=(answer)
        self.bushels-=(answer*2)

        return answer




    def plagueDeaths(self, population):
        if random.randint(0, 99) < 15:
            self.people = self.people // 2

        
        
    def starvationDeaths(self,population, bushelsFedToPeople):
        #Each person needs 20 bushels of grain to survive. 
        #If you feed them more than this, they are happy, but the grain is still gone. 
        #You don't get any benefit from having happy subjects. 
        #Return the number of deaths from starvation (possibly zero).
        
        #if more people than needed are fed, deaths are 0
        #set people to 
        if self.askHowMuchGrainToFeedPeople()//20>=self.people:
            return 0
        self.people-=(self.askHowMuchGrainToFeedPeople()//20)
        return self.people-(self.askHowMuchGrainToFeedPeople()//20)

    def uprising(self, population, howManyPeopleStarved):
        if self.people/self.starvationDeaths()>=0.45:
            return True
        return False

    def immigrants(self, population, acresOwned, grainInStorage):
        if self.starvationDeaths==0:
            return (20 * self.acres + self.bushels) / (100 * self.bushels) + 1

    def harvest(self, acres, bushelsUsedAsSeed):
        ran_num = random.randint(1, 6)
        self.bushels+=(ran_num*self.askHowManyAcresToPlant())
        return ran_num*self.askHowManyAcresToPlant()


    def grainEatenByRats(self, bushels):
        grain_eaten=0
        ran_num=random.randint(0, 99)
        if ran_num < 40:
            grain_eaten=self.bushels*ran_num//100
        self.bushels-=grain_eaten
        return grain_eaten

    def newCostOfLand(self):
        self.price=random.randint(17, 23)
        return self.price











if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
