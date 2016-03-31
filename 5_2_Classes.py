from random import randint, choice


class Hero:
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.critical_chance = 10
        self.fire_spell_mana_cost = 8
        self.ice_spell_mana_cost = 11
        self.arcane_spell_mana_cost = 20

    def take_a_hit(self, received_damage):
        self.hp -= received_damage
        return self.hp

    def critical_strike(self):
        if randint(1, self.critical_chance) == self.critical_chance:
            return 1
        return 0

    def hit(self, damage):
        crit = self.critical_strike()
        return randint(damage[0], damage[1]) * (1 + crit)

    def info(self):
        return self.hp, self.mp

    def spell_cast(self, magic_damage, mana_cost):
        self.mp -= mana_cost
        return randint(magic_damage[0], magic_damage[1])


class Warrior(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.hp *= 2
        self.mp *= 0.5
        self.critical_chance *= 1.5
        self.hammer_damage = [10, 15]
        self.fire_spell_damage = [3, 8]

    def hammer_hit(self):
        return 'physical', self.hit(self.hammer_damage)

    def fire_spell_cast(self):
        return 'fire', self.spell_cast(self.fire_spell_damage, self.fire_spell_mana_cost)


class Rogue(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.hp *= 1
        self.mp *= 1
        self.critical_chance *= 0.7
        self.dagger_damage = [6, 8]
        self.ice_spell_damage = [6, 8]

    def dagger_hit(self):
        return 'physical', self.hit(self.dagger_damage)

    def ice_spell_cast(self):
        return 'ice', self.spell_cast(self.ice_spell_damage, self.ice_spell_mana_cost)


class Mage(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.hp *= 0.8
        self.mp *= 2
        self.critical_chance *= 0.8
        self.fire_spell_damage = [4, 12]
        self.ice_spell_damage = [8, 12]
        self.arcane_spell_damage = [14, 15]

    def spell_cast(self, magic_damage, mana_cost):
        self.mp -= mana_cost
        return randint(magic_damage[0], magic_damage[1]) * (1 + self.critical_strike())

    def fire_spell_cast(self):
        return 'fire', self.spell_cast(self.fire_spell_damage, self.fire_spell_mana_cost)

    def ice_spell_cast(self):
        return 'ice', self.spell_cast(self.ice_spell_damage, self.ice_spell_mana_cost)

    def arcane_spell_cast(self):
        return 'arcane', self.spell_cast(self.arcane_spell_damage, self.arcane_spell_mana_cost)


class Monster(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.hp *= 2
        self.claw_damage = [10, 15]
        self.affix = choice(['none', 'physical', 'ice', 'fire', 'arcane'])
        self.affix_describe = ''

    def take_a_hit(self, recived_damage_affix, received_damage):
        if self.affix == recived_damage_affix:
            received_damage = int(received_damage*0.6)
        self.hp -= received_damage
        return self.hp

    def monster_attack(self):
        return self.hit(self.claw_damage)

    def monster_hp(self):
        return self.hp


def hero_create():
    print "Choose your Hero:\n" \
          "1) Warrior - A lot of HP, high physical damage, fire spell\n" \
          "2) Rogue - Medium HP and MP, high critical chance, ice spell\n" \
          "3) Mage - A lot of MP, but low HP, three types of spells"
    user_choice = input()
    if user_choice == 1:
        hero = Warrior()
        hero_class = 'warrior'
    elif user_choice == 2:
        hero = Rogue()
        hero_class = 'rogue'
    elif user_choice == 3:
        hero = Mage()
        hero_class = 'mage'
    else:
        print "Well, then I`ll choose. You are a Rogue"
        hero = Rogue()
        hero_class = 'rogue'

    monster = Monster()
    return hero, monster, hero_class


def warrior_attack(hero, monster):
    print "Choose an action:\n1) Use a hammer {} - {} physical damage\n2) Cast 'Fireball' spell {} - {} fire damage\n" \
          "0) Hero info\n".format(hero.hammer_damage[0], hero.hammer_damage[1],
                                  hero.fire_spell_damage[0], hero.fire_spell_damage[1])
    action = input()
    if action == 1:
        damage_affix,enemy_hp = hero.hammer_hit()
        print "You hit monster with your hammer. {} HP is {}".format(monster.affix_describe,
                                                                     monster.take_a_hit(damage_affix,enemy_hp))
    elif action == 2:
        damage_affix,enemy_hp = hero.fire_spell_cast()
        print "You cast a fireball. {} HP is {}".format(monster.affix_describe,
                                                        monster.take_a_hit(damage_affix,enemy_hp))
    elif action == 0:
        hero_hp, hero_mp = hero.info()
        print "Your HP = {}, MP = {}".format(hero_hp,hero_mp)
        hero, monster = warrior_attack(hero, monster)
    return hero, monster


def rogue_attack(hero, monster):
    print "Choose an action:\n1) Use a dagger {} - {} physical damage\n2) Cast 'Freeze' spell {} - {} ice damage\n" \
          "0) Hero info\n".format(hero.dagger_damage[0], hero.dagger_damage[1],
                                  hero.ice_spell_damage[0], hero.ice_spell_damage[1])
    action = input()
    if action == 1:
        damage_affix, enemy_hp = hero.dagger_hit()
        print "You hit monster with your dagger. {} HP is {}".format(monster.affix_describe,
                                                                          monster.take_a_hit(damage_affix,enemy_hp))
    elif action == 2:
        damage_affix, enemy_hp = hero.ice_spell_cast()
        print "You cast a freeze. {} HP is {}".format(monster.affix_describe,monster.take_a_hit(damage_affix,enemy_hp))
    elif action == 0:
        hero_hp, hero_mp = hero.info()
        print "Your HP = {}, MP = {}".format(hero_hp,hero_mp)
        hero, monster = rogue_attack(hero, monster)
    return hero, monster


def mage_attack(hero, monster):
    print "Choose an action:\n1) Cast 'Fireball' spell {} - {} fire damage\n" \
          "2) Cast 'Freeze' spell {} - {} ice damage\n" \
          "3) Cast 'Black Hole' spell {} - {} arcane damage\n0) Hero info\n" \
        .format(hero.fire_spell_damage[0], hero.fire_spell_damage[1],
                hero.ice_spell_damage[0], hero.ice_spell_damage[1],
                hero.arcane_spell_damage[0], hero.arcane_spell_damage[1])
    action = input()
    if action == 1:
        damage_affix,enemy_hp = hero.fire_spell_cast()
        print "You cast a fireball. {} HP is {}".format(monster.affix_describe,
                                                        monster.take_a_hit(damage_affix,enemy_hp))
    elif action == 2:
        damage_affix,enemy_hp = hero.ice_spell_cast()
        print "You cast a freeze. {} HP is {}".format(monster.affix_describe,monster.take_a_hit(damage_affix,enemy_hp))
    elif action == 3:
        damage_affix,enemy_hp = hero.arcane_spell_cast()
        print "You cast a black hole. {} HP is {}".format(monster.affix_describe,
                                                          monster.take_a_hit(damage_affix,enemy_hp))
    elif action == 0:
        hero_hp, hero_mp = hero.info()
        print "Your HP = {}, MP = {}".format(hero_hp,hero_mp)
        hero, monster = mage_attack(hero, monster)
    return hero, monster


def hero_turn(hero, monster, hero_class):
    if hero_class == 'warrior':
        hero, monster = warrior_attack(hero, monster)
    elif hero_class == 'rogue':
        hero, monster = rogue_attack(hero, monster)
    else:
        hero, monster = mage_attack(hero, monster)
    return hero, monster


def monster_turn(hero, monster):
    print "{} strikes you. Your HP = {}".format(monster.affix_describe,hero.take_a_hit(monster.monster_attack()))


def main():
    print "\t\t\tWelcome to The Game\n"
    user_hero, random_monster, user_hero_class = hero_create()
    if random_monster.affix == 'physical':
        random_monster.affix_describe = 'Armored Death Knight'
    elif random_monster.affix == 'fire':
        random_monster.affix_describe = 'Burning Imp'
    elif random_monster.affix == 'ice':
        random_monster.affix_describe = 'Ice Golem'
    elif random_monster.affix == 'arcane':
        random_monster.affix_describe = 'Arcane Prophet'
    print "Your opponent for this battle is {}".format(random_monster.affix_describe)
    while random_monster.hp > 0 and user_hero.info()[0] > 0:
        hero_turn(user_hero, random_monster, user_hero_class)
        monster_turn(user_hero, random_monster)
    if random_monster.hp <=0:
        print "You Win!!!"
    else:
        print "You Lose..."

if __name__ == '__main__':
    main()
