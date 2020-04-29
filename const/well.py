import mcpi.minecraft as minecraft
import mcpi.block as block

import server
import sys



mc = minecraft.Minecraft()
mc.postToChat("Well")
playerPos = mc.player.getPos()
mc.player.setRotation(0)

height = 1
width = 3
org_x = playerPos.x + 5
org_y = playerPos.y
org_z = playerPos.z + 5

for y in range(0, height):
    for x in range(1, width):
        mc.setBlock(
            org_x + 1 + x,
            org_y + y,
            org_z,
            block.BRICK_BLOCK)
for y in range(0, height):
    for x in range(1, width):
        mc.setBlock(
            org_x + 1 + x,
            org_y + y,
            org_z + 2 + width,
            block.BRICK_BLOCK)
for y in range(0, height):
    for z in range(1, width):
        mc.setBlock(
            org_x,
            org_y + y,
            org_z + 1 + z,
            block.BRICK_BLOCK)
for y in range(0, height):
    for z in range(1, width):
        mc.setBlock(
            org_x + 2 + width,
            org_y + y,
            org_z + 1 + z,
            block.BRICK_BLOCK)
for y in range(0, height):
    mc.setBlock(
        org_x + 1,
        org_y + y,
        org_z + 1,
        block.BRICK_BLOCK)
    mc.setBlock(
        org_x + 1 + width,
        org_y + y,
        org_z + 1,
        block.BRICK_BLOCK)
    mc.setBlock(
        org_x + 1,
        org_y + y,
        org_z + 1 + width,
        block.BRICK_BLOCK)
    mc.setBlock(
        org_x + 1 + width,
        org_y + y,
        org_z + 1 + width,
        block.BRICK_BLOCK)

mc.postToChat("Well constructed!")
