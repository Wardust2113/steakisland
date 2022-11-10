import sys
sys.path.insert( 0, r"E:\Users\Jason\Development\git\steakisland\web\utility" )

from Logger import *
from Utility import *

class Airport:

	__icao			= None
	__id			= None
	__name			= None
	__runway_length	= None
	
	__log			= None
	
	# constructor
	def __init__( self, id ):
		self.__log = Logger( "Airport", "steakisland" )
		self.__log.add_log_stream( "main" )
		self.__log.add_log_stream( "aircraft" )
		Utility.var_check( id, int )
		self.id = id
	
	def __get_icao( self ):
		return self.__icao
	
	def __set_icao( self, icao ):
		Utility.var_check( icao, str )
		self.__icao = icao
	
	icao = property( __get_icao, __set_icao )
	
	def __get_id( self ):
		return self.__id
	
	def __set_id( self, id ):
		Utility.var_check( id, int )
		self.__id = id
	
	id = property( __get_id, __set_id )
	
	def __get_name( self ):
		return self.__name
	
	def __set_name( self, name ):
		Utility.var_check( name, str )
		self.__name = name
	
	name = property( __get_name, __set_name )

	def __get_runway_length( self ):
		return self.__runway_length
	
	def __set_runway_length( self, runway_length ):
		Utility.var_check( runway_length, int )
		self.__runway_length = runway_length
	
	runway_length = property( __get_runway_length, __set_runway_length )
