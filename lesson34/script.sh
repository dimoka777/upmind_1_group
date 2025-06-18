##!/bin/bash
#
##for FILE in */*.txt; do
##  echo "Файл: $FILE"
##done
#
##count=1
##while [ $count -le 5 ]; do
##  echo "Счётчик: $count"
##  count=$((count + 1))
##done
##
##say_hello() {
##  echo "Привет, $1!"
##}
##say_hello "Анна"
##
##echo "Привет, $2!"
##echo "Вы передали $# аргументов: $@"
#
##mkdir backup
##if [ $? -ne 0 ]; then
##  echo "Ошибка при создании папки" >> error.log
##fi
#
##read -p "Введите имя: " username
##echo "Привет, $username!"
#
#
##read -p "Выберите язык (en/ru): " lang
##case $lang in
##  en) echo "Hello!" ;;
##  ru) echo "Привет!" ;;
##  *) echo "Язык не распознан" ;;
##esac
#
##trap "echo Прерывание!" SIGINT
##while true; do sleep 1; done
#
#
##if [ $# -eq 0 ]; then
##  echo "Нет аргументов"
##  exit 1
##fi
##echo "Argument 1 is" $1
#
#
#
##1. Напишите for-цикл, который выводит числа от 1 до 10.
#for i in 1 2 3 4 5 6 7 8 9 10; do
#    echo $i
#done
#
##2. Используйте while-цикл для вывода чётных чисел до 20.
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
  if [ $((i % 2)) -eq 0 ]; then
    echo $i
  fi
done

