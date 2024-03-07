#     Saya Tattha Maharany Yasmin Akbar dengan NIM 2201805 mengerjakan soal Tugas Praktikum 1 
#    dalam Praktikum mata kuliah Desain dan Pemrograman Berbasis Objek, untuk keberkahan-Nya
#    maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamin.

# import semua file
from Character import Character
from PlayableCharacter import PlayableCharacter
from Player import Player
from BadNPC import BadNPC
from GoodNPC import GoodNPC
from Missions import Missions
from Items import Items

good_npc = GoodNPC()  # digunakan saat assign mission ke player

# mengisi data misi
mission1 = Missions("M1", "Menjelajahi Hutan", "Jelajahi hutan selama 30 menit", "Easy", 20, 50, "Not Yet")
mission2 = Missions("M2", "Menjelajahi Sungai", "Jelajahi sungai selama 30 menit", "Easy", 20, 45, "Not Yet")
mission3 = Missions("M3", "Melawan Zombie", "Kalahkan 30 zombie", "Medium", 40, 80, "Not Yet")
mission4 = Missions("M4", "Melawan Zombie", "Kalahkan 60 zombie", "Hard", 80, 160, "Not Yet")
mission5 = Missions("M5", "Menjelajahi Hutan", "Jelajahi hutan selama 60 menit", "Easy", 40, 75, "Not Yet")
mission6 = Missions("M6", "Menjelajahi Sungai", "Jelajahi sungai selama 60 menit", "Easy", 40, 80, "Not Yet")
list_missions = [mission1, mission2, mission3] # memasukkan misi ke list

# mengisi data good npc
good_npc1 = GoodNPC("N1", "Adrian", 'M')
good_npc2 = GoodNPC("N2", "Lyra", 'F')
list_npcs = [good_npc1, good_npc2] # memasukkan data good npc ke list

#  memilih misi mana saja yang dimiliki oleh setiap good npc
good_npc1.add_mission(mission1)
good_npc1.add_mission(mission2)
good_npc1.add_mission(mission3)
good_npc2.add_mission(mission4)
good_npc2.add_mission(mission5)
good_npc2.add_mission(mission6)

# mengisi data bad npc/enemy
enemy1 = BadNPC("E1", "Thor", 'M', 100, 15, "Easy", 20, 150, "Alive")
enemy2 = BadNPC("E2", "Loki", 'M', 98, 10, "Medium", 8, 80, "Alive")
enemy3 = BadNPC("E3", "Thanos", 'M', 100, 30, "Hard", 28, 210, "Alive")
list_enemies = [enemy1, enemy2, enemy3] # memasukkan data bad npc/enemy ke list

# mengisi data player
player1 = Player("P1", "Nova", 'M', 100, 20, "DPS", 200, 300, 3)
player2 = Player("P2", "Mia", 'F', 100, 10, "Healer", 150, 45, 0)
player3 = Player("P3", "Sora", 'M', 100, 25, "Assassin", 200, 300, 2)
player4 = Player("P4", "Aloy", 'F', 40, 5, "Mage", 100,  35, 0)
list_players = [player1, player2, player3, player4] # memasukkan data player ke list

# mengisi data items
item1 = Items("I1", "Leaf", 15, "Ready") 
item2 = Items("I2", "Wood", 25, "Ready") 
item3 = Items("I3", "Gold", 60, "Ready") 
item4 = Items("I4", "Leaf", 15, "Ready") 
item5 = Items("I5", "Iron", 40, "Ready") 
item6 = Items("I6", "Iron", 40, "Ready") 
item7 = Items("I7", "Iron", 40, "Ready") 
item8 = Items("I8", "Gold", 60, "Ready") 
item9 = Items("I9", "Gold", 60, "Ready") 
item10 = Items("I10", "Wood", 25, "Ready") 
item11 = Items("I11", "Wood", 25, "Ready") 
item12 = Items("I12", "Wood", 25, "Ready") 

