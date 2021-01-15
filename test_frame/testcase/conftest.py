import os
import signal
import subprocess
import shlex
import pytest


@pytest.fixture(scope='class', autouse=True)
def record_vedio():
    cmd = shlex.split("scrcpy --record tmp.mp4")
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    print("hello world")
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)