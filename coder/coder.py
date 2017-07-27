#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
from UI import UI


def main():
    app = wx.App()
    UI(None, "encode-decode")
    app.MainLoop()


if __name__ == '__main__':
    main()
