{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "577da9ce",
   "metadata": {},
   "source": [
    "- There are 5280 feet in a mile. write a python statement that calculates and print the numbers of feet in 13 miles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0eb2545a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no of feet in 13 mile:  68640\n"
     ]
    }
   ],
   "source": [
    "a=5280\n",
    "b=13*a\n",
    "print('no of feet in 13 mile: ',b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a01194d",
   "metadata": {},
   "source": [
    "- write a python statement that calculates and prints the number of seconds in 7hr, 21 min, 31 sec"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "37c2f6f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no of sec in 7hr 21min and 37sec are:  26497\n"
     ]
    }
   ],
   "source": [
    "a=60*60\n",
    "b=60\n",
    "c=7*a+21*b+37\n",
    "print('no of sec in 7hr 21min and 37sec are: ',c)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d88dfef",
   "metadata": {},
   "source": [
    "- The perimeter of a rectangle is 2w+2h, where w and h are the lengths of\n",
    "its sides. Write a Python statement that calculates and prints the length in inches of\n",
    "the perimeter of a rectangle with sides of length 4 and 7 inches."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0d985586",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "perimeter of given rectangle is:  22\n"
     ]
    }
   ],
   "source": [
    "w=4\n",
    "h=7\n",
    "p=2*(w+h)\n",
    "print('perimeter of given rectangle is: ' , p)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "949a07f6",
   "metadata": {},
   "source": [
    "- The circumference of a circle is 2πr where r is the radius of the circle.\n",
    "Write a Python statement that calculates and prints the circumference in inches of a\n",
    "circle whose radius is 8 inches. Assume that the constant π=3.14."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f5d3f50b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "perimeter of circle is:  50.24\n"
     ]
    }
   ],
   "source": [
    "r=8\n",
    "p=2*3.14*r\n",
    "print('perimeter of circle is: ' , p)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2bad090",
   "metadata": {},
   "source": [
    "- Given p dollars, the future value of this money when compounded\n",
    "yearly at a rate of r percent interest for y years is p(1+0.01r)y. Write a Python\n",
    "statement that calculates and prints the value of 1000 dollars compounded at 7\n",
    "percent interest for 10 years."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6159a37e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "final value will be: 10700.0\n"
     ]
    }
   ],
   "source": [
    "p=1000\n",
    "r=7\n",
    "y=10\n",
    "ci=p*(1+0.01*r)*y\n",
    "print('final value will be:', ci)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6794b85",
   "metadata": {},
   "source": [
    "- Write a Python expression that combines the string \"Joe Warren is 52\n",
    "years old.\" from the string \"Joe Warren\" and the number 52 and then prints the result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d630d1dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "joe warren is 52 year's old\n"
     ]
    }
   ],
   "source": [
    "name= 'joe warren'\n",
    "age=52\n",
    "print(name , 'is' , age , \"year's old\" )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "61463e57",
   "metadata": {},
   "source": [
    "- Write a single Python statement that combines the three strings \"My\n",
    "name is\", \"Joe\" and \"Warren\" (plus a couple of other small strings) into one larger\n",
    "string \"My name is Joe Warren.\" and prints the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b22d0fc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is joe warren\n"
     ]
    }
   ],
   "source": [
    "print('my name is','joe','warren') "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b62acad",
   "metadata": {},
   "source": [
    "- The distance between two points (x0,y0) and (x1,y1) is\n",
    "(x0−x1)2+(y0−y1)2. Write a Python statement that calculates and prints the distance\n",
    "between the points (2,2) and (5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "31443143",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "distance between the points is 25\n"
     ]
    }
   ],
   "source": [
    "x0,y0=2,2\n",
    "x1,y1=5,6\n",
    "c=(x0-x1)**2 + (y0-y1)**2\n",
    "print('distance between the points is' , c)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "610fddcf",
   "metadata": {},
   "source": [
    "- Write a program to check whether a year is leap year or not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e90acd84",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2024\n",
      "given year is leap year\n"
     ]
    }
   ],
   "source": [
    "y=int(input())\n",
    "if y%4==0:\n",
    "    if y%100!=0 or y%400==0:\n",
    "        print('given year is leap year')\n",
    "else:\n",
    "    print('given year is not leap year')\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "55981c6d",
   "metadata": {},
   "source": [
    "- Write a program to output the grade of student based on the percentage\n",
    "entered by the student"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "48af60db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2024\n",
      "2024 is a leap year\n"
     ]
    }
   ],
   "source": [
    "import calendar\n",
    "year=int(input())\n",
    "if calendar.isleap(year):\n",
    "    print(year,'is a leap year')\n",
    "else:\n",
    "    print(year,'is not a leap year')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22be9ba8",
   "metadata": {},
   "source": [
    "- Write a program to output the grade of student based on the percentage\n",
    "entered by the student"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c979655f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your percentage: 95\n",
      "Your grade is:  A\n"
     ]
    }
   ],
   "source": [
    "percentage = float(input(\"Enter your percentage: \"))\n",
    "\n",
    "if percentage >= 90:\n",
    "    grade = \"A\"\n",
    "elif percentage >= 80:\n",
    "    grade = \"B\"\n",
    "elif percentage >= 70:\n",
    "    grade = \"C\"\n",
    "elif percentage >= 60:\n",
    "    grade = \"D\"\n",
    "else:\n",
    "    grade = \"F\"\n",
    "\n",
    "print(\"Your grade is: \", grade)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4c5939a6",
   "metadata": {},
   "source": [
    "- Write a Python program to check whether an alphabet is a vowel or\n",
    "consonant"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d68cc576",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a letter: H\n",
      "h is a consonant.\n"
     ]
    }
   ],
   "source": [
    "letter = input(\"Enter a letter: \").lower()\n",
    "\n",
    "if letter in ['a', 'e', 'i', 'o', 'u']:\n",
    "    print(letter, \"is a vowel.\")\n",
    "else:\n",
    "    print(letter, \"is a consonant.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "424f1065",
   "metadata": {},
   "source": [
    "- Write a python function that receive one number and print it is even\n",
    "number or odd number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "c37511b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "write your number5874\n",
      "your number is even\n"
     ]
    }
   ],
   "source": [
    "n = int(input('write your number'))\n",
    "if n%2==0:\n",
    "    print('your number is even')\n",
    "else:\n",
    "    print('ypur number is odd')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a788cacf",
   "metadata": {},
   "source": [
    "- Write a python program that receive 5 numbers by user and print sum\n",
    "and average of these numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "3ef7bf67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 5\n",
      "Enter a number: 8\n",
      "Enter a number: 6\n",
      "Enter a number: 62\n",
      "Enter a number: 754\n",
      "The sum of the numbers is:  835.0\n",
      "The average of the numbers is:  167.0\n"
     ]
    }
   ],
   "source": [
    "total = 0\n",
    "\n",
    "for i in range(5):\n",
    "    num = float(input(\"Enter a number: \"))\n",
    "    total += num\n",
    "\n",
    "average = total / 5\n",
    "\n",
    "print(\"The sum of the numbers is: \", total)\n",
    "print(\"The average of the numbers is: \", average)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1516f461",
   "metadata": {},
   "source": [
    "- Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is\n",
    "stored in spam, and prints Greetings! if anything else is stored in spam."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "50426c9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter 1 for hello, 2 for howdy, and any number for greetings52\n",
      "Greetings!\n"
     ]
    }
   ],
   "source": [
    "spam = int(input('enter 1 for hello, 2 for howdy, and any number for greetings'))\n",
    "\n",
    "if spam == 1:\n",
    "    print(\"Hello\")\n",
    "elif spam == 2:\n",
    "    print(\"Howdy\")\n",
    "else:\n",
    "    print(\"Greetings!\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
