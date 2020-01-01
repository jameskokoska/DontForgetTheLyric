def openFile(fileName):
    fileIn = open(fileName + ".html", "r")
    coreList = []
    for line in fileIn:
        coreList.append(line)
    fileIn.close()
    return(coreList)

def replaceInList(searchList, keyWordSearch, keyWordReplace):
    index = -1
    for word in searchList:
        index += 1
        if word == keyWordSearch+"\n":
            searchList[index] = keyWordReplace + "\n"
    return searchList

def save(fileName, saveList):
    file = open(fileName + ".html", "w")
    for word in saveList:
        file.write(word)
    file.close()

def main():
    numWord = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth"]
    indexDefault = openFile("indexDefault - Copy")
    start = openFile("START - Copy")

    for genreCount in range(0,8):
        genreName = input(numWord[genreCount] + " genre?\n('done' - finishes and saves)\n")
        if genreName == "done":
            break
        else:
            indexDefault = replaceInList(indexDefault, "Genre"+str(genreCount+1), genreName)
            start = replaceInList(start, "Genre"+str(genreCount+1), genreName)

        for songCount in range(0,3):
            songName = input(numWord[songCount] + " song?\n")
            currentSong = openFile("song"+str(genreCount+1)+str(songCount+1)+" - Copy")
            currentSong = replaceInList(currentSong, "\t\tSong"+str(songCount+1)+"Name", songName)

            lyricCount = 0
            for lyricCount in range(1,5):
                print("Lyrics (" + str(lyricCount) + "/4)\n('missing' - start entering missing lyrics)")
                lyrics = ""
                while True:
                    line = input()
                    if line == "":
                        break
                    if line == "missing":
                        break
                    lyrics += line + "\n"
                if line == "missing":
                    break
                else:
                    currentSong = replaceInList(currentSong, "LyricsPage"+str(lyricCount), lyrics)

                
            if lyricCount == 4:
                lyricCount += 1
                
            missingLyrics = input("Enter the missing lyrics:\n")
            emptified = ""
            for letter in missingLyrics:
                if letter != " ":
                    emptified += "_"
                else:
                    emptified += " "
            if len(missingLyrics.split()) == 1:
                currentSong = replaceInList(currentSong, "LyricsPage"+str(lyricCount), str(len(missingLyrics.split()))+" Word\n" + emptified)
            else:
                currentSong = replaceInList(currentSong, "LyricsPage"+str(lyricCount), str(len(missingLyrics.split()))+" Words\n" + emptified)
            currentSong = replaceInList(currentSong, "LyricsPage"+str(lyricCount+1), missingLyrics)
            
            save("song"+str(genreCount+1)+str(songCount+1), currentSong)

    print("Saving main menu")
    save("START", start)
    save("indexDefault", indexDefault)
    print("Done!")
 
if __name__ == '__main__':
    main()
