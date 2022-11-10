class LogStream:

	name		= None
	severity	= 0
	log_file	= None
	
	# constructor
	def __init__( self, name, severity = 1, log_file = None ):
		self.name = name
		self.severity = severity
		if( log_file == None ):
			# Auto-generate log file name based on provided stream name
			self.log_file = self.name + ".log"
		else:
			self.log_file = log_file
