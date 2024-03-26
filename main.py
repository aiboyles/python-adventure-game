# Simple text based adventure game

character = {'inventory': [],
             'location': 'courtyard'}

mansion = {
    'courtyard': {
        'name': 'courtyard',
        'description': 'You stand in the middle of courtyard, thick with thorny vines and tall grass. A formerly majestic fountain is placed in the middle, but it lies dry, still, and overgrown with moss. A tall, foreboding house looms before you to the north. In the distance, an owl hoots, and then falls silent.',
        'contents': [
          {
           'name': 'spoon',
           'description': 'a shiny silver spoon',
           'room to use': 'kitchen',
           'action': 'You dig into the bowl of ice cream. It tastes delicious... almost bewitchingly so. You feel a strange tingle on your tongue that travels to your fingertips, and then fades. It almost seems like your eyes can see a bit better in the dark with every spoonful.'
          },
          {
           'name': 'golden key',
           'description': 'a small, glimmering, heavy key made of pure gold',
           'room to use': 'attic',
           'action': 'You turn the key in the lock and gasp as the door opens and a breath '
          }
        ],
        'exits': {'north': 'grand foyer'}
    },
    'grand foyer': {
        'name': 'grand foyer',
        'description': 'The grand, decaying foyer speaks to the decadent splendour that this house once held. Gilded wallpaper peels from the walls.',
        'contents': [],
        'exits': {'west': 'kitchen',
                  'north': 'hallway',
                  'south': 'courtyard',
                  'east' : 'dining room'}
    },
    'kitchen': {
        'name': 'kitchen',
        'description': 'A cold stone kitchen. It is dark, and damp. You hear the sound of dripping somewhere. A slowly melting bowl of ice cream sits on the counter. How long has it been here? Did someone leave it? Why?',
        'contents': [
          {
           'name': 'jug',
           'description': 'a worn ceramic jug with a fine crack running through it',
           'room to use': 'dining room',
           'action': 'You fill the jug with water and pour it into the basin. You peer into the basin... vague human-like shapes swim before your eyes, silvery and faint but somehow alive. You rub your eyes and look again. They have vanished--the surface of the water is smooth and glassy.'
          }
        ],
        'exits': {'east': 'grand foyer'}
    },
    'dining room': {
        'name': 'dining room',
        'description': 'A formerly lavish dining room. A crystal chandelier hangs motionless above the great oak table, its sparkle obscured by the layer of dust. The table is set with crisp white linens and ornate silver dinnerware, curiously untarnished, as though it had been freshly polished and laid out only hours before. In the corner sits an oaken barrel filled with water, and on the sideboard a gleaming, empty silver basin is perched.',
        'contents': [],
        'exits': {'west': 'grand foyer'}
    }
}

def print_inventory():
  if (len(character['inventory']) > 0):
    str = ""
    for i in character['inventory']:
      str += i['name'] + ", "
    str = str[0:len(str) - 2]
    print('Inventory: ' + str)
  else:
    print('Your inventory is empty.')

def list_room_items():
  if (len(room['contents']) > 0):
    str = ""
    for i in room['contents']:
      str += i['name'] + ", "
    str = str[0:len(str) - 2]
    print('In this room: ' + str)
  else:
    print('There is nothing for you to take in this room.')

def list_room_exits():
  str = ""
  for key in room['exits']:
    str += key + ' - ' + room['exits'][key] + ", "
  str = str[0:len(str) - 2]
  print("Exits: " + str)

def take_item(item_name):
  if item_name == 'all':
    if room['contents']:
      for item in room['contents']:
        print('You pick up the', item['name'])
        character['inventory'].append(item)
        room['contents'] = []
    else:
      print('There is nothing to take!')
  else:
    found = False
    for i, val in enumerate(room['contents']):
      if (val['name'] == item_name):
        found = True
        item = room['contents'][i]
        character['inventory'].append(item)
        print('You pick up the ' + item['name'])
        room['contents'].remove(item)
    if not found:
      print("There is no such item in this room.")

def print_help():
  print("north, east, west, south > if there is an exit in one of the")

def use_item(item_name):
  found = False
  for i, val in enumerate(character['inventory']): 
    if (val['name'] == item_name):
      found = True
      item = character['inventory'][i]
      if room['name'] == item['room to use']:
        print(item['action'])
        character['inventory'].remove(item)
      else:
        print("You can't use that item in this room.")
  if not found:
    print("You do not have that item in your inventory.")

room = mansion[character['location']]
print(room['description'])
list_room_exits()
list_room_items()

while True:
    room = mansion[character['location']]
    # prompt should include the room's short description
    command = input(room['name'] + ' > ')
    # split can have a MAX ELEMENTS parameter
    command_parts = command.split(" ", 1)
    verb = command_parts[0]
    obj = command_parts[-1]

    if verb in ['east', 'west', 'north', 'south']:
        if verb in room['exits']:
            character['location'] = room['exits'][verb]
            room = mansion[character['location']]
            print(room['description'])
            list_room_exits()
            list_room_items()
        else:
            print('You cannot go that way')
    if verb == 'inventory' or verb == 'i':
        print_inventory()
    if verb == 'quit' or verb == 'q':
        print('Goodbye')
        break
    if verb == 'take' or verb == 't':
        take_item(obj)
    if verb == 'd' or verb == 'description':
      print(room['description'])
      list_room_items()
      list_room_exits()
    if verb == 'help' or verb == 'h':
      print_help()
    if verb == 'use' or verb == 'u':
      use_item(obj)