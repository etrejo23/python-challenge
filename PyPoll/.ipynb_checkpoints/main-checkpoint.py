{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "inpath=os.path.join(\"Resources\",\"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(inpath,'r') as csvfile:\n",
    "    csvreader = csv.reader(csvfile,delimiter=',')\n",
    "    csv_header=next(csvreader)\n",
    "    \n",
    "    totalVotes = 0\n",
    "    Candidates=[]\n",
    "    dicOfCandidates = {}\n",
    "    for row in csvreader:\n",
    "        totalVotes = totalVotes + 1\n",
    "        if row[2] in dicOfCandidates:\n",
    "            dicOfCandidates[row[2]]= dicOfCandidates[row[2]]+1\n",
    "        else: \n",
    "            dicOfCandidates[row[2]]= 1\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3521001\n"
     ]
    }
   ],
   "source": [
    "print(totalVotes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "print(Candidates[:100])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#NumOfCandidates=collections.Counter(Candidates)\n",
    "#print(NumOfCandidates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Khan': 2218231, 'Correy': 704200, 'Li': 492940, \"O'Tooley\": 105630}\n"
     ]
    }
   ],
   "source": [
    "print(dicOfCandidates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Khan:63.0% (2218231)\n",
      "Correy:20.0% (704200)\n",
      "Li:14.0% (492940)\n",
      "O'Tooley:3.0% (105630)\n",
      "The winner is: Khan\n"
     ]
    }
   ],
   "source": [
    "for candidate in dicOfCandidates:\n",
    "    percentageOfVotes=round((dicOfCandidates[candidate]/float(totalVotes))*100.0,3)\n",
    "        \n",
    "    print(f\"{candidate}:{percentageOfVotes}% ({dicOfCandidates[candidate]})\")\n",
    "          \n",
    "        \n",
    "listOfValues=list(dicOfCandidates.values())\n",
    "mostVotes=max(listOfValues)\n",
    "indexOfWinner=listOfValues.index(mostVotes)\n",
    "namesOfCandidates=list(dicOfCandidates.keys())\n",
    "print(\"The winner is: \" + str(namesOfCandidates[indexOfWinner]))\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
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
