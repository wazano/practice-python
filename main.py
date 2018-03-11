import tkinter

#ウィンドウの作成
root = tkinter.Tk()
root.title("テストプログラム")
root.minsize(640, 480)

#画像表示
#背景の表示と表示する背景の大きさの指定
canvas = tkinter.Canvas(bg="black", width=640, height=480)

#背景の位置の指定
canvas.place(x=0, y=0)

#メインループ
root.mainloop()