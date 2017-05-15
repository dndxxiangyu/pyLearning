#  python的进程和线程
'''
单核cpu是如何执行多任务：操作系统轮流让各个人物交替执行，任务1执行0.01s，切换到任务2执行0.01s，这样反复下去表面上看去每个人物都是交替执行的
但是由于cpu的执行速度太快，所以人为感觉上所有人物都在同事执行一样

对于操作系统来说：
一个任务就是一个进程，比如浏览器进程，记事本进程。比如word进程可以同事打字、拼写检查、打印等，在一个进程内部要同事干多件事，就需要同事运行多个子任务，我们把进程内的这些子任务称为线程

为了要同时执行多个任务，有两种解决方案：
- 启动多个进程，每个进程虽然只有一个线程，但是每个进程可以可以一块执行多个任务。
- 启动一个进程，在一个进程内部启动多个线程，这样多个线程也可以一块执行多个任务。
- 多个进程+多个线程，这样同时执行的任务就更多了，但是很少采用


试想一下：为了看电影，就必须一个线程播放视频，另一个线程播放音频

'''

'''
多进程：unix/linux提供了一个fork系统调用，操作系统自动把当前进程(称为父进程)复制了一份(称为子进程)，然后分别在父进程和子进程内返回。
子进程用于返回0，而父进程返回子进程的id，理由是：一个父进程可以fork出很多子进程，所以父进程要记下每个子进程的id，而子进程只需要调用getppid就可以拿到父进程的id

fork调用，返回两次
'''
import os
print('process (%s) start....' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('i am child process (%s) and my parent is (%s)' % (os.getpid(), os.getppid()))
# else:
#     print('i (%s) just created a child process (%s)' % (os.getpid(), pid))
# 注：在fork之前，都是在父进程中执行的
'''
result:
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
'''

from multiprocessing import Process
import os
def run_proc(name):
    print('run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print("child process will start.")
    p.start()
    p.join()
    print("child process ends")

#在thread和process中，应当优先选择Process，因为process更稳定，而且process可以分布到多台机器上，而thread最多只能分布到同一台机器的多个cpu上，


from datetime import datetime
now = datetime.now()
print(now)
