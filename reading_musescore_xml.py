import json
import xmltodict

# Parse the xml file
with open('output/Mii Channel.xml') as fd:
    doc = xmltodict.parse(fd.read())
    # write the json file with indent=4
    with open('output/Mii Channel.json', 'w') as f:
        json.dump(doc, f, indent=4)








# import xml.etree.ElementTree as ET
# import json

# # Parse the XML file
# tree = ET.parse('output/Mii Channel.xml')
# root = tree.getroot()

# # score-partwise.part[].measure[].note[].pitch.step & score-partwise.part[].measure[].note[].pitch.octave & score-partwise.part[].measure[].note[].duration


# # Find the <part> element containing the notes
# parts = root.findall('.//part')

# my_parts = [] # convert to a list of dictionaries

# for part in parts:
#   # print(part.attrib)
#   my_part = {}
#   my_part['id'] = part.attrib['id']
#   my_part['measures'] = []
#   for measure in part.findall('.//measure'):
#     # print(measure.attrib)
#     my_measure = {}
#     my_measure['number'] = measure.attrib['number']
#     my_measure['attributes'] = {}
#     my_measure['attributes']['key'] = {}
#     my_measure['attributes']['key']['fifths'] = None
#     if measure.find('.//attributes/key/fifths') is not None:
#       my_measure['attributes']['key']['fifths'] = int(measure.find('.//attributes/key/fifths').text)
#     my_measure['notes'] = []
#     for note in measure.findall('.//note'):
#       # print(note.attrib)
#       my_note = {}
#       my_note['note_attrib'] = note.attrib # Denotes when to change to the next note
#       my_note['note_attrib']['default-x'] = float(my_note['note_attrib']['default-x'])
#       my_note['note_attrib']['default-y'] = float(my_note['note_attrib']['default-y'])
#       my_note['pitch'] = None
#       if note.find('.//step') is not None and note.find('.//octave') is not None:
#         my_note['pitch'] = note.find('.//step').text + note.find('.//octave').text
#       my_note['alter'] = 0
#       if note.find('.//alter') is not None:
#         my_note['alter'] = int(note.find('.//alter').text)
#       my_note['duration'] = float(note.find('.//duration').text) / 2
#       my_note['staff'] = int(note.find('.//staff').text)
#       my_measure['notes'].append(my_note)
#     my_part['measures'].append(my_measure)
#   my_parts.append(my_part)

# # Now go through my_parts and distinguish between the different notes --> i.e. note_attrib
# # There are 4 beats per measure, so we need to find the first x amount of notes depending on their duration
# #  0.25 = 1/16th note, 0.5 = 1/8th note, 1 = 1/4 note, 2 = 1/2 note, 4 = 1 whole note, and dotted notes are somewhere in between



# print(my_parts)

# # dump the parts to the Mii Channel.json file with indentation of 2 spaces
# with open('output/Mii Channel.json', 'w') as outfile:
#   json.dump(my_parts, outfile, indent=2)


# # for part in parts:
# #   # print(part.attrib)
# #   for measure in part.findall('.//measure'):
# #     # print(measure.attrib)
# #     for note in measure.findall('.//note'):
# #       # print(note.attrib)
# #       for pitch in note.findall('.//pitch'):
# #         # print(pitch.attrib)
# #         for step in pitch.findall('.//step'):
# #           # print(step.attrib)
# #           print(step.text)
# #         for octave in pitch.findall('.//octave'):
# #           # print(octave.attrib)
# #           print(octave.text)
# #       for duration in note.findall('.//duration'):
# #         # print(duration.attrib)
# #         print(duration.text)

# # Initialize an empty list to store the notes
# notes = []

# # Iterate through each <note> element in the <part>
# # for note in part.findall('.//note'):
# #   # Find the <step> and <octave> elements
# #   step_elem = note.find('.//step')
# #   octave_elem = note.find('.//octave')

# #   # Extract the pitch by combining the step and octave
# #   pitch = step_elem.text + octave_elem.text

# #   # Find the <duration> element
# #   duration_elem = note.find('.//duration')

# #   # Convert the duration value to a float and divide by 2
# #   duration = float(duration_elem.text) / 2

# #   # Append the pitch and duration as a tuple to the notes list
# #   notes.append((pitch, duration))

# # Print the list of notes
# print(notes)