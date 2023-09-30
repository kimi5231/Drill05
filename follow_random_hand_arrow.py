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

running = True
frameX, frameY = 0, 3
x, y = WIDTH//2, HEIGHT//2

while(running):
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    character.clip_draw(frameX * 100, frameY * 100, 100, 100, x, y)
    update_canvas()
    handle_events()

close_canvas()