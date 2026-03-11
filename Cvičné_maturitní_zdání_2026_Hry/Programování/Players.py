players = {
 1: {"id": 1, "nick": "ShadowFox", "age": 17},
 2: {"id": 2, "nick": "IronWolf", "age": 19},
 3: {"id": 3, "nick": "PixelRider", "age": 16},
 4: {"id": 4, "nick": "NightEagle", "age": 21},
 5: {"id": 5, "nick": "BlueComet", "age": 18}
}

results = {
 1: {"player_id": 3, "slot_1": 2, "slot_2": 7, "slot_3": 4, "date": "2026-02-01"},
 2: {"player_id": 4, "slot_1": 5, "slot_2": 5, "slot_3": 5, "date": "2026-02-02"},
 3: {"player_id": 1, "slot_1": 9, "slot_2": 1, "slot_3": 6, "date": "2026-02-04"},
 4: {"player_id": 2, "slot_1": 0, "slot_2": 8, "slot_3": 3, "date": "2026-02-05"},
 5: {"player_id": 5, "slot_1": 4, "slot_2": 2, "slot_3": 9, "date": "2026-02-06"}
}



def print_player_summary(p_id):
    player = players.get(p_id)
    # Najdeme výsledek podle player_id vnořeného v dictu results
    res = next((r for r in results.values() if r["player_id"] == p_id), None)

    if not player:
        print(f"ID {p_id}: Hráč neexistuje.")
        return

    # Čistý výpis pomocí f-stringu
    print(f"Hráč: {player['nick']} ({player['age']} let)")
    
    if res:
        score = res['slot_1'] + res['slot_2'] + res['slot_3']
        print(f"  -> Poslední hra {res['date']}: Skóre {score}")
    else:
        print("  -> Žádné herní výsledky.")

# Volání
print_player_summary(1)
