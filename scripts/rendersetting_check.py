#-*- coding: utf-8 -*-
#
#	Author : Chia Xin Lin
#	This standalone maya script 
#	can be check out render setting (Mental Ray)
#
import sys
import os
import os.path
import logging
import maya.standalone
import maya.cmds as mc
maya.standalone.initialize()

RENDERABLE_CAM = ('shotCamShape', )
logging.basicConfig(level=logging.INFO, format='\n[%(levelname)s] - %(message)s\n')

def check_camera():
	'''
	Check just only "shotCam" is launch
	'''
	global RENDERABLE_CAM
	cameraShapes = mc.ls(type='cameraShape')
	for camera in cameraShapes:
		if mc.getAttr(camera+'.renderable') \
		and camera not in RENDERABLE_CAM:
			logging.warning('%s should not be launch renderable!'%(camera))
			return -1

def check_renderlayer():
	'''
	Check the masterLayer(defaultRenderLayer) is not launch
	'''
	# Get all render layers, without reference
	all_renderlayers = mc.ls(type='renderLayer')
	referenced_rl = mc.ls(type='renderLayer', rn=True)
	for layer in all_renderlayers:
		if layer in referenced_rl:
			continue
		renderable = mc.getAttr(layer+'.renderable')
		if layer == 'defaultRenderLayer':
			if renderable:
				logging.warning(
					'Master Render Layer should not be launch renderable!')
				return -1
		if renderable:
			logging.info('<Render Layer launch> %s'%(layer))
	return 0

def main(check_maya_file):
	if not os.path.isfile(check_maya_file):
		logging.warning(
			'Failed because Maya file was not found! - %s'%(check_maya_file))
		return -1
	logging.info('START CHECK - %s'%(check_maya_file))
	mc.file(check_maya_file, open=True)
	#
	logging.info('Check out unit')
	current_unit = mc.currentUnit(q=True, l=True)
	if current_unit != 'cm':
		logging.warning('Maya unit is not \"centimeter\"')
		return -1
	logging.info('Check out time')
	current_time = mc.currentUnit(q=True, t=True)
	if current_time != 'ntsc':
		logging.warning('Maya time is not \"ntsc(30FPS)\"')
		return -1
	logging.info('Check out camera')
	if check_camera() == -1:
		return -1
	logging.info('Check out render layer')
	if check_renderlayer() == -1:
		return -1
	logging.info('Check Renderer (Mental Ray)')
	if mc.getAttr('defaultRenderGlobals.currentRenderer') != 'mentalRay':
		logging.warning('Current Renderer is not Mental Ray!')
		return -1
	logging.info('Check render size')
	if mc.getAttr('defaultResolution.width') != 1920 \
	or mc.getAttr('defaultResolution.height') != 1080:
		logging.warning('Render Size is Error!')
		return -1
	logging.info('Check render image format')
	if mc.getAttr('defaultRenderGlobals.imfPluginKey') != 'exr':
		logging.warning('Render Image format is not EXR!')
		return -1
	logging.info('Check render image compression')
	if mc.getAttr('defaultRenderGlobals.exrCompression') != 3:
		logging.warning('Render Image Compression is wrong!')
		return -1
	#
	# If everything is right, return 0
	return 0

if __name__=='__main__':
	check_maya_file = sys.argv[1]
	if main(check_maya_file) == 0:
		logging.info('>>> Render Setting Check Finish : Result - OK .')
		sys.exit(0)
	logging.info('>>> Render Setting Check Failed! Please check out them .')
	sys.exit(-1)
