from LogStream import *
import datetime

class Logger:

	name		= None
	log_streams	= None
	
	# constructor
	def __init__( self, name, log_file = None ):
		self.name = name
		self.log_streams = []
	
	# log data to log file
	def log( self, data, message, severity = 1 ):
		# for each log stream
		for log_stream in self.log_streams:
			# if the log stream severity fence is below the log message severity
			if log_stream.severity >= severity:
				self.__post_log_message( log_stream, data, message )
	
	# add a log stream to the logger
	def add_log_stream( self, name, severity = 1, log_file = None ):
		self.log_streams.append( LogStream( name, severity, log_file ))
		
	# construct and return a date/time for right now
	def __date_time( self ):
		dt = datetime.datetime.now()
		dtf = dt.strftime( "%Y-%m-%d %H:%M:%S" )
		dtf = dtf + "." + str( int( dt.microsecond / 1000 ))
		return dtf
	
	def __post_log_message( self, log_stream, data, message ):
		log_file = open( log_stream.log_file, "a" )
		# TODO: frame inspection information for class name and line number
		log_file.write( self.__date_time() + "  " + message + ": " + data + "\n" )
		log_file.close()
