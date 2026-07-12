import pytest
from pkg.response import HttpCode

class TestAppHandler:

    @pytest.mark.parametrize("query", [None, "你是什么模型"])
    def test_completion(self, query, client):
        resq = client.post("/app/completion", json={"query": query})
        assert resq.status_code == 200
        if query is None:
            assert resq.json.get("code") == HttpCode.VALIDATION_ERROR
        else:
            assert resq.json.get("code") == HttpCode.SUCCESS
        print("响应内容", resq.json)