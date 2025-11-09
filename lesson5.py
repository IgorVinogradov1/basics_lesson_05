import file_operations
import random
import ast
import os
from faker import Faker


def main():
    fake = Faker("ru_RU")
    with open('src/skills.txt', 'r', encoding='utf-8') as f:
        all_skills = ast.literal_eval(f.read())
    with open('src/letters_mapping.txt', 'r', encoding='utf-8') as f:
        letters_mapping = ast.literal_eval(f.read())

    runic_skills = []
    for skill in all_skills:
	    new_runic_skill = ''
	    for symbol in skill:
		    new_runic_skill += letters_mapping[symbol]
	    runic_skills.append(new_runic_skill)
    skills_for_card = random.sample(runic_skills, 3)
    
    for player_card in range(10):
	    context = {
		    'first_name': fake.first_name(),
		    'last_name': fake.last_name(),
		    'job': fake.job(),
		    'town': fake.city(),
		    'strength': random.randint(3, 18),
		    'agility': random.randint(3, 18),
		    'endurance': random.randint(3, 18),
		    'intelligence': random.randint(3, 18),
		    'luck': random.randint(3, 18),
		    'skill_1': skills_for_card[0],
		    'skill_2': skills_for_card[1],
		    'skill_3': skills_for_card[2]
	    }
	    file_operations.render_template('src/charsheet.svg', 'output/svg/player_card_{}.svg'.format(player_card + 1), context)
if __name__ == '__main__':
	main()