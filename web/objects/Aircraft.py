import sys
sys.path.insert( 0, r"E:\Users\Jason\Development\git\steakisland\web\utility" )

from Logger import *
from Utility import *

class Aircraft:

	__cost_index	= None
	__current_route	= None
	__flight_number	= None
	__id			= None
	__last_a_check	= None
	__mod_level		= None
	__tail_num		= None
	__type			= None
	
	__log			= None

	# constructor
	def __init__( self, id ):
		# set logger
		self.__log = Logger( "Aircraft", "steakisland" )
		self.__log.add_log_stream( "main" )
		self.__log.add_log_stream( "aircraft" )
		self.__log.log( "Test data", "test message", 1 )
		Utility.var_check( id, int )
		self.id = id

	def __get_cost_index( self ):
		return self.__cost_index

	def __set_cost_index( self, cost_index ):
		Utility.var_check( cost_index, int )
		self.__cost_index = cost_index

	# cost index to use for this aircraft's current route
	cost_index = property( __get_cost_index, __set_cost_index )
	
	def __get_current_route( self ):
		return self.__current_route
	
	def __set_current_route( self, current_route ):
		Utility.var_check( current_route, Route )
		self.__current_route = current_route

	# route to which this aircraft is currently assigned
	current_route = property( __get_current_route, __set_current_route )

	def __get_flight_number( self ):
		return self.__flight_number
	
	def __set_flight_number( self, flight_number ):
		Utility.var_check( flight_number, int )
		self.__flight_number = flight_number
	
	# flight number currently assigned to this aircraft
	flight_number = property( __get_flight_number, __set_flight_number )
	
	def __get_id( self ):
		return self.__id
	
	def __set_id( self, id ):
		Utility.var_check( id, int )
		self.__id = id
	
	# system ID for this aircraft
	id = property( __get_id, __set_id )
	
	def __get_last_a_check( self ):
		return self.__last_a_check
	
	def __set_last_a_check( self, last_a_check ):
		Utility.var_check( last_a_check, datetime )
		self.__last_a_check = last_a_check
	
	last_a_check = property( __get_last_a_check, __set_last_a_check )

	def __get_mod_level( self ):
		return self.__mod_level
	
	def __set_mod_level( self, mod_level ):
		Utility.var_check( mod_level, str )
		self.__mod_level = mod_level
	
	# code denoting which modifications have been made to this aircraft
	mod_level = property( __get_mod_level, __set_mod_level )
	
	def __get_tail_num( self ):
		return self.__tail_num
	
	def __set_tail_num( self, tail_num ):
		Utility.var_check( tail_num, str )
		self.__tail_num = tail_num
	
	# tail number assigned to this aircraft
	tail_num = property( __get_tail_num, __set_tail_num )
	
	def __get_type( self ):
		return self.__type
	
	def __set_type( self, type ):
		Utility.var_check( type, str )
		self.__type = type

	type = property( __get_type, __set_type )
	