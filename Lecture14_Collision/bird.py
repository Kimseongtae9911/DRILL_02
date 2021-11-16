import game_framework
from pico2d import *

import random

# 새는 앵무새를 기준으로 하였음
# 앵무새의 속도는 19.8km ~ 34.2km이므로 새의 속도는 중간값인 27km로 설정하였음
# 제일 큰 앵무새는 106.68cm이다 따라서 10픽셀당 30cm이므로 115cm를 기준으로 잡아 35픽셀로 츌력하였음
# Bird Fly Speed 300~400km
# Bird scale 106.68cm
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 27.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
# 새의 날개짓 한번에 14프레임
# 날개짓이 가장 빠른 벌새가 1초에 15~90회의 날개짓을 한다고한다
# 따라서 기준인 앵무새의 날개짓 횟수는 벌새보다 적은 1초에 5번으로 정하였다
TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


# Bird Event
FLY_LEFT, FLY_RIGHT = range(2)

key_event_table = {
}


class FLYRState:
    def enter(bird, event):
        bird.velocity = FLY_SPEED_PPS
        bird.dir = clamp(-1, bird.velocity, 1)

    def exit(bird, event):
        pass

    def do(bird):
        # bird.frame = (bird.frame + 1) % 14
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)
        if (bird.x >= 1600 - 25):
            bird.add_event(FLY_LEFT)

    def draw(bird):
        # 제일 큰 앵무새는 106.68cm이다 따라서 10픽셀당 30cm이므로 115cm를 기준으로 잡아 35픽셀로 츌력하였음
        bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y, 35, 35)



class FLYLState:
    def enter(bird, event):
        bird.velocity = -FLY_SPEED_PPS
        bird.dir = clamp(-1, bird.velocity, 1)

    def exit(bird, event):
        pass

    def do(bird):
        #bird.frame = (bird.frame + 1) % 14
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)
        if(bird.x <= 25):
            bird.add_event(FLY_RIGHT)

    def draw(bird):
        # 제일 큰 앵무새는 106.68cm이다 따라서 10픽셀당 30cm이므로 115cm를 기준으로 잡아 35픽셀로 츌력하였음
        bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y, 35, 35)



next_state_table = {
    FLYRState: {FLY_LEFT: FLYLState, FLY_RIGHT: FLYRState},
    FLYLState: {FLY_LEFT: FLYLState, FLY_RIGHT: FLYRState},

}

class Bird:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 1000), random.randint(100, 500)
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = random.randint(-1, 1)
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.fly_dir = random.randint(0, 1)
        if self.fly_dir == 0:
            self.cur_state = FLYRState
        else:
            self.cur_state = FLYLState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

