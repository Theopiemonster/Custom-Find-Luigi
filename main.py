import random, json, pygame # Imports
pygame.init() # Initialize Pygame

settings = { # DEFAULT SETTINGS
    "windowSize": [250, 250], # The size of your window. Smaller sizes improve performance.
    "fps": 30, # Setting lower FPS (20-30) can improve performance.
    "images": { # List of icons
        "Luigi": "foundhim.png", # found him
        "Mario": "mario.png",
        "Wario": "wario.png",
        "Yoshi": "yoshi.png"
    },
    "wanted": "Luigi", # Specific icon that spawns once, usually Luigi. NOT case sensitive
    "scale": 1, # Size of icons.
    "amount": 100, # Amount of total icons that spawn.
    "speed": 2 # Speed of icons.
}

try:
    with open("settings.json", "r") as file: settings = dict(json.load(file)) # Reads the settings JSON.
except:
    with open("settings.json", "w") as file: json.dump(settings, file, indent=4) # If the settings JSON does not exist, make one.

WINDOW = pygame.display.set_mode(settings.get("windowSize", (250, 250)), pygame.DOUBLEBUF) # Create the window and set size
pygame.display.set_caption(f"Find {settings['wanted']}") # Set window caption to Find [wanted]
clock = pygame.time.Clock() # For FPS

class Game: # Class for actual game
    def __init__(self, screen): # Create icons upon class creation
        self.objects, self.iconImages, self.screen = [], {}, screen
        for icon in settings["images"].keys():
            if icon.lower() != settings["wanted"].lower(): self.iconImages[icon] = pygame.image.load(f"images/{settings['images'][icon]}").convert_alpha()
            else: continue # Prevents special icon from spawning multiple times.
        self.wantedIcon = pygame.image.load(f"images/{settings['images'][settings['wanted']]}").convert_alpha()
        self.generate()

    def generate(self): # Icon setup
        for icon in range(settings["amount"] - 1): # Create icons and their attributes.
            char = random.choice(list(self.iconImages.keys()))
            self.objects.append({"name": char, "image": self.iconImages[char], "x": random.randint(0, settings["windowSize"][0]), "y": random.randint(0, settings["windowSize"][1]), "xSpeed": random.uniform(-settings["speed"], settings["speed"]), "ySpeed": random.uniform(-settings["speed"], settings["speed"])})
        self.objects.append({"image": self.wantedIcon, "x": random.randint(0, settings["windowSize"][0]), "y": random.randint(0, settings["windowSize"][1]), "xSpeed": random.uniform(-settings["speed"], settings["speed"]), "ySpeed": random.uniform(-settings["speed"], settings["speed"])}) # Make special icon afterwards

        for icon in self.objects:
            imageSize = icon["image"].get_rect()
            scaleMulti = 32 / imageSize[3]
            icon["image"] = pygame.transform.scale(icon["image"], ((imageSize[2] * scaleMulti) * settings["scale"], (imageSize[3] * scaleMulti) * settings["scale"]))
            icon["w"], icon["h"] = icon["image"].get_rect()[2], icon["image"].get_rect()[3]
        random.shuffle(self.objects) # Randomize layers

    def simulate(self): # Simulate positions
        for icon in self.objects:
            icon["x"] -= icon["xSpeed"] # Move icons horizontally. If border is hit, bounce!
            if icon["x"] + icon["image"].get_rect()[2] > settings.get("windowSize", (250, 250))[0]: icon["xSpeed"] = abs(icon["xSpeed"])
            elif icon["x"] < 0: icon["xSpeed"] = -icon["xSpeed"]

            icon["y"] -= icon["ySpeed"] # Move icons vertically. If border is hit, bounce!
            if icon["y"] + icon["image"].get_rect()[3] > settings.get("windowSize", (250, 250))[0]: icon["ySpeed"] = abs(icon["ySpeed"])
            elif icon["y"] < 0: icon["ySpeed"] = -icon["ySpeed"]
        self.renderFrame()

    def renderFrame(self): # Self-explanitory with the name here
        for icon in self.objects: self.screen.blit(icon["image"], (icon["x"], icon["y"]))

running = True
game = Game(WINDOW)
pygame.display.set_icon(game.wantedIcon)
while running: # Main loop
    WINDOW.fill((0,0,0))
    for event in pygame.event.get(): # Event loop
        if event.type == pygame.QUIT: running = False # Quit if the X is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False # Quit if esc is pressed
            elif event.key == pygame.K_r: # Reset if r is pressed
                game = Game(WINDOW)
                print("Reset board.")

    game.simulate()
    pygame.display.flip() # Update frame
    clock.tick(settings.get("fps", 30)) # FPS tick