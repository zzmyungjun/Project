import game_framework
import pico2d

import title_state

pico2d.open_canvas(1024, 768)
game_framework.run(title_state)
pico2d.close_canvas()
