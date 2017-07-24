#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx


btn_text = ['Unicode', 'Upper', 'Lower', 'Base64Encode', 'Base64Decode',
            'Base64URLEncode', 'Base64URLDecode', 'URLEncode', 'URLDecode',
            'HTMLEncode', 'HTMLDecode', 'JSStringEncode', 'JSStringDecode',
            'UTF7Encode', 'UTF7Decode', 'MD5', 'SHA1', 'SHA256', 'SHA384',
            'SHA512']


class MainWindow(wx.Frame):
    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title, size=(600, 450))
        self.sizer_btn = wx.BoxSizer(wx.VERTICAL)

        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        for x in btn_text:
            button = wx.Button(self, -1, x)
            button.Bind(wx.EVT_BUTTON, self.Onclick)
            self.sizer_btn.Add(button, 1, wx.EXPAND)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.text, 1, wx.ALL | wx.EXPAND)
        self.sizer.Add(self.sizer_btn, 0, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.sizer)
        self.Show()
        self.Centre()

    def Onclick(self, event):
        print('point')


if __name__ == '__main__':
    app = wx.App()
    frame = MainWindow(None, "encode-decode")
    app.MainLoop()
