class pelco_options(object):
    def __init__(self):
        self.__sense = 0
        self.__toggle_automan = 0
        self.__toggle_onoff = 0
        self.__iris_close = 0
        self.__iris_open = 0
        self.__focus_near = 0
        self.__focus_far = 0
        self.__zoom_wide = 0
        self.__zoom_tele = 0
        self.__tilt_down = 0
        self.__tilt_up = 0
        self.__pan_left = 0
        self.__pan_right = 0
        
        
    def get_sense(self):
        return self.__sense
    def set_sense(self, sense):
        self.__sense = sense
    sense = property(get_sense, set_sense)
    
    def get_toggle_automan(self):
        return self.__toggle_automan
    def set_toggle_automan(self, toggle_automan):
        self.__toggle_automan = toggle_automan
    toggle_automan = property(get_toggle_automan, set_toggle_automan)

    def get_toggle_onoff(self):
        return self.__toggle_onoff
    def set_toggle_onoff(self, toggle_onoff):
        self.__toggle_onoff = toggle_onoff
    toggle_onoff = property(get_toggle_onoff, set_toggle_onoff)
    
    def get_iris_close(self):
        return self.__iris_close
    def set_iris_close(self, iris_close):
        self.__iris_close = iris_close
    iris_close = property(get_iris_close, set_iris_close)
    
    def get_iris_open(self):
        return self.__iris_open
    def set_iris_open(self, iris_open):
        self.__iris_open = iris_open
    iris_open = property(get_iris_open, set_iris_open)
    
    def get_focus_near(self):
        return self.__focus_near
    def set_focus_near(self, focus_near):
        self.__focus_near = focus_near
    focus_near = property(get_focus_near, set_focus_near)
    
    def get_focus_far(self):
        return self.__focus_far
    def set_focus_far(self, focus_far):
        self.__focus_far = focus_far
    focus_far = property(get_focus_far, set_focus_far)
    
    def get_zoom_wide(self):
        return self.__zoom_wide
    def set_zoom_wide(self, zoom_wide):
        self.__zoom_wide = zoom_wide
    zoom_wide = property(get_zoom_wide, set_zoom_wide)
    
    def get_tilt_down(self):
        return self.__tilt_down
    def set_tilt_down(self, tilt_down):
        self.__tilt_down = tilt_down
    tilt_down = property(get_tilt_down, set_tilt_down)
    
    def get_tilt_up(self):
        return self.__tilt_up
    def set_tilt_up(self, tilt_up):
        self.__tilt_up = tilt_up
    tilt_up = property(get_tilt_up, set_tilt_up)
    
    def get_pan_left(self):
        return self.__pan_left
    def set_pan_left(self, pan_left):
        self.__pan_left = pan_left
    pan_left = property(get_pan_left, set_pan_left)
    
    def get_pan_right(self):
        return self.__pan_right
    def set_pan_right(self, pan_right):
        self.__pan_right = pan_right
    pan_right = property(get_pan_right, set_pan_right)
        
    
def pelcod(camera, camera_options, pan_speed, tilt_speed):
    command1 = 0
    command1 += camera_options.sense*128
    command1 += 0*64
    command1 += 0*32
    command1 += camera_options.toggle_automan*16
    command1 += camera_options.toggle_onoff*8
    command1 += camera_options.iris_close*4
    command1 += camera_options.iris_open*2
    command1 += camera_options.focus_near*1
    
    command2 = 0
    command2 += camera_options.focus_far*128
    command2 += camera_options.zoom_wide*64
    command2 += camera_options.zoom_tele*32
    command2 += camera_options.tilt_down*16
    command2 += camera_options.tilt_up*8
    command2 += camera_options.pan_left*4
    command2 += camera_options.pan_right*2
    command2 += camera_options.0*1
    
    checksum = (camera + command1 + command2 + pan_speed + tilt_speed) % 256
    
    return [camera, command1, command2, pan_speed, tilt_speed, checksum]
