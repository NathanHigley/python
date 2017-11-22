from mcpi.minecraft import Minecraft
from mcpi import block	  
from time import sleep

def init():
	mc = Minecraft.create("192.168.3.5",4711)
	x,y,z = mc.player.getPos()
	return mc
	
def cabin(mc,x,y,z,m):  
	#walls
	mc.setBlocks(x-6,y,z-20,x+6,y+10,z-20,5)
	mc.setBlocks(x-6,y,z-20,x-6,y+10,z+20,5)
	mc.setBlocks(x+6,y,z-20,x+6,y+10,z+20,5)
	mc.setBlocks(x-6,y,z+20,x+6,y+10,z+20,5)
	mc.setBlocks(x-6,y,z-20,x+6,y,z+20,5)
	mc.setBlocks(x-6,y+10,z-20,x+6,y+10,z+20,5)
	mc.setBlocks(x-2,y+1,z-20,x+2,y+8,z-20,0)
	#log
	mc.setBlocks(x-7,y+8,z-21,x+7,y+10,z-21,17)
	mc.setBlocks(x-7,y+8,z-21,x-7,y+10,z+21,17)
	mc.setBlocks(x+7,y+8,z-21,x+7,y+10,z+21,17)
	mc.setBlocks(x-7,y+8,z+21,x+7,y+10,z+21,17)
	#fence
	mc.setBlocks(x-6,y+11,z-20,x+6,y+11,z-20,85)
	mc.setBlocks(x-6,y+11,z-20,x-6,y+11,z+20,85)
	mc.setBlocks(x+6,y+11,z-20,x+6,y+11,z+20,85)
	mc.setBlocks(x-6,y+11,z+20,x+6,y+11,z+20,85)		
	#torch
	mc.setBlocks(x-5,y+3,z-19,x-5,y+3,z+19,50)
	mc.setBlocks(x-5,y+3,z+19,x+5,y+3,z+19,50)
	mc.setBlocks(x+5,y+3,z-19,x+5,y+3,z+19,50)
	mc.setBlocks(x-5,y+8,z-19,x-5,y+8,z+19,50)
	mc.setBlocks(x-5,y+8,z+19,x+5,y+8,z+19,50)
	mc.setBlocks(x+5,y+8,z-19,x+5,y+8,z+19,50)
	#fence
	mc.setBlocks(x-4,y+1,z-19,x-4,y+1,z+19,85)
	mc.setBlocks(x+4,y+1,z-19,x+4,y+1,z+19,85)
			
def main():	
	mc = init()
	mc.player.setPos(50,50,50)
	x,y,z = mc.player.getPos()  
	cabin(mc,x,y-12,z,m)

main()
