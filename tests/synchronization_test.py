import os
import shutil
import pytest
from tempfile import TemporaryDirectory
from pathlib import Path
from src.synchronization import sync_copy, sync_remove

@pytest.fixture(scope="module")
def tmp_dir():
    with TemporaryDirectory() as tmp:
        yield Path(tmp)

def test_sync_copy(tmp_dir):
    source_path = tmp_dir / 'src'
    source_path.mkdir()
    (source_path / 'file1.txt').write_text('hello')
    (source_path / 'file2.txt').write_text('world')
    replica_path = tmp_dir / 'replica'

    sync_copy(str(source_path), str(replica_path), test_mode=True)

    assert (replica_path / 'file1.txt').read_text() == 'hello'
    assert (replica_path / 'file2.txt').read_text() == 'world'

    sync_copy(str(source_path), str(replica_path), test_mode=True)

    assert (replica_path / 'file1.txt').read_text() == 'hello'
    assert (replica_path / 'file2.txt').read_text() == 'world'

def test_sync_remove(tmp_dir):
    source_path = "./test_dir/source"
    replica_path = "./test_dir/replica"
    os.makedirs(source_path)
    os.makedirs(replica_path)
    with open(os.path.join(source_path, "file1.txt"), "w") as f:
        f.write("test")
    with open(os.path.join(replica_path, "file1.txt"), "w") as f:
        f.write("test")
    with open(os.path.join(replica_path, "file2.txt"), "w") as f:
        f.write("test")
    
    sync_remove(source_path, replica_path, test_mode=True)

    assert not os.path.exists(os.path.join(replica_path, "file2.txt"))
    shutil.rmtree('./test_dir')