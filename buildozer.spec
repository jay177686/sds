[app]
title = OvertimeTracker
package.name = overtimetracker
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

# 🔥 防止编译卡UI
log_level = 2

# =========================
# Android 配置（关键）
# =========================
[buildozer]

android.api = 33
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

# 🔥 关键：禁止 root 提示
warn_on_root = 0

# 🔥 防止交互卡死
p4a.branch = master

# 🔥 推荐稳定架构
android.archs = arm64-v8a, armeabi-v7a

# 🔥 关闭不必要交互
android.accept_sdk_license = True
