import json
import os


def test_manifest_structure():
    manifest_path = "manifest.json"
    assert os.path.exists(manifest_path)

    with open(manifest_path, "r") as f:
        data = json.load(f)

    assert "project_name" in data
    assert "tools" in data
    assert isinstance(data["tools"], list)

    for tool in data["tools"]:
        assert "name" in tool
        assert "repo" in tool
        assert "asset_pattern" in tool
        assert "target_dir" in tool
