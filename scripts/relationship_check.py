#-*- coding: utf-8 -*-
#
#	Author : Chia Xin Lin
#	This standalone maya script 
#	can be check out reference & texture relationship
#
import sys
import os
import os.path
import logging
import maya.standalone
import maya.cmds as mc
maya.standalone.initialize()

logging.basicConfig(level=logging.WARNING, format='\n[%(levelname)s] - %(message)s\n')

def main(check_maya_file):
	if not os.path.isfile(check_maya_file):
		logging.warning(
			'Failed because Maya file was not found! - %s'%(check_maya_file))
		return -1
	logging.info('START CHECK - %s'%(check_maya_file))
	mc.file(check_maya_file, open=True)
	# Check reference relationship
	for reference in mc.ls(type='reference'):
		if reference == '_UNKNOWN_REF_NODE_':
			logging.warning('Got Unknown Reference Node!')
			continue
		if reference == 'sharedReferenceNode':
			continue
		logging.info('Check refernece - %s'%(reference))
		referenced_file = mc.referenceQuery(
			reference, f=True, wcn=True)
		logging.info('Check reference path - %s'%(referenced_file))
		if not os.path.isfile(referenced_file):
			logging.error('[!] The reference was not exists! : %s'%(referenced_file))
			return -1
		if not mc.referenceQuery(reference, isLoaded=True):
			logging.error('[!] The reference was not loaded! : %s'%(reference))
			return -1
		logging.info('> Check OK .')

	# Try to get "PROJECTWORKS" environment variable
	projectworks = os.environ.get('PROJECTWORKS', 0)
	if not projectworks:
		logging.error('[!] Project works is undefined! \
			Please to check out Maya.env file.')
		return -1
	# Check texture file
	for texture in mc.ls(type='file'):
		logging.info('Check File - %s'%(texture))
		tex_name = mc.getAttr(texture+'.fileTextureName')
		if not tex_name:
			continue
		logging.info('Check File Path - %s'%(tex_name))
		if tex_name.startswith('$'):
			replace_name = tex_name.replace('$PROJECTWORKS', projectworks)
			tex_name = replace_name
			logging.debug('Replace variable : %s -> %s'%(tex_name, replace_name))
		if not os.path.isfile(tex_name):
			logging.warning('The texture was not found! - %s'%(tex_name))
			return -1
	# If everything is right, return 0
	return 0

if __name__=='__main__':
	check_maya_file = sys.argv[1]
	if main(check_maya_file) == 0:
		logging.info('>>> Relationship Check Finish : Result - OK .')
		sys.exit(0)
	logging.info('>>> Relationship Check Failed! Please check out them .')
	sys.exit(-1)
