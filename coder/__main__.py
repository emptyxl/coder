#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import coder.UI

app = wx.App()
coder.UI.UI(None, "encode-decode")
app.MainLoop()
