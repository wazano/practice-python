import tkinter

#ウィンドウの作成
root = tkinter.Tk()
root.title("テストプログラム")
root.minsize(640, 480)
root.option_add("*font", ["MS Pゴシック", 22])

#画像表示
#背景の表示と表示する背景の大きさの指定
canvas = tkinter.Canvas(bg="black", width=640, height=480)

#背景の位置の指定
canvas.place(x=0, y=0)

img = tkinter.PhotoImage(file="img3/chap3-back.png")
canvas.create_image(320, 240, image=img)

#テキストボックスを表示
entry = tkinter.Entry(width=12, bd=4)
entry.place(x=50, y=133)

#質問ボタンを表示
askbutton = tkinter.Button(text="聞く")
askbutton.place(x=260, y=125)

#テキストを表示
question = tkinter.Label(text="知りたいのは何分かな?", bg="white")
question.place(x=100, y=40)

#答えを表示
answer = tkinter.Label(text="...", bg="white")
answer.place(x=115, y=235)

#メインループ
root.mainloop()