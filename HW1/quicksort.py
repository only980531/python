{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = [56,98,56,35,94,65,65,38,75,72,48,95,86,31,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 31, 35, 38, 48, 56, 56, 65, 65, 72, 75, 86, 94, 95, 98]\n"
     ]
    }
   ],
   "source": [
    "def quick_sort(data,left,right):\n",
    "    if left>=right: #如果左邊的數>=右邊的數,因為排序不對,所以執行下面排序\n",
    "        return\n",
    "    l=left\n",
    "    r=right\n",
    "    key=data[right] #設右邊的數為基準點\n",
    "    \n",
    "    while l!=r:\n",
    "        while data[l]<key and l<r: #左邊的部分如果l的位置在key(基準點)的左邊,且l<r,往後看下一個數\n",
    "            l+=1\n",
    "        while data[r]>=key and l<r:#右邊的部分如果r的位置等於或在key的右邊,且l<r,往前看上一個數\n",
    "            r-=1\n",
    "        if l<r: #如果l<r但相對位置不對則交換位置\n",
    "            data[l],data[r]=data[r],data[l] \n",
    "       \n",
    "    data[right]=data[r]\n",
    "    data[r]=key\n",
    "    \n",
    "    quick_sort(data,left,r-1)\n",
    "    quick_sort(data,r+1,right)\n",
    "        \n",
    "quick_sort(data, 0, len(data)-1)\n",
    "print(data)                    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "data=[1,6,3,5,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
