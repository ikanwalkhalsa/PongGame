from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ObjectProperty,ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock

class Base(Widget):
    def serve_ball(self, vel=(4, 4)):
        self.ball.center = self.center
        self.ball.velocity = vel
    def update(self,dt):
        score1=int(self.p1sc.text)
        score2=int(self.p2sc.text)
        self.ball.move()
        self.p1.bounce(self.ball)
        self.p2.bounce(self.ball)
        if(self.ball.y<-100):
            self.ball.center=self.center
            score2+=1
            self.p2sc.text=str(score2)
        if(self.ball.top>self.height+100):
            self.ball.center=self.center
            score1+=1
            self.p1sc.text=str(score1)
        if(self.ball.x<0) or (self.ball.right>self.width):
            self.ball.ballx*=-1
    def on_touch_move(self, touch):
        if touch.y < self.height / 2:
            self.p1.center_x = touch.x
        if touch.y > self.height - self.height / 2:
            self.p2.center_x = touch.x

class PongBall(Widget):
    ballx=NumericProperty(0)
    bally=NumericProperty(0)
    velocity=ReferenceListProperty(ballx,bally)
    def move(self):
        self.pos=Vector(*self.velocity)+self.pos

class Paddle(Widget):
    def bounce(self,ball):
        if self.collide_widget(ball):
            ball.bally*=-1

class PongApp(App):
    Window.size=300,500
    def build(self):
        base=Base()
        base.serve_ball()
        Clock.schedule_interval(base.update,1.0/60.0) 
        return base

if __name__ == "__main__":
    r=PongApp()
    r.run()