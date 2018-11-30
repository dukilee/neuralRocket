import math

game = {
	'caption':'Neural Rocket',
	'height' : 600,
	'width'  : 800,
	'fps'    : 30,
	'scale'  : 50, #conversion from meters to pixels
	'floorHeight' : 50, #in pixels
};

initialPosition = {
	#(0, 0) the center of the floor
	'x':0, #in meters
	'y':7, #in meters
	'angle':math.pi/2 #in radians
};

rocket = {
	'mass'        :7,   #in kg
	'width'       :1,    #in meters
	'height'      :3,    #in meters
	'motorPower'  :10,  #in newtons
};

physics = {
	'gravity'   :0.981,   #in m/s²
};

colors = {
	'white':(255, 255, 255),
	'black':(0, 0, 0),
	'red':(200, 0, 0),
	'green':(0, 200, 0),
	'blue':(0, 0, 200),

};
