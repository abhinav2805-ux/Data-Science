class Agent:
    def __init__(self, name, health, age, uniqueness):
        self.name = name
        self.health = health
        self.age = age
        self.uniqueness = uniqueness
    
    def display_info(self):
        """Display the agent's information."""
        print("Agent Name:",self.name)
        print("Health:",self.health)
        print("Age: " ,self.age)
        print("Uniqueness:", self.uniqueness)
        print("-" * 20)
    
    def take_damage(self, amount):
        """Reduce the agent's health by a specified amount."""
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {amount} damage. Current health: {self.health}")
    
    def heal(self, amount):
        """Increase the agent's health by a specified amount."""
        self.health += amount
        print(f"{self.name} was healed by {amount}. Current health: {self.health}")
    
    def is_alive(self):
        """Check if the agent is still alive (health > 0)."""
        return self.health > 0

# Creating 4 Agent objects
agent1 = Agent(name="Alpha", health=100, age=25, uniqueness="Stealth")
agent2 = Agent(name="Bravo", health=85, age=30, uniqueness="Sniper")
agent3 = Agent(name="Charlie", health=120, age=28, uniqueness="Tank")
agent4 = Agent(name="Delta", health=95, age=26, uniqueness="Hacker")

# Using the methods on the objects
agent1.display_info()
agent2.display_info()
agent3.take_damage(30)
agent4.heal(20)


#  to use inheritance in python use this Syntax
 
#  class boss(Agent):
#      ------ code ------

