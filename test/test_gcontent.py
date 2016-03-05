from __future__ import absolute_import
import responses
import os
from gcontent import GContent
from . import MockResponse, PROJECT_ROOT, path


class GContentMock(GContent):
    _name_file = path.join(PROJECT_ROOT, "content_test.json")


class GContentDefault(GContentMock):
    _name_file = path.join(PROJECT_ROOT, "content.json.default")


@responses.activate
def test_build_blog_content():
    body = MockResponse("index.html")
    responses.add(
        responses.GET,
        "http://blog.henriquelopes.com.br",
        body=str(body)
    )
    gcontent = GContentDefault()
    assert gcontent.content['posts']['content'] is None
    gcontent.run()

    assert gcontent.content['posts']['content'] is not None
    assert gcontent.content['posts']['content'][1]["label"] == "Como criar uma api com nodejs e express"
    assert len(gcontent.content['posts']['content']) == 5


@responses.activate
def test_build_blog_content_error():
    responses.add(
        responses.GET,
        "http://blog.henriquelopes.com.br",
        status=500
    )
    gcontent = GContent()
    assert gcontent.build_blog_content() is False


@responses.activate
def test_salve_content():
    body = MockResponse("index.html")
    responses.add(
        responses.GET,
        "http://blog.henriquelopes.com.br",
        body=str(body)
    )
    gcontent = GContentMock()
    before_status = os.stat(GContentMock._name_file)
    gcontent.salve()
    after_status = os.stat(GContentMock._name_file)
    assert before_status.st_mtime != after_status.st_mtime