# memilih items mana saja yang dimiliki oleh setiap player
player1.add_item(item1)
player1.add_item(item2)
player1.add_item(item3)
player2.add_item(item4)
player2.add_item(item8)
player2.add_item(item10)
player3.add_item(item5)
player3.add_item(item9)
player3.add_item(item11)
player4.add_item(item6)
player4.add_item(item7)
player4.add_item(item12)

# menampilkan list player untuk dipilih oleh user
print("\nAVAILABLE PLAYERS :")
print("==================================")
for player in list_players:
    player.dislay_players()
choose_player = input("Choose your character by ID : ")
for player in list_players:
    if choose_player == player.get_id():
        selected_player = player
        break
        
if selected_player:
    print("-> Your Character is", selected_player.get_name())
    status = True       
    while status:
        # pilih action yang ingin dilakukan
        print("\nCHOOSE ACTION :")
        print("(1) Ask mission to good NPC")
        print("(2) Fight to bad NPC")
        print("(3) Ask to good NPC about your information")
        print("(4) Interact to Good NPC (sell your items)")
        print("(5) End Game\n", end='')
        action = int(input("Choose (1/2/3/4/5) : "))
        
        if action == 1: # melakukan misi
            do_mission_status = True
            while do_mission_status:
                # menampilkan data npc dan misi yang ada pada npc tersebut
                print("\nAVAILABLE NPCs :")
                print("==================================")
                for npc in list_npcs:
                    print("NPC ID  ->", npc.get_id())
                    print("Name     : " + npc.get_name() + " (" + npc.get_gender() + ')' )
                    print("Missions :")
                    for mission in npc.get_mission():
                        if mission.get_status().lower() == "not yet":
                            print("  MISSION ID ->", mission.get_id_mission())
                            print("  Level       :", mission.get_level())
                            print("  Name        :", mission.get_name())
                            print("  Detail      :", mission.get_detail())
                            print("  Reward      : $", mission.get_reward_money())
                            print("  Reward EXP  :", mission.get_reward_exp())
                            print("---------------------------------------------")
                    print("\n", end='')
                choose_goodNPC = input("Choose Good NPC's ID! ") # memilih npc
                
                for npc in list_npcs:
                    if choose_goodNPC == npc.get_id():
                        selected_npc = npc
                        break
                if selected_npc:
                    # menampilkan misi yang belum dilakukan pada npc yang sebelumnya sudah dipilih
                    print("\nAVAILABLE MISSIONS FROM", selected_npc.get_name(), ':')
                    print("==================================================")
                    for mission in selected_npc.get_mission():
                        if mission.get_status().lower() == "not yet":
                            print(" MISSION ID ->", mission.get_id_mission())
                            print(" Level       :", mission.get_level())
                            print(" Name        :", mission.get_name())
                            print(" Detail      :", mission.get_detail())
                            print(" Reward      : $", mission.get_reward_money())
                            print(" Reward EXP  :", mission.get_reward_exp())
                        print("--------------------------------------------------")
                            
                    # memilih misi yang ingin dikerjakan oleh player
                    choose_id = input("Choose Mission's ID! ")
                    for mission in selected_npc.get_mission():
                        if choose_id == mission.get_id_mission(): 
                            selected_mission = mission
                            break
                        
                    if selected_mission:
                        good_npc.assign_mission_to_player(selected_player, selected_mission) # npc assign mission kepada player
                        print("//", selected_npc.get_name(), "(NPC) give mission", selected_mission.get_name(), "to", selected_player.get_name(), "...")
                        
                        confirm = input("\nConfirm when finished! (Yes) ")
                        if confirm.lower() == "yes":
                            # player mendapatkan reward setelah berhasil menyelesaikan misi
                            selected_mission.set_status(selected_mission, 1) # menjadikan status misi sudah selesai dikerjakan
                            selected_mission.display_reward()
                            selected_player.add_coin(selected_mission.get_reward_money())
                            print("  - Coin : $", selected_player.get_coin())
                            selected_player.add_exp(selected_mission.get_reward_exp())
                            print("  - EXP  : ", selected_player.get_exp())
                            print("+--------------------------------------------------+\n")
                    do_another_mission = input("Want to do another mission? (Yes/No) : ")

                if do_another_mission.lower() != "yes":
                    do_mission_status = False 
                    
        elif action == 2: # melawan bad npc/enemy
            if selected_player.get_hp() >= 50: # (bonus) player hanya bisa bertarung jika HP-nya besar sama 50
                fight_status = True
                while fight_status:
                    if selected_player.get_hp() < 50: 
                        # jika setelah pertarungan pertama, player bisa melakukan pertarungan lainnya dan jika HP-nya tidak cukup ada metode heals self untuk mengembalikan HP ke value semula
                        print("-> Your Health Point is not enough to fight!")
                        confirm_heals = input("Want to heal ypurself? (Yes/No) : ")
                        if confirm_heals.lower() == "yes": 
                            selected_player.heals(selected_player)
                            print("Your Health Point right now is", selected_player.get_hp(), ". Ready to fight again!")
                        else:
                            break
                        
                    # menampilkan data enemy yang belum dikalahkan
                    print("\nAVAILABLE ENEMIES :")
                    print("==================================")
                    for enemy in list_enemies:
                        enemy.display_enemies(1)
                        print("--------------------------------------------------")
                    choose_enemy = input("Choose Enemy's ID! ")
                    
                    for attack in list_enemies:
                        if attack.get_id() == choose_enemy:
                            selected_enemy = attack
                            break
                    
                    winner = 0
                    i = 0
                    if selected_enemy:
                        print("-> You will fight with", selected_enemy.get_name(), "right now!")
                        battle_status = True
                        while battle_status:
                            do_fight = input("\nAtack Enemy? (Yes) ")
                            if do_fight.lower() == "yes":
                                
                                i+=1
                                if i == 2: # pada putaran kedua, player bisa menggukan ulti (total atk +50% dari atk awal)
                                    selected_player.set_ulti_atk(1)
                                    selected_player.attack_enemy(selected_enemy, 1)
                                else: 
                                    selected_player.attack_enemy(selected_enemy, 2)
                                print("// Enemy attacks...")
                                
                                if i == 3: # untuk ulti yang dikeluarkan oleh enemy keluar pada putaran ke 3
                                    selected_enemy.set_ulti_atk(2)
                                    selected_enemy.attack_player(selected_player, 1)
                                else:
                                    selected_enemy.attack_player(selected_player, 2)
                                
                                # setiap melakukan attack, akan menampilkan total hp yang sudah berkurang
                                if selected_player.get_hp() <= 0:    
                                    print(selected_player.get_name(), "'s HP 0")
                                    print(selected_enemy.get_name(), "'s HP ", selected_enemy.get_hp())
                                elif selected_enemy.get_hp() <= 0:    
                                    print(selected_player.get_name(), "'s HP", selected_player.get_hp())
                                    print(selected_enemy.get_name(), "'s HP  0")
                                else:     
                                    print(selected_player.get_name(), "'s HP", selected_player.get_hp())
                                    print(selected_enemy.get_name(), "'s HP ", selected_enemy.get_hp())
                                    
                                if selected_player.get_hp() <= 0: # player kalah
                                    winner = 1
                                elif selected_enemy.get_hp() <= 0: # npc kalah
                                    winner = 2
                                    
                            if winner != 0:
                                battle_status = False
                                
                        if winner == 1: # player kalah
                            print("\n+--------------------------------------------------+")
                            print("|               Failed defeating enemy!            |")
                            print("+--------------------------------------------------+")
                        elif winner == 2: # player menang
                            selected_enemy.set_status(selected_enemy, 1) # mengganti status enemy sudah dikalahkan
                            selected_enemy.display_reward()
                            selected_player.add_exp(selected_enemy.get_bonus_exp())
                            selected_player.add_coin(selected_enemy.get_bonus_coin())
                            print("  - Coin : $", selected_player.get_coin())
                            print("  - EXP  : ", selected_player.get_exp())
                            print("+--------------------------------------------------+\n")
                    
                    want_to_fight_again = input("Want to fight again? (Yes/No) : ") 
           
                    if want_to_fight_again.lower() != "yes":
                        fight_status = False   
                        
            else: # (Bonus) HP tidak cukup
                print("Your Health Point is not enough to fight!")
                break
            
        elif action == 3: # Meminta informasi mengenai data player kepada good npc
            print("\nAVAILABLE NPCs :")
            print("==================================")
            for npc in list_npcs:
                print("NPC ID  ->", npc.get_id())
                print("Name     : " + npc.get_name() + " (" + npc.get_gender() + ')' )
                print("----------------------------------")
            selected_npc = input("Choose NPC ID! ") # pilih npc mana yang akan memberikan data informasi player
            if selected_npc:
                for npc in list_npcs:
                    if npc.get_id() == selected_npc:
                        informan_npc = npc
                        break
            
                if informan_npc:
                    #  menampilkan informasi player
                    print("\nHi,", selected_player.get_name(), "I'm", informan_npc.get_name(), ". Here is your information :")
                    informan_npc.display_player_information(selected_player)  
                         
        elif action == 4: # action jual beli dengan good npc

            sell_item_status = True
            while sell_item_status:
                print("\n(1) Want to sell your item to NPC?")    
                print("(2) Ask NPC for help selling your item?") 
                print("(3) Cancel Action")   
                choose_action = int(input("Choose (1/2/3) : ")) # pilih action
                
                if choose_action != 3:
                    # menampilkan item yang player miliki
                    print("\nAVAILABLE ITEMS :")
                    print("==================================")
                    for item in selected_player.get_items():
                        item.display_item()
                        print("--------------------------------------------------")
                    choose_item = input("Choose Item ID! ") # pilih item yang ingin dijual
                    for item in selected_player.get_items():
                        if choose_item == item.get_id():
                            selected_item = item
                            break
                        
                    if selected_item:
                        #  menampilkan data npc untuk tujuan jual beli item player
                        print("\nAVAILABLE NPCs :")
                        print("==================================")
                        for npc in list_npcs:
                            print("NPC ID  ->", npc.get_id())
                            print("Name     : " + npc.get_name() + " (" + npc.get_gender() + ')' )
                            print("----------------------------------")
                        choose_goodNPC = input("Choose NPC's ID! ") # memilih npc
                        for npc in list_npcs:
                            if choose_goodNPC == npc.get_id():
                                selected_npc = npc
                                break
                        
                        if selected_npc:
                            selected_player.sell_item(selected_npc, selected_item) # player menjual item ke good npc
                            if choose_action == 1:
                                print("// Selling item to", selected_npc.get_name())
                            elif choose_action == 2:
                                print("//", selected_npc.get_name(), "helps sell your item")
                            selected_item.set_status(selected_item, 1) # mengganti status item sudah terjual
                            selected_player.add_coin(selected_item.get_price())
                            print("\n+--------------------------------------------------+")
                            print("|               Succeed Selling Item!              |")
                            print("+--------------------------------------------------+")
                            print("  Your Wallet :")
                            print("  - Coin : $", selected_player.get_coin())
                            print("  - EXP  : ", selected_player.get_exp())
                            print("+--------------------------------------------------+")
                        
                if choose_action == 3:
                    sell_item_status = False        
                                                     
        else: # action keluar dari game
            print("\nBye bye", selected_player.get_name() + '~')
        
        if action == 5:
            status = False   
 