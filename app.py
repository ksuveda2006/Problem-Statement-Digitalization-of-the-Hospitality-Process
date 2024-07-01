from flask import Flask, render_template, request, send_file
import csv
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        group_file = request.files['group_file']
        hostel_file = request.files['hostel_file']
        
        groups = parse_group_file(group_file)
        hostels = parse_hostel_file(hostel_file)
        
        allocations = allocate_rooms(groups, hostels)
        
        return render_template('result.html', allocations=allocations)
    
    return render_template('mainpage.html')

@app.route('/download_csv')
def download_csv():
    # Generate CSV file from allocations
    # This is a placeholder and needs to be implemented
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Group ID', 'Hostel Name', 'Room Number', 'Members Allocated'])
    # Add allocation data here
    
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, attachment_filename='allocations.csv')

def parse_group_file(file):
    groups = []
    csv_reader = csv.reader(file.stream.read().decode("UTF-8").splitlines())
    next(csv_reader)  # Skip header
    for row in csv_reader:
        group_id, members, gender = row
        groups.append({
            'id': group_id,
            'members': int(members),
            'gender': gender
        })
    return groups

def parse_hostel_file(file):
    hostels = []
    csv_reader = csv.reader(file.stream.read().decode("UTF-8").splitlines())
    next(csv_reader)  # Skip header
    for row in csv_reader:
        hostel_name, room_number, capacity, gender = row
        hostels.append({
            'name': hostel_name,
            'room': room_number,
            'capacity': int(capacity),
            'gender': gender,
            'available': int(capacity)
        })
    return hostels

def allocate_rooms(groups, hostels):
    allocations = []
    for group in groups:
        allocated_members = 0
        for hostel in hostels:
            if hostel['gender'] == group['gender'] and hostel['available'] > 0:
                allocated = min(group['members'] - allocated_members, hostel['available'])
                allocations.append({
                    'group_id': group['id'],
                    'hostel_name': hostel['name'],
                    'room_number': hostel['room'],
                    'members_allocated': allocated
                })
                hostel['available'] -= allocated
                allocated_members += allocated
                if allocated_members == group['members']:
                    break
    return allocations

if __name__ == '__main__':
    app.run(debug=True)