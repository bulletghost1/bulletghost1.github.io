#Juan Barraza
from mcpi.minecraft import Minecraft
from mcpi import block    

mc = Minecraft.create("127.0.0.1", 4711)                                           
x, y, z = mc.player.getPos()  
zz = z + 1
#air
mc.setBlocks(x-20, y-1, zz, x+20,y+30,zz+30,0)
#temple
mc.setBlocks(x-5, y, zz, x+5, y, zz+16, 7)


#Side Walls
mc.setBlocks(x+5, y+1, zz, x+1,y,zz, 7)
mc.setBlocks(x-5, y+1, zz, x-1,y,zz, 7)
mc.setBlocks(x+5, y+1, zz+16, x-5,y+1,zz+16, 7)
mc.setBlocks(x+5, y+1, zz, x+5, y+1, zz+16, 7)
mc.setBlocks(x-5, y+1, zz, x-5, y+1, zz+16, 7)
mc.setBlocks(x+5, y+4, zz, x-5, y+4, zz, 7)
mc.setBlocks(x+5, y+4, zz+16, x-5, y+4, zz+16, 7)
mc.setBlocks(x+5, y+4, zz, x+5, y+4, zz+16, 7)
mc.setBlocks(x-5, y+4, zz, x-5, y+4, zz+16, 7)

#Corner Towers
mc.setBlocks(x+5, y+1, zz, x+5, y+5, zz, 7)
mc.setBlocks(x+5, y+1, zz+16, x+5, y+5, zz+16, 7)
mc.setBlocks(x-5, y+1, zz, x-5, y+5, zz, 7)
mc.setBlocks(x-5, y+1, zz+16, x-5, y+5, zz+16, 7)

#Window Gaps
mc.setBlocks(x+1, y+2, zz, x+1, y+3, zz, 7)
mc.setBlocks(x+3, y+2, zz, x+3, y+3, zz, 7)
mc.setBlocks(x-1, y+2, zz, x-1, y+3, zz, 7)
mc.setBlocks(x-3, y+2, zz, x-3, y+3, zz, 7)
mc.setBlocks(x+1, y+2, zz+16, x+1, y+3, zz+16, 7)
mc.setBlocks(x+3, y+2, zz+16, x+3, y+3, zz+16, 7)
mc.setBlocks(x-1, y+2, zz+16, x-1, y+3, zz+16, 7)
mc.setBlocks(x-3, y+2, zz+16, x-3, y+3, zz+16, 7)
mc.setBlocks(x+5, y+2, zz+2, x+5, y+3, zz+2, 7)
mc.setBlocks(x+5, y+2, zz+4, x+5, y+3, zz+4, 7)
mc.setBlocks(x+5, y+2, zz+6, x+5, y+3, zz+6, 7)
mc.setBlocks(x+5, y+2, zz+8, x+5, y+3, zz+8, 7)
mc.setBlocks(x+5, y+2, zz+10, x+5, y+3, zz+10, 7)
mc.setBlocks(x+5, y+2, zz+12, x+5, y+3, zz+12, 7)
mc.setBlocks(x+5, y+2, zz+14, x+5, y+3, zz+14, 7)
mc.setBlocks(x-5, y+2, zz+2, x-5, y+3, zz+2, 7)
mc.setBlocks(x-5, y+2, zz+4, x-5, y+3, zz+4, 7)
mc.setBlocks(x-5, y+2, zz+6, x-5, y+3, zz+6, 7)
mc.setBlocks(x-5, y+2, zz+8, x-5, y+3, zz+8, 7)
mc.setBlocks(x-5, y+2, zz+10, x-5, y+3, zz+10, 7)
mc.setBlocks(x-5, y+2, zz+12, x-5, y+3, zz+12, 7)
mc.setBlocks(x-5, y+2, zz+14, x-5, y+3, zz+14, 7)

