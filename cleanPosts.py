import csv

with open('questionposts.csv',"r") as fin:
    with open('reorderedPosts.csv',"w") as fout:
        writer=csv.writer(fout)
        for row in csv.reader(fin):
            tempRow = row[:-1]
            posts = tempRow[3:]

            id = row[0]
            state = row[1]
            questionID = row[2]
            created = row[-1]

            newRow = []
            newRow.append(id)
            newRow.append("∞")
            newRow.append(state)
            newRow.append("∞")
            newRow.append(questionID)
            newRow.append("∞")
            newRow.append(created)
            newRow.append("∞")
            writer.writerow(newRow + posts)