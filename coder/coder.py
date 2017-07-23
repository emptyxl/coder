#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import encryption
from tkinter.scrolledtext import ScrolledText


def callback(en_input, en_result, fn):
    fn()


def GUI():
    """
    start encode/decode GUI.
    """

    # config main interface
    root = Tk()
    root.title('encode-decode')
    root.resizable(False, False)

    
    # config text
    frame_text = Frame(root)

    text_input = Text(frame_text, height=15, width=60,
                      highlightbackground='#000', highlightthickness=1)
    text_input.pack(pady=20)

    text_result = Text(frame_text, height=15, width=60,
                       highlightbackground='#000', highlightthickness=1)
    text_result.pack(pady=20)
    frame_text.pack(side=LEFT, padx=10, pady=20)

    # config button
    # Unicode
    frame_btn = Frame(root)
    btn_Unicode = Button(frame_btn, text='Unicode', command=lambda: callback(
        text_input, text_result, encryption.Unicode), width=13)
    btn_Unicode.pack(anchor='w')

    # upper
    btn_upper = Button(frame_btn, text='Upper', command=lambda: callback(
        text_input, text_result, encryption.upper), width=13)
    btn_upper.pack()

    # lower
    btn_lower = Button(frame_btn, text='Lower', command=lambda: callback(
        text_input, text_result, encryption.lower), width=13)
    btn_lower.pack()

    # Base64
    btn_Base64_encode = Button(frame_btn, text='Base64Encode', command=lambda: callback(
        text_input, text_result, encryption.Base64_encode),width=13)
    btn_Base64_encode.pack()
    btn_Base64_decode = Button(frame_btn, text='Base64Decode', command=lambda: callback(
        text_input, text_result, encryption.Base64_decode),width=13)
    btn_Base64_decode.pack()

    # Base64URL
    btn_Base64URL_encode = Button(frame_btn, text='Base64URLEncode', command=lambda: callback(
        text_input, text_result, encryption.Base64URL_encode),width=13)
    btn_Base64URL_encode.pack()
    btn_Base64URL_decode = Button(frame_btn, text='Base64URLDecode', command=lambda: callback(
        text_input, text_result, encryption.Base64URL_decode),width=13)
    btn_Base64URL_decode.pack()

    # URL
    btn_URL_encode = Button(frame_btn, text='URLEncode', command=lambda: callback(
        text_input, text_result, encryption.URL_encode),width=13)
    btn_URL_encode.pack()
    btn_URL_decode = Button(frame_btn, text='URLDecode', command=lambda: callback(
        text_input, text_result, encryption.URL_decode),width=13)
    btn_URL_decode.pack()

    # HTML
    btn_HTML_encode = Button(frame_btn, text='HTMLEncode', command=lambda: callback(
        text_input, text_result, encryption.HTML_encode),width=13)
    btn_HTML_encode.pack()
    btn_HTML_decode = Button(frame_btn, text='HTMLDecode', command=lambda: callback(
        text_input, text_result, encryption.HTML_decode),width=13)
    btn_HTML_decode.pack()

    # JSString
    btn_JSString_encode = Button(frame_btn, text='JSStringEncode', command=lambda: callback(
        text_input, text_result, encryption.JSString_encode),width=13)
    btn_JSString_encode.pack()
    btn_JSString_decode = Button(frame_btn, text='JSStringDecode', command=lambda: callback(
        text_input, text_result, encryption.JSString_decode),width=13)
    btn_JSString_decode.pack()

    # UTF7
    btn_UTF7_encode = Button(frame_btn, text='UTF7Encode', command=lambda: callback(
        text_input, text_result, encryption.UTF7_encode),width=13)
    btn_UTF7_encode.pack()
    btn_UTF7_decode = Button(frame_btn, text='UTF7Decode', command=lambda: callback(
        text_input, text_result, encryption.UTF7_decode),width=13)
    btn_UTF7_decode.pack()

    # MD5
    btn_MD5 = Button(frame_btn, text='MD5', command=lambda: callback(
        text_input, text_result, encryption.MD5),width=13)
    btn_MD5.pack()

    # SHA1
    btn_SHA1 = Button(frame_btn, text='SHA1', command=lambda: callback(
        text_input, text_result, encryption.SHA1),width=13)
    btn_SHA1.pack()

    # SHA256
    btn_SHA256 = Button(frame_btn, text='SHA256', command=lambda: callback(
        text_input, text_result, encryption.SHA256),width=13)
    btn_SHA256.pack()

    # SHA384
    btn_SHA384 = Button(frame_btn, text='SHA384', command=lambda: callback(
        text_input, text_result, encryption.SHA384),width=13)
    btn_SHA384.pack()

    # SHA512
    btn_SHA512 = Button(frame_btn, text='SHA512', command=lambda: callback(
        text_input, text_result, encryption.SHA512),width=13)
    btn_SHA512.pack()

    frame_btn.pack(side=LEFT, padx=20, pady=40, anchor='n')
    root.mainloop()


if __name__ == '__main__':
    GUI()
