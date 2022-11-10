class Utility:

	def __init__( self ):
		pass

	# type checking function
	@staticmethod
	def var_check( var_data, var_type ):
		observed_var_type = type( var_data )
		if type( var_data ) is not var_type:
			raise Exception( "Variable type mismatch!" )

	# convert kilometers into nautical miles
	@staticmethod
	def km_to_nm( dist_km ):
		#TODO: conversion method
		pass
