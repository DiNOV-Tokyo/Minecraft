import mcpi.minecraft as minecraft
import mcpi.block as block

import server
import sys



mc = minecraft.Minecraft()
mc.postToChat("Pyramid!")
playerPos = mc.player.getPos()
mc.player.setRotation(0)

height = 10
org_x = playerPos.x + 5
org_y = playerPos.y
org_z = playerPos.z + 5

for y in range(0, int(height / 2)):
    for z in range(1, height - 2 * y):
        for x in range(1, height - 2 * y):
            mc.setBlock(
                org_x + x + y,
                org_y + y,
                org_z + z + y,
                block.GOLD_BLOCK)

mc.postToChat("Pyramid constructed!")
