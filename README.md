PartyOptimizer
==============

Course work for data structures and algorithms. Given a set of seats and participants, find the best possible seating arrangement. 

Still work in progress.

See wiki for more detailed problem definition (in Finnish only)

How to use
----------

Participants for parties are defined in a json-file, with format

	[
		{"id": uid,
		 "avec": id,
		 "friends": [list of ids],
		 "gender": "F|M"},
		 ...
	]

See ./sampleparticipants for example

main.py takes 4 arguments in following order: source/for/participants.json, sizeOfPopulation, numberOfGenerations, where/to/save.json

For example:

	python main.py ./sampleparticipants/20.json 1000 200 ./seatings/20_1.json  


Size of population defines how many items there are in a generations, while the number of generation is how many generations will be simulated.

Source for participants (1st argument) is required, others are optional.

You can convert the results-json into a html table using:
	
	python renderer/render.py /path/to/source.json /path/to/target.html