#Ceiling and Roof
mc.setBlocks(x+4, y+5, zz, x-4,y+5,zz,114, 2)
mc.setBlocks(x+3, y+6, zz+1, x-3,y+6,zz+1,114, 2)
mc.setBlocks(x+2, y+7, zz+2, x-2,y+7,zz+2,114, 2)
mc.setBlocks(x+1, y+8, zz+3, x-1,y+8,zz+3,114, 2)
mc.setBlocks(x+4, y+5, zz+15, x-4,y+5,zz+15,114, 3)
mc.setBlocks(x+3, y+6, zz+14, x-3,y+6,zz+14,114, 3)
mc.setBlocks(x+2, y+7, zz+13, x-2,y+7,zz+13,114, 3)
mc.setBlocks(x+1, y+8, zz+12, x-1,y+8,zz+12,114, 3)
mc.setBlocks(x-5, y+5, zz+1, x-5,y+5,zz+15,114)
mc.setBlocks(x-4, y+6, zz+1, x-4,y+6,zz+14,114)
mc.setBlocks(x-3, y+7, zz+2, x-3,y+7,zz+13,114)
mc.setBlocks(x-2, y+8, zz+3, x-2,y+8,zz+12,114)
mc.setBlocks(x+5, y+5, zz+1, x+5,y+5,zz+15,114, 1)
mc.setBlocks(x+4, y+6, zz+1, x+4,y+6,zz+14,114, 1)
mc.setBlocks(x+3, y+7, zz+2, x+3,y+7,zz+13,114, 1)
mc.setBlocks(x+2, y+8, zz+3, x+2,y+8,zz+12,114, 1)




#API Blocks
#====================
#   AIR                   0
#   STONE                 1
#   GRASS                 2
#   DIRT                  3
#   COBBLESTONE           4
#   WOOD_PLANKS           5
#   SAPLING               6
#   BEDROCK               7
#   WATER_FLOWING         8
#   WATER                 8
#   WATER_STATIONARY      9
#   LAVA_FLOWING         10
#   LAVA                 10
#   LAVA_STATIONARY      11
#   SAND                 12
#   GRAVEL               13
#   GOLD_ORE             14
#   IRON_ORE             15
#   COAL_ORE             16
#   WOOD                 17
#   LEAVES               18
#   GLASS                20
#   LAPIS_LAZULI_ORE     21
#   LAPIS_LAZULI_BLOCK   22
#   SANDSTONE            24
#   BED                  26
#   COBWEB               30
#   GRASS_TALL           31
#   WOOL                 35
#   FLOWER_YELLOW        37
#   FLOWER_CYAN          38
#   MUSHROOM_BROWN       39
#   MUSHROOM_RED         40
#   GOLD_BLOCK           41
#   IRON_BLOCK           42
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#	BRICK_BLOCK			 45
#	TNT					 46
#	BOOKSHELF			 47
#	MOSS_STONE			 48
#	OBSIDIAN			 49
#	TORCH				 50
#	FIRE				 51
#	STAIRS_WOOD			 53
#	CHEST				 54
#	DIAMOND_ORE			 56
#	DIAMOND_BLOCK		 57
#	CRAFTING_TABLE		 58
#	OAK_STAIRS			 59
#	FARMLAND			 60
#	FURNACE_INACTIVE	 61
#	FURNACE_ACTIVE		 62
#	DOOR_WOOD			 64
#	LADDER				 65
#	STAIRS_COBBLESTONE	 67
#	DOOR_IRON			 71
#	REDSTONE_ORE		 73
#	SNOW				 78
#	ICE					 79
#	SNOW_BLOCK			 80
#	CACTUS				 81
#	CLAY				 82
#	SUGAR_CANE			 83
#	FENCE				 85
#	NETHERRACK			 87
#	GLOWSTONE_BLOCK		 89
#	BEDROCK_INVISIBLE	 95
#	TRAPDOOR			 96
#	STONE_BRICK			 98
#	GLASS_PANE			 102
#	MELON				 103
# 	MELON_SEEDS			 105
#	FENCE_GATE			 107
#	BRICK_STAIRS		 108
#	STONE_BRICK_STAIRS	 109
#	NETHER_BRICK		 112
#	NETHER_BRICK_STAIRS	 114
#	SANDSTONE_STAIRS	 128
#	QUARTZ_BLOCK		 155
#	QUARTZ_STAIRS		 156
#	STONE_CUTTER		 245
#	GLOWING_OBSIDIAN	 246
#	NETHER_REACTOR_CORE	 247
#	PAINTING			 321
#	BONE_MEAL			 351
