from src.app import activities


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_names = set(activities.keys())

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert set(payload.keys()) == expected_activity_names


def test_get_activities_includes_expected_fields(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert activity_name in payload
    assert set(payload[activity_name].keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }