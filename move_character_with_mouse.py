from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1200, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
left = load_image('left.png')
diagonal_up = load_image('left_up.png')
diagonal_down = load_image('left_down.png')
up = load_image('up.png')
down = load_image('down.png')
mouse = load_image('hand_arrow.png')
def handle_events():
    global running
    global x, y, mx, my, dx, dy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            running = False

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mx, my = random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)
dx, dy = 0, 0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    # 마우스 위치를 랜덤으로 이동
    if mx == x and my == y:
        mx = random.randint(0, TUK_WIDTH - 1)
        my = random.randint(0, TUK_HEIGHT - 1)
    # 캐릭터의 방향 설정
    if mx > x:
        dx = 1
    elif mx < x:
        dx = -1
    else:
        dx = 0

    if my > y:
        dy = 1
    elif my < y:
        dy = -1
    else:
        dy = 0
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dx < 0 and dy > 0:  # 좌상
        diagonal_up.clip_draw(frame * 27, 0, 27, 32, x, y, 60, 90)
    elif dx < 0 and dy < 0:  # 좌하
        diagonal_down.clip_draw(frame * 28, 0, 28, 32, x, y, 60, 90)
    elif dx > 0 and dy > 0:  # 우상
        diagonal_up.clip_composite_draw(frame * 27, 0, 27, 32, 0, 'h', x, y, 60, 90)
    elif dx > 0 and dy < 0:  # 우하
        diagonal_down.clip_composite_draw(frame * 28, 0, 28, 32, 0, 'h', x, y, 60, 90)

    mouse.draw(mx, my)
    update_canvas()
    frame = (frame + 1) % 3
    x += dx
    y += dy
    handle_events()
close_canvas()




