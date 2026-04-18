[app]
# App 名称
title = OvertimeTracker
# 包名
package.name = overtimetracker
package.domain = org.example
# 源代码目录
source.dir = .
# 入口 Python 文件
source.main = main.py
# 版本号
version = 1.0
# 支持的扩展
source.include_exts = py,png,jpg
# 依赖
requirements = python3,kivy
# 屏幕方向
orientation = portrait

[buildozer]
# 如果你用 CI/CD，可以指定 Android API/NDK
android.api = 33
android.ndk = 25b
