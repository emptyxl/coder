#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import base64
import urllib.parse
import json

class UI(wx.Frame):
    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title, size=(600, 500))

        # define sizers
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_btn = wx.BoxSizer(wx.VERTICAL)
        self.sizer_text = wx.BoxSizer(wx.VERTICAL)

        # config sizers
        self.sizer.Add(self.sizer_text, 1, wx.ALL | wx.EXPAND)
        self.sizer.Add(self.sizer_btn, 0, wx.EXPAND)

        # config text layout
        self.label_input = wx.StaticText(self, -1, 'Input:')
        self.label_result = wx.StaticText(self, -1, 'Result:')
        self.text_input = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.text_result = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.sizer_text.Add(self.label_input, 0, wx.ALL | wx.EXPAND)
        self.sizer_text.Add(self.text_input, 1, wx.ALL | wx.EXPAND)
        self.sizer_text.Add(self.label_result, 0, wx.ALL | wx.EXPAND)
        self.sizer_text.Add(self.text_result, 1, wx.ALL | wx.EXPAND)

        # config button layout
        button = wx.Button(self, -1, 'Unicode')
        button.Bind(wx.EVT_BUTTON, self.Unicode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'Upper')
        button.Bind(wx.EVT_BUTTON, self.Upper)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'Lower')
        button.Bind(wx.EVT_BUTTON, self.Lower)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'Base64Encode')
        button.Bind(wx.EVT_BUTTON, self.Base64Encode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'Base64Decode')
        button.Bind(wx.EVT_BUTTON, self.Base64Decode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'Base64URLEncode')
        button.Bind(wx.EVT_BUTTON, self.Base64URLEncode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'Base64URLDecode')
        button.Bind(wx.EVT_BUTTON, self.Base64URLDecode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'URLEncode')
        button.Bind(wx.EVT_BUTTON, self.URLEncode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'URLDecode')
        button.Bind(wx.EVT_BUTTON, self.URLDecode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'URLJSONEncode')
        button.Bind(wx.EVT_BUTTON, self.URLJSONEncode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'URLJSONDecode')
        button.Bind(wx.EVT_BUTTON, self.URLJSONDecode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'HTMLEncode')
        button.Bind(wx.EVT_BUTTON, self.HTMLEncode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'HTMLDecode')
        button.Bind(wx.EVT_BUTTON, self.HTMLDecode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'JSStringEncode')
        button.Bind(wx.EVT_BUTTON, self.JSStringEncode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'JSStringDecode')
        button.Bind(wx.EVT_BUTTON, self.JSStringDecode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'UTF7Encode')
        button.Bind(wx.EVT_BUTTON, self.UTF7Encode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'UTF7Decode')
        button.Bind(wx.EVT_BUTTON, self.UTF7Decode)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'MD5')
        button.Bind(wx.EVT_BUTTON, self.MD5)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'SHA1')
        button.Bind(wx.EVT_BUTTON, self.SHA1)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'SHA256')
        button.Bind(wx.EVT_BUTTON, self.SHA256)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'SHA384')
        button.Bind(wx.EVT_BUTTON, self.SHA384)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        button = wx.Button(self, -1, 'SHA512')
        button.Bind(wx.EVT_BUTTON, self.SHA512)
        self.sizer_btn.Add(button, 1, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.sizer)
        self.Show()
        self.Centre()

    def Unicode(self, event):
        content = self.text_input.GetValue()
        result = ' '
        content_list = []
        for word in content:
            content_list.append(str(ord(word)))
        self.text_result.SetValue(result.join(content_list))

    def Upper(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(content.upper())

    def Lower(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(content.lower())

    def Base64Encode(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(base64.b64encode(
            bytes(content, encoding='UTF8')))

    def Base64Decode(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(base64.b64decode(
            bytes(content, encoding='UTF8')))

    def Base64URLEncode(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(base64.urlsafe_b64encode(
            bytes(content, encoding='UTF8')))

    def Base64URLDecode(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(base64.urlsafe_b64decode(
            bytes(content, encoding='UTF8')))

    def URLEncode(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(urllib.parse.quote(content,safe=''))

    def URLDecode(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(urllib.parse.unquote(content))

    def URLJSONEncode(self, event):
        content = self.text_input.GetValue()
        json_content = json.loads(content)
        self.text_result.SetValue(urllib.parse.urlencode(json_content))

    def URLJSONDecode(self, event):
        content = self.text_input.GetValue()
        self.text_result.SetValue(str(urllib.parse.parse_qs(content)))

    def HTMLEncode(self, event):
        pass

    def HTMLDecode(self, event):
        pass

    def JSStringEncode(self, event):
        pass

    def JSStringDecode(self, event):
        pass

    def UTF7Encode(self, event):
        pass

    def UTF7Decode(self, event):
        pass

    def MD5(self, event):
        pass

    def SHA1(self, event):
        pass

    def SHA256(self, event):
        pass

    def SHA384(self, event):
        pass

    def SHA512(self, event):
        pass
