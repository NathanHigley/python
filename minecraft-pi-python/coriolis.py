from mcpi.minecraft import Minecraft

'''
air = 0
stone = 1
obs = 49
ice = 79
glow = 89
core = 247
'''

def init():
	mc = Minecraft.create()
	#mc = Minecraft.create("10.183.3._", 4711)
	x,y,z = mc.player.getPos()
	return mc
	
def sector(mc, x , y, z):
	import random
	#clear area
	mc.setBlocks(x+5, y+1, z+0, x+75, y+75, z+75, 0)

	#create sector
	mc.setBlocks(x+5, y+1, z+0, x+75, y+75, z+75, 49)
	mc.setBlocks(x+6,y+2, z+1, x+74, y+74, z+74, 0)
	
	#create planet
	n = 0
	b = [22, 79, 247]
	while n <= 9:
		mc.setBlocks(x+6+n, y+2+n, z+1+n, x+74-n, y+2+n, z+74-n, (random.choice(b)))
		if n == 0:
			mc.setBlocks(x+6, y+2, z+1, x+74, y+2, z+74, 89)
		n = n + 1
	
def frame(mc, x, y, z):
	#create frame
	mc.setBlocks(x+0, y+0, z+0, x+30, y+30, z+30, 1)
	
	#shave corners
	n = 0
	while n <= 10:
		#front top right
		mc.setBlocks(x+0+n, y+30, z+10-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+29, z+9-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+28, z+8-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+27, z+7-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+26, z+6-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+25, z+5-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+24, z+4-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+23, z+3-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+22, z+2-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+21, z+1-n, x+0, y+30, z-1, 0)
		mc.setBlocks(x+0+n, y+20, z+0-n, x+0, y+30, z-1, 0)
		
		#front top left
		mc.setBlocks(x+30-n, y+30, z+10-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+29, z+9-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+28, z+8-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+27, z+7-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+26, z+6-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+25, z+5-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+24, z+4-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+23, z+3-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+22, z+2-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+21, z+1-n, x+30, y+30, z-1, 0)
		mc.setBlocks(x+30-n, y+20, z+0-n, x+30, y+30, z-1, 0)
		
		#front bottom right
		mc.setBlocks(x+0+n, y+0, z+10-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+1, z+9-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+2, z+8-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+3, z+7-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+4, z+6-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+5, z+5-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+6, z+4-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+7, z+3-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+8, z+2-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+9, z+1-n, x+0, y+0, z-1, 0)
		mc.setBlocks(x+0+n, y+10, z+0-n, x+0, y+0, z-1, 0)
		
		#front bottom left
		mc.setBlocks(x+30-n, y+0, z+10-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+1, z+9-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+2, z+8-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+3, z+7-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+4, z+6-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+5, z+5-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+6, z+4-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+7, z+3-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+8, z+2-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+9, z+1-n, x+30, y+0, z-1, 0)
		mc.setBlocks(x+30-n, y+10, z+0-n, x+30, y+0, z-1, 0)
		
		#back top right
		mc.setBlocks(x+0+n, y+30, z+20+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+29, z+21+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+28, z+22+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+27, z+23+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+26, z+24+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+25, z+25+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+24, z+26+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+23, z+27+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+22, z+28+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+21, z+29+n, x+0, y+30, z+31, 0)
		mc.setBlocks(x+0+n, y+20, z+30+n, x+0, y+30, z+31, 0)
		
		#back top left
		mc.setBlocks(x+30-n, y+30, z+20+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+29, z+21+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+28, z+22+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+27, z+23+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+26, z+24+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+25, z+25+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+24, z+26+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+23, z+27+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+22, z+28+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+21, z+29+n, x+30, y+30, z+31, 0)
		mc.setBlocks(x+30-n, y+20, z+30+n, x+30, y+30, z+31, 0)
		
		#back bottom right
		mc.setBlocks(x+0+n, y+0, z+20+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+1, z+21+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+2, z+22+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+3, z+23+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+4, z+24+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+5, z+25+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+6, z+26+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+7, z+27+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+8, z+28+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+9, z+29+n, x+0, y+0, z+31, 0)
		mc.setBlocks(x+0+n, y+10, z+30+n, x+0, y+0, z+31, 0)
		
		#back bottom left
		mc.setBlocks(x+30-n, y+0, z+20+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+1, z+21+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+2, z+22+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+3, z+23+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+4, z+24+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+5, z+25+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+6, z+26+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+7, z+27+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+8, z+28+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+9, z+29+n, x+30, y+0, z+31, 0)
		mc.setBlocks(x+30-n, y+10, z+30+n, x+30, y+0, z+31, 0)
		
		n = n + 1
		
	#create mailslot
	mc.setBlocks(x+12, y+16, z+0, x+18, y+16, z+2, 79)
	mc.setBlocks(x+15, y+17, z+0, x+15, y+15, z+2, 0)
	
