import mcpi.minecraft as minecraft
import mcpi.block as block
from board2d import Board2D
from creature import Creature

import server
import sys



mc = minecraft.Minecraft()

creature = Creature(mc, 0, 0, distance=6)

mc.postToChat("Hello world!")
playerPos = mc.player.getPos()
mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.DIAMOND_ORE)

creature.spawnEntity("Endermite", 3, 0, 0)
creature.spawnEntity("Enderman", 4, 0, 0)
creature.spawnEntity("Sheep", 1, 0, 0)
#creature.spawnEntity("EnderDragon", 0, 9, 0)


for y in range(0, 5):
    for z in range(1, 10 - 2 * y):
        for x in range(1, 10 - 2 * y):
            mc.setBlock(
                playerPos.x + x + y + 5,
                playerPos.y + y,
                playerPos.z + z + y + 5,
                block.BEACON)

creature.deleteEntity("Endermite")
