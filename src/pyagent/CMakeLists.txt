install(DIRECTORY
	./
	DESTINATION dist-packages/pyagent
	COMPONENT ha
	PATTERN *.py
	PATTERN *.pyc EXCLUDE
	PATTERN *.xml EXCLUDE
)
 
