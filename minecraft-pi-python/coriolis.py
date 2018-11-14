from mcpi.minecraft import Minecraft

#MATERIAL
air = 0
stone = 1
wood = 1
water = 8
obs = 49
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
	n = 0
	while n <= 14:
		mc.setBlocks(x+18, y+18, z+18, x+36, y+36, z+36, air)
		n = n + 1
	#mc.setBlocks(x+, y+, z+, x+, y+, z+, air)
	#mc.setBlocks(x+, y+, z+, x+, y+, z+, air)
	#mc.setBlocks(x+, y+, z+, x+, y+, z+, air)
	#create mailslot(water)
	#more thing
	
#def port(mc, x, y, z):
	#create cylinder
	#thing
	
def small(mc,x,y,z,m):	
	m = 0	
	while m < 14:
		if x-12+m<=x: 
			mc.setBlocks(x-12+m,y-6+m,z+25+m,x-12+m,y-3+m,z+26+m, wood) #6 #lower right
		if x-11+m<=x: 
			mc.setBlocks(x-11+m,y-8+m,z+25+m,x-11+m,y-6+m,z+26+m, wood) #8
		if x-10+m<=x: 
			mc.setBlocks(x-10+m,y-9+m,z+25+m,x-10+m,y-7+m,z+26+m, wood) #9
		if x-9+m<=x:
			mc.setBlocks(x-9+m,y-10+m,z+25+m,x-9+m,y-8+m,z+26+m, wood) #10
		if x-8+m<=x:
			mc.setBlocks(x-8+m,y-11+m,z+25+m,x-8+m,y-10+m,z+26+m, wood) #11
		if x-7+m<=x:
			mc.setBlocks(x-7+m,y-12+m,z+25+m,x-7+m,y-11+m,z+26+m, wood) #12
		if x-6+m<=x:
			mc.setBlocks(x-6+m,y-13+m,z+25+m,x-6+m,y-11+m,z+26+m, wood) #13
		if x-5+m<=x:
			mc.setBlocks(x-5+m,y-13+m,z+25+m,x-5+m,y-12+m,z+26+m, wood) #13
		if x-13+m<=x:
			mc.setBlocks(x-13+m,y+3+m,z+25+m,x-13+m,y-3+m,z+26+m, wood) #left

		if x+13-m>=x: 
			mc.setBlocks(x+13-m,y+3+m,z+25+m,x+13-m,y-3+m,z+26+m, wood) #right
		if x+12-m>=x: 
			mc.setBlocks(x+12-m,y-6+m,z+25+m,x+12-m,y-3+m,z+26+m, wood) #6 #lower left
		if x+11-m>=x:
			mc.setBlocks(x+11-m,y-8+m,z+25+m,x+11-m,y-6+m,z+26+m, wood) #8
		if x+10-m>=x:
			mc.setBlocks(x+10-m,y-9+m,z+25+m,x+10-m,y-7+m,z+26+m, wood) #9 
		if x+9-m>=x:
			mc.setBlocks(x+9-m,y-10+m,z+25+m,x+9-m,y-8+m,z+26+m, wood) #10
		if x+8-m>=x:
			mc.setBlocks(x+8-m,y-11+m,z+25+m,x+8-m,y-10+m,z+26+m, wood) #11
		if x+7-m>=x:
			mc.setBlocks(x+7-m,y-12+m,z+25+m,x+7-m,y-11+m,z+26+m, wood) #12
		if x+6-m>=x:
			mc.setBlocks(x+6-m,y-13+m,z+25+m,x+6-m,y-11+m,z+26+m, wood) #13
		if x+5-m>=x:
			mc.setBlocks(x+5-m,y-13+m,z+25+m,x+5-m,y-12+m,z+26+m, wood) #13
		m = m + 1	

def coriolis():
	mc = init()
	x, y, z = mc.player.getPos()
	mc.player.setPos(50,50,50)
	#sector(mc,x-17.5, y-17.5, z+5)
	frame(mc, x-18, y-18, z+5)
	#port(mc, x-17.5, y-17.5, z+8)
	#small(mc, 30, 30, 30, 1)

coriolis()
