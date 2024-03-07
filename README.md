<img width="618" alt="do mission_2" src="https://github.com/tatxha/TP1DPBO/assets/134766457/8a4b2d9c-6a20-4bfb-8ced-41257fd83aef"># TP1DPBO

# Janji
Saya Tattha Maharany Yasmin Akbar dengan NIM 2201805 mengerjakan Tugas Praktikum 1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Diagram
![DIAGRAM_TP1DPBO](https://github.com/tatxha/TP1DPBO/assets/134766457/a3ddde9b-eaf6-46c0-93e8-387b6c08f383)

## Desain Program 
Terdiri dari 3 class yaitu **Character**, **PlayableCharacter**, **Player**, **BadNPC**, **GoodNPC**, **Missions**, dan **Items**. PlayableCharacter dan GoodNPC adalah child dari Character. Player dan BadNPC adalah child dari PlayableCharacter. GoodNPC mempunyai Items, Mission, dan data Player. Player juga memiliki data Mission dari GoodNPC.


## Alur Program
Pertama data diisi secara statis, lalu melakukan pemilihan karakter. Setelah memilih karakter, user dapat melakukan 5 aksi:
(1) Ask mission to good NPC
(2) Fight to bad NPC
(3) Ask to good NPC about your information
(4) Interact to Good NPC (sell your items)
(5) End Game

Jika user memilih 1, akan muncul data npc sekaligus data misi yang ada, lalu user dapat memilih misi yang ingin dikerjakan berdasarkan id misi. Setelah misi berhasil dikerjakan maka akan mendapatkan reward

Jika user memilih 2, maka akan muncul data bad np untuk melakukan pertarungan, setalh player menang akan mendapatkan reward, lalu user bisa heals HP jika ingin fight kembali

Jika user memilih 3, maka good npc akan memunculkan informasi data player

Jika user memilih 4, maka akan muncul data item player terlebih dahulu lalu akan muncul 2 pilihan action lagi yaitu:
    (1) Want to sell your item to NPC?
    (2) Ask NPC for help selling your item?
    (3) Cancel Action

    Jika user memilih 1, maka user akan menjual item yang dipilih berdasarkan id, jika 2 maka npc akan membantu menjual item

Jika memilih 5, keluar dari game

bonus soal: untuk melawan musuh ada batasan hp yaitu >= 50
