from mcpi.minecraft import Minecraft

#MATERIAL
air = 0
stone = 1
wood = 1
water = 8
slab = 44
obs = 49
ice = 79
glow = 89
glowred = 246
core = 247

def init():
	mc = Minecraft.create()
	x,y,z = mc.player.getPos()
	return mc
	
def sector(mc, x , y, z):
	#import random
	mc.setBlocks(x+5, y+1, z+0, x+75, y+75, z+75, 0)
	mc.setBlocks(x+5, y+1, z+0, x+75, y+75, z+75, 49)
	mc.setBlocks(x+6,y+2, z+1, x+74, y+74, z+74, 0)
	n = 0
	while n <= 9:
		mc.setBlocks(x+6+n, y+2+n, z+1+n, x+74-n, y+2+n, z+74-n, 246)
		n = n + 1

def frame(mc, x, y, z):
	#create structure
	mc.setBlocks(x+0, y+0, z+0, x+30, y+30, z+30, stone)
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
		
	#create mailslot(outline edges with slabs, insides with water)
	mc.setBlocks(x+12, y+16, z+0, x+18, y+16, z+2, ice)
	
def port(mc, x, y, z):
	#clear area
	mc.setBlocks(x+7, y+7, z+3, x+23, y+23, z+29, air)
	#create cylinder
	#thing
        
def coriolis():
	mc = init()
	x, y, z = mc.player.getPos()
	mc.player.setPos(70,30,70)
	sector(mc, 50, -15, 50)
	#frame(mc, 75, 20, 75)
	#port(mc, 75, 20, 75)

coriolis()
