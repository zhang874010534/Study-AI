from pgk.response import HttpCode


class TestAppHandler:
    def test_completion(self, client):
        resq = client.post("/app/completion", json={"query": "你好"})
        assert resq.status_code == 200
        assert resq.json.get("code") == HttpCode.SUCCESS