def port(mc, x, y, z):
	#clear area
	mc.setBlocks(x-6, y+8, z+0, x+10, y+23, z+26, 0)
	
	#create cylinder
	mc.setBlocks(x+4, y+8, z+0, x+0, y+8, z+26, 1)
	mc.setBlocks(x-2, y+9, z+0, x-1, y+9, z+26, 1)
	mc.setBlocks(x+5, y+9, z+0, x+6, y+9, z+26, 1)
	mc.setBlocks(x-4, y+10, z+0, x-3, y+10, z+26, 1)
	mc.setBlocks(x+8, y+10, z+0, x+7, y+10, z+26, 1)
	mc.setBlocks(x-4, y+11, z+0, x-4, y+1, z+26, 1)
	mc.setBlocks(x+8, y+11, z+0, x+8, y+1, z+26, 1)
	mc.setBlocks(x-5, y+13, z+0, x-5, y+12, z+26, 1)
	mc.setBlocks(x+9, y+13, z+0, x+9, y+12, z+26, 1)
	mc.setBlocks(x-6, y+14, z+0, x-6, y+18, z+26, 1)
	mc.setBlocks(x+10, y+14, z+0, x+10, y+18, z+26, 1)
	mc.setBlocks(x-5, y+19, z+0, x-5, y+20, z+26, 1)
	mc.setBlocks(x+9, y+19, z+0, x+9, y+20, z+26, 1)
	mc.setBlocks(x-4, y+21, z+0, x-4, y+22, z+26, 1)
	mc.setBlocks(x+8, y+21, z+0, x+8, y+22, z+26, 1)
	mc.setBlocks(x-3, y+22, z+0, x-3, y+22, z+26, 1)
	mc.setBlocks(x+7, y+22, z+0, x+7, y+22, z+26, 1)
	mc.setBlocks(x-2, y+23, z+0, x-1, y+23, z+26, 1)
	mc.setBlocks(x+6, y+23, z+0, x+5, y+23, z+26, 1)
	mc.setBlocks(x+4, y+24, z+0, x+0, y+24, z+26, 1)

def relic(mc, x, y, z):
	#create crater
	n = 0
	while n <= 9:
		mc.setBlocks(x+50-n, y+11-n, z+50-n, x+25+n, y+11-n, z+25+n, 0)
		n = n + 1
		
	#create relic
	x = x + 22
	y = y + 6
	z = z + 38
	mc.setBlocks(x+5, y+0, z+0, x+1, y+0, z+0, 42)
	mc.setBlocks(x+5, y+1, z+0, x+4, y+1, z+0, 20)
	mc.setBlocks(x+6, y+2, z+0, x+10, y+2, z+0, 20)
	mc.setBlocks(x+11, y+2, z+0, x+11, y+2, z+0, 42)
	mc.setBlocks(x+6, y+1, z+1, x+8, y+1, z+1, 35,11)
	mc.setBlocks(x+6, y+1, z-1, x+8, y+1, z-1, 35,11)
	mc.setBlocks(x+9, y+1, z+1, x+9, y+1, z+1, 42)
	mc.setBlocks(x+9, y+1, z-1, x+9, y+1, z-1, 42)
	mc.setBlocks(x+9, y+2, z+1, x+10, y+2, z+1, 35,11)
	mc.setBlocks(x+9, y+2, z-1, x+10, y+2, z-1, 35,11)
	mc.setBlocks(x+10, y+3, z+1, x+11, y+3, z+1, 35,11)
	mc.setBlocks(x+10, y+3, z-1, x+11, y+3, z-1, 35,11)
	mc.setBlocks(x+6, y-1, z+0, x+6, y-1, z+0, 42)
	mc.setBlocks(x+6, y-1, z+1, x+7, y-1, z+1, 35,11)
	mc.setBlocks(x+6, y-1, z-1, x+7, y-1, z-1, 35,11)
	mc.setBlocks(x+8, y-2, z+1, x+10, y-2, z+1, 35,11)
	mc.setBlocks(x+8, y-2, z-1, x+10, y-2, z-1, 35,11)
	mc.setBlocks(x+6, y+0, z+1, x+6, y+0, z+1, 245)
	mc.setBlocks(x+6, y+0, z-1, x+6, y+0, z-1, 245)
	mc.setBlocks(x+7, y+0, z+1, x+7, y+0, z+1, 42)
	mc.setBlocks(x+7, y+0, z-1, x+7, y+0, z-1, 42)
	mc.setBlocks(x+9, y+0, z+1, x+9, y+0, z+1, 42)
	mc.setBlocks(x+9, y+0, z-1, x+9, y+0, z-1, 42)
	mc.setBlocks(x+8, y+0, z+2, x+10, y+0, z+2, 42)
	mc.setBlocks(x+8, y+0, z-2, x+10, y+0, z-2, 42)
	mc.setBlocks(x+11, y+0, z+3, x+13, y+0, z+3, 42)
	mc.setBlocks(x+11, y+0, z-3, x+13, y+0, z-3, 42)
	mc.setBlocks(x+14, y+0, z+4, x+15, y+0, z+4, 42)
	mc.setBlocks(x+14, y+0, z-4, x+15, y+0, z-4, 42)
	mc.setBlocks(x+16, y+0, z+5, x+17, y+0, z+5, 42)
	mc.setBlocks(x+16, y+0, z-5, x+17, y+0, z-5, 42)
	mc.setBlocks(x+9, y+0, z+0, x+9, y+0, z+0, 49)
	mc.setBlocks(x+10, y+1, z+0, x+10, y+1, z+0, 35,1)
	        
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	mc.player.setPos(70,30,70)
	sector(mc, 50, -15, 50)
	frame(mc, 75, 20, 75)
	port(mc, 88, 20, 78)
	relic(mc, 50, -15, 50)

main()
