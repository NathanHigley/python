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
	
#def sector():
	#create obsidian box of space
	#include glowstone/water, potentially spherical

def frame(mc, x, y, z):
	#clear area
	mc.setBlocks(x-50, y-50, z-50, x+50, y+50, z+50, air)
	#create structure
	mc.setBlocks(x+0, y+0, z+0, x+30, y+30, z+30, stone)
	#shave corners, max of 13
	#front top right
	n = 0
	if n <= 3:
		mc.setBlocks(x+0+n, y+30-n, z+10-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+29-n, z+9-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+28-n, z+8-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+27-n, z+7-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+26-n, z+6-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+25-n, z+5-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+24-n, z+4-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+23-n, z+3-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+22-n, z+2-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+21-n, z+1-n, x+0, y+30, z+0, 0)
		mc.setBlocks(x+0+n, y+20-n, z+0-n, x+0, y+30, z+0, 0)
	
	#mc.setBlocks(x+0, y+30, z+0, x+13, y+30, z+13, air)
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
	mc.player.setPos(50,50,50)
	#sector(mc,x-17.5, y-17.5, z+5)
	frame(mc, 50, 10, 50)
	port(mc, 50, 10, 50)

coriolis()
