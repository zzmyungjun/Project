import server

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

# def collide_1(a, b):
#     left_a, bottom_a, right_a, top_a = a.get_bb()
#     left_b, bottom_b, right_b, top_b = b.get_bb()
#
#     if left_a <= right_b:
#         server.boy.left = True
#         return True
#     if right_a >= left_b:
#         server.boy.right = True
#         return True
#     if top_a < bottom_b:
#         server.boy.top = True
#         return True
#     if bottom_a > top_b:
#         server.boy.bottom =True
#         return True
#
#     return False

# def collide_attack(a, b):
#     left_a_attack, bottom_a_attack, right_a_attack, top_a_attack = a.get_bb_attack()
#     left_b_attack, bottom_b_attack, right_b_attack, top_b_attack = b.get_bb_attack()
#
#     if left_a_attack > right_b_attack: return False
#     if right_a_attack < left_b_attack: return False
#     if top_a_attack < bottom_b_attack: return False
#     if bottom_a_attack > top_b_attack: return False
#
#     return True