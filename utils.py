import math

def wrapToPi(x):
	while x>math.pi:
		x-=2*math.pi;
	while x<-math.pi:
		x+=2*math.pi;
	return x;

def hypot(x, y):
	return math.sqrt(x*x + y*y);
