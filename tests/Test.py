#!/usr/bin/env python
from pathlib import Path
import PyLivestream

rdir = Path(__file__).parent

inifn = rdir / 'test.ini'

def test_screenshare():
    PyLivestream.Screenshare(inifn,'periscope')

    PyLivestream.Screenshare(inifn,'youtube')

    PyLivestream.Screenshare(inifn,'facebook')


def test_webcam():
    PyLivestream.Webcam(inifn,'periscope')

    PyLivestream.Webcam(inifn,'youtube')

    PyLivestream.Webcam(inifn,'facebook')


def test_loop():
    PyLivestream.Loop(inifn,'periscope')

    PyLivestream.Loop(inifn,'youtube')

    PyLivestream.Loop(inifn,'facebook')

if __name__ == '__main__':
    test_screenshare()

    test_webcam()