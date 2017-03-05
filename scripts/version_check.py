#-*- coding: utf-8 -*-
#
#	Author : Chia Xin Lin
#	This standalone maya script 
#	can be check out version compatiable
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
	logging.info('START VERSION CHECK - %s'%(check_maya_file))
	app_info = [ \
	    ' @ Application - %s\n'%(mc.about(a=True)), \
	    ' @ Production - %s\n'%(mc.about(p=True)), \
	    ' @ Version - %s\n'%(mc.about(v=True)), \
	    ' @ Cut Identifier - %s\n'%(mc.about(c=True)), \
	    ' @ OS Version - %s\n'%(mc.about(osv=True))]
	logging.info(' \n@ Application Info - \n%s'%(''.join(app_info)))
	# If everything is right, return 0
	return 0

if __name__=='__main__':
	check_maya_file = sys.argv[1]
	if main(check_maya_file) == 0:
		logging.info('>>> Version Check : Result - OK .')
		sys.exit(0)
	logging.info('>>> Version Check Failed! Please check out them .')
	sys.exit(-1)
