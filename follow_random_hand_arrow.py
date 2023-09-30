import random

from pico2d import*

WIDTH, HEIGHT = 1100, 600
open_canvas(WIDTH, HEIGHT)

character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def make_random_hand_arrow():
    global arrowX, arrowY
    x = random.randint(5, 105)
    y = random.randint(5, 55)
    arrowX = x * 10
    arrowY = y * 10

def follow_hand_arrow():
    global boyX, boyY
    a = (arrowY - boyY)/(arrowX - boyX)
    b = boyY - a * boyX
    if arrowX > boyX:
        boyX += 10
    elif arrowX < boyX:
        boyX -= 10
    boyY = a * boyX + b

running = True
frameX, frameY = 0, 0
boyX, boyY = WIDTH//2, HEIGHT//2
arrowX, arrowY = 50, 50

while(running):
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    arrow.draw(arrowX, arrowY)
    character.clip_draw(frameX * 100, frameY * 100, 100, 100, boyX, boyY)
    update_canvas()
    handle_events()
    if arrowX == boyX and arrowY == boyY:
        make_random_hand_arrow()
    else:
        follow_hand_arrow()
    frameX = (frameX + 1) % 8
    delay(0.05)

close_canvas()