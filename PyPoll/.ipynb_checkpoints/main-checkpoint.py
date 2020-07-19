{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "inpath=os.path.join(\"Resources\",\"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
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
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Total Votes: 3521001\n",
      "-------------------------\n",
      "Khan:63.0% (2218231)\n",
      "Correy:20.0% (704200)\n",
      "Li:14.0% (492940)\n",
      "O'Tooley:3.0% (105630)\n",
      "-------------------------\n",
      "Winner: Khan\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"Election Results\")\n",
    "print(\"-------------------------\")\n",
    "print(\"Total Votes: \" +str(totalVotes))\n",
    "print(\"-------------------------\")\n",
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
    "print(\"-------------------------\")\n",
    "print(\"Winner: \" + str(namesOfCandidates[indexOfWinner]))\n",
    "print(\"-------------------------\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open(\"Analysis//findings.txt\",\"w\")\n",
    "print(\"Election Results\", file =f)\n",
    "print(\"-------------------------\", file=f)\n",
    "print(\"Total Votes: \" +str(totalVotes), file=f)\n",
    "print(\"-------------------------\",file=f)\n",
    "for candidate in dicOfCandidates:\n",
    "    percentageOfVotes=round((dicOfCandidates[candidate]/float(totalVotes))*100.0,3)\n",
    "        \n",
    "    print(f\"{candidate}:{percentageOfVotes}% ({dicOfCandidates[candidate]})\",file=f)\n",
    "          \n",
    "        \n",
    "listOfValues=list(dicOfCandidates.values())\n",
    "mostVotes=max(listOfValues)\n",
    "indexOfWinner=listOfValues.index(mostVotes)\n",
    "namesOfCandidates=list(dicOfCandidates.keys())\n",
    "print(\"-------------------------\",file=f)\n",
    "print(\"Winner: \" + str(namesOfCandidates[indexOfWinner]),file=f)\n",
    "print(\"-------------------------\",file=f)\n",
    "f.close()\n",
    "\n",
    "    "
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
