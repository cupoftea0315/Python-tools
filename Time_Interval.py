import time
import tkinter as tk
from tkinter import messagebox


def main():
    # 设置第一个窗口实例
    window1 = tk.Tk()
    window1.title('Time Interval')
    window1.geometry('300x200')

    # 设置引言demo
    l1 = tk.Label(window1, text='Current time:', font=('Helvetica', 15))
    l1.place(x=5, y=10)

    def time_now():
        global seconds_now  # 申明全局变量seconds_now
        seconds_now = time.time()  # 取系统当前时间戳
        lt = time.localtime(seconds_now)  # 根据参数的秒数转换为表示本地时间的时间tuple
        time1 = []
        time2 = '%04d/%02d/%02d\n%02d:%02d:%02d' % (lt[0], lt[1], lt[2], lt[3], lt[4], lt[5])  # 将tuple编译为固定格式

        # 设置时钟demo
        if time1 != time2:
            time1 = time2
            l1_2 = tk.Label(window1, text=time1, font=('Helvetica', 20))
            l1_2.config(text=time2)
            l1_2.place(x=80, y=50)
            l1_2.after(200, time_now)  # 使调出的时间能够流动显示(在1ms后再次调用函数time_now）

    time_now()

    def input_time():
        # 设置第二个窗口实例
        window2 = tk.Tk()
        window2.title('Input date')
        window2.geometry('300x120')

        # 设置单位demo
        l2_1 = tk.Label(window2, text='(year)', font=('Helvetica', 10))
        l2_1.place(x=95, y=20)
        l2_2 = tk.Label(window2, text='(month)', font=('Helvetica', 10))
        l2_2.place(x=165, y=20)
        l2_3 = tk.Label(window2, text='(day)', font=('Helvetica', 10))
        l2_3.place(x=245, y=20)
        l2_4 = tk.Label(window2, text='Effective date [1970/1/2-3001/1/1]', font=('Helvetica', 10))
        l2_4.place(x=45, y=50)

        # 设置用户填写时间数据的空格（Entry 控件允许用户输入或显示一行文字）
        year = tk.Entry(window2, text=None, font=('Helvetica', 15), width=4)
        month = tk.Entry(window2, text=None, font=('Helvetica', 15), width=2)
        day = tk.Entry(window2, text=None, font=('Helvetica', 15), width=2)
        year.place(x=45, y=20)
        month.place(x=135, y=20)
        day.place(x=215, y=20)

        def get_time():
            # 得到写入时间的时间戳
            try:
                y = int(year.get())
                m = int(month.get())
                d = int(day.get())
                lt_ = time.strptime(f'{y} {m} {d}', '%Y %m %d')
                seconds_get = time.mktime(lt_)
            except BaseException:
                tk.messagebox.showerror(message='Input error！')
            else:
                window2.withdraw()

            # 利用秒差计算得出相差的年月日
            seconds_lasting = seconds_get - seconds_now

            day_lasting = abs(seconds_lasting) // 86400
            month_lasting = 0
            year_lasting = 0
            days = day_lasting

            if day_lasting > 356:
                year_lasting = day_lasting // 365
                day_lasting -= year_lasting * 365
                if day_lasting > 30:
                    month_lasting = day_lasting // 30
                    day_lasting -= month_lasting * 30
            elif day_lasting > 30:
                year_lasting = 0
                month_lasting = day_lasting // 30
                day_lasting -= month_lasting * 30
            else:
                year_lasting, month_lasting = 0, 0

            # 分辨过去和未来
            string1 = 'Query date is the upcoming'
            string2 = 'Query date is the preceding'
            if seconds_lasting > 0:
                prompt = string1
                days += 1
                day_lasting += 1
            else:
                prompt = string2

            # 最后结果的弹窗messagebox
            tk.messagebox.showinfo(
                message='%s %d days\nAlmost %d year, %d month and %d day' % (prompt, days, year_lasting, month_lasting, day_lasting))

        button2 = tk.Button(window2, text='Search result', font=('Helvetica', 15), command=get_time)
        button2.place(x=75, y=75)

        window2.mainloop()

    button1 = tk.Button(window1, text='Enter the query date', font=('Helvetica', 15), command=input_time)
    button1.place(x=50, y=125)

    window1.mainloop()


if __name__ == '__main__':
    main()
