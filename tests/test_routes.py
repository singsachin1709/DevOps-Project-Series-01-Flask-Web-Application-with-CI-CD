from app.routes import app

client = app.test_client()

def test_health_route():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'UP'

def test_journey_route():
    response = client.get('/journey')
    assert response.status_code == 200
    assert 'name' in response.json
    assert isinstance(response.json['milestones'], list)

def test_tools_route():
    response = client.get('/tools')
    assert response.status_code == 200
    assert 'CI/CD' in response.json
    assert 'Containers' in response.json

def test_projects_route():
    response = client.get('/projects')
    assert response.status_code == 200
    assert 'active_projects' in response.json

def test_certifications_route():
    response = client.get('/certifications')
    assert response.status_code == 200
    assert 'in_progress' in response.json

def test_mentorship_route():
    response = client.get('/mentorship')
    assert response.status_code == 200
    assert 'mentor' in response.json

def test_resources_route():
    response = client.get('/resources')
    assert response.status_code == 200
    assert 'docs' in response.json

def test_contact_route():
    response = client.get('/contact')
    assert response.status_code == 200
    assert response.json['email'] == 'singsachin348@gmail.com'
