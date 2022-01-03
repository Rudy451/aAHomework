from metacorgis import SnackBox, CorgiSnacks, MetaCorgiSnacks

snack_box = SnackBox()
print("Snack BOx")
print(snack_box.get_bone_info(1))
print(snack_box.get_kibble_tastiness(3))

print("CorgiSnacks")
snacks = CorgiSnacks(snack_box, 1)
print(snacks.bone())
print(snacks.kibble())

print("MetaCorgiSnacks")
snack_box = SnackBox()
meta_snacks = MetaCorgiSnacks(snack_box, 1)
meta_snacks.bone
meta_snacks.kibble
meta_snacks.treat
