#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:15:16 2018

A 2d pool game derived from the kivy ping-pong tutorial

@author: ervin
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class PoolSide(Widget):
    #
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            if self.orient == 0:
                ball.velocity_y *= -1
            else:
                ball.velocity_x *= -1

class PoolGame(Widget):
    # Class for the Game base
    ball = ObjectProperty(None)
    side_left = ObjectProperty(None)
    side_right = ObjectProperty(None)
    side_up = ObjectProperty(None)
    side_bottom = ObjectProperty(None)
    sides = [side_bottom, side_up, side_left, side_right]

    def serve_ball(self, vel=(3, 3)):
        # Starting conditions for the ball
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of the sides
        self.side_right.bounce_ball(self.ball)
        self.side_left.bounce_ball(self.ball)
        self.side_up.bounce_ball(self.ball)
        self.side_bottom.bounce_ball(self.ball)

class PoolBall(Widget):
    friction= 0.001
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.velocity = Vector(*self.velocity) * (1-self.friction)

class PoolApp(App):

    def build(self):
        #Config.set('graphics', 'resizable', False)
        #Config.set('graphics', 'width', '400')
        #Config.set('graphics', 'height', '600')
        game = PoolGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PoolApp().run()
