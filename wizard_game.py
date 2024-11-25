import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        # Randomize damage within a range
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def ability_one(self, opponent):
        print(f"{self.name} uses 'Mega Strike'! Deals 35 damage to {opponent.name}.")
        opponent.health -= 35

    def ability_two(self):
        print(f"{self.name} uses 'Battle Cry'! Increases attack power by 10!")
        self.attack_power += 10

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def ability_one(self, opponent):
        print(f"{self.name} uses 'Fireball'! Deals 40 damage to {opponent.name}.")
        opponent.health -= 40

    def ability_two(self):
        heal = 20
        print(f"{self.name} uses 'Healing Spell'! Restores {heal} health.")
        self.health += heal
        if self.health > self.max_health:
            self.health = self.max_health

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
    def regenerate(self):
        heal = 10
        self.health += heal
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates {heal} health! Current health: {self.health}")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30)

    def ability_one(self, opponent):
        total_damage = 12 * 3
        print(f"{self.name} uses 'Arrow Flurry'! Deals 3 hits of 12 damage to {opponent.name}, totaling {total_damage}.")
        opponent.health -= total_damage
        if opponent.health < 0:
            opponent.health = 0

    def ability_two(self):
        print(f"{self.name} uses 'Power Shot'! Doubles attack power for the next attack.")
        self.attack_power *= 2

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=35)

    def ability_one(self, opponent):
        print(f"{self.name} uses 'Holy Rage'! Deals 30 damage to {opponent.name}.")
        opponent.health -= 30

    def ability_two(self):
        heal = 15
        print(f"{self.name} uses 'Divine Light'! Restores {heal} health.")
        self.health += heal
        if self.health > self.max_health:
            self.health = self.max_health

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Ability One")
        print("3. Use Ability Two")
        print("4. View Stats")
        print("5. Exit Battle")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.ability_one(wizard)
        elif choice == '3':
            player.ability_two()
        elif choice == '4':
            player.display_stats()
        elif choice == '5':
            print(f"{player.name} has chosen to forfeit the battle. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.attack(player)

        if player.health <= 0:
            print("\n--- Game Over ---")
            print(f"{player.name} has been defeated by {wizard.name}. Better luck next time!")
            return

    if wizard.health <= 0:
        print("\n--- Victory! ---")
        print(f"Congratulations, {player.name}! You have defeated {wizard.name} and saved the realm!")

def main():
    while True:
        player = create_character()
        wizard = EvilWizard("The Dark Wizard")
        battle(player, wizard)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()