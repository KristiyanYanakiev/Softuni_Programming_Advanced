def draw_cards(*tuples, **kwargs):
    monster_cards = []
    spell_cards = []

    for tuple in tuples:
        card_name = tuple[0]
        card_type = tuple[1]

        if card_type == "monster":
            monster_cards.append(card_name)
        elif card_type == "spell":
            spell_cards.append(card_name)

    for k, v in kwargs.items():
        if v == "monster":
            monster_cards.append(k)
        elif v == "spell":
            spell_cards.append(k)

    sorted_monster_cards = sorted(monster_cards, reverse=True)
    sorted_spell_cards = sorted(spell_cards)

    output = ""

    if sorted_monster_cards:
        output += f"Monster cards:\n"
        for card in sorted_monster_cards:
            output += f"  ***{card}\n"

    if sorted_spell_cards:
        output += f"Spell cards:\n"
        for card in sorted_spell_cards:
            output += f"  $$${card}\n"

    return output[:-1]




print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))