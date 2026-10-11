import app


class MockResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        pass

    def json(self):
        return self.payload


# Checks that a city name shorter than two characters is rejected.
def test_weather_rejects_short_city():
    client = app.app.test_client()

    response = client.get("/weather?city=A")

    assert response.status_code == 400


# Checks that an unmatched city returns a not-found response.
def test_weather_returns_not_found_for_unknown_city(monkeypatch):
    monkeypatch.setattr(
        app.requests,
        "get",
        lambda *args, **kwargs: MockResponse({"results": []}),
    )
    client = app.app.test_client()

    response = client.get("/weather?city=Atlantis")

    assert response.status_code == 404


# Checks that a successful lookup returns the expected weather fields.
def test_weather_returns_current_conditions(monkeypatch):
    responses = iter(
        [
            MockResponse(
                {
                    "results": [
                        {"name": "London", "country": "United Kingdom", "latitude": 51.5, "longitude": -0.1}
                    ]
                }
            ),
            MockResponse(
                {
                    "current": {
                        "temperature_2m": 18.5,
                        "apparent_temperature": 17.9,
                        "relative_humidity_2m": 65,
                        "wind_speed_10m": 12.3,
                        "weather_code": 0,
                    }
                }
            ),
        ]
    )
    monkeypatch.setattr(app.requests, "get", lambda *args, **kwargs: next(responses))
    client = app.app.test_client()

    response = client.get("/weather?city=London")

    assert response.status_code == 200
    data = response.get_json()
    assert data["city"] == "London"
    assert data["temperature"] == 18.5
    assert data["description"] == "Clear sky"