class SnackBox:
  SNACK_BOX_DATA = {
    1 : {
      "bone" : {
        "info" : "Phoenician rawhide",
        "tastiness" : 20
        },
      "kibble" : {
        "info" : "Delicately braised hamhocks",
        "tastiness" : 33
      },
      "treat" : {
        "info" : "Chewy dental sticks",
        "tastiness" : 40
      }
    },
    2 : {
      "bone" : {
        "info" : "An old dirty bone",
        "tastiness": 2
      },
      "kibble" : {
        "info" : "Kale clusters",
        "tastiness" : 1
      },
      "treat" : {
        "info" : "Bacon",
        "tastiness" : 80
      }
    },
    3 : {
      "bone" : {
        "info" : "A steak bone",
        "tastiness" : 64
      },
      "kibble" : {
        "info" : "Sweet Potato nibbles",
        "tastiness" : 45
      },
      "treat" : {
        "info" : "Chicken bits",
        "tastiness" : 75
      }
    }
  }

  def __init__(self, data = None):
    self.data = self.SNACK_BOX_DATA if data == None else data

  def get_bone_info(self, box_id):
    return self.data[box_id]["bone"]["info"]

  def get_bone_tastiness(self, box_id):
    return self.data[box_id]["bone"]["tastiness"]

  def get_kibble_info(self, box_id):
    return self.data[box_id]["kibble"]["info"]

  def get_kibble_tastiness(self, box_id):
    return self.data[box_id]["kibble"]["tastiness"]

  def get_treat_info(self, box_id):
    return self.data[box_id]["treat"]["info"]

  def get_treat_tastiness(self, box_id):
    return self.data[box_id]["treat"]["tastiness"]

class CorgiSnacks:

  def __init__(self, snack_box, box_id):
    self.snack_box = snack_box
    self.box_id = box_id

  def bone(self):
    info = self.snack_box.get_bone_info(self.box_id)
    tastiness = self.snack_box.get_bone_tastiness(self.box_id)
    result = f"Bone: {info}: {tastiness}"
    tastiness = f"* {result}" if tastiness > 30 else result
    return tastiness

  def kibble(self):
    info = self.snack_box.get_kibble_info(self.box_id)
    tastiness = self.snack_box.get_kibble_tastiness(self.box_id)
    result = f"Kibble: {info}: {tastiness}"
    tastiness = f"* #{result}" if tastiness > 30 else result
    return tastiness

  def treat(self):
    info = self.snack_box.get_treat_info(self.box_id)
    tastiness = self.snack_box.get_treat_tastiness(self.box_id)
    result = f"Treat: {info}: {tastiness}"
    tastiness = f"* {result}" if tastiness > 30 else result
    return tastiness

class MetaCorgiSnacks:

  def __init__(self, snack_box, box_id):
    self.snack_box = snack_box
    self.box_id = box_id
    self.bone = self.define_method('bone')
    self.kibble = self.define_method('kibble')
    self.treat = self.define_method('treat')

  """def __getattr__(self, item):
    item = str(item)
    def default():
      info = self.snack_box.get_bone_info(self.box_id) if item == "bone" else self.snack_box.get_kibble_info(self.box_id) if item == "kibble" else self.snack_box.get_treat_info(self.box_id)
      tastiness = self.snack_box.get_bone_tastiness(self.box_id) if item == "bone" else self.snack_box.get_kibble_tastiness(self.box_id) if item == "kibble" else self.snack_box.get_treat_tastiness(self.box_id)
      new_item = item[0].upper() + item[1:]
      result = f"{new_item}: {info}: {tastiness}"
      tastiness = f"* #{result}" if tastiness > 30 else result
      print(tastiness)
      return item
    return default"""

  def define_method(self, item):
    if item == "bone":
      info = self.snack_box.get_bone_info(self.box_id)
      tastiness = self.snack_box.get_bone_tastiness(self.box_id)
      new_item = item[0].upper() + item[1:]
    elif item == "kibble":
      info = self.snack_box.get_kibble_info(self.box_id)
      tastiness = self.snack_box.get_kibble_tastiness(self.box_id)
      new_item = item[0].upper() + item[1:]
    else:
      info = self.snack_box.get_treat_info(self.box_id)
      tastiness = self.snack_box.get_treat_tastiness(self.box_id)
      new_item = item[0].upper() + item[1:]
    result = f"{new_item}: {info}: {tastiness}"
    tastiness = f"* {result}" if tastiness > 30 else result
    print(tastiness)
    return tastiness
