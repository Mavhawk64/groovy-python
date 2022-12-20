from scamp import *

def readMuseScoreJSON(filename):
	# read the json file
	import json
	with open("output/" + filename) as f:
		data = json.load(f)

		output = {"measure":[]}

		measures = data['score-partwise']['part']['measure']
		for measure in measures:
			output['measure'].append({"@number":int(measure['@number']),"note":[]})
			notes = measure['note']
			x = []
			for note in notes:
				if '@default-x' in note and note['@default-x'] not in x:
					x.append(note['@default-x'])
				# get the index of the note
				num = x.index(note['@default-x'])
				val = None
				if 'pitch' in note:
					alter = 0
					if 'alter' in note['pitch']:
						alter = int(note['pitch']['alter'])
					val = get_pitch(note['pitch']['step'] + note['pitch']['octave'],alter)
				output['measure'][-1]['note'].append({'id':num,'pitch':val,'duration':float(note['duration'])/2,'staff':int(note['staff'])})
		# dump output to output/tester.json with indent of 4
		with open('output/tester.json', 'w') as outfile:
			json.dump(output, outfile, indent=4)
		return output
	
	return None

def create_pianos(song):
	# Get a list of all the notes' id's and find the id in that measure that occurs the most
	# This will be the number of pianos
	# Create a list of pianos
	idsm = []
	for measure in song['measure']:
		notes = measure['note']
		ids = {}
		for note in notes:
			if note['id'] in ids:
				ids[note['id']] += 1
			else:
				ids[note['id']] = 1
		# get the largest id's count
		idsm.append(max(ids.values()))
	return max(idsm)

def get_pitch(pitch,alter):
	# Define the pitch dictionary
	pitch_dict = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}

	# Get the pitch letter and octave
	pitch_letter = pitch[0]
	octave = int(pitch[1])

	# Get the pitch number
	pitch_number = pitch_dict[pitch_letter] + (octave + 1) * 12

	# Add the alter
	pitch_number += alter
	return pitch_number

# print(get_pitch('F4',1))
# exit()

s = Session()

# create piano, cello, and clarinet
# piano = s.new_part("piano")
# cello = s.new_part("cello",clef_preference="treble")
# clarinet = s.new_part("clarinet")

# piano1 = s.new_part("piano")
# piano2 = s.new_part("piano")
# piano3 = s.new_part("piano")
# piano4 = s.new_part("piano",clef_preference="bass")
# piano5 = s.new_part("piano",clef_preference="bass")

# the pitches are as follows:
# C4 = 60
# D4 = 62
# E4 = 64
# ...

# melody = [(67,1.5),(66,0.5),(68,1),(70,0.5),(71,1),(69,1.5)]
# melody = [(60,1),(62,1),(64,1),(65,1),(67,1),(69,1),(71,1),(72,1),(71,1),(69,1),(67,1),(65,1),(64,1),(62,1),(60,1)]

song = readMuseScoreJSON('Mii Channel.json')

pianos = create_pianos(song)

print(pianos)

exit()

s.start_transcribing()

# play the melody on both parts simultaneously
for i in range(0,len(song['measure'])):
	pass

s.stop_transcribing().to_score(time_signature="3/4").show()