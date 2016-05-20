TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    src/Excalibur.cpp \
    src/interpreter.cpp

HEADERS += \
    src/Excalibur.h \
    src/interpreter.h
