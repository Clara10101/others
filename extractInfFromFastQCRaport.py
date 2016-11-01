'''
Wyniki analizy w raporcie:
1. Basic Statistics
2. Per base sequence quality
3. Per tile sequence quality
4. Per sequence quality scores
5. Per base sequence content
6. Per sequence GC content
7. Per base N content
8. Sequence Length Distribution
9. Sequence Duplication Levels
10. Overrepresented sequences
11. Adapter Content
12. Kmer Content
'''
import os

def extractInfo(rawDataFile):
    data = open(rawDataFile,'r')

    basicStat = ''
    baseSeqQual = ''
    tileSeqQual = ''
    perSeqQual = ''
    perBaseCont = ''
    perSeqGC = ''
    perBaseN = ''
    seqLengDist = ''
    seqDupLevel = ''
    overrepSeq = ''
    adapterCont = ''
    kmerCont = ''

    fileName = ''
    encoding = ''


    for line in data:
        actualLine = line.strip().split('\t')
        if actualLine[0].startswith('>>'):
            if actualLine[0][2:] == 'Basic Statistics':
                basicStat = actualLine[1]
            elif actualLine[0][2:] == 'Per base sequence quality':
                baseSeqQual = actualLine[1]
            elif actualLine[0][2:] == 'Per tile sequence quality':
                tileSeqQual = actualLine[1]
            elif actualLine[0][2:] == 'Per sequence quality scores':
                perSeqQual = actualLine[1]
            elif actualLine[0][2:] == 'Per base sequence content':
                perBaseCont = actualLine[1]
            elif actualLine[0][2:] == 'Per sequence GC content':
                perSeqGC = actualLine[1]
            elif actualLine[0][2:] == 'Per base N content':
                perBaseN = actualLine[1]
            elif actualLine[0][2:] == 'Sequence Length Distribution':
                seqLengDist = actualLine[1]
            elif actualLine[0][2:] == 'Sequence Duplication Levels':
                seqDupLevel = actualLine[1]
            elif actualLine[0][2:] == 'Overrepresented sequences':
                overrepSeq = actualLine[1]
            elif actualLine[0][2:] == 'Adapter Content':
                adapterCont = actualLine[1]
            elif actualLine[0][2:] == 'Kmer Content':
                kmerCont = actualLine[1]
        elif actualLine[0].startswith('Filename'):
            fileName = actualLine[1]
        elif actualLine[0].startswith('Encoding'):
            encoding = actualLine[1]
        
    return fileName + ';' + encoding + ';' + basicStat + ';' + baseSeqQual + ';' + tileSeqQual + ';' + perSeqQual + ';' + perBaseCont + ';' + perSeqGC + ';' \
    + perBaseN + ';' + seqLengDist + ';' + seqDupLevel + ';' + overrepSeq + ';' + adapterCont + ';' + kmerCont + ';'

if __name__ == '__main__':
    #wykonanie dla kazdego pliku txt w folderze
    raport_file = open('resultFastQC','w')
    for file in os.listdir("."):
        if file.endswith(".txt"):
            raport_file.write('File name; Encoding;Basic Statistics;Per base sequence quality;Per tile sequence quality;Per sequence quality scores;Per base sequence content;Per sequence GC content;Per base N content;Sequence Length Distribution;Sequence Duplication Levels;Overrepresented sequences;Adapter Content;Kmer Content\n')
            raport_file.write(extractInfo(file) + '\n')
    #print extractInfo('FastQC_on_data_34__RawData.txt')