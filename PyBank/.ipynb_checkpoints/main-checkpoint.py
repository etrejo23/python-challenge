{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\elisa\\\\Desktop\\\\Python_HW\\\\PyBank'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "inpath=os.path.join(\"Resources\",\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Resources\\\\budget_data.csv'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inpath"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(inpath,'r') as csvfile:\n",
    "    csvreader = csv.reader(csvfile,delimiter=',')\n",
    "    csv_header=next(csvreader)\n",
    "\n",
    "    totalMonths = 0\n",
    "    NetProfitLoss = 0\n",
    "    AvgChangePL = 0\n",
    "    prevRow=0\n",
    "    ListAvg=[]\n",
    "    list_of_months=[]\n",
    "    for row in csvreader:\n",
    "        #Total Number of Months \n",
    "        totalMonths = totalMonths+1\n",
    "        #Total Amount of Profit/Losses\n",
    "        NetProfitLoss += int(row[1])\n",
    "        #Average changes in \"Profit/Losses\"\n",
    "        #prevRow = int(csvreader[row])\n",
    "        AvgChangePL = int(row[1])-prevRow\n",
    "        ListAvg.append(AvgChangePL)\n",
    "        list_of_months.append(row[0])\n",
    "        prevRow=int(row[1])\n",
    "        \n",
    "    \n",
    "    greatest_Increase = max(ListAvg)\n",
    "    greatest_Decrease = min(ListAvg)\n",
    "    index_of_great_ind=ListAvg.index(greatest_Increase)\n",
    "    index_of_great_dec=ListAvg.index(greatest_Decrease)\n",
    "    month_of_greatest_Increase=list_of_months[index_of_great_ind]\n",
    "    month_of_greatest_Decrease=list_of_months[index_of_great_dec]\n",
    "    AvgChange = round(sum(ListAvg[1:])/int(len(ListAvg)-1),2)\n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"-------------------------------\")\n",
    "    print(\"Total Months: \"+str(totalMonths))\n",
    "    print(\"Total: $\"+str(NetProfitLoss))\n",
    "    print(\"Average Chage: $\"+str(AvgChange))\n",
    "    print(\"Greatest Increase in Profits: \"+str(month_of_greatest_Increase)+ \" ($\" +str(greatest_Increase) +\")\")\n",
    "    print(\"Greatest Decrease in Profits: \"+str(month_of_greatest_Decrease)+\" ($\" +str(greatest_Decrease) +\")\")\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "    \n",
    "    f= open(\"Analysis//findings.txt\",\"w\")\n",
    "    print(\"Financial Analysis\", file=f)\n",
    "    print(\"-------------------------------\", file=f)\n",
    "    print(\"Total Months: \"+str(totalMonths), file=f)\n",
    "    print(\"Total: $\"+str(NetProfitLoss), file=f)\n",
    "    print(\"Average Chage: $\"+str(AvgChange),file=f)\n",
    "    print(\"Greatest Increase in Profits: \"+str(month_of_greatest_Increase)+ \" ($\" +str(greatest_Increase) +\")\", file=f)\n",
    "    print(\"Greatest Decrease in Profits: \"+str(month_of_greatest_Decrease)+\" ($\" +str(greatest_Decrease) +\")\", file=f)\n",
    "    f.close()"
   ]
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
