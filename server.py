from flask import Flask, render_template, request, jsonify, url_for, redirect
import re
app = Flask(__name__)

# Dummy show data
shows = [
  {"id": "SWiUqDM3dGI", "artist": "Parfait", "location": "London", "year": 2021, "genres": ["Techno"],
   "description": "Parfait, real name Naïla Guiguet is a French techno producer, DJ and co-founder of Possession. She is known for her dark and energetic sets, where she plays mainly hard techno. Parfait first started out mixing at alternative LGBT+ community parties."},
  {"id": "djGlyTcW30Q", "artist": "Minna-no-kimochi (みんなのきもち)", "location": "Tokyo", "year": 2023, "genres": ["Trance"],
   "description": "A long, long-awaited collaboration with rising superstar Tohji, & his party series u-ha. Featuring: Peterparker69, nasthug, JUMADIBA, E.O.U & Minna-no-kimochi (みんなのきもち)."},
  {"id": "r6p1mQxOhLU", "artist": "Yung Sherman", "location": "Stockholm", "year": 2023, "genres": ["Techno", "Gabber", "Drum and Bass"],
   "description": "Description of Kareem Ali's set at Boiler Room Festival New York 2021."},
  {"id": "2o1oFqchxbY", "artist": "Varg²™", "location": "Stockholm", "year": 2023, "genres": ["Club", "Techno", "Gabber"],
    "description": "Description of Kareem Ali's set at Boiler Room Festival New York 2021."},
  {"id": "vc35GjGCVHY", "artist": "Kenny Beats", "location": "Barcelona", "year": 2022, "genres": ["Hip-Hop", "Rap"],
    "description": "Description of Kareem Ali's set at Boiler Room Festival New York 2021."},
  {"id": "c0-hvjV2A5Y", "artist": "Fred again..", "location": "London", "year": 2021, "genres": ["Bass", "House", "Rap"],
    "description": "Description of Kareem Ali's set at Boiler Room Festival New York 2021."},
  {"id": "pZhUS_q4jkc", "artist": "Brutalismus 3000", "location": "London", "year": 2021, "genres": ["Techno" , "Hardcore"],
    "description": "Description of Kareem Ali's set at Boiler Room Festival New York 2021."},
  {"id": "-5EQIiabJvk", "artist": "Kaytranada", "location": "Montreal", "year": 2013, "genres": ["Bass", "Club", "Rap"],
    "description": "Description of Kareem Ali's set at Boiler Room Festival New York 2021."},
  {"id": "yuY0-DmqaJ8", "artist": "foreigner", "location": "DC", "year": 2023, "genres": ["Dancehall"],
    "description": "Description of Kareem Ali's set at Boiler Room Festival New York 2021."},
]

# Generate unique genre list based on shows data
genres = list(set(genre for show in shows for genre in show['genres']))

@app.route('/')
def index():
  return render_template('index.html', shows=shows[:3], genres=genres)

@app.route('/search')
def search():
  query = request.args.get('q', '').strip().lower()
  if query:
    results = [show for show in shows
               if query in show['artist'].lower()
               or query in show['location'].lower()
               or any(query in genre.lower() for genre in show['genres'])
               or query in str(show['year'])]
    return render_template('search.html', query=query, results=results)
  else:
    return render_template('search.html', query=query, results=[])

@app.route('/view/<id>')
def view(id):
  show = next((show for show in shows if show['id'] == id), None)
  if show:
    return render_template('view.html', show=show)
  else:
    return "Show not found"

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
  show = next((show for show in shows if show['id'] == id), None)
  if not show:
    return jsonify({'error': 'Show not found'}), 404

  if request.method == 'POST':
    show['artist'] = request.form['artist']
    show['location'] = request.form['location']
    show['description'] = request.form['description']
    show['genres'] = request.form.getlist('genre[]')
    return jsonify({'id': id})

  return render_template('edit.html', show=show)

@app.route('/add', methods=['GET', 'POST'])
def add():
  if request.method == 'GET':
    return render_template('add.html')
  # Get form data from AJAX request
  youtube_url = request.form.get('youtubeUrl')
  artist = request.form.get('artist')
  location = request.form.get('location')
  year = request.form.get('year')
  description = request.form.get('description')
  genres = request.form.getlist('genre[]')

  # Validate form data
  if not (youtube_url and artist and location and year):
    return jsonify({'error': 'All fields are required'}), 400

  # Extract ID from YouTube URL
  video_id = extract_video_id(youtube_url)

  # Validate video ID
  if not video_id:
    return jsonify({'error': 'Invalid YouTube URL'}), 400

  # Convert year to integer
  try:
    year = int(year)
  except ValueError:
    return jsonify({'error': 'Year must be a number'}), 400

  # Add new entry to shows dictionary
  new_show = {
    "id": video_id,
    "artist": artist,
    "location": location,
    "year": year,
    "genres": genres,
    "description": description
  }
  shows.append(new_show)

  return jsonify({'message': 'New item successfully created', 'id': video_id})

def extract_video_id(youtube_url):
  # Regex pattern to extract video ID from YouTube URL
  pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
  match = re.search(pattern, youtube_url)
  if match:
    return match.group(1)
  return None

if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(debug=True)
