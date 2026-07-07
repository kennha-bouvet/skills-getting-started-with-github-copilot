from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities for deterministic tests."""
    original = deepcopy(activities)

    yield

    activities.clear()
    activities.update(deepcopy(original))


@pytest.fixture
def client():
    """Provide a FastAPI test client."""
    return TestClient(app)