from pynput.keyboard import Key, Controller
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from uvicorn import run


app = FastAPI()


class MediaController:

    keyboard = Controller()

    def increase_volume(self):
        self.keyboard.press(Key.media_volume_up)
        self.keyboard.release(Key.media_volume_up)

    def decrease_volume(self):
        self.keyboard.press(Key.media_volume_down)
        self.keyboard.release(Key.media_volume_down)

    def mute_system(self):
        self.keyboard.press(Key.media_volume_mute)
        self.keyboard.release(Key.media_volume_mute)


    def playpause(self):
        self.keyboard.press(Key.media_play_pause)
        self.keyboard.release(Key.media_play_pause)
    
    def next_track(self):
        self.keyboard.press(Key.media_next)
        self.keyboard.release(Key.media_next)

    def prev_track(self):
        self.keyboard.press(Key.media_previous)
        self.keyboard.release(Key.media_previous)

    def full_screen(self):
        self.keyboard.press("f")
        self.keyboard.release("f")

    def skip_5s(self):
        self.keyboard.press(Key.right)
        self.keyboard.release(Key.right)

    def back_5s(self):
        self.keyboard.press(Key.left)
        self.keyboard.release(Key.left)

app.add_middleware(CORSMiddleware, 
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


media_controller = MediaController()

@app.get("/playpause")
def playpause():
    media_controller.playpause()
    return { "message": "Success" }


@app.get("/volumeup")
def volup():
    media_controller.increase_volume()
    return { "message": "Success" }


@app.get("/volumedown")
def voldown():
    media_controller.decrease_volume()
    return { "message": "Success" }


@app.get("/mutevolume")
def mutevol():
    media_controller.mute_system()
    return { "message": "Success" }


@app.get("/prev")
def prev():
    media_controller.prev_track()
    return { "message": "Success" }


@app.get("/next")
def next():
    media_controller.next_track()
    return { "message": "Success" }

@app.get("/full_screen")
def full_screen():
    media_controller.full_screen()
    return { "message": "Success" }

@app.get("/skip5s")
def skip_5s():
    media_controller.skip_5s()
    return { "message": "Success" }

@app.get("/back5s")
def back_5s():
    media_controller.back_5s()
    return { "message": "Success" }

app.mount("/", StaticFiles(directory="public"), name="public")

if __name__=="__main__":
    run(app, host="0.0.0.0", port=80)